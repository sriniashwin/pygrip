import json 
import requests
import time

import sqlite3

conn = sqlite3.connect('teldb01.sqlite')
cur = conn.cursor()

TOKEN = "" #Enter key for the script to work!
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

def main():

    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        try:
            text, chat, msgid, usr, etime = get_last_chat_details(get_updates())
        except:
            print("No updates found")
		
        humantime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(etime))
        
        if ((text == "/quitit") and (str(chat) == "12345")): # Enter correct chat ID
            print("Exit message received from user, ending program..")
            last_update_id = get_last_update_id(updates) + 2
            exit() 
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            #echo_all(updates)
            cur.execute('''INSERT INTO Log (User, MessageID, ChatID, Text, Timestamp) VALUES (?, ?, ?, ?, ?)''', (usr, msgid, chat, text, humantime,))
            conn.commit()
			
        #time.sleep(0.5)
		
if __name__ == '__main__':
    main()
