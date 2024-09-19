# Weather Information Script

## Description

This Python script provides two functionalities:
1. Scrapes weather information for a specific city from Google.
2. Retrieves weather information for the current location based on the public IP address using the `wttr.in` service.

The script fetches the current temperature, time, sky conditions, and wind details. Additionally, it automatically retrieves the current city based on the user's IP address and provides a schematic view of the weather.

### Features
- Extracts and displays the current temperature, time, and sky conditions for a specified city (in this case, Bhubaneswar).
- Retrieves the current city based on the user's IP address and displays the weather details for that city from `wttr.in`.

## Dependencies

To run this script, you need the following Python libraries:
- `requests`: For sending HTTP requests to retrieve weather and location data.
- `beautifulsoup4`: For parsing the HTML content of the Google weather page.

You can install the required dependencies by running the following command:

```bash
pip install requests beautifulsoup4


## Acknowledgement
### Notes:
- The README file explains the script's functionality, dependencies, and how to run it.
- It includes instructions for customizing the city for scraping weather data.
