import telegram
import os

TOKEN = os.environ["TOKEN"]

bot = telegram.Bot(token=TOKEN)

get_me = bot.getMe()

updates = bot.getUpdates()

update = updates[-1]

chat_id = update.message.chat.id

text = update.message.text

last_update_id = update.update_id




while True:
    curr_updates = bot.getUpdates()

    curr_update = curr_updates[-1]

    chat_id = curr_update.message.chat.id
    current_update_id = curr_update.update_id
    
    if last_update_id!=current_update_id:

        text = curr_update.message.text
        chat_id= curr_update.message.from_user.id

        bot.send_message(chat_id, text)

        last_update_id = current_update_id
 