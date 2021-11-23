
import turtle
import random
import os
#install:
import requests
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
#PyAudio


        
#Create a window
window = turtle.Screen()
window.setup(1128,564)
window.bgpic('background2.gif')
window.title('MoveForward Smart Assistant')

#turtle to write the heading
heading = turtle.Turtle()
heading.penup()
heading.hideturtle()
heading.goto(0,150)
heading.write("Hey! I'm  chatbot, ask my anything about the ISS",align='center',font=('Comic Sans MS',25,'bold'))

#turtle to write on the chat box
DeeBot = turtle.Turtle()
DeeBot.hideturtle()
DeeBot.penup()
DeeBot.color('black')
DeeBot.right(90)
def text_to_speech(reply): #function to convert Text to Speech

    #language to use
    language_code = 'en'

    speed = False

    text = reply

    try :
        speech = gTTS(text = text , lang = language_code , slow = speed)
        speech.save('speech.mp3')
        playsound('speech.mp3')
        os.remove('speech.mp3')
    except:
        pass


def speech_to_text(): #function to convert Speech to Text

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        speech = r.listen(source)

        DeeBot.clear()
        DeeBot.write('Processing...' , align='center',font=('Courier',24,'bold'))
        DeeBot.goto(00,-210)
        #exception handling
        try:
            text = r.recognize_google(speech)
            DeeBot.clear()
            DeeBot.write('You said: {}'.format(text),align='center',font=('Courier',24,'bold'))
            return text
        except:

            DeeBot.clear()
            DeeBot.write('Sorry! Did not catch that...',align='center',font=('Courier',24,'bold'))    
            return "Empty"
             

def answer_question(): #function to answer the questions

    reply = '' #variable to store the replies

    #question = window.textinput("Hey! I'm DeeBot" , 'How are you feeling today?')
    DeeBot.goto(0,0)
    DeeBot.clear()
    DeeBot.write('Listening...' , align='center',font=('Courier',24,'bold'))
    user_input = speech_to_text()

    
    
    category = classify(user_input)

    if category == 'Salutation':
        reply = 'Hey Human!, test my knowledge...'
        
    elif category == 'Introduction':
        reply = 'Hello, I am the International Space Station, a large spacecraft orbiting around the earth.'             

    elif category == 'Purpose':
        reply = 'I act as space-home for scientists living in the space. I am also a part-time laboratory.'

    elif category == 'Full_Form':
        reply = 'My name is Station...the International Space Station.'

    elif category == 'Birthday':
        reply = "I cut my cake on 20th November every year. I've been doing this since 1998."

    elif category == 'CurrentLocation':
        reply = "I am flying 408 kilometers above the earth's surface"

    elif category == 'FunFact':
        reply = ISS_funfacts()

    #How many orbits of the Earth does the ISS complete in a day?92 orbits

    elif category == 'Empty' :
        reply = " "

    elif category == 'Exit':
        turtle.bye()
        return

    elif category == 'Error':
        return
    
   

    DeeBot.clear()
    DeeBot.goto(0,0)
    DeeBot.write(reply ,align='center',font=('Comic Sans MS',14,'bold'))
    
    text_to_speech(reply)

    

def classify(question):  #function to classify the user's questions

    key = "8071cef0-bdf9-11ea-95af-8120357a7d6008ab7537-5a22-40a4-9c32-57e4be98c882"
    url = 'https://machinelearningforkids.co.uk/api/scratch/'+ key + '/classify/'
    parameters = {'data' : question} #creating a dictionary to pass as a parameter
    response= requests.get(url , params = parameters)

    if response.status_code != 200:   #if the request was unsuccessful
        window.clearscreen()
        window.bgpic('Broken.gif')
        window.exitonclick()
        return 'Error'

    else: #if the request was successful
        data = response.json()
        print(data)
        #print(json.dumps(data , indent = 4))
        top_match  = data[0]
        category = top_match['class_name']
        return category
    


window.listen()
window.onkey(answer_question, 'space') 
window.mainloop()

















