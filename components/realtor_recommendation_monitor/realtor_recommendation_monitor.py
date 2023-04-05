
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class UserConfigurations(BaseModel):
    facebook_api_credentials: dict
    targeted_facebook_groups: list
    messaging_platform_credentials: dict
    melissa_api_credentials: dict


class MessageInfo(BaseModel):
    name: str
    phone_number: str


class RealtorRecommendationMonitor(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: UserConfigurations, callbacks: typing.Any
    ) -> MessageInfo:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        name = results_dict[-2]["name"]
        phone_number = results_dict[-1]["phone_number"]
        out = MessageInfo(
            name=name,
            phone_number=phone_number
        )
        return out


load_dotenv()
realtor_recommendation_monitor_app = FastAPI()


@realtor_recommendation_monitor_app.post("/transform/")
async def transform(
    args: UserConfigurations,
) -> MessageInfo:
    realtor_recommendation_monitor = RealtorRecommendationMonitor()
    return await realtor_recommendation_monitor.transform(args, callbacks=None)

