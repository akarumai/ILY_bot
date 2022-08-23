from asyncore import dispatcher
from cgitb import text
from copyreg import dispatch_table
from email import message
from aiogram import types
from keyboards.default import keyboard_menu
from loader import dp 
from keyboards.default import kb_menu
from keyboards.default import kb_menu_da
from aiogram.utils.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram import Bot,Dispatcher
import urllib
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType,Message,InputFile,MediaGroup
from aiogram.types import LoginUrl
import requests
import logging
import random
from bs4 import BeautifulSoup


CHUNEL_ID=-750094713
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message:Message):
    await message.reply(message.video.file_id)



@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет,mоё золотце!💝 \n'
                        f'💗Ты самая лучшая девочка из всех,и это факт.\n'
                        f'💞Ты умеешь меня поддержать,хоть ты и думаешь что у тебя не получется это сделать.\n'
                        f'💕Ты невероятно красивая.\n'
                        f'❤️‍🩹Спасибо за все, что ты для меня делаешь.\n'
                        f'💘Я ценю, как хорошо ты ко мне относишься.\n'
                        f'Переходи в меню и смотри что я для тебя сделал => /menu')

@dp.message_handler(text='/help')
async def command_start(message: types.Message):
    await message.answer(f'Если у тебя возникла проблемка,напиши мне в телеграмм,всё исправлю ;) \n'
                         f'=========@Akarumai_bcl=========')

@dp.message_handler(text='/menu')
async def command_menu(message:types.Message):
    await message.answer('👀Выбери что хочешь посмотреть первым👀',reply_markup=kb_menu)

@dp.message_handler(text='Да?😏')
async def command_da(message: types.Message ):
    await message.answer('Pizda',reply_markup=kb_menu_da)

@dp.message_handler(text='Моя?')
async def command_moy(message: types.Message):
    await message.answer('Разумеется,солнышко💋')

@dp.message_handler(text='Назад🔮')
async def send_back(message: types.Message):
    await message.answer('Ты в меню',reply_markup=kb_menu)


@dp.message_handler(text='Твоя?')
async def send_video(message: Message):
    chat_id=message.from_user.id

    video_file_id='BAACAgIAAxkBAAIBUGMDcECSEr_2_fFCFe4DEh_1uU9KAALaHQAC9ywgSMOjOa50TRr3KQQ'

    await dp.bot.send_video(chat_id=chat_id,video=video_file_id,caption='Нет , у меня как бы...',)

@dp.message_handler(text='Фото меня😘')
async def send_photo(message: Message):
    chat_id=message.from_user.id
    arr=["media2/photo1.jpg","media2/photo2.jpg","media2/photo3.jpg","media2/photo4.jpg","media2/photo5.jpg","media2/photo6.jpg","media2/photo7.jpg","media2/photo8.jpg"] 
    photo_1=open(random.choice(arr), "rb")

    await dp.bot.send_photo(chat_id=chat_id,photo=photo_1)

@dp.message_handler(text='Фото где мы вместе😳')
async def send_photo(message: Message):
    chat_id=message.from_user.id
    arr=["media/photo1.jpg","media/photo2.jpg","media/photo3.jpg","media/photo4.jpg"] 
    photo_2=open(random.choice(arr), "rb")

    await dp.bot.send_photo(chat_id=chat_id,photo=photo_2)

@dp.message_handler()
async def send_photo(message: Message):
    button_text=message.text
    logger.debug('The answer is %r,button_text')
    if button_text=='Хочу домой':
        reply_text="Я лечу!!!"
    

    await message.reply(reply_text,reply_markup=types.ReplyKeyboardRemove())
    await dp.bot.send_message(CHUNEL_ID,button_text)

#@dp.message_handler()
#async def back(message: Message, state: FSMContext):
    #text = message.text
    #if 'Назад' in message.text:
        #await message.answer('Ты вернулся', reply_markup=kb_menu)
        #await kb_menu.Update.set()