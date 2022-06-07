from asyncore import dispatcher
from multiprocessing.sharedctypes import Value
import requests
import json
from telegram.ext import Updater,CommandHandler,MessageHandler,filters
updater = Updater(token = '5339006488:AAFYSWAfHIM7pSNnnDl8HnEAc-ziH94E44Y',use_context = True)
dispatcher = updater.dispatcher
def hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="HELLLOOOOOO USERRRRR😎😎👍")
hello_hadler = CommandHandler('hello',hello)
dispatcher.add_handler(hello_hadler)
updater.start_polling()
def summary(update,context):
    response = requests.get('https://api.covid19api.com/summary')
    if response.status_code == 200:
        data = response.json()
        date = data['Date'][:10]
        answer = str(data['Global'].items())
        output =f'covid19 summary (AS OF {date}):\n'
        for attribute,Value in data['Global'].items():
            if attribute not in ['NewConfirmed','NewDeaths','NewRecovered']:
                output+='Total '+attribute[::].lower()+':'+str(Value)+'\n'
            
        context.bot.send_message(chat_id = update.effective_chat.id,text = output)




summaryhandler = CommandHandler('summary',summary)
dispatcher.add_handler(summaryhandler)


