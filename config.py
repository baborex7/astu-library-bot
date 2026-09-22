# ============================================================
# ASTU Muslim Students Jema — Library Bot configuration
# ------------------------------------------------------------
# Edit SEMESTERS below to add subjects, categories, or new
# semesters. Every category MUST have a Google Drive link.
# If you don't have a link yet, use the placeholder text
# "ADD_LINK_HERE" — the bot will tell students it's coming soon.
# ============================================================

BOT_NAME = "ASTU Muslim Students Jema Library Bot"

CHANNEL_LINK = "https://t.me/ASTU_FirstYear_Library"

# Structure: Semester -> Subject -> ONE Google Drive folder link.
# That folder can hold everything for the subject: books, notes,
# assignments, exams — just organize it with sub-folders inside
# Google Drive itself if you want (the bot doesn't need to know
# about those, students will see them once they open the link).
SEMESTERS = {
    "Semester 1": {
        "🧪 Chemistry": "https://drive.google.com/drive/folders/18-I-Es5ON8jF1xYDvlSHOEie8LaqmjDH",
        "⚛️ Physics": "https://drive.google.com/drive/folders/1iUFW8TqEC0Ve-0jOljF7LIi1TxvULv7l",
        "📐 Mathematics": "https://drive.google.com/drive/folders/1lEnmaDbieJN_J0RykFspOxfqw2UJOsTc",
        "🧠 Logic": "https://drive.google.com/drive/folders/1nMfZTV28-urzjlZIHJwjFUkJAHKTjbs0",
        "🐍 Python": "https://drive.google.com/drive/folders/12QraCni6AvsM6-k5peWwkPveEz8EssP6",
        "🗣️ English": "https://drive.google.com/drive/folders/1aTONIOpMIPWW-WNnbg_UlGT_wRWRyx5z",
        "🏛️ Civic": "https://drive.google.com/drive/folders/1xv9OQu5kp1B87tFSY5yoXSLEuq1Z4-qq",
        # Add more Semester 1 subjects here, same pattern, e.g.:
        # "💻 Introduction to Computing": "https://drive.google.com/drive/folders/....",
    },
    # Add "Semester 2": { ... } here later using the same structure.
}
