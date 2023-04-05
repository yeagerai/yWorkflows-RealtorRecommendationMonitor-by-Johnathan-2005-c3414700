
import os
import asyncio
from typing import List, Dict

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from facebook import GraphAPI

from core.abstract_component import AbstractComponent


class MonitorFacebookGroupsInputDict(BaseModel):
    facebook_api_credentials: Dict
    target_groups: List[str]


class MonitorFacebookGroupsOutputDict(BaseModel):
    filtered_posts: List[Dict]


class MonitorFacebookGroups(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.monitoring_interval: int = yaml_data["parameters"]["monitoring_interval"]
        self.keywords: List[str] = yaml_data["parameters"]["keywords"]

    async def transform(
        self, args: MonitorFacebookGroupsInputDict
    ) -> MonitorFacebookGroupsOutputDict:

        # Initialize the Facebook API
        graph = GraphAPI(access_token=args.facebook_api_credentials["access_token"])

        def fetch_new_posts(group_id: str) -> List[Dict]:
            posts = graph.get_connections(group_id, "feed")
            return posts["data"]

        def filter_posts(posts: List[Dict], keywords: List[str]) -> List[Dict]:
            filtered = []
            for post in posts:
                if any(keyword.lower() in post["message"].lower() for keyword in keywords):
                    filtered.append(post)
            return filtered

        async def monitor_groups() -> List[Dict]:
            filtered_posts = []
            while True:
                for group in args.target_groups:
                    new_posts = fetch_new_posts(group)
                    relevant_posts = filter_posts(new_posts, self.keywords)
                    filtered_posts += relevant_posts
                await asyncio.sleep(self.monitoring_interval)
            return filtered_posts

        output = await monitor_groups()
        return MonitorFacebookGroupsOutputDict(filtered_posts=output)


load_dotenv()
monitor_facebook_groups_app = FastAPI()


@monitor_facebook_groups_app.post("/transform/")
async def transform(
    args: MonitorFacebook
    _groupsInputDict,
) -> MonitorFacebookGroupsOutputDict:
    monitor_facebook_groups = MonitorFacebookGroups()
    return await monitor_facebook_groups.transform(args)

