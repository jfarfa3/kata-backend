import logging

logger = logging.getLogger('uvicorn.error')
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s"
 )
console_handler.setFormatter(formatter)