import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio

logging.basicConfig(level=logging.INFO)

API_TOKEN = '7940509241:AAGFZ6qlw9pEenpsAzZslOIqKvOHyxMRptc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

router = Router()

# Создаем клавиатуру с кнопкой для команды /help
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Помощь")]  # Кнопка для вызова /help
    ],
    resize_keyboard=True  # Автоматическая подстройка размера кнопок
)

# Функция-хендлер для команды /start
async def send_welcome(message: Message):
    await message.answer("Привет! Я ваш новый бот. Вот список доступных команд:", reply_markup=keyboard)

# Функция-хендлер для команды /help
async def send_help(message: Message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать список команд"
    )
    await message.answer(help_text)

# Регистрация хендлеров для команд /start и /help
router.message.register(send_welcome, Command(commands=['start']))
router.message.register(send_help, Command(commands=['help']))

async def main():
    # Добавляем router к диспетчеру
    dp.include_router(router)

    # Запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
