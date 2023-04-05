
# RealtorRecommendationMonitor

A Yeager Component designed to monitor and process realtor recommendation requests from users by taking input from Facebook groups and messaging platforms. It uses the input configurations like Facebook API credentials, targeted Facebook groups, messaging platform credentials, and Melissa API credentials to authenticate and fetch the data. It then filters and extracts the relevant information about the person looking for a realtor recommendation, such as their name and phone number.

## Initial generation prompt
description: "IOs - inputs:\n- description: Configuration data including Facebook\
  \ API credentials, targeted Facebook\n    groups, messaging platform credentials,\
  \ and Melissa API credentials.\n  name: UserConfigurations\noutputs:\n- description:\
  \ Information about the person looking for a realtor recommendation,\n    including\
  \ their name and phone number.\n  name: MessageInfo\n"
name: RealtorRecommendationMonitor


## Transformer breakdown
- Initialize API clients for Facebook and Messaging Platforms with the provided credentials
- Listen for messages from the targeted Facebook Groups and MessagePlatforms
- Filter and extract relevant realtor recommendation requests
- Retrieve the user's name and phone number from the recommendation requests
- Return the message information, including the person's name and phone number

## Parameters
[]

        