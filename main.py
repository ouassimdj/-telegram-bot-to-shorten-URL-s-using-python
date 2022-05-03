import telegram.ext
import pyshorteners
from check import keep_alive

keep_alive()

with open('token.txt', 'r') as f:
    token = f.read()


class linkshortner():
    def __init__(self) -> None:
        updater = telegram.ext.Updater(token, use_context=True)
        disp = updater.dispatcher
        disp.add_handler(telegram.ext.CommandHandler("start", self.start))
        disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, self.handle_link))
        updater.start_polling()
        updater.idle()
        
    def start(self, update, context):
        update.message.reply_text("""
        Hello, and welcome to "URL shortener" ;)
        PLEASE ENTER YOUR LINK HERE -->
        """)

    def handle_link(self, update, context):
        link = self.real_link(update.message.text)
        update.message.reply_text(link)
        
        
    def real_link(self, link):
        shortener = pyshorteners.Shortener()
        url = shortener.tinyurl.short(link)
        return f"{url} "



linkshortner()