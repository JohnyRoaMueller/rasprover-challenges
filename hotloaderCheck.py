import threading
from logger_configurator import setup_ugv_logger
from time import sleep

logger = setup_ugv_logger()

def saySomething():
    logger.info("message from the hotload-checker")
    
def saySomethingLoop():
    while True:
        saySomething()
        sleep(30)

#hotloaderCheckThread = threading.Thread(target=saySomethingLoop, daemon=True).start()

