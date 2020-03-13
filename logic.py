import subprocess
from datetime import datetime
import logging


def get_process_name() -> str:
    try:
        process = subprocess.Popen(["./script.sh"], stdout=subprocess.PIPE)
    except FileNotFoundError:
        logging.error("script.sh does not exist")
        exit(0)
    else:
        output, error = process.communicate()
        output = str(output).split("'")[1][0:-2]
        if output == "" or output is None:
            return "nothing"
        return output


class ActiveProcess:
    def __init__(self):
        self.current_process = get_process_name()
        self.current_process_begin = datetime.now()

    def update_process(self):
        current_process = get_process_name()
        if self.current_process != current_process:
            prev_process = self.current_process
            prev_process_time = datetime.now() - self.current_process_begin
            self.current_process = current_process
            self.current_process_begin = datetime.now()
            return prev_process, prev_process_time
        return None


class ProcessRepository:
    def __init__(self):
        self.process_map = {}

    def add_process(self, process: tuple):
        if process is not None:
            if process[0] in self.process_map:
                self.process_map[process[0]] += process[1]
            else:
                self.process_map.update({process[0]: process[1]})

    def print_all(self):
        print(self.process_map)

