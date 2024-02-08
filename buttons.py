from aiogram import types

btn = [
    [types.KeyboardButton(text="O'g'il 🙍‍♂️"), types.KeyboardButton(text="Qiz 🙍‍♀️")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True, input_field_placeholder="Tanlang:")

btn_boy1 = [
    [types.KeyboardButton(text="Bosh kiyim 🧢"), types.KeyboardButton(text="Ustki kiyim 👕")],
    [types.KeyboardButton(text="Pastki kiyim 👖"), types.KeyboardButton(text="Oyoq kiyim 🥾")],
    [types.KeyboardButton(text="🔙 Orqaga qaytish")]
]
button_boy = types.ReplyKeyboardMarkup(keyboard=btn_boy1, resize_keyboard=True, input_field_placeholder="Tanlang:")

btn_girl1 = [
    [types.KeyboardButton(text="Bosh kiyim 👒"), types.KeyboardButton(text="Ustki kiyim 👗")],
    [types.KeyboardButton(text="Pastki kiyim 👖"), types.KeyboardButton(text="Oyoq kiyim 👠")],
    [types.KeyboardButton(text="🔙 Orqaga qaytish")]
]
button_girl = types.ReplyKeyboardMarkup(keyboard=btn_girl1, resize_keyboard=True, input_field_placeholder="Tanlang:")
