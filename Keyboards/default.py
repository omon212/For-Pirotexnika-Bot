import requests
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Telefon raqamni yuborish ☎️',request_contact=True)
        ]
    ],
    resize_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Joylashuvni Yuborish 📍',request_location=True)
        ]
    ],
    resize_keyboard=True
)