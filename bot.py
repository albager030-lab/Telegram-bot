import os
import telebot

# جلب التوكن من متغيرات البيئة
BOT_TOKEN = os.getenv("")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN غير موجود في متغيرات البيئة")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ البوت يعمل بنجاح 24 ساعة!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("🤖 Bot is running...")

bot.infinity_polling()

