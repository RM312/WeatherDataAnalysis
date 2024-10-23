```markdown
# Weather Data Analysis

## Overview

This project is a **Weather Data Analysis** application that retrieves and displays current weather information for a specified city using the OpenWeatherMap API. The application provides temperature, weather description, humidity, wind speed, and a corresponding weather image. The workflow is divided into two main components:

1. **Weather Data Retrieval**: The application uses the OpenWeatherMap API to fetch weather data based on user input. The data is processed to extract relevant information, which is then displayed in a user-friendly format.
  
2. **Image Representation of Weather**: Based on the weather description, an appropriate weather image is displayed, enhancing the user experience by providing a visual context for the current conditions.

You can access the live version of the project here: [Weather Data Analysis](https://weatherdataanalysis-4dwpe9un8sn5tzaeemjykc.streamlit.app/)

---

## Dataset

This project utilizes the OpenWeatherMap API, which provides real-time weather data. You will need an API key to access this service. You can sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/).

---

## Project Structure

- **weather_analysis.py**: 
    - Contains the main functionality for retrieving weather data and processing user input.
    - Calls the OpenWeatherMap API to fetch current weather details.
    - Extracts relevant information such as temperature, humidity, wind speed, and weather description.

- **app.py**: 
    - Implements the user interface for the weather application.
    - Displays the weather details and an appropriate image based on the current conditions.
    - Provides an interactive console where users can input the city name to retrieve weather information.

---

## How to Run

### 1. Setting Up the Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/RM312/WeatherDataAnalysis.git
   cd WeatherDataAnalysis
   ```

2. Install the required dependencies using `pip`:

   ```bash
   pip install requests Pillow
   ```

### 2. API Key

Replace the `api_key` variable in the `weather_analysis.py` file with your OpenWeatherMap API key to enable data retrieval.

### 3. Running the Application

Run the application:

```bash
python app.py
```

### 4. User Interaction

When prompted, enter the name of the city for which you want to retrieve weather information. The application will display the current temperature, weather description, humidity, wind speed, and show an image representing the weather.

---

## Dependencies

Install the required dependencies using the following command:

```bash
pip install requests Pillow
```

These commands ensure all necessary packages are installed for retrieving weather data and displaying images.

---

## Error Handling

The application includes error handling for potential issues, such as:
- Network errors when fetching data from the API.
- Parsing errors if the response format is unexpected.
- Invalid city names that do not return valid weather data.

---

### Explanation:

1. **Weather Data Retrieval**: The application connects to the OpenWeatherMap API to fetch real-time weather data based on user input. It processes the JSON response to extract relevant weather information.

2. **Image Representation**: Depending on the weather conditions, the application fetches an appropriate image to visually represent the current weather, enhancing user engagement.

3. **OpenWeatherMap API**: Users must register for an API key to access weather data. Instructions are provided for setting up the API key within the application.

