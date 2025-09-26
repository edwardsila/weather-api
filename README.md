# 🌦️ Weather API

This is a simple yet modern FastAPI project that provides real-time weather information using the [OpenWeather API](https://openweathermap.org/api). The goal is to give developers a lightweight backend service that can be extended to larger applications. It is powered by **FastAPI**, runs on **Uvicorn**, and integrates with **OpenWeather** to fetch live data such as temperature and conditions for any city in the world.

## 🚀 Getting Started

To run the project, first clone the repository and navigate into it:
```bash
git clone https://github.com/edwardsila/weather-api.git
cd weather-api

Install the dependencies:

pip install -r requirements.txt

Next, create a .env file in the project root and add your OpenWeather API key:

OPENWEATHER_API_KEY=your_real_api_key_here

Once that’s done, start the server with:

uvicorn main:app --reload

Your API will now be running locally at http://127.0.0.1:8000.
📡 How to Use

The root endpoint simply shows that the API is running:

GET /

To fetch weather data for a city, use:

GET /weather/{city}

For example, to check Nairobi’s weather:

curl "http://127.0.0.1:8000/weather/Nairobi"

You’ll receive a response like this:

{
  "city": "Nairobi",
  "temperature": 22.5,
  "weather": "scattered clouds"
}

📂 Project Layout

The project is lightweight and organized as follows:

weather-api/
│── main.py          # FastAPI app
│── .env             # Environment variables
│── requirements.txt # Dependencies
│── README.md        # Project docs

🎬 Visual Demo
<p align="center"> <img src="https://assets9.lottiefiles.com/private_files/lf30_editor_dcwkhmns.json" width="280" alt="Weather Animation"> </p>

🛠️ Tech Used

Built with FastAPI ⚡, Uvicorn 🚀, Requests 🌍, and python-dotenv 🔑. It’s easy to extend with more features like multi-day forecasts, caching, or even integration with a React/Next.js frontend.
🌱 What’s Next

Planned improvements include a 7-day forecast endpoint, optional historical weather data, deployment to Railway/Render/Vercel, and a simple frontend dashboard.
👤 Author

Made with ❤️ by Islam edward Sila

---
