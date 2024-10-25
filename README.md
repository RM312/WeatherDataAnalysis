```markdown
# Weather Data Analysis

## Overview

This project is a **Weather Data Analysis** application that retrieves and displays real-time weather information for a specified city using the **OpenWeatherMap API**. It provides details such as temperature, weather description, humidity, wind speed, and a corresponding weather image. The workflow consists of two main components:

1. **Weather Data Retrieval**: The application fetches weather data based on user input, processes it, and displays relevant information in a user-friendly format.
2. **Image Representation of Weather**: An image representing the current weather conditions is displayed based on the weather description, providing a visual context for users.

You can access the live version of the project here: [Weather Data Analysis](https://weatherdataanalysis-4dwpe9un8sn5tzaeemjykc.streamlit.app/)

---

## Dataset

The application uses data from the **OpenWeatherMap API** to provide real-time weather information. To access this data, you need an API key, which can be obtained by registering at [OpenWeatherMap](https://openweathermap.org/).

---

## Project Structure

- **weather_analysis.py**: 
    - Contains the main functions for retrieving and processing weather data based on user input.
    - Uses the OpenWeatherMap API to fetch details like temperature, humidity, wind speed, and weather description.

- **app.py**: 
    - Implements the user interface.
    - Displays weather details and an image representing the current weather conditions.
    - Provides an input field where users can enter the city name to retrieve weather information.

---

## How to Run

### 1. Setting Up the Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/RM312/WeatherDataAnalysis.git
   cd WeatherDataAnalysis
   ```

2. Install the required dependencies:

   ```bash
   pip install requests Pillow
   ```

### 2. API Key

Replace the `api_key` variable in `weather_analysis.py` with your own OpenWeatherMap API key to enable data retrieval.

### 3. Running the Application

Run the application:

```bash
python app.py
```

### 4. User Interaction

Enter the city name when prompted, and the application will display current temperature, weather description, humidity, wind speed, and a relevant weather image.

---

## Dependencies

Install dependencies using:

```bash
pip install requests Pillow
```

This ensures all necessary packages are available for data retrieval and image display.

---

## Error Handling

The application includes error handling for:
- Network errors when accessing the API.
- Parsing errors for unexpected response formats.
- Invalid city names that do not return valid data.

---

### Explanation

1. **Weather Data Retrieval**: Connects to the OpenWeatherMap API to fetch current weather details based on user input, processes the JSON response, and extracts relevant information.
  
2. **Image Representation**: Displays an image representing the weather, enhancing user experience through visual feedback.

3. **API Key Setup**: Instructions are provided for obtaining and setting up the API key for accessing the OpenWeatherMap data.
```
