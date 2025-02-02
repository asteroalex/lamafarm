from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Вставьте свой токен сюда
TOKEN = '7103273993:AAHLlt_j7Gbw2lZRn2APwe_eqA4mcx3r-vI'

async def start(update: Update, context: CallbackContext):
    photo_path = 'lamafarm.jpg'

    keyboard = [
        [InlineKeyboardButton("Начать фарм ⚡", url="https://t.me/LamaFarmBot/App")],
        [InlineKeyboardButton("Как это работает? 🤔", callback_data="how_it_works")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=open(photo_path, 'rb'),
        caption="👋 Хай! Это Lama farm - первый бот Telegram, в котором за просмотр рекламы тебя будут вознаграждать. Начинай свой фарм по кнопке ниже 👇",
        reply_markup=reply_markup
    )

async def how_it_works(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    photo_path = 'lamafarm.jpg'

    keyboard = [
        [InlineKeyboardButton("Начать фарм ⚡", url="https://t.me/LamaFarmBot/App")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_photo(
        photo=open(photo_path, 'rb'),
        caption="💰 *Lama farm* - первый бот в Telegram по заработку просто просматривая рекламу!\n\n"
                "1️⃣ Открой приложение по кнопке ниже\n"
                "2️⃣ Нажми *«Начать фарм»* и посмотри рекламу от наших партнеров\n"
                "3️⃣ Пока ты смотришь рекламу - бот майнит в-баксы, и ты их получишь как только досмотришь рекламу до конца\n\n"
                "Когда наберется нужное количество в-баксов – можешь смело их выводить! 🚀",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(how_it_works, pattern="^how_it_works$"))

    application.run_polling()

if __name__ == '__main__':
    main()
