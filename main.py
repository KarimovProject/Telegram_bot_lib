import telegram
import os

TOKEN = os.environ["TOKEN"]

bot = telegram.Bot(token=TOKEN)

get_me = bot.getMe()

print(get_me.first_name)
