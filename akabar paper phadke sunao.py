import requests
import json

def speak(string):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(string)


if __name__ == "__main__":
    r = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-09-18&sortBy=publishedAt&apiKey=ac342991e9e74c5fa8485d455c279937")
    load = json.loads(r.text)
    speak("first news is started")
    for articlesss in load["articles"]:
        speak(f'author of news are {articlesss["author"]}')
        speak(f'title of news is {articlesss["title"]}')
        speak(f'description of news is {articlesss["description"]}')
        speak("next news is")
            
