# Weather Data Analysis

## Overview

The **Weather Data Analysis** application retrieves and displays real-time weather data for a specified city using the OpenWeatherMap API, showing temperature, weather description, humidity, wind speed, and a representative weather image. 

## Live App

Access the live version of the project here: [Weather Data Analysis](https://weatherdataanalysis-4dwpe9un8sn5tzaeemjykc.streamlit.app/)

## Dataset

This project uses data from the [OpenWeatherMap API](https://openweathermap.org/). An API key is required to access this service.

## Project Structure

- **weather_analysis.py**: Handles API calls, retrieves weather data, and processes it for display.
- **app.py**: Implements the user interface to show weather details and an appropriate image based on current conditions.

## How to Run

1. **Clone the repository and install dependencies**:
   ```bash
   git clone https://github.com/RM312/WeatherDataAnalysis.git
   cd WeatherDataAnalysis
   pip install requests Pillow
   ```

2. **Configure API Key**: Replace the `api_key` variable in `weather_analysis.py` with your OpenWeatherMap API key.

3. **Run the Application**:
   ```bash
   python app.py
   ```

## Error Handling

The application handles network issues, parsing errors, and invalid city names by notifying users appropriately.

## Explanation of Components

1. **Weather Data Retrieval**: Connects to OpenWeatherMap to obtain real-time weather data, processes the JSON response, and extracts details.
2. **Image Representation**: Displays a weather-specific image based on the retrieved weather description to enhance the user experience.
3. **API Key**: Set up instructions for obtaining and configuring the API key are included to streamline access to the OpenWeatherMap data.

---
