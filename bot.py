import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("📄 PDF Tools", callback_data="pdf"),
            InlineKeyboardButton("🖼️ Image Tools", callback_data="image"),
        ],
        [
            InlineKeyboardButton("📝 Documents", callback_data="documents"),
            InlineKeyboardButton("💼 Resume Maker", callback_data="resume"),
        ],
        [
            InlineKeyboardButton("🤖 AI Solver", callback_data="ai"),
        ],
        [
            InlineKeyboardButton("💰 Buy Credits", callback_data="credits"),
            InlineKeyboardButton("👤 My Account", callback_data="account"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⚡ *QuickFix AI*\n\n"
        "Your All-in-One Utility Bot 🚀\n\n"
        "Choose a service below 👇"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "pdf": "📄 *PDF Tools*\n\nComing soon! 🚀",
        "image": "🖼️ *Image Tools*\n\nComing soon! 🚀",
        "documents": "📝 *Document Tools*\n\nComing soon! 🚀",
        "resume": "💼 *Resume Maker*\n\nComing soon! 🚀",
        "ai": "🤖 *AI Problem Solver*\n\nComing soon! 🚀",
        "credits": "💰 *Buy Credits*\n\nPayment system coming soon! 🚀",
        "account": "👤 *My Account*\n\nAccount system coming soon! 🚀",
    }

    text = responses.get(query.data, "❌ Something went wrong.")

    await query.edit_message_text(
        text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Main Menu", callback_data="menu")]]
        ),
    )


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "⚡ *QuickFix AI*\n\n"
        "Your All-in-One Utility Bot 🚀\n\n"
        "Choose a service below 👇"
    )

    await query.edit_message_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


def run_bot():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        CallbackQueryHandler(menu_handler, pattern="^menu$")
    )
    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("⚡ QuickFix AI Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    run_bot()
