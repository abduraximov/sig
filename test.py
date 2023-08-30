import telegram
import asyncio


# bot = telegram.Bot(token='1907297658:AAF6PFeOWh8Fd7oRCrjcfkOCEx6GETUFHZM')
# chat_id = '@inform_lead'
# message = 'Test message from Python'
# bot.send_message(chat_id=chat_id, text=message)


async def send(msg, chat_id, token):
    bot = telegram.Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=msg)


asyncio.run(send(msg="assalamu alekum", chat_id="@inform_lead", token='1907297658:AAF6PFeOWh8Fd7oRCrjcfkOCEx6GETUFHZM'))


