from aiogram import Bot
from aiogram.dispatcher import Dispatcher, storage
import  os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage=MemoryStorage()

TOKEN='6543148667:AAHgAdeVPAxAVNlC80P0MWwGVtQGbLfj79Q'
bot = Bot(token=TOKEN)#переделал под token на время 

#bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
