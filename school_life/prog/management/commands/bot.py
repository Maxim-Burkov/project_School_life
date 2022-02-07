from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import Bot
from telegram import Update
from telegram.ext import Filters, CallbackContext, MessageHandler, Updater
from telegram.utils.request import Request


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        pass





