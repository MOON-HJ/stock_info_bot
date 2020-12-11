import telegram
import json

token = ""
master = ""
with open("config/info.config") as config:
    data = json.load(config)
    token = data["bot_token"]
    master = data["master"]


print(token)
print(master)

bot = telegram.Bot(token)
updates = bot.getUpdates()

chat_id = updates[-1].message.chat_id




bot.sendMessage(chat_id=chat_id, text="안녕하세요. 저는 봇입니다.")