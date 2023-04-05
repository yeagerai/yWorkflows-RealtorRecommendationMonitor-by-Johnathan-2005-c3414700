
import pytest
import json
from fastapi.testclient import TestClient
from typing import Tuple
from my_module import StoredCredentials, UserConfigurations, StoreCredentials, store_credentials_app

client = TestClient(store_credentials_app)
