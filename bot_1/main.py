from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5482474945:AAHPNi1LETWW28Woi0FnaN6TWj6llsFIpU4").build()

app.add_handler(CommandHandler("hello", hello))
print("start cmpltd")

app.run_polling()