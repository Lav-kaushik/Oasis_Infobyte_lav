import requests

# API key 
api_key = '11f5f14c5295baef0ade1e3ae6f86d0e'

def get_weather(city):
    
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
        )
        response.raise_for_status()  

        data = response.json()

        # Check if the city was found
        if data.get('cod') != 200:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None

        return data

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def print_weather(city):
    
    weather_data = get_weather(city)

    if weather_data:
        weather = weather_data['weather'][0]['main']
        temp = round(weather_data['main']['temp'])
        
        print(f"The weather in {city} is: {weather}")
        print(f"The temperature in {city} is: {temp}ºF")
    else:
        print("Error: Unable to fetch weather data. Please check the city name and try again.")

def main():
    user_input = input("Enter city: ")
    print_weather(user_input)

if __name__ == "__main__":
    main()
