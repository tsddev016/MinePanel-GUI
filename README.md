# 🧩 MinePanel GUI

MinePanel GUI is a lightweight cross-platform Minecraft server manager.

It provides a graphical interface to control Minecraft servers with live console, command input, chat support, configuration saving, and theme customization.

Supports Linux (Ubuntu, Mint, Debian-based) and Windows.

---

# ⚠️ IMPORTANT

## 🪟 Windows users (ADMIN REQUIRED)

> 🚨 YOU MUST RUN CMD / TERMINAL AS ADMINISTRATOR

Without administrator privileges, installation and server execution may fail.

---

# 🐧 Linux (Ubuntu / Mint / Debian)

## 📦 Install dependencies

```[bash
sudo apt update
sudo apt install python3 python3-tk openjdk-17-jre -y
▶️ Run server
bash run.sh
📜 run.sh
#!/usr/bin/env bash
cd minecraft-server
exec java -Xms2G -Xmx4G -jar server.jar nogui]
```


```[🪟 Windows (.bat)
▶️ Run server
run.bat
📜 run.bat
@echo off
cd minecraft-server
java -Xms2G -Xmx4G -jar server.jar nogui
pause
🐍 Python launcher (auto detect OS)
import platform
import subprocess

if platform.system() == "Windows":
    subprocess.Popen(["run.bat"])
else:
    subprocess.Popen(["bash", "run.sh"])]]
```






📦 Requirements
Linux

```[sudo apt update
sudo apt install python3 python3-tk openjdk-17-jre -y]
```




Windows
Install Python 3
Install Java 17+
Run as Administrator
✨ Features
Start / Stop server
Live console output
Command execution
Chat system
Theme customization
Config save (window size + position)
📌 Notes
Do NOT place server files inside GitHub repo
Requires Java 17+
Works best on NeoForge / Forge servers
