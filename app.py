
import datetime
import string

def parse(mssg):
    clean = ''.join([char for char in mssg if char not in string.punctuation])
    return clean.lower().split()

def intent(mssg_parsed):
    usr_intent = '' 
    if "remember" in mssg_parsed or "remind" in mssg_parsed:
        usr_intent = "reminder"

    if "weather" in mssg_parsed:
        usr_intent = "weather"

    if "joke" in mssg_parsed:
        usr_intent = "joke"

    if "shutdown" in mssg_parsed:
        usr_intent = "shutdown"

    if "help" in mssg_parsed:
        usr_intent = "help"

    return usr_intent 

def reply(intent):

    if intent == "reminder":
        return("I will remind you , Cause I apprearently have nothing better to do. ")
    elif intent == "weather":
        return(f"The weather seems fine to me, LOL.")
    elif intent == 'joke':
        return("Do i look like a clown to you?")
    elif intent == 'shutdown':
        return("Allright then , I guess . Bye.")
    elif usr_intent == "help":
        return("I can help you with reminding you of stuff , or I can maybe tell you joke.\n"
        " You can even try asking me about the weather.")

    else:
        return("MHM... sorry I forgot to care.")




print("Go ahead then, ... take my time.    ")
usr_intent = ''

while usr_intent != "shutdown":
    time = datetime.datetime.now()
    message = input()
    print(f"{time}    you: {message}")
    mssg_parsed = parse(message)
    usr_intent = intent(mssg_parsed)
    print(f"{time}    jarvis: {reply(usr_intent)}")