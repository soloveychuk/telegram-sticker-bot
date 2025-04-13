import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from apscheduler.schedulers.background import BackgroundScheduler
import time

# 🔐 Токен читається з середовища (Render -> Environment Variable)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 📥 ID чату (твій або каналу)
FORWARD_TO_ID = -1002553058634  # заміни, якщо потрібно

# 📌 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я телеграм-бот для стікерпаку Regbi_Phtl https://t.me/addstickers/Regbi_Phtl.\n"
        "Надішли мені фото або стікер і ми розглянемо їх для додавання у стікерпак!"
    )

# 📤 Пересилання повідомлень
async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.forward(chat_id=FORWARD_TO_ID)
    except Exception as e:
        print(f"Помилка при пересиланні: {e}")

# Функція для періодичного запуску
def periodic_task():
    print("Бот перевіряє з'єднання...")  # Це просто повідомлення в консолі, щоб підтримати активність бота

# 📅 Періодичне завдання
def start_periodic_task():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_task, 'interval', minutes=0.5)  # Перевірка кожні 10 хвилин
    scheduler.start()

# ▶️ Запуск
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, forward))

    # Запуск періодичного завдання
    start_periodic_task()

    print("Бот запущено...")
    app.run_polling()
