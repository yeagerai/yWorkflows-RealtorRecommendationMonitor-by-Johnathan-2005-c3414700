
import pytest
from pydantic import BaseModel
from typing import Optional
from fastapi.testclient import TestClient
from core.workflows.realtor_recommendation_monitor import (
    RealtorRecommendationMonitor,
    UserConfigurations,
    MessageInfo,
)

client = TestClient(realtor_recommendation_monitor_app)

# Define mocked input and expected output data
test_data = [
    (
        UserConfigurations(
            facebook_api_credentials={"api_key": "test_key"},
            targeted_facebook_groups=["test_group1", "test_group2"],
            messaging_platform_credentials={"platform_key": "test_key"},
            melissa_api_credentials={"melissa_key": "test_key"},
        ),
        MessageInfo(name="John Doe", phone_number="555-555-1234"),
    ),
    (
        UserConfigurations(
            facebook_api_credentials={"api_key": "test_key2"},
            targeted_facebook_groups=["test_group1", "test_group2"],
            messaging_platform_credentials={"platform_key": "test_key2"},
            melissa_api_credentials={"melissa_key": "test_key2"},
        ),
        MessageInfo(name="Jane Smith", phone_number="555-555-5678"),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_transform(input_data: UserConfigurations, expected_output: MessageInfo):
    # Initialize RealtorRecommendationMonitor and call transform() method
    realtor_recommendation_monitor = RealtorRecommendationMonitor()
    output = client.post("/transform/", json=input_data.dict())
    
    # Assert that the output matches the expected output
    assert output.json() == expected_output.dict()

# Test cases with error handling and edge cases can be added here
