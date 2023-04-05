
# ExtractPosterInfo

This is a Yeager Component that is designed to extract the poster's first and last name from the relevant post detected by the MonitorFacebookGroups component. It assumes that the post information has already been received by this component as input, which includes information such as the content of the post and the poster's name. The ExtractPosterInfo component then processes the input data to separate and extract the first and last names of the poster.

## Initial generation prompt
description: Component that extracts the poster's first and last name from the relevant
  post detected by the MonitorFacebookGroups component.
name: ExtractPosterInfo


## Transformer breakdown
- 1. Extract the 'poster_name' field from the input 'post_info'
- 2. Split 'poster_name' based on the 'name_separator' parameter
- 3. Ensure that there are exactly two parts to the split result (first and last name)
- 4. If there are exactly two parts, create a dictionary containing {'first_name': first_name, 'last_name': last_name}; otherwise, return an error
- 5. Return the dictionary as the 'poster_first_last_name' output

## Parameters
[{'name': 'name_separator', 'default_value': ' ', 'description': 'The character or string that separates the first and last name of the poster in the input data', 'type': 'string'}]

        