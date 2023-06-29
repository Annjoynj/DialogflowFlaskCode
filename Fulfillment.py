import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        req = request.get_json(force=True)
        intent_name = req['queryResult']['intent']['displayName']

        if intent_name == 'Forecast':
            location = req['queryResult']['parameters'].get('location')

            if location is None:
                fulfillment_text = "Sure, I can provide the weather forecast. However, I need to know the location. Please tell me the city name."
            else:
                city = location['city']

                # Make a request to the weather API
            base_url= 'https://api.openweathermap.org/data/2.5/weather?q=&appid=5912a61722fb5c2ba267fec878084651'
            params = {
                    'q': city
                   
                }
            response = requests.get(base_url, params=params)
            weather_data = response.json()

            temperature = weather_data.get('main', {}).get('temp', 0) - 273.15
            condition = weather_data.get('weather', [{}])[0].get('description', '')
            


                # Prepare the fulfillment text response
            fulfillment_text = f"The weather in {location} is {condition}. The current temperature is {temperature}°C."
        else:
            fulfillment_text = "I'm sorry, but I'm not sure how to respond to that."

        webhook_response = {
            'fulfillmentMessages': [
                {
                    'text': {
                        'text': [fulfillment_text]
                    }
                }
            ]
        }

        return jsonify(webhook_response)
    except Exception as e:
        print(str(e))  # Print the exception for debugging
        return jsonify({'fulfillmentMessages': [{'text': {'text': ['Sorry, an error occurred.']}}]}), 500

if __name__ == "__main__":
    app.run(debug=True)
