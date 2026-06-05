import requests
from datetime import datetime

# Replace with your OpenWeatherMap API Key
API_KEY = "458909a312ea50144c8d5ba1b21dafa2"


def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print("\n❌ City not found! Please enter a valid city name.")
            return

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])

        print("\n" + "=" * 35)
        print("        WEATHER REPORT")
        print("=" * 35)
        print(f"🌍 City          : {data['name']}")
        print(f"🏳️ Country       : {data['sys']['country']}")
        print(f"🌡 Temperature   : {data['main']['temp']} °C")
        print(f"🤗 Feels Like    : {data['main']['feels_like']} °C")
        print(f"☁️ Condition     : {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity      : {data['main']['humidity']}%")
        print(f"🌬 Wind Speed    : {data['wind']['speed']} m/s")
        print(f"🌅 Sunrise       : {sunrise.strftime('%H:%M:%S')}")
        print(f"🌇 Sunset        : {sunset.strftime('%H:%M:%S')}")
        print("=" * 35)

    except requests.exceptions.ConnectionError:
        print("\n❌ No internet connection.")

    except requests.exceptions.Timeout:
        print("\n❌ Request timed out. Try again later.")

    except requests.exceptions.RequestException as e:
        print("\n❌ Error:", e)


def main():
    print("=" * 35)
    print("      🌦 WEATHER APP 🌦")
    print("=" * 35)

    while True:
        city = input("\nEnter city name: ").strip()

        if not city:
            print("⚠ Please enter a city name.")
            continue

        get_weather(city)

        choice = input("\nSearch another city? (y/n): ").lower().strip()

        if choice != "y":
            print("\n👋 Thank you for using Weather App!")
            break


if __name__ == "__main__":
    main()