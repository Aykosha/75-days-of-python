""" 
Day5: Real-World API Integration - Live Weather App
API: OpenWeatherApp

⚠️ SECURITY NOTE:
- This implementation uses environment variables for API key security
- Never hardcode or commit secrets in production code
- To replicate:
  1. Set environment variable:
     Windows: `setx OWM_API_KEY "your_key"`
     Mac/Linux: `export OWM_API_KEY="your_key"`
  2. Reload your terminal/IDE
"""

import os
import requests 

# Get data from API (error handling)
try:
    API_KEY = os.environ["OWM_API_KEY"]
except KeyError:
    print("⚠️ Error: OWM_API_KEY environment variable not set!")
    print("Please set it first with:")
    print("Windows: setx OWM_API_KEY 'your_key_here'")
    print("Mac/Linux: export OWM_API_KEY='your_key_here'")
    exit(1)

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status() # Raises exception for HTTP errors
        data = response.json()
        # Check for API error messages
        if data.get("cod") != 200:
            return f"⚠️ API Error: {data.get('message', 'Unknown error')}"   
#Extract info
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        return(
            f"\n☀️ {city} Weather:\n"
            f"- Temperature: {temp}°C\n" 
            f"- Humidity: {humidity}%"
        )
    
    except requests.exceptions.RequestException as e: # Network errors
        return f"⚠️ Network Error: {str(e)}"    
    except KeyError as e: 
        return f"⚠️ Data Parsing Error: Missing {str(e)} in API response"
    
if __name__ == "__main__":
    city = input("Enter city: ")
    print(get_weather(city))
