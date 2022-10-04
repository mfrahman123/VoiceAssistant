import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# hear microphone and return audio as text
def transform_audio_into_text():

    #store recognizer in var
    r = sr.Recognizer()

    #set mic
    with sr.Microphone() as source:

        #waiting time
        r.pause_threshold = 0.8

        #report recording start
        print("You can now speak")

        #save audio
        audio = r.listen(source)

        #error catching
        try:
            # search on google
            request = r.recognize_google(audio,language="en-gb")

            # test in text
            print("You said " + request)

            return request
        except sr.UnknownValueError:

            print("Sorry, I didn't understand audio")

            return 'I am still waiting'

        except sr.RequestError:

            print("Sorry, there is no service")

            return 'I am still waiting'

        except:

            print("Sorry, Something went wrong")

            return 'I am still waiting'

def speak(message):


    #start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)

    #deliver message
    engine.say(message)
    engine.runAndWait()

def ask_day():

    # Create a variable with today information
    day = datetime.datetime.today()

    week_day = day.weekday()

    calendar = {0:'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}
    speak(f'Today is {calendar[week_day]}')

#Inform of the time
def ask_time():
    time = datetime.datetime.now()
    time = f'At this moment it is {time.hour} hours and {time.minute} minutes'
    speak(time)

#initial greeting
def initial_greeting():
    speak('Hello I am Hazel. How can I help you?')

# Main function
def my_assistant():

    initial_greeting()

    #Cut off variable
    go_on = True

    #Loop
    while go_on:

        #activate mic
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak('Sure, I am opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            webbrowser.open('https:www.google.com')
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue
        elif 'what time is it' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            speak('I am looking for it')
            my_request = my_request.replace('do a wikipedia search for','')
            answer = wikipedia.summary(my_request,sentences=1)
            speak('according to wikipedia: ')
            speak(answer)
            continue
        elif 'search the internet for' in my_request:
            speak('Of course ')
            my_request = my_request.replace('search the internet for','')
            pywhatkit.search(my_request)
            speak('This is what I found')
            continue
        elif 'play' in my_request:
            speak('oh, what a great idea! I will play it right now')
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {'apple': 'APPL',
                         'amazon' : 'AMZN',
                         'google' : 'GOOGL'}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f'I found it! The price of {share} is {price}')
                continue
            except:
                speak('I am sorry but I could not find it')
                continue
        elif 'goodbye' in my_request:
            speak('I am going to rest. Let me know if you need anything')
            break


my_assistant()