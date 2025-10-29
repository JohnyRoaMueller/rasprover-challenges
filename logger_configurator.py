import logging

# indipendent logger with own formatting ##

def setup_ugv_logger():
    logfile = "/home/FlottiRobotti/ugv_rpi/logs/ugv.log"

    logger = logging.getLogger("ugv")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.FileHandler(logfile)
        formatter = logging.Formatter(
            '[%(asctime)s] [%(module)s] %(message)s',
            '%d/%b/%Y %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
