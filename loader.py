from email import message
import logging
from aiogram import Bot, Dispatcher , executor , types 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config 

bot= Bot(token=config.BOT_TOKEN,parse_mode=types.ParseMode.HTML)



dp=Dispatcher(bot)