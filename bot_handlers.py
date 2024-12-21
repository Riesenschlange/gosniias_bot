from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from bot_token import BOT_TOKEN

gosniias_bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer("Привет!\nЯ создан для облегчения жизни всех работников подразделения № 3100.\n\nВнизу представлены команды, с которыми я могу помочь.")


@dp.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer("Вот список доступных команд. Если тебе нужно проконтактировать напрямую - напиши сообщение @julisimp")


if __name__ == '__main__':
    dp.run_polling(gosniias_bot)