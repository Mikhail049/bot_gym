import os
import logging
import Modules.BL_common as bl
import pprint

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("BOT_API_TOKEN")

logging.basicConfig(level=logging.INFO)

#Initialize bot and dispatchet
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def other_command(message: types.Message):
    try:
        print(message)
        await message.reply(str(message.from_user.full_name) + ", your exercise is great! Wait a sec...")
        bl.parsingMessage(message)
        await message.reply(str(message.from_user.full_name) + ", all is ok! I add it to your stack.")
    except Exception as e:
        pprint.pprint(e)
        await message.reply(str(message.from_user.full_name) + ", something is going wrong...")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


print("Bot finish")

