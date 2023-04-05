
import os
import json
from typing import Optional
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class UserConfigurations(BaseModel):
    credentials: dict


class StoredCredentials(BaseModel):
    confirmation: str


class StoreCredentials(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.localStorageKey: str = yaml_data["parameters"]["localStorageKey"]

    def transform(self, args: UserConfigurations) -> StoredCredentials:
        key = self.localStorageKey
        data = json.dumps(args.credentials)
        
        # Here we assume that the "store_in_local_storage" function represents
        # the implementation for storing data in your browser plugin's local storage.
        # Replace it with the appropriate implementation for storing data.
        store_in_local_storage(key, data)
        
        confirmation_message = f"Credentials saved under the key: {key}"
        return StoredCredentials(confirmation=confirmation_message)


load_dotenv()
store_credentials_app = FastAPI()


@store_credentials_app.post("/transform/")
async def transform(args: UserConfigurations) -> StoredCredentials:
    store_credentials = StoreCredentials()
    return store_credentials.transform(args)
