# 🔄 VizX-UB Rebranding Plan & Module Output Templates

## Part 1: Rebranding Scope

### Files to Rebrand (48 files total)

Every file below contains one or more "Moon" references that need replacing. The modules repo URLs (`The-MoonTg-project/custom_modules`) are **excluded** from rebranding per your request.

#### Branding Map
| Old | New |
|-----|-----|
| `Moon-Userbot` | `VizX-UB` |
| `Moon Userbot` | `VizX-UB` |
| `Moon_Userbot` | `VizX_UB` |
| `moonuserbot` (docker/compose) | `vizxub` |
| `Moon-userbot` | `VizX-UB` |
| `moonub` (db name) | `vizxub` |
| `moonlogs.txt` | `vizxlogs.txt` |
| `Moon` (PM2/systemd process) | `VizX` |
| `Moon_Userbot_Notes_Filters` (supergroup) | `VizX_UB_Notes_Filters` |
| `moonuserbot` (telegram channel) | Keep as-is (external link, unless you have your own) |
| `moonub_chat` (telegram chat) | Keep as-is (external link, unless you have your own) |
| `moonub_modules` (telegram channel) | Keep as-is (external link, unless you have your own) |
| `@Moonub_chat` (help link) | Replace with your own support link |
| `moon_` (variable in string_gen.py) | `vizx_` |
| Header comment `Moon-Userbot - telegram userbot` | `VizX-UB - telegram userbot` |
| Header comment `Moon Userbot Organization` | `VizX-UB` |

> [!IMPORTANT]
> The **modules repo** (`The-MoonTg-project/custom_modules`) URLs are **NOT** changed — only the branding text, headers, user-facing strings, and the git remote for the **main repo** (`The-MoonTg-project/Moon-Userbot`).

---

### Files by Category

#### 🔧 Core Python Files
| File | Changes |
|------|---------|
| `main.py` | Header, `device_model`, `moonlogs.txt` → `vizxlogs.txt`, log message |
| `app.py` | `moonlogs.txt` → `vizxlogs.txt` (2 locations) |
| `install.py` | Header, PM2/systemd names, launch message, channel refs |
| `string_gen.py` | ASCII banner, copyright text, variable name |

#### 🧰 Utils
| File | Changes |
|------|---------|
| `utils/__init__.py` | Header, git remote URL |
| `utils/scripts.py` | Header only |
| `utils/module.py` | Help page header link |
| `utils/handlers.py` | Header only |
| `utils/db.py` | Header only |
| `utils/conv.py` | Header only |

#### 📦 Modules (Prebuilt)
| File | Changes |
|------|---------|
| `modules/help.py` | Header only |
| `modules/ping.py` | Header only |
| `modules/support.py` | Header, **all user-facing text** (support info, version, repo links) |
| `modules/updater.py` | Header, `moonlogs.txt` → `vizxlogs.txt` |
| `modules/loader.py` | Header only (module repo URLs stay) |
| `modules/upl.py` | Header, `moonlogs` command → `vizxlogs`, log filename |
| `modules/filters.py` | Header, `Moon_Userbot_Notes_Filters` → `VizX_UB_Notes_Filters` |
| `modules/notes.py` | Header, `Moon_Userbot_Notes_Filters` → `VizX_UB_Notes_Filters` |
| `modules/example.py` | Header only |
| `modules/id.py` | Header only |
| All other modules | Header only (admintool, admlist, afk, antipm, clear_notifs, open, prefix, purge, python, removebg, say, sendmod, sessionkiller, sgb, shell, spam, squotes, stickers, thumbnail, user_info, vt) |

#### 🐳 Deployment
| File | Changes |
|------|---------|
| `compose.yml` | `moonuserbot` → `vizxub` |
| `docker-compose.yml` | `moonuserbot` → `vizxub` |
| `render.yaml` | Service name, repo URL |
| `app.json` | Name, keywords, description refs, STRINGSESSION desc |
| `install.sh` | All `Moon-Userbot` refs, PM2/systemd names, db_name |
| `termux-install.sh` | All `Moon-Userbot` refs, db_name |

#### 📄 Docs & HTML
| File | Changes |
|------|---------|
| `README.md` | Full rewrite with VizX-UB branding |
| `public/base.html` | Title and header |

---

## Part 2: Module Output Template Drafts

### Current Output Style (Before)
The current modules produce very basic, flat HTML output like:

```
.ping → Pong! 123ms
.support → Moon-Userbot\nGitHub: ...\nCustom modules: ...
.help → Help for Moon-Userbot\n• module: .cmd1, .cmd2
.version → Moon Userbot version: 2.5.X
```

### Proposed VizX-UB Output Styles

Below are **3 draft template styles** for the revamped output. These use Telegram HTML formatting (`<b>`, `<i>`, `<code>`, `<a>`) which is supported by Pyrogram.

---

### 🎨 Template A: "Clean Card" (Minimal & Elegant)

Uses subtle box-drawing characters and clean spacing.

#### Ping
```html
⚡ <b>VizX-UB</b> │ <code>Ping</code>

  ╭─ Response
  │  <b>Pong!</b> <code>123ms</code>
  ╰─────────────
```

#### Help (Module List Page)
```html
📘 <b>VizX-UB</b> │ <code>Help</code>

  ╭─ Modules (Page 1/3)
  │
  │  <b>• ping</b>: <code>.ping</code>
  │  <b>• help</b>: <code>.help</code>, <code>.h</code>, <code>.hs</code>
  │  <b>• updater</b>: <code>.update</code>, <code>.restart</code>
  │  <b>• loader</b>: <code>.loadmod</code>, <code>.unloadmod</code>
  │
  ╰─ <i>Total: 31 modules</i>

💡 <code>.help [name]</code> for details │ <code>.pn</code> / <code>.pp</code> to navigate
```

#### Help (Single Module)
```html
📘 <b>VizX-UB</b> │ <code>Module: ping</code>

  ╭─ Commands
  │
  │  <code>.ping</code> — <i>Check ping to Telegram servers</i>
  │
  ╰─────────────
```

#### Support / Repo Info
```html
🔮 <b>VizX-UB</b> │ <code>Info</code>

  ╭─ About
  │  Userbot: <b>VizX-UB</b>
  │  Version: <code>2.5.X</code>
  │  Python: <code>3.11.X</code>
  │
  ├─ Stats
  │  Modules: <code>31</code>
  │  Commands: <code>87</code>
  │
  ├─ Links
  │  <a href="...">GitHub</a> • <a href="...">Channel</a> • <a href="...">Chat</a>
  │
  ╰─────────────
```

#### Version
```html
🔮 <b>VizX-UB</b> │ <code>Version</code>

  ╭─ Release Info
  │  Version: <code>2.5.X</code>
  │  Branch: <code>main</code>
  │  Commit: <a href="...">abc1234</a> by <i>Author</i>
  │  Time: <code>2026-05-07 10:00:00 UTC</code>
  │
  ╰─────────────
```

#### Error Output
```html
❌ <b>VizX-UB</b> │ <code>Error</code>

  ╭─ Exception
  │  <code>[400 MESSAGE_NOT_MODIFIED] — ...</code>
  ╰─────────────
```

---

### 🎨 Template B: "Modern Block" (Bold & Structured)

Uses emoji headers and block sections with horizontal rules.

#### Ping
```html
<b>⚡ PONG!</b>
━━━━━━━━━━━━━━━
<b>Latency:</b> <code>123ms</code>
<b>Bot:</b> <code>VizX-UB</code>
━━━━━━━━━━━━━━━
```

#### Help (Module List Page)
```html
<b>📚 VizX-UB Help</b>
━━━━━━━━━━━━━━━━━━━
Page <b>1</b>/<b>3</b> │ <code>.pn</code> next │ <code>.pp</code> prev

▸ <b>ping</b> — <code>.ping</code>
▸ <b>help</b> — <code>.help</code> <code>.h</code> <code>.hs</code>
▸ <b>updater</b> — <code>.update</code> <code>.restart</code>
▸ <b>loader</b> — <code>.loadmod</code> <code>.unloadmod</code>
▸ <b>support</b> — <code>.support</code> <code>.version</code>

━━━━━━━━━━━━━━━━━━━
<b>📦 31 modules</b> │ <code>.help [name]</code> for details
```

#### Help (Single Module)
```html
<b>📖 Module: ping</b>
━━━━━━━━━━━━━━━

<code>.ping</code>
  └ <i>Check ping to Telegram servers</i>

━━━━━━━━━━━━━━━
```

#### Support / Repo Info
```html
<b>🔮 VizX-UB</b>
━━━━━━━━━━━━━━━━━━━

<b>📊 Stats</b>
  ├ Version: <code>2.5.X</code>
  ├ Python: <code>3.11.X</code>
  ├ Modules: <code>31</code>
  └ Commands: <code>87</code>

<b>🔗 Links</b>
  ├ <a href="...">GitHub Repository</a>
  ├ <a href="...">Custom Modules</a>
  └ <a href="...">Support Chat</a>

<b>👨‍💻 Devs</b>
  └ @dev1, @dev2
━━━━━━━━━━━━━━━━━━━
```

#### Version
```html
<b>📋 VizX-UB Version</b>
━━━━━━━━━━━━━━━━━━━━━
  ├ <b>Version:</b> <code>2.5.X</code>
  ├ <b>Branch:</b> <code>main</code>
  ├ <b>Commit:</b> <a href="...">abc1234</a>
  ├ <b>Author:</b> <i>Name</i>
  └ <b>Time:</b> <code>2026-05-07 10:00 UTC</code>
━━━━━━━━━━━━━━━━━━━━━
```

#### Error Output
```html
<b>❌ Error!</b>
━━━━━━━━━━━━━━━
<code>[400 MESSAGE_NOT_MODIFIED] — ...</code>
━━━━━━━━━━━━━━━
```

---

### 🎨 Template C: "Neon Tag" (Compact & Cyberpunk)

Uses bracket-tags and compact formatting for a sleek, developer feel.

#### Ping
```html
<b>[VizX]</b> <code>PING</code> → <b>123ms</b> ⚡
```

#### Help (Module List Page)
```html
<b>[VizX]</b> 📦 <code>Help</code> — Page <b>1/3</b>

<b>›</b> <code>ping</code> → <code>.ping</code>
<b>›</b> <code>help</code> → <code>.help</code> <code>.h</code> <code>.hs</code>
<b>›</b> <code>updater</code> → <code>.update</code> <code>.restart</code>
<b>›</b> <code>loader</code> → <code>.loadmod</code> <code>.unloadmod</code>

<i>31 modules loaded</i> ─ <code>.help [name]</code> for usage
<code>.pn</code> next │ <code>.pp</code> prev │ <code>.pq</code> quit
```

#### Help (Single Module)
```html
<b>[VizX]</b> 📖 <code>ping</code>

  <code>.ping</code> — <i>Check ping to Telegram servers</i>
```

#### Support / Repo Info
```html
<b>[VizX-UB]</b> ℹ️ <code>System Info</code>

  <b>⟩</b> ver <code>2.5.X</code> │ py <code>3.11.X</code>
  <b>⟩</b> <code>31</code> modules │ <code>87</code> commands
  <b>⟩</b> <a href="...">repo</a> │ <a href="...">channel</a> │ <a href="...">chat</a>
  <b>⟩</b> devs: @dev1, @dev2
```

#### Version
```html
<b>[VizX-UB]</b> 📋 <code>v2.5.X</code>

  branch: <code>main</code>
  commit: <a href="...">abc1234</a> by <i>Author</i>
  time: <code>2026-05-07 10:00 UTC</code>
```

#### Error Output
```html
<b>[VizX]</b> ❌ <code>[400 MSG_NOT_MODIFIED]</code> — <i>message content unchanged</i>
```

---

## Template Comparison Summary

| Aspect | A: Clean Card | B: Modern Block | C: Neon Tag |
|--------|:---:|:---:|:---:|
| Verbosity | Medium | High | Low |
| Visual Weight | Light | Heavy | Minimal |
| Box Drawing | ╭╰│├ | ━━━ ├└ | None |
| Emoji Use | 1 per output | Multiple | Minimal |
| Best For | General use | Detailed info | Quick responses |
| Personality | Professional | Feature-rich | Hacker/Dev |

> [!TIP]
> You can also **mix styles** — e.g., use **Template C** for quick commands (ping, id) and **Template A** for info-heavy outputs (help, support, version). This hybrid approach gives the best UX.

---

## Next Steps

1. **Pick a template style** (A, B, C, or hybrid) — let me know your preference
2. I'll **implement all rebranding changes** across the 48 files
3. I'll **revamp the module output functions** with a shared `format_output()` helper in `utils/scripts.py`
4. The helper will make it easy for all modules (and future custom modules) to use the new style consistently

> [!NOTE]
> The rebranding and output revamp are **independent** — I can do both simultaneously, or one at a time if you prefer.
