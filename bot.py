from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Your bot's token
TOKEN = "7569379124:AAFpsRTaydY5b73tG_B84iZ82W-T6HTe__I"

# Command to handle '/start'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to India Web Algorithms! We provide high-quality, cost-effective web and IT solutions. Use /help to see more!")

# Command to handle '/about'
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("At India Web Algorithms, we specialize in delivering tailored, high-quality web development and IT solutions to help businesses grow.")

# Command to handle '/services'
async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Our Services:  \n- Web Development \n- Digital Marketing \n- SEO Optimization \n- Graphic Designing \n- Web Hosting")

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are some website demos for your reference:\n 1. [Tradify Me](https://tradifyme.com/)\n \nFor more website demos or custom references, feel free to contact us. Send us a message at @StuckGrow.")


# Command to handle '/contact'
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Message for Services: @StuckGrow")

# Command to handle '/help'
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Here are the available commands:\n\n"
        "/start - Start the bot\n"
        "/about - Learn about our company\n"
        "/services - Explore our services\n"
        "/website-demo - Check some demo websites for reference\n"
        "/contact - Get in touch with us\n"
        "/help - Show this help message"
    )
    await update.message.reply_text(help_text)

# Handle regular messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()  # Get the message text
    if "hello" in user_message:
        await update.message.reply_text("Hi there! How can I assist you?")
    elif "help" in user_message:
        await update.message.reply_text("Sure! Type /help to get the available commands.")
    else:
        await update.message.reply_text("I'm not sure how to respond to that. Try typing /help.")

# Main function to run the bot
def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("services", services))
    application.add_handler(CommandHandler("website", website))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("help", help))  # Add the /help command handler

    # Add a message handler for text messages that are not commands
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
