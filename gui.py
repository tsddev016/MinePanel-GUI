import tkinter as tk
import subprocess
import threading
import traceback
import sys
import json
import os

CONFIG_FILE = "config.json"
current_theme = "default"

# ---------------- THEMES ----------------
themes = {
    "default": {
        "bg": "black",
        "fg": "white",
        "console_bg": "black",
        "console_fg": "white"
    },
    "light": {
        "bg": "white",
        "fg": "black",
        "console_bg": "white",
        "console_fg": "black"
    },
    "red": {
        "bg": "black",
        "fg": "red",
        "console_bg": "darkred",
        "console_fg": "black"
    }
}

# ---------------- SERVER ----------------
class ServerController:
    def __init__(self):
        self.process = None

    def start(self, on_output):
        if self.process and self.process.poll() is None:
            return "already running"

        self.process = subprocess.Popen(
            ["bash", "/home/oem/minecraft-server/run.sh"],
            cwd="/home/oem/minecraft-server",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        def reader():
            for line in self.process.stdout:
                if line:
                    on_output(line.rstrip())

        threading.Thread(target=reader, daemon=True).start()
        return "started"

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None

    def is_running(self):
        return self.process and self.process.poll() is None

    def send_command(self, cmd):
        if self.is_running() and self.process.stdin:
            self.process.stdin.write(cmd + "\n")
            self.process.stdin.flush()

    def send_chat(self, msg):
        self.send_command(f"say {msg}")


server = ServerController()

# ---------------- APP ----------------
app = tk.Tk()
app.title("Minecraft Panel Server")
app.geometry("800x600")

# ---------------- CONSOLE ----------------
log_box = tk.Text(app, bg="black", fg="white")
log_box.pack(fill="both", expand=True)

def write_log(msg):
    log_box.insert("end", msg + "\n")
    log_box.see("end")

# ---------------- ERROR LOG ----------------
def handle_exception(exc_type, exc_value, exc_traceback):
    err = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    write_log(err)

sys.excepthook = handle_exception

# ---------------- CONFIG ----------------
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None

def save_config():
    config = {
        "x": app.winfo_x(),
        "y": app.winfo_y(),
        "w": app.winfo_width(),
        "h": app.winfo_height(),
        "theme": current_theme
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

    write_log("✔ Config salva com sucesso")

def apply_theme(name):
    global current_theme
    current_theme = name
    t = themes[name]

    app.configure(bg=t["bg"])
    log_box.configure(bg=t["console_bg"], fg=t["console_fg"])

cfg = load_config()
if cfg:
    app.geometry(f"{cfg['w']}x{cfg['h']}+{cfg['x']}+{cfg['y']}")
    apply_theme(cfg.get("theme", "default"))

# ---------------- CONFIG WINDOW ----------------
def open_settings():
    settings = tk.Toplevel(app)
    settings.title("Configurações")
    settings.geometry("300x250")

    tk.Label(settings, text="Temas").pack(pady=5)

    tk.Button(settings, text="Default", command=lambda: apply_theme("default")).pack()
    tk.Button(settings, text="Light", command=lambda: apply_theme("light")).pack()
    tk.Button(settings, text="Red", command=lambda: apply_theme("red")).pack()

    tk.Button(settings, text="Salvar Config", command=save_config).pack(pady=10)

# botão engrenagem
tk.Button(app, text="⚙ Config", command=open_settings).place(x=5, y=5)

# ---------------- ACTIONS ----------------
def start_server():
    result = server.start(write_log)
    write_log(result)

def stop_server():
    server.stop()
    write_log("🛑 Servidor parado")

def send_cmd():
    if not server.is_running():
        write_log("❌ Servidor offline")
        return

    cmd = cmd_entry.get()
    if cmd.strip():
        server.send_command(cmd)
        write_log(f">>> {cmd}")
        cmd_entry.delete(0, "end")

def send_chat():
    if not server.is_running():
        write_log("❌ Servidor offline")
        return

    msg = chat_entry.get()
    if msg.strip():
        server.send_chat(msg)
        write_log(f"[CHAT] {msg}")
        chat_entry.delete(0, "end")

# ---------------- UI ----------------
tk.Button(app, text="Start Server", command=start_server).pack(pady=5)
tk.Button(app, text="Stop Server", command=stop_server).pack(pady=5)

status = tk.Label(app, text="OFFLINE")
status.pack()

cmd_entry = tk.Entry(app, width=60)
cmd_entry.pack(pady=5)

tk.Button(app, text="Send Command", command=send_cmd).pack()

chat_entry = tk.Entry(app, width=60)
chat_entry.pack(pady=5)

tk.Button(app, text="Send Chat", command=send_chat).pack()

# ---------------- LOOP ----------------
def update():
    status.config(text="ONLINE" if server.is_running() else "OFFLINE")
    app.after(1000, update)

update()
app.mainloop()
