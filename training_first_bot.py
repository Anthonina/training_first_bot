import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # Импорт необходимых компонентов

import settings

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'training_first_bot.log'
                    )


def start_bot(bot, update):
    hitext = ('Здравствуй, {}! Рад общению! '
        'Я простой бот и понимаю только команду {}'
    ).format(update.message.chat.first_name, '/start')
    
    update.message.reply_text(hitext)

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    upd = Updater(settings.TELEGRAM_API_KEY) # Уникальный код, который выдаёт @BotFather
    
    upd.dispatcher.add_handler(CommandHandler('start', start_bot))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    
    upd.start_polling() 	# Подключаемся к платформе
    upd.idle()

# Проверка. Если файл запустили напрямую, то функция отработает. 
# Если файл куда-то импортировать и, например, использовать его. 
# Так как в нём находятся какие-то функции, - при импорте часть 
# вызова функции не отработает, и не возникнет ошибки.
if __name__ == '__main__': 
    logging.info('Bot started')
    main()
