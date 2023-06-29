# Weather Forecast Webhook

This project is a webhook implementation for providing weather forecasts based on user queries. It integrates with the OpenWeatherMap API to retrieve weather data for a specific location.

## Getting Started


### Prerequisites

To run this application, you need to have the following installed:

- Python (version 3.6 or higher)
- Flask (install using `pip install flask`)
- Requests (install using `pip install requests`)
- Make sure you have ngrok installed in your PC
  
### Installation

1. Clone the repository:
  git clone <repository_url>
  
2. Navigate to the project directory:
   cd weather-forecast-webhook

4. Install the required dependencies:
    pip install -r requirements.txt

### Usage
Set up your OpenWeatherMap API key:

1. Sign up for a free account on OpenWeatherMap.
2. Generate an API key from your account dashboard.
3. Open the app.py file and replace <YOUR_API_KEY> in api_key variable with your actual OpenWeatherMap API key.

Start the Flask server:
python app.py
The server should be up and running locally at http://127.0.0.1:5000/.

Test the webhook by sending a POST request to http://127.0.0.1:5000/webhook with the following JSON payload:

{
  "queryResult": {
    "intent": {
      "displayName": "Forecast"
    },
    "parameters": {
      "location": "<CITY_NAME>"
    }
  }
}
Replace <CITY_NAME> with the desired location for the weather forecast.

### API Reference
Endpoints
GET /: Returns "Hello World" to test if the server is running.
POST /webhook: Accepts a JSON payload with the user query and returns a weather forecast based on the location.

### Error Handling
If an error occurs during the webhook processing, a JSON response with an error message will be returned.

### Contributing
Contributions are welcome! If you have any suggestions or improvements, please create a pull request.

### License
This project is licensed under the MIT License.



