def add ():
    x, y = int (input ('enter a number')), int (input ('enter the second number: '))
    return x + y
def sub ():
    x, y = int (input ('enter a number')), int (input ('enter the second number: '))
    return x - y


if __name__ == 'main':
    x = int (input ())
    print (searchDictionary [x])
    
searchDictionary = {
    1 : add (),
    2 : sub ()import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb
import os

engine = pyttsx3.init ('sapi5')
voices = engine.getProperty ('voices')
engine.setProperty ('voice', voices [1].id)
def speak (audio):
    engine.say (audio)
    engine.runAndWait ()
import datetime
def wishMe ():
    wishingString = ''
    hour = int (datetime.datetime.now ().hour)
#     print (hour)
    if (hour >= 4 and hour < 12):
        wishString = 'Good Morning'
    elif (hour == 12):
        wishString = 'Good Noon'
    elif hour > 12 and hour < 16:
        wishString = 'Good Afternoon'
    elif hour >= 16 and hour < 21:
        wishString = 'Good Evening'
    else: wishString = 'Good Night'
    if wishString == 'Good Night':
        string = f'Hey Malay how may I help you'
        speak (string)
    string = f'Hello Malay {wishString}, How May I Help you'
    speak (string)
wishMe ()
def getLocation ():
    import geocoder

    g = geocoder.ip('me')
    return g.latlng
def search (query):
    string = query.lower ()
    if 'maps' in string:
        location = getLocation ()
        getLoc = f'https://www.google.co.in/maps/@{location [0]},{location [1]},15.33z'
#         speak (location)
        wb.open (getLoc)
    if 'google' in string:
        wb.open ('google.com')
    elif 'yahoo' in string:
        wb.open ('yahoo.com')
    elif 'youtube' in string:
        wb.open ('youtube.com')
    elif 'facebook' in string:
        wb.open ('facebook.com')
    elif 'twitter' in string:
        wb.open ('twitter.com')
    elif 'instagram' in string:
        wb.open ('instagram.com')
    elif 'baidu' in string:
        wb.open ('baidu.com')
def time ():
    strtf = datetime.datetime.now().strftime ('%H:%M:%S')
    speak (f'The time is : {strtf}')
def takeCommand ():
    '''
    it takes microphone input
    '''
    print ('Please wait')
    r = sr.Recognizer ()
    with sr.Microphone() as source:
        print ('ask about anything')
        r.pause_threshold = 1
    try:
        print ('Recognizing')
        query = r.recognize_google (audio, language = 'en-in')
        print (f'user said: {query}')
        query = query.lower()
        if 'search' or 'open' in query:
            if 'search' in query: query = query.replace ('search', '')
            elif 'open' in query: query = query.replace ('open', '')
        elif 'the time' in query: 
            search (query)
#         if query == 'wikipedia':
#             results = wk.summary (query, sentences = 2)
#             speak ('According to wikipedia')
#             speak (results)
    except Exception as e:
        print (e)
        print ("Say that again please")
        return 'None'
    if query == 'pause':
        return 
    speak (query)
    return query

while True:
    try:
        time ()
        break
    except:
        print ('sorry cant find this data')
}