from telegram.ext import Updater, CommandHandler

# إعداد التوكن الخاص بالبوت
TELEGRAM_TOKEN = "8166763619:AAHfd3_oAPNbiuaqcqfEPR7yJDRvAqo6bVM"  # استبدل بالتوكن الخاص بك

# دالة الترحيب
def start(update, context):
    update.message.reply_text('مرحبًا! أنا بوت Telegram يعمل على Render.')

# الدالة الرئيسية
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة الأوامر
    dp.add_handler(CommandHandler("start", start))

    # بدء البوت
    updater.start_polling()
    updater.idle()

# تشغيل الدالة الرئيسية
if __name__ == "__main__":
    main()