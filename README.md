# MinePanel-GUI
MinePanel GUI is a lightweight cross-platform Minecraft server manager.  It provides a graphical interface to control Minecraft servers with live console, command input, chat support, configuration saving, and theme customization.  Supports Linux (Ubuntu, Mint, Debian-based) and Windows.
MinePanel GUI é um painel leve para gerenciar servidores Minecraft com interface gráfica.

Permite iniciar, parar e enviar comandos ao servidor, com console em tempo real.

Compatível com Linux (Ubuntu/Mint) e Windows.

Feito em Python + Tkinter.
🐧 Linux (Ubuntu / Mint / Debian)
bash run.sh

Exemplo run.sh:

#!/usr/bin/env bash
cd minecraft-server
exec java -Xms2G -Xmx4G -jar server.jar nogui
🪟 Windows (.bat)
@echo off
cd minecraft-server
java -Xms2G -Xmx4G -jar server.jar nogui
pause
🧠 no Python (detecção simples)
import platform

if platform.system() == "Windows":
    subprocess.Popen(["run.bat"])
else:
    subprocess.Popen(["bash", "run.sh"])
 REQUIREMENTS.TXT

 Linux
sudo apt update
sudo apt install python3 python3-tk openjdk-17-jre -y

Rodar:

bash run.sh
Windows
Instalar Python 3
Instalar Java 17+
Rodar:
run.bat
📌 E pronto
