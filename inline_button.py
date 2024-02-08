from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Batafsil", callback_data="alert")],
    [InlineKeyboardButton(text="Sotib Olish 🛒", callback_data="inline", url="https://t.me/DIMA_156")]
])
