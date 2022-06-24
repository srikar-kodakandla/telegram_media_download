from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm

api_id=173231312443  #change this to your api_id
api_hash='fcf80641103ws2cd0adede64dc85095' #change this to your api_hash


messag=0
def download_media(group, cl, name):
    global messag
    messages = cl.get_messages(group, limit=200000)
    try:
        for message in tqdm(range(messag-1,len(messages)+1)):
            messages[message].download_media('./' + name + '/')
            messag=message
        print(message)    
    except:
        download_media(channel.full_chat, client, title)
  
    #print(message)


with TelegramClient('name', api_id, api_hash) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=50000,
        hash=0,
    ))

    title = 'Chat Title'            # Title for group chat
    for chat in result.chats:
        print(chat)

        if chat.title == title:
            download_media(chat, client, title)

    title = 'Channel title'         # Title for channel
    channel = client(GetFullChannelRequest(title))
    print(channel.full_chat)

    download_media(channel.full_chat, client, title)
