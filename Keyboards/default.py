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

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Blok 💣"),
            KeyboardButton("Pachka 🧨")
        ]
    ],
    resize_keyboard=True

)

differentbooms = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Salyut 🎇'),
            KeyboardButton("Paqildoq 🧨")
        ],
        [
            KeyboardButton("Svetafor 🚦"),
            KeyboardButton("Lenta 📼")
        ],
    ],
    resize_keyboard=True
)

paqildoqturali = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mikki"),
            KeyboardButton("Titan")
        ],
        [
            KeyboardButton("Atrgul"),
            KeyboardButton("Chipaq")
        ]
    ],
    resize_keyboard=True
)
