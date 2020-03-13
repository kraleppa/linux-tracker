import subprocess
from datetime import datetime
import logging
import time


def get_process_name() -> str:
    try:
        process = subprocess.Popen(["./script.sh"], stdout=subprocess.PIPE)
    except FileNotFoundError:
        logging.error("script.sh does not exist")
        exit(0)
    else:
        output, error = process.communicate()
        output = str(output).split("'")[1][0:-2]
        return output


def get_time() -> datetime.date:
    return datetime.now()


class ProcessManager:
    def __init__(self):
        self.current_process = None
        self.current_process_begin = datetime.now()
        self.process_list = list()

    def update_process(self) -> bool:
        current_process = get_process_name()
        if self.current_process != current_process:
            self.current_process = current_process
            self.current_process_begin = datetime.now()
            return True
        return False


if __name__ == "__main__":
    manager = ProcessManager()
    for i in range(0, 40):
        print(manager.current_process, datetime.now() - manager.current_process_begin)
        time.sleep(1)
        manager.update_process()

