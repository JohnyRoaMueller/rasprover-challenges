from watchfiles import watch
import importlib, threading, os, sys
from logger_configurator import setup_ugv_logger

logger = setup_ugv_logger()

def reload_on_change():
    logger.info("hotloader started")
    for changes in watch('/home/FlottiRobotti/ugv_rpi', recursive=True):
        for change_type, path in changes:
            # Ignore non-Python files and temporary/editor backup files
            if not path.endswith('.py'):
                continue
            filename = os.path.basename(path)
            if filename.startswith('.') or '~' in filename or '-checkpoint' in filename:
                continue

            module_name = os.path.splitext(filename)[0]
            if module_name in sys.modules:
                logger.info(f"reloading module: {module_name}")
                importlib.reload(sys.modules[module_name])
                logger.info(f"{module_name} reloaded successfully")
            else:
                logger.warning(f"{module_name} not found in sys.modules")
