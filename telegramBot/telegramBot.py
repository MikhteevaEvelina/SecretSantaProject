from aiogram.utils import executor
from createBot import dp
from aiogram.utils import executor

async def on_startup(_):
    print('Бот вышел в онлайн')

from handlers import client

client.register_handlers_client(dp)


executor.start_polling(dp, skip_updates = True, on_startup = on_startup)