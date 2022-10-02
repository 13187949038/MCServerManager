import logging
import consts


def get_logger(module):
    if consts.DEBUG:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s')

    logger = logging.getLogger(module)

    return logger
