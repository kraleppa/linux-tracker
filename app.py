import subprocess
from time import sleep
import logging


def get_process_name():
    try:
        process = subprocess.Popen(["./script.sh"], stdout=subprocess.PIPE)
    except FileNotFoundError:
        logging.error("script.sh does not exist")
        exit(0)
    else:
        output, error = process.communicate()
        output = str(output).split("'")[1][0:-2]
        return output


for i in range(0, 100):
    print(get_process_name())
    sleep(0.5)
