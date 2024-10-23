import streamlit as st
import requests

def get_weather_for_location(city):
    try:
        api_key = "6cfe406302dee8d37bf32fef53bdbc87"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        data = response.json()
        
        # Extract relevant information from the JSON response
        temperature = data['main']['temp']
        weather_info = data['weather'][0]
        weather_description = weather_info['description']
        time = data['dt']  # UNIX timestamp
        additional_info = f"Humidity: {data['main']['humidity']}%, Wind Speed: {data['wind']['speed']} m/s"
        
        return city, temperature, weather_description, additional_info
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None
    except KeyError as e:
        st.error(f"Error parsing data: {e}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

def get_weather_image(weather):
    weather = weather.lower()
    if "clear" in weather:
        return "https://ssl.gstatic.com/onebox/weather/64/sunny.png"
    elif "cloud" in weather:
        return "https://ssl.gstatic.com/onebox/weather/64/partly_cloudy.png"
    elif "rain" in weather:
        return "https://ssl.gstatic.com/onebox/weather/64/rain_light.png"
    elif "snow" in weather:
        return "https://ssl.gstatic.com/onebox/weather/64/snow_light.png"
    elif "storm" in weather:
        return "https://ssl.gstatic.com/onebox/weather/64/thunderstorms.png"
    elif "fog" in weather or "mist" in weather:
        return "https://ssl.gstatic.com/onebox/weather/64/fog.png"
    else:
        return "https://ssl.gstatic.com/onebox/weather/64/partly_cloudy.png"

st.title("Weather Analysis")

city = st.text_input("Enter The City Name:", "")

if city:
    city = city.strip().capitalize()  
    with st.spinner('Fetching weather data...'):
        result = get_weather_for_location(city)
    
    if result is not None:
        location, temperature, weather_description, additional_info = result
        weather_image_url = get_weather_image(weather_description)
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(f"Weather details for {location}")
            st.write(f"🌡️ Temperature: {temperature} °C")
            st.write(f"☁️ Weather: {weather_description}")
            st.write(f"💨 {additional_info}")
        
        with col2:
            st.image(weather_image_url, caption=f"Current weather: {weather_description}", width=100)
    else:
        st.warning("Failed to retrieve data. Please check the city name and try again.")
else:
    st.info("Please enter a city name to get weather information.")
