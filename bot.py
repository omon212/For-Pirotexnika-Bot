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
from Keyboards.default import phone, location, menu, differentbooms, paqildoqturali
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



son = {
    'user_id': 1
}

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

class boom(StatesGroup):
    checkphone = State()
    checklocations = State()
    umumiy = State()


@dp.message_handler(commands=['start'])
async def start(message:Message,state:FSMContext):
    id = message.from_user.id
    print(id)
    await message.reply(f'''
Assalomu aleykum Xurmatli <b>{message.from_user.full_name}</b> 😁

Bot orqali Pirotexnika Vositalarini sotib olsanigiz boladi✅
Eng muximi Bizda Hammasi halol✅

Avvalam bor telegram nomeringizni kiriting ☎️ 
    ''',reply_markup=phone)
    await state.finish()
    await boom.checkphone.set()
@dp.message_handler(content_types=types.ContentType.CONTACT,state=boom.checkphone)
async def checksendphone(message:Message,state:FSMContext):
    await bot.send_message(6498877955,f'''
<b>Id 🆔</b> : {message.contact.user_id}
<b>Nomer 📱</b> : +{message.contact.phone_number}
    ''')
    await message.reply('Qayerdagi joylashuvga yetkazib berish kerak 📍',reply_markup=location)
    await state.finish()
    await boom.checklocations.set()

@dp.message_handler(content_types=types.ContentType.LOCATION,state=boom.checklocations)
async def checkloc(message:Message,state:FSMContext):
    await message.reply(f'''
Bizning botimizga Xush kelbisiz 😇

Quyidagi kategoriyalardan birin tanlang:
    ''',reply_markup=menu)
    await state.finish()
    await boom.umumiy.set()

#---------------BLOK----------------#

@dp.message_handler(text='Blok 💣',state=boom.umumiy)
async def blok(message:Message,state:FSMContext):
    url = 'https://adti.uz/wp-content/uploads/2020/12/2-63.jpg'
    await message.answer_photo(photo=url,caption="Tanlang : ",reply_markup=differentbooms)
    await state.finish()

@dp.message_handler(text='Paqildoq 🧨')
async def paqildoq(message:Message):
    print("Paqildoq")
    url = 'https://xabar.uz/static/crop/1/8/920__95_180670630.jpg'
    await message.answer_photo(photo=url,caption="<b>Paqildoq</b> turini tanlang : ",reply_markup=paqildoqturali)
@dp.message_handler(text='Mikki')
async def mikki(message:Message):

    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='mikki_minus'),
                InlineKeyboardButton("0", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='mikki_plus'),
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='mikki_savat'),
            ],
        ],

    )

    url = "https://i.ytimg.com/vi/v3hmWwsTxCk/maxresdefault.jpg"
    await message.answer_photo(photo=url,caption="Narxi : 10 000 so'm",reply_markup=new_buttons)

#-----------------mikki-----------------#




#-----------------------------#



@dp.callback_query_handler(text='mikki_minus')
async def mikki_minus(call:CallbackQuery):
    print(True)
    user_id = call.message.chat.id
    fake_son = son.get(user_id, 0)
    fake_son += 1
    son[user_id] = fake_son
    print(son)
    if fake_son == 0:
        await call.answer('0 dan ortga qaytib bolmaydi')

    await update_mikki_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_mikki_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='mikki_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='mikki_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='mikku_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='mikki_plus')
async def mikki_plus(call:CallbackQuery):
    print(True)
    user_id = call.message.chat.id
    fake_son = son.get(user_id, 0)
    fake_son += 1
    son[user_id] = fake_son
    print(son)
    if fake_son == 0:
        await call.answer('0 dan ortga qaytib bolmaydi')

    await update_mikki_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_mikki_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='mikki_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='mikki_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='mikki_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#---------------PACHKA----------------#
@dp.message_handler(text='Pachka 🧨',state=boom.umumiy)
async def pachka(message:Message,state:FSMContext):
    await message.answer('Tanlang : ')
    await state.finish()














if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)