
# StoreCredentials

A component that receives the Facebook API credentials, targeted groups, messaging platform credentials, and Melissa API credentials from the UserConfigurations input and saves them to the browser plugin's local storage. This component allows stored credentials and configurations to be reused across multiple sessions and workflows.

## Initial generation prompt
description: Component that receives the Facebook API credentials, targeted groups,
  messaging platform credentials, and Melissa API credentials from the UserConfigurations
  input and saves them to the browser plugin's local storage.
name: StoreCredentials


## Transformer breakdown
- 1. Receive UserConfigurations input
- 2. Access browser plugin's local storage using the localStorageKey parameter
- 3. Store the UserConfigurations data in the local storage
- 4. Return a confirmation message as StoredCredentials output

## Parameters
[{'name': 'localStorageKey', 'default_value': 'yeager_credentials', 'description': "The key used to store the credentials in the browser plugin's local storage.", 'type': 'str'}]

        