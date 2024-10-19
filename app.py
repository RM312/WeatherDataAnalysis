import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_weather_for_location(city):
    try:
        url = f"https://www.google.com/search?q=weather+{city}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, 'html.parser')

        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
        temp = temp.text if temp else "N/A"

        strd = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
        weather_info = strd.text.split('\n') if strd else []
        time = weather_info[0] if len(weather_info) > 0 else "N/A"
        weather = weather_info[1] if len(weather_info) > 1 else "N/A"

        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        other_data = listdiv[5].text.split("Wind")[1] if len(listdiv) > 5 else "N/A"

        return city, temp, time, weather, other_data
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None
    except AttributeError as e:
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
        location, temperature, time, weather, additional_info = result
        weather_image_url = get_weather_image(weather)
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(f"Weather details for {location}")
            st.write(f"🌡️ Temperature: {temperature}")
            st.write(f"🕒 Time: {time}")
            st.write(f"💨 {additional_info}")
        
        with col2:
            st.image(weather_image_url, caption=f"Current weather: {weather}", width=100)
            st.write(f"☁️ Weather: {weather}")
    else:
        st.warning("Failed to retrieve data. Please check the city name and try again.")
else:
    st.info("Please enter a city name to get weather information.")