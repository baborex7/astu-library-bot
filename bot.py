"""
ASTU Muslim Students Jema — Library Bot
----------------------------------------
A Telegram bot that lets students tap through
Semester -> Subject -> Category and get a Google Drive link.

Run locally:
    1. pip install -r requirements.txt
    2. Create a .env file with BOT_TOKEN=your_token_here
    3. python bot.py

See README.md for free hosting instructions.
"""

import logging
import os

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from config import BOT_NAME, CHANNEL_LINK, SEMESTERS

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# callback_data uses "|" as a separator between levels, and short
# codes (s0, subj0, cat0 ...) since Telegram limits callback_data to 64 bytes.


def _semester_keys():
    return list(SEMESTERS.keys())


def build_semester_menu():
    buttons = [
        [InlineKeyboardButton(sem, callback_data=f"sem|{i}")]
        for i, sem in enumerate(_semester_keys())
    ]
    return InlineKeyboardMarkup(buttons)


def build_subject_menu(sem_idx: int):
    sem_name = _semester_keys()[sem_idx]
    subjects = list(SEMESTERS[sem_name].keys())
    buttons = [
        [InlineKeyboardButton(subj, callback_data=f"subj|{sem_idx}|{i}")]
        for i, subj in enumerate(subjects)
    ]
    buttons.append([InlineKeyboardButton("⬅️ Back", callback_data="home")])
    return InlineKeyboardMarkup(buttons), sem_name


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"📚 *{BOT_NAME}*\n\n"
        "Assalamu alaikum! Tap a semester to browse course materials.\n\n"
        f"📢 Channel: {CHANNEL_LINK}"
    )
    await update.message.reply_text(
        text, reply_markup=build_semester_menu(), parse_mode=ParseMode.MARKDOWN
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use /start to browse the library.\n"
        "Tap Semester → Subject → Category, and I'll send you the Google Drive link."
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "home":
        await query.edit_message_text(
            f"📚 *{BOT_NAME}*\n\nTap a semester to browse course materials.",
            reply_markup=build_semester_menu(),
            parse_mode=ParseMode.MARKDOWN,
        )
        return

    parts = data.split("|")
    level = parts[0]

    if level == "sem":
        sem_idx = int(parts[1])
        menu, sem_name = build_subject_menu(sem_idx)
        await query.edit_message_text(
            f"📚 *{sem_name}*\n\nChoose a subject:",
            reply_markup=menu,
            parse_mode=ParseMode.MARKDOWN,
        )

    elif level == "subj":
        sem_idx, subj_idx = int(parts[1]), int(parts[2])
        sem_name = _semester_keys()[sem_idx]
        subj_name = list(SEMESTERS[sem_name].keys())[subj_idx]
        link = SEMESTERS[sem_name][subj_name]

        back_menu, _ = build_subject_menu(sem_idx)

        if not link or link == "ADD_LINK_HERE":
            text = (
                f"{subj_name}\n\n"
                "⏳ This folder hasn't been added yet. Check back soon, "
                f"or see the channel: {CHANNEL_LINK}"
            )
        else:
            text = f"{subj_name}\n\n📂 {link}"

        await query.edit_message_text(
            text, reply_markup=back_menu, disable_web_page_preview=False
        )


def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is not set. Create a .env file (see .env.example) "
            "or set the BOT_TOKEN environment variable on your host."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Bot starting with polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
