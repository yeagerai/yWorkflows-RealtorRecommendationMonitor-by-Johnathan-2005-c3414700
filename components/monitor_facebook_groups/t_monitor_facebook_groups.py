
import os
import pytest
from typing import List, Dict
from unittest.mock import Mock

from fastapi import FastAPI
from pydantic import BaseModel

from your_component_file import (
    MonitorFacebookGroups,
    MonitorFacebookGroupsInputDict,
    MonitorFacebookGroupsOutputDict,
)

# Test data
valid_facebook_api_credentials = {
    "access_token": "mocked_access_token",
}

valid_target_groups = [
    "123456789",
    "987654321",
]

mocked_new_posts = [
    {"message": "Hello! Check out our Python project."},
    {"message": "Join our JavaScript workshop next week."},
]

mocked_filtered_posts = [
    {"message": "Hello! Check out our Python project."},
]

# Test cases
test_cases = [
    (valid_facebook_api_credentials, valid_target_groups, mocked_filtered_posts),
]


@pytest.mark.parametrize("api_credentials, target_groups, expected_output", test_cases)
def test_monitor_facebook_groups_transform(api_credentials, target_groups, expected_output):
    # Mock the GraphAPI instance
    mocked_graph_api = Mock()
    
    # Define the mocked graph_api.get_connections() method
    def mock_get_connections(group_id, connection):
        assert group_id in target_groups
        assert connection == "feed"
        return {"data": mocked_new_posts}

    mocked_graph_api.get_connections = mock_get_connections

    # Mock the GraphAPI class
    custom_module.GraphAPI = lambda access_token: mocked_graph_api

    # Prepare the input data
    input_data = MonitorFacebookGroupsInputDict(
        facebook_api_credentials=api_credentials,
        target_groups=target_groups,
    )

    # Initialize the component and call the transform() method
    monitor_facebook_groups = MonitorFacebookGroups()
    output = monitor_facebook_groups.transform(input_data)

    # Assert that the output matches the expected output
    assert output.dict()["filtered_posts"] == expected_output
