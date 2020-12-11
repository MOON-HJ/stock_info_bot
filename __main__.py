import telegram
import json
import get_stock_price
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
    context.bot.send_message(chat_id=update.effective_chat.id, text="주식 정보 노예를 시작합니다")

def echo(update, context): 
    text = "현재 " + update.message.text +"의 가격은 \'"+get_stock_price.get_stock_info(update.message.text)+"\'입니다." 
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo) 
dispatcher.add_handler(echo_handler) 


updater.start_polling()
updater.idle()