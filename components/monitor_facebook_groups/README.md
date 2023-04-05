
# MonitorFacebookGroups

This component monitors targeted Facebook groups for posts mentioning a realtor or real estate agent using the stored Facebook API credentials. It continuously scans the groups for new posts and filters the ones that request recommendations or information about realtors, assisting users in finding potential clients.

## Initial generation prompt
description: Component that monitors the targeted Facebook groups for posts asking
  about a realtor or real estate agent using the stored Facebook API credentials.
name: MonitorFacebookGroups


## Transformer breakdown
- Initialize the Facebook API with the provided credentials.
- Start an infinite loop to continuously monitor targeted Facebook groups.
- Fetch new posts from the target groups using the Facebook API.
- Filter the fetched posts based on the presence of the provided keywords.
- Collect and store the filtered posts in the output structure.
- Wait for the monitoring_interval before fetching next batch of posts.

## Parameters
[{'name': 'monitoring_interval', 'default_value': '60', 'description': 'The interval (in seconds) at which the component will check the target groups for new posts.', 'type': 'int'}, {'name': 'keywords', 'default_value': "['realtor', 'real estate agent']", 'description': 'Keywords used to filter the posts mentioning a realtor or real estate agent.', 'type': 'list'}]

        