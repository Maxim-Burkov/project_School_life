from django.core.management.base import BaseCommand
from django.conf import settings

from django.contrib import admin


from telegram import Bot
from telegram import Update
from telegram.ext import Filters, CallbackContext, MessageHandler, Updater
from telegram.utils.request import Request

# from .models import Profile
# from .models import Homework


def test(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text


    reply_text = 'Ваш id = {}\n\n{}'.format(chat_id, text)
    update.message.reply_text(
        text = reply_text,
    )


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        # Подключение бота
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True,
        )
        message_handler = MessageHandler(Filters.text, test)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()





