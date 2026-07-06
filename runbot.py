import threading
import time

class RunBot:
    def __init__(self, server, log):
        self.server = server
        self.log = log
        self.active = False

    def shutdown(self, minutes=5):
        if self.active:
            self.log("Shutdown já em andamento")
            return

        self.active = True

        def task():
            self.log(f"Servidor vai desligar em {minutes} minutos!")

            time.sleep((minutes - 1) * 60)

            self.log("1 minuto restante!")

            time.sleep(50)

            self.log("Desligando servidor agora!")

            self.server.stop()
            self.active = False

        threading.Thread(target=task, daemon=True).start()
