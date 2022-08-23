from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ikb_menu=InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Сообщение',callback_data='Сообщение'),
                                    InlineKeyboardButton(text='Ссылка',url='https://vk.com/akarumaibcl'),
                                ],
                                [
                                    InlineKeyboardButton(text='alert',callback_data='alert')
                                ],
                                [
                                    InlineKeyboardButton(text='Заменить кнопки меню',callback_data='Кнопки2')
                                ],
                                ])
