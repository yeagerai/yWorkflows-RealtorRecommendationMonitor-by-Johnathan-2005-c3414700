
# RealtorRecommendationMonitor

A Yeager Workflow that scans local Facebook groups for anyone asking for a realtor or real estate agent recommendation. The workflow collects the necessary information from the user, such as the Facebook API credentials, targeted groups to monitor, messaging platform credentials, and Melissa API credentials, and stores them in a browser plugin's local storage. The workflow monitors the targeted Facebook groups for posts asking about a realtor or real estate agent. When a relevant post is detected, it extracts the poster's first and last name and retrieves a valid phone number using the Melissa API. Then, it sends a text or Whatsapp message with the person's name and phone number to the real estate agent. This process is repeated each time a new relevant post is made.
## Initial generation prompt
a workflow that scans local Facebook groups for anyone asking for a realtor or real estate agent recommendation. The workflow should collect the necessary information from the user, such as the Facebook API credentials, targeted groups to monitor, messaging platform credentials, and Melissa API credentials, and store them in a browser plugin's local storage. The workflow should then monitor the targeted Facebook groups for posts asking about a realtor or real estate agent. When a relevant post is detected, the workflow should extract the poster's first and last name from the post and run it through Melissa to retrieve a valid phone number using the stored Melissa API credentials. The workflow should then use the stored messaging platform credentials to send a text or Whatsapp message to the real estate agent containing the person's name and phone number for immediate contact. The workflow should repeat this process each time a new relevant post is made.

## Authors: 
- yWorkflows
- Johnathan#2005
        