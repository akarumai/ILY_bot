#создаём переменную бота
#bot=Bot(token='5753969399:AAEr_8ii5CSUJTt19_28il5F9SQZ2mnJ7eI')

# создаём Dispatcher ,он принимает все апдейты и обрабатывает их. Можете отправлять сообщения как вам удобно, хоть await mybot.bot.send_sticker хоть await bot.send_sticker лишь бы импортировали все правильно

#dp=Dispatcher(bot) 

#@dp.message_handler() #все сообщения 
#async def get_message(message: types.Message):
#Если в скобках написано (message: types.Message) то к скрипте мы можем использовать message вместо types.Message

# Пример получения айпи пользователя:
    #chat_id=types.Message.chat.id # first
    #chat_id=message.chat.id # secod
# функционал не меняется 

#Отпревка сообщения пользователю №1
    #chat_id=message.chat.id
    #text='Хай'

    #await bot.send_message(chat_id=chat_id,text=text) 

#executor.start_polling(dp)
#Отпревка сообщения пользователю №2
   #text='ку'
    #await message.answer(text=text)

##executor.start_polling(dp)
    # 
    # 
    # 