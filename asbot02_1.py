import json 
import requests
import time

import sqlite3

#conn = sqlite3.connect('teldb01.sqlite')
#cur = conn.cursor()

TOKEN = "" #Enter Telegram api ID
URL = "https://api.telegram.org/bot{}/".format(TOKEN)



def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

#Original function, without offset
#def get_updates():
#    url = URL + "getUpdates"
#    js = get_json_from_url(url)
#    return js

#With offset parameter, to avoid retreiving all messages every time
def get_updates(offset=None):
    #url = URL + "getUpdates"
    #Instead of sending random updates, use Long Polling:
    url = URL + "getUpdates?timeout=100" 
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_details(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    message_id = updates["result"][last_update]["message"]["message_id"]
    try:
        user = updates["result"][last_update]["message"]["from"]["username"]
    except:
        user = "Not available"
    eptime = updates["result"][last_update]["message"]["date"]
    return (text, chat_id, message_id, user, eptime)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

#text, chat = get_last_chat_id_and_text(get_updates())
#send_message(text, chat)

#def main():
#    last_textchat = (None, None)
#    while True:
#        text, chat = get_last_chat_id_and_text(get_updates())
#        if (text, chat) != last_textchat:
#            send_message(text, chat)
#            last_textchat = (text, chat)
#        time.sleep(0.5)

#Contents from OWM to be written into this method, which will be called based on the if() condition within the while (True) loop in main()
#def getweatherdata(cityID):


def main():
    #flag = 1 #testing

    #Insert python code to retrieve weather parameters from OWM"
    # Define parameters to pass to URL
    owmapi = "" # Enter api ID from OWM
    cityID = "12345" #Enter cityID from list available on OWM
    outputunit = "metric"

    PARAMS = {'id':cityID, 'APPID':owmapi, 'units':outputunit}

    # url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s" % (cityID, owmapi)

    URL = "http://api.openweathermap.org/data/2.5/weather"

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()

    CloudCover = data["weather"]
    
	#We do not want to print any irrelevant info on chat
    #print (data)
    #print ("***")
    #print ("Current temp:", data ["main"]["temp"], "°C")
    #print ("Max temp:", data ["main"]["temp_max"], "°C")
    #print ("Min temp:", data ["main"]["temp_min"], "°C")
    #print ("Cloud cover:", CloudCover[0]["description"])
    #print ("Wind speed:", data["wind"]["speed"],"kmph")
	
	# End of contents from owm.py, figure out how to do this with using include functionality
	
	#Here the relevant params from json are being copied into variables that can be echo'd in the Telegram chat based on text entered by user
    currTemp = data ["main"]["temp"]
    maxTemp = data ["main"]["temp_max"]
    minTemp = data ["main"]["temp_min"]
    clouds = CloudCover[0]["description"]
    windSpeed = data["wind"]["speed"]
    
    firstTime = 1 #Used to avoid quitting based on quitit message from last use of program
    
    last_update_id = None
    userCity = "undefined" # to handle city entry by user, move that part of the code into teh while True loop
	
    while True:
        updates = get_updates(last_update_id)
        updatesFound = 1
		
        try:
            text, chat, msgid, usr, etime = get_last_chat_details(get_updates())
        except:
            print("No updates found")
            updatesFound = 0

        if (firstTime == 1): 
            text = "first time"

        if updatesFound == 1:
        #humantime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(etime))
        
            if ((text == "/quitit") and (str(chat) == "123456")): #Enter chat ID of user allowed to terminate python program from Telegram
                print("Exit message received from user, ending program..")
                #last_update_id = get_last_update_id(updates) + 2
                last_update_id = get_last_update_id(updates) + 2
                #flag = 0
                exit() 
            if (text == "/currenttemp"):
                send_message(currTemp,chat)

            if (text == "/windspeed"):
                send_message(windSpeed,chat)

            if (text == "/cloudcover"):
                send_message(clouds,chat)

            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                #echo_all(updates)
                #cur.execute('''INSERT INTO Log (User, MessageID, ChatID, Text, Timestamp) VALUES (?, ?, ?, ?, ?)''', (usr, msgid, chat, text, humantime,))
                #conn.commit()
			
            #time.sleep(0.5)
            firstTime = firstTime + 1
		
if __name__ == '__main__':
    main()