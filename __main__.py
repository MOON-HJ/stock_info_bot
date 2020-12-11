import telegram
import json
import get_domestic_stock_price
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = ""
master = ""
with open("config/info.config") as config:
    data = json.load(config)
    token = data["bot_token"]
    master = data["master"]


print(token)
print(master)

updater = Updater(token=token)#, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text="주식 정보 노예를 시작합니다")

def search(update, context): 
    text = "현재 " + update.message.text +"의 가격은 \'"
    + get_domestic_stock_price.get_stock_info(update.message.text)+"\'입니다." 
    print(update)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), search) ) 

updater.start_polling()
updater.idle()