# from flask import Flask, request, render_template
# from translator import Translator

# app = Flask(__name__)
# translator = Translator(api_key='7339a05f37764826b5fa9d33033cdf92', location='centralindia')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     translation = ''
#     if request.method == 'POST':
#         text = request.form['text']
#         target_language = request.form['language']

#         # Basic validation: Check if the input text is gibberish
#         if len(text) < 1:  # Example condition: reject very short text
#             translation = "Please enter more meaningful text."
#         else:
#             try:
#                 response = translator.translate(text, target_language)
#                 print(response)  # Debug line to inspect the response structure

#                 # Check if the response contains translations
#                 if response and isinstance(response, list) and len(response) > 0:
#                     translations = response[0].get('translations', [])
#                     if translations:
#                         translated_text = translations[0].get('text', "Translation not available.")
#                         # Check if translated text is the same as input
#                         if translated_text.lower() == text.lower():
#                             translation = "Translation not available or input was gibberish."
#                         else:
#                             translation = translated_text
#                     else:
#                         translation = "Translation not available."
#                 else:
#                     translation = "Translation not available."
#             except Exception as e:
#                 translation = f"Error: {str(e)}"

#     return render_template('index.html', translation=translation)


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template
from translator import Translator
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Retrieve API key and location from environment variables
api_key = os.getenv('TRANSLATOR_API_KEY')
location = os.getenv('TRANSLATOR_LOCATION')

if not api_key or not location:
    raise ValueError("API key or location not set in environment variables")

translator = Translator(api_key=api_key, location=location)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['language']

        # Basic validation: Check if the input text is gibberish
        if len(text) < 1:  # Example condition: reject very short text
            translation = "Please enter more meaningful text."
        else:
            try:
                response = translator.translate(text, target_language)
                print(response)  # Debug line to inspect the response structure

                # Check if the response contains translations
                if response and isinstance(response, list) and len(response) > 0:
                    translations = response[0].get('translations', [])
                    if translations:
                        translated_text = translations[0].get('text', "Translation not available.")
                        # Check if translated text is the same as input
                        if translated_text.lower() == text.lower():
                            translation = "Translation not available or input was gibberish."
                        else:
                            translation = translated_text
                    else:
                        translation = "Translation not available."
                else:
                    translation = "Translation not available."
            except Exception as e:
                translation = f"Error: {str(e)}"

    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
