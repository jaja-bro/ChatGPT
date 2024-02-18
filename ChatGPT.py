from pyrogram import Client, filters
from requests import get

api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"
bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"

app = Client(
    "my_account",
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(chat_id = message.chat.id, message = 'The bot is running.', reply_to_message_id = message.id)


app.on_message(filters.text)
async def client(client, message) :
    txt = message.text
    if txt.startswith('چت:') :
        try:
            patience = await client.send_message(
                chat_id = message.chat.id,
                text = 'لطفا صبر کنید...',
                reply_to_message_id = message.id
            )
            ask = txt.split('بات:')[1]
            url = f'http://mahrez.iapp.ir/santcoin/index.php?text={ask}'
            res = get(url).json()['message']

            await client.send_message(
                chat_id = message.chat.id,
                text = res,
                reply_to_message_id = message.id
            )
            await client.delete_message(message.chat.id, [patience.id])

        except Exception as e :
            try :
                await client.send_message(
                    chat_id= message.chat.id,
                    text= f'Error : {e}',
                    reply_to_message_id= message.id
                )
            except : pass            
            
app.run()



