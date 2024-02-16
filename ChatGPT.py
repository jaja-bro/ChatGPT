from pyrogram import Client, filters
from requests import get

app = Client(
    'Account',
    api_id= 28761601,
    api_hash= 'dvnwdb51914b8d40799wce90a5oabb16'
)

app.on_message(filters.group & filters.text)
async def client(client, message):
    txt = message.text
    if txt.startswith('بات:'):
        try:
            patience = await client.send_message(
                chat_id= message.chat.id,
                text= 'لطفا صبر کنید...',
                reply_to_message_id= message.id
            )
            ask = txt.split('بات:')[1]
            url = f'https://magic-api.ir/apis/gpt/normal/gpt3.php?text={ask}'
            response = get(url).json()['message']

            await client.send_message(
                chat_id= message.chat.id,
                text= response,
                reply_to_message_id= message.id
            )
            await client.delete_message(message.chat.id, [patience.id])

        except Exception as e:
            await client.send_message(
                chat_id= message.chat.id,
                text= f'Error : {e}',
                reply_to_message_id= message.id
            )

app.run()



# ChatGPT-Telegram
ChatGPT client for telegram with python

## Installing libraries
```bash
pip install pyrogram
```
```bash
pip install requests
```

## Connection
Put your account's api_id and api_hash in lines 6 and 7

## run project
```bash
python3 chatGPT.py
```