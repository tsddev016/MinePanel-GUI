import subprocess

class ServerController:
    def __init__(self):
        self.process = None

    def start(self):
        if self.process and self.process.poll() is None:
            return "already running"

        self.process = subprocess.Popen(
            ["bash", "/home/oem/minecraft-server/run.sh"],
            cwd="/home/oem/minecraft-server"
        )

        return "started"

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process = None
            return "stopped"

        return "already stopped"

    def is_running(self):
        return self.process and self.process.poll() is None
