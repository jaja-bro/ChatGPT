from pyrogram import Client, filters
from requests import get

app = Client('my_bot')

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(chat_id = message.chat.id, text = 'The bot is running.', reply_to_message_id = message.id)

@app.on_message(filters.text)
async def handler(client, message):
    try:
        txt = message.text
        
        patience = await client.send_message(
            chat_id = message.chat.id,
            text = 'لطفا صبر کنید...',
            reply_to_message_id = message.id
        )
        
        url = f'''http://ehsancoder.b80.xyz/chatGpt.php/?text={txt}'''
        res = get(url).json()['message']

        await client.send_message(
            chat_id = message.chat.id,
            text = res,
            reply_to_message_id = message.id
        )
        await client.delete_messages(message.chat.id, [patience.id])

    except Exception as e :
        try :
            await client.send_message(
                chat_id= message.chat.id,
                text= f'Error : {e}',
                reply_to_message_id= message.id
            )
        except : pass   
        
app.run()
