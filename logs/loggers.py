import logging

from reuse_funs import functions


class log_Details():

    @staticmethod
    def logen():
        dir = functions()
        logging.basicConfig(filename=dir.get_log_file_dir()+'/status.log',format='%(asctime)s : %(levelname)s : %(message)s',datefmt='%m-%d-%Y %I:%M:%S%p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger