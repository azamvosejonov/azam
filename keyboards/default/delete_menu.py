from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_delete=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Tasdiqlash"),
            KeyboardButton(text="❌Bekor Qilish"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


menu_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menu_button.add(KeyboardButton("🎥 Barcha Kinolar"))


