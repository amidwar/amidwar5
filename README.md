from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# التوكن الخاص ببوت Telegram
TOKEN = 8166763619:AAHfd3_oAPNbiuaqcqfEPR7yJDRvAqo6bVM

# إعداد البوت
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# وظيفة تجريبية للرد على الأوامر
def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا بك! البوت يعمل بنجاح 🎉")

# إضافة الأمر /start
dispatcher.add_handler(CommandHandler("start", start))

# تشغيل البوت
if name == "main":
    updater.start_polling()
    updater.idle()
