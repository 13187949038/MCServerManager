import logging
import os
import zerorpc

import consts


def get_logger(module):
    if consts.DEBUG:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s')

    logger = logging.getLogger(module)

    return logger


def get_temp_logfile_path(number=0, head='default'):
    if os.path.exists(f'/tmp/{head}_{number}.log'):
        return get_temp_logfile_path(number + 1)
    else:
        return f'/tmp/{head}_{number}.log'


def get_temp_logfile_list(head='default'):
    old_cwd = os.getcwd()

    os.chdir('/tmp')
    file_list = [
        os.path.abspath(x)
        for x in os.listdir('/tmp')
    ]
    os.chdir(old_cwd)

    logfile_list = [
        os.path.abspath(x)
        for x in file_list
        if x.find(f'{head}_') != -1
    ]

    return logfile_list


def start_server():
    os.system('java -jar server.jar')
