
import datetime


def parse(mssg):
    return mssg.lower().split()


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

    else:
        return("MHM... sorry I forgot to care.")


time = datetime.datetime.now()
message = input("Go ahead then, ... take my time.    ")
print(f"{time}    you: {message}")
mssg_parsed = parse(message)
usr_intent = intent(mssg_parsed)
print(f"{time}    jarvis: {reply(usr_intent)}")
