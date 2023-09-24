import logging


def get_logger():
    logging.basicConfig(level=logging.INFO,
                        filename='logging.log',
                        format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                        datefmt='%d/%m/%Y %H:%M:%S',
                        encoding='utf-8',
                        filemode='w')
    return logging.getLogger()