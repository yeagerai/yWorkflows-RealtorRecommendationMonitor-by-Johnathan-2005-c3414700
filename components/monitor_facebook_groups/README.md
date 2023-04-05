markdown
# Component Name

MonitorFacebookGroups

## Description

The `MonitorFacebookGroups` component is designed to regularly monitor specified Facebook groups for new relevant posts based on a set of provided keywords. It uses the Facebook API to fetch and filter the posts, and returns a list of relevant posts.

## Input and Output Models

### Input Model

The input data type `MonitorFacebookGroupsInputDict` is a Pydantic BaseModel that requires:

- `facebook_api_credentials`: A dictionary containing Facebook API credentials.
    - `access_token`: The access token for the Facebook Graph API.
- `target_groups`: A list of strings containing the Facebook group IDs to monitor.

### Output Model

The output data type `MonitorFacebookGroupsOutputDict` is a Pydantic BaseModel that contains:

- `filtered_posts`: A list of dictionaries, each representing a relevant post that matches the specified keywords.

## Parameters

The component uses the following parameters defined in its configuration file:

- `monitoring_interval`: The interval (in seconds) at which the component monitors the Facebook groups. Default value is defined in the configuration file.
- `keywords`: A list of strings containing the keywords used to filter relevant posts. Default values are defined in the configuration file.

## Transform Function

The `transform()` method in the `MonitorFacebookGroups` component performs the following steps:

1. Initialize the Facebook Graph API object with the provided access token.
2. Define the `fetch_new_posts` function to retrieve new posts from the Facebook group using the group ID.
3. Define the `filter_posts` function to filter the relevant posts based on the provided keywords.
4. Define the asynchronous `monitor_groups` function to continuously monitor the target Facebook groups, fetch new posts, and filter relevant posts based on the keywords.
5. Await the `monitor_groups` function and return the output as `MonitorFacebookGroupsOutputDict`.

## External Dependencies

The component uses the following external libraries:

- `os`: Used for handling environment variables.
- `asyncio`: Used for asynchronous processing while continuously monitoring Facebook groups.
- `typing`: Used for type hinting.
- `yaml`: Used for reading the component configuration file.
- `dotenv`: Used for loading environment variables from a .env file.
- `fastapi`: Used for setting up a FastAPI instance for API calls.
- `pydantic`: Used for data validation, serialization, and deserialization of input and output data models.
- `facebook`: Used for interacting with the Facebook Graph API.

## API Calls

The `MonitorFacebookGroups` component makes the following external API call:

- Facebook Graph API `get_connections` method to fetch new posts from the specified Facebook group using the group ID.

## Error Handling

The component does not handle any specific exceptions, but Pydantic will handle input validation and raise appropriate errors if the input model does not meet the expected schema.

## Examples

To use the `MonitorFacebookGroups` component within a Yeager Workflow, follow this example:

1. Configure the component settings in the associated configuration file, including the `monitoring_interval` and `keywords`.

2. Set up a .env file with the necessary environment variables, including the Facebook API `access_token`.

3. Import the component and instantiate it:

   