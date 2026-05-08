# 🔮 VizX-UB

<div align="center">
  <p><i>A simple, fast, lightweight, and highly customizable Telegram Userbot</i></p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL%20v3-pink?style=flat-square" alt="License"></a>
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platforms-Windows%20%7C%20Linux%20%7C%20Termux-green?style=flat-square" alt="Platforms">
</div>

---

## ✨ Features

- 🤖 **AI-Powered:** Gemini, Cohere, ChatGPT, image generation, upscaling, and more.
- 🧩 **Modular:** 30+ built-in modules + a curated custom-modules registry.
- 🌐 **Web UI:** Built-in dashboard for stats, module management, and logs.
- 🔁 **Self-updating:** `.update` pulls the latest from your remote.
- 🪟 **Cross-platform:** Windows, Linux, and Android (Termux).

---

## 🚀 Local Installation

### Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
.\start.bat
```

> Requires Python 3.11+ from [python.org](https://www.python.org/downloads/windows/). The installer creates `.venv`, installs dependencies, and prompts for API keys.

### Linux

```bash
chmod +x install.sh
./install.sh
./start
```

### Android (Termux)

```bash
chmod +x termux-install.sh
./termux-install.sh
```

---

## 🔑 Getting Started

1. **Get API credentials** from [my.telegram.org](https://my.telegram.org/) (API_ID and API_HASH).
2. **Run the installer** for your platform — it walks you through the rest.
3. **Optional API keys** (skip any you don't need):
   - `APIFLASH_KEY` — webshot module
   - `RMBG_KEY` — remove-background module
   - `VT_KEY` — VirusTotal lookup
   - `GEMINI_KEY` — Gemini AI modules
   - `COHERE_KEY` — Cohere AI modules

---

## 🧩 Modules

After login, in any chat send:

| Command | Purpose |
|---------|---------|
| `.help` | List all modules with command summaries |
| `.help [module]` | Show details for a specific module |
| `.hs [query]` | Fuzzy search modules and commands |
| `.ping` | Latency check |
| `.support` / `.repo` | Bot info, links, stats |
| `.version` | Build info (commit, branch, time) |
| `.update` | Pull latest from upstream and restart |
| `.restart` | Restart the bot |
| `.loadmod [name\|url]` | Install a custom module |
| `.unloadmod [name]` | Remove a custom module |

The default command prefix is `.` — change it with `.setprefix [char]`.

---

## 🖥️ Web Dashboard

Once running, open http://localhost:8000 (or whatever `PORT` you set in `.env`) for:

- Live uptime, CPU, and memory stats
- Module list (built-in + custom) with delete actions
- Tail of `vizxlogs.txt`

---

## 🐳 Docker

```bash
docker compose up -d
```

The compose file builds from the included `Dockerfile`. Set environment variables in `.env`.

---

## 🔄 Migrating Between Machines

`.env`, `db.sqlite3`, and `my_account.session` carry the bot's full state. Copy the project folder (skip `.venv`), recreate the venv on the target with `pip install -r requirements.txt`, and run `start.bat` / `./start`. No re-login needed.

---

## ⚠️ Disclaimer

> Use of this userbot is entirely at your own risk. The maintainers are not responsible for misuse, account bans, or any damages arising from your use of this software. You are solely responsible for ensuring compliance with Telegram's Terms of Service and all applicable laws.

---

## 📄 License

Released under the **GNU General Public License v3.0**. See [LICENSE](LICENSE) for the full text.
