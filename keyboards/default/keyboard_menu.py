from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Фото меня😘'),
            KeyboardButton(text='Фото где мы вместе😳'),
            KeyboardButton(text='Стикеры😼')
        ],
        [
            KeyboardButton(text='Рандомный мем🗿'),
            KeyboardButton(text='Картинка из Pinterest🎆'),
            KeyboardButton(text='Да?😏')
        ],
        [
            KeyboardButton(text='Хочу домой'),
        ],
    ],
    resize_keyboard=True
)

kb_menu_da=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Моя?'),
            KeyboardButton(text='Твоя?'),
           
        
        ],
        [
            KeyboardButton(text='Назад🔮')
        ],

    ],
    resize_keyboard=True
)