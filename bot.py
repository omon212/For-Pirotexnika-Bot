import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import CallbackQuery,Message

#----------------STATE----------------#
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboards.accses import API_TOKEN
from Keyboards.default import phone,location

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

class boom(StatesGroup):
    checkphone = State()
    checklocations = State()


@dp.message_handler(commands=['start'])
async def start(message:Message,state:FSMContext):
    await message.answer(f'''
Assalomu aleykum Xurmatli <b>{message.from_user.full_name}</b> 😁

Bot orqali Pirotexnika Vositalarini sotib olsanigiz boladi✅
Eng muximi Bizda Hammasi halol✅

Avvalam bor telegram nomeringizni kiriting ☎️ 
    ''',reply_markup=phone)
    await state.finish()

@dp.message_handler(content_types=types.ContentType.CONTACT,state=boom.checkphone)
async def checksendphone(message:Message,state:FSMContext):
    await message.answer('Qayerdagi joylashuvga yetkazib berish kerak 📍',reply_markup=location)
    await state.finish()
    await boom.checklocations.set()

@dp.message_handler(content_types=types.ContentType.LOCATION,state=boom.checklocations)
async def checkloc(message:Message,state:FSMContext):
    await message.answer(f'''
Bizning botimizga Xush kelbisiz 😇    
    ''',)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)