import logging
async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp) 

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Бот запущен')
  
if __name__ == '__main__':
    from aiogram import executor
    from handlers.users import dp 

executor.start_polling(dp, on_startup=on_startup)