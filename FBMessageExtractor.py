"""
#FBMessageExtractor.py - Written by Brendan Wilby 20/08/2019

This script can be used to extract all individual Facebook messages from the HTML file containing all messages - provided by Facebook upon request.

===============================
USAGE
==============================

1. The data can be found in your Facebook settings, by clicking "Your Facebook Information". 
2. Request your messages in HTML format - then wait until they provide a download link
3. Extract the zip file to somewhere safe, even password protect it if you can, especially if you don't want other people reading/accessing this data!!!
4. Navigate to "messages/inbox/{name of conversation/person/group}/message_1.html" (or similar) and copy this path
5. Simply input this path to the extract_messages function, which will return you a list of every message

"""

from bs4 import BeautifulSoup

def extract_messages(path):
    messages = []
    html = open(path)
    soup = BeautifulSoup(html, "lxml")

    div_msg_element = soup.findAll("div", {"class" : "_3-96 _2let"})

    for div in div_msg_element:
        messages.append(div.text)
    
    return messages
