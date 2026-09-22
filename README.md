# ASTU Muslim Students Jema — Library Bot

A Telegram bot for browsing course materials by **Semester → Subject → Category**,
each linking out to a Google Drive folder.

## 1. Create the bot on Telegram

1. Open Telegram, message **@BotFather**.
2. Send `/newbot`, choose a name (e.g. "ASTU MSJ Library") and a username
   ending in `bot` (e.g. `astu_msj_library_bot`).
3. BotFather gives you a **token** like `123456789:AAExample...`. Save it.

## 2. Add your Google Drive links

Open `config.py`. Replace every `"ADD_LINK_HERE"` with the real shareable
Google Drive folder link for that subject/category. Make sure each Drive
folder's sharing setting is **"Anyone with the link can view."**

To add more subjects (e.g. "Introduction to Computing") or a "Semester 2"
block, copy the pattern already in the file — instructions are commented
inside `config.py`.

## 3. Run it locally (to test)

```bash
pip install -r requirements.txt
cp .env.example .env
# edit .env and paste your real BOT_TOKEN
python bot.py
```

Open Telegram, find your bot, send `/start`. Tap through the menus to
confirm the links work, then stop the script (Ctrl+C).

## 4. Deploy for free — Railway (recommended)

Railway runs the bot as a background "worker" process, which fits this
kind of always-on polling bot well.

1. Push this folder to a new GitHub repository.
2. Go to https://railway.app → sign in with GitHub → **New Project** →
   **Deploy from GitHub repo** → select your repo.
3. In the Railway project settings, add an environment variable:
   - `BOT_TOKEN` = your token from BotFather.
4. Railway will detect the `Procfile` and run `python bot.py` automatically.
5. Check the **Deploy Logs** — you should see `Bot starting with polling...`.

Railway's free trial credit is enough to keep a small bot like this running
continuously for a good while. Once it runs out, you can move to Fly.io or
add a payment method for a few dollars a month.

### Alternative: Fly.io / PythonAnywhere

- **Fly.io** also supports small always-on background processes on its
  free allowance — deploy with `fly launch`, set `BOT_TOKEN` as a secret
  (`fly secrets set BOT_TOKEN=...`), and it will use the same `Procfile`/
  `bot.py`.
- **PythonAnywhere**'s free tier does *not* support long-running background
  processes (only scheduled tasks and web apps), so it isn't a good fit for
  this polling-based bot without a paid plan.

## 5. Keeping it updated

Whenever you get a new Drive folder link, edit `config.py`, commit, and
push — Railway/Fly will redeploy automatically. No need to touch `bot.py`.

## Commands

- `/start` — opens the Semester menu
- `/help` — quick usage reminder
