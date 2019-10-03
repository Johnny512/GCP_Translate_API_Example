# Imports the Google Cloud client library
from google.cloud import translate

#Import json and os
import json, os

#Create environment variable with creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\[user]\\Downloads\\[file name].json"

def translate_json(file,target):
    # Instantiates a client
    translate_client = translate.Client()
    print('Calling Google Translate...')

    # Open and load json file into python dictionary
    with open(file) as json_file:
        data = json.load(json_file)

    #Create function to accept data and target language then return translated text.
    def google_translate(text,target):
        translated_text= translate_client.translate(
                text,
                target_language=target)
        return translated_text['translatedText']

    #Use dictionary comprehension to loop through text and apply translate function to values
    new_data = {key:google_translate(value,target) for (key, value) in data.items()}
    print('Translation into {} successful!'.format(target.upper()))

    #Return translated dictionary to write function
    return new_data

#Write translated values to file
with open('es.json','w') as outfile:
    json.dump(translate_json('en.json','es'),outfile,ensure_ascii=True,indent=1)
