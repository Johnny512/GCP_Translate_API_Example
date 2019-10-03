# GCP_Translate_Example
Uses Google Translate API to translate JSON object values into any language.
The main function loads the json file then converts to Python Dictionary.
Another function uses GCP Translate API which loops through each value in the Python Dictionary Comprehension.
Translated Dictionary is then written to file with json.dump() method which writes final json object.

## You must create an account with Google Cloud Translate API then download the Python Library.
This is the Quickstart example which this project is based on
[https://cloud.google.com/translate/docs/quickstart-client-libraries](https://cloud.google.com/translate/docs/quickstart-client-libraries)

