# Fastapi with Unleash SDK Demo App

This is a simple FastAPI app to demo feature flags with Unleash SDK For SFD 2025 Bukidnon.

# Requirements

1. Docker
2. Python (^3.13)
3. Poetry

# Instructions

1. Clone [Unleash-Docker](https://docs.getunleash.io/using-unleash/deploy/getting-started) and get that running. This is your Unleash server.

2. Clone this repo and run 

    `# poetry install` 

    Don't forget to activate the virtual environment after:

    `# eval $(poetry env activate)`

    You will have to checkout certain commits to follow the presentation.

3. Login to your Unleash server and setup your first feature flag. There should be only one project - `default` - on the dashboard.

4. Make sure the feature flag NAME matches with one in the fastapi app. Change it to something different if you want. 

    Don't forget to set the API key on the fastapi app.

5. Use a REST API client like Insomnia, Bruno or Postman to test functionality

# Author

Jaypax Ginete <killer.tilapia@gmail.com>

[My Blog](https://killertilapia.blogspot.com)

[Presentation](https://google.com)
