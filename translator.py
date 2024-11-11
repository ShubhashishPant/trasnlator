import requests
import uuid
import json

class Translator:
    def __init__(self, api_key, location):
        self.api_key = api_key
        self.endpoint = "https://api.cognitive.microsofttranslator.com"
        self.location = location

    def translate(self, text, target_languages):
        path = '/translate'
        constructed_url = self.endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'en',
            'to': target_languages
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{'text': text}]
        
        response = requests.post(constructed_url, params=params, headers=headers, json=body)

        # Debugging: Print the full response
        print("Response from translation API:", response.json())
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Translation API error: {response.status_code} - {response.text}")
