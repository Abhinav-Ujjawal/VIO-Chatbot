import os
import pyttsx3
import speech_recognition as sr
import openai
import textwrap
# put your api key here
openai.api_key = "sk-????????????????????????????????????????????????"
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Speed in wpm
engine.setProperty('volume', 1) # Volume (0-1)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # Volume (0-1)

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Pardon me but I could not recognize your speech."
    except sr.RequestError as e:
        return "Pardon me but I am currently facing problem in detecting your language due to server error at our end. I apologize for this."

# history=[]
chat=""
def generate_response(question):
    global chat
    chat+=question+'\n'
    prompt = question+"\n"
    # history.append({'role':'user',"content":prompt})
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=chat,
            max_tokens=100,
            temperature=0.7,
            # messages=history
        )
        reply = response.choices[0].text.strip()
        return reply
    except:
        return "We are currently facing a rate limit error due to high demand and hence am not able to extract answer at the moment. I apologise for the inconvenience."
    # history.append({'role':'assistant',"content":reply})

os.system('cls')

print("""
         Welcome to the ChatBot 
         This chatbot attempts to answer your queries using voice input and output 
         Hope you have an enjoyable experience.\n""")

# r=generate_response('Answer anything that is asked')
# wrapped_text = textwrap.wrap(r, width=150)
# for line in wrapped_text:
#     print(line,end="")
# print()
# engine.say(r)
# engine.runAndWait()

engine.say("Welcome to the ChatBot. This chatbot attempts to answer your queries using voice input and output. Hope you have an enjoyable experience!")
engine.runAndWait()
while(True):
    text=recognize_speech()
    if text=="Pardon me but I could not recognize your speech.":
        print("\033[4mResponse detected\033[0m: ???",)
        print("\033[4mResponse generated\033[0m: ",text,end="")
        print()
        engine.say(text)
        engine.runAndWait()
        continue

    elif text=="Pardon me but I am currently facing problem in detecting your language due to server error at our end. I apologize for this.":
        print("\033[4mResponse detected\033[0m: ???",)
        print("\033[4mResponse generated\033[0m: ",text,end="")
        print()
        engine.say(text)
        engine.runAndWait()
        continue

    print("\033[4mResponse detected\033[0m: ", (str(text[0])).upper(),text[1:],sep="")
    user_question = text
    response= generate_response(user_question)
    print("\033[4mResponse generated\033[0m: ",end="")
    wrapped_text = textwrap.wrap(response, width=150)
    for line in wrapped_text:
        print(line,end="")
    print()
    ### text to speech..
    engine.say(response)
    engine.runAndWait()