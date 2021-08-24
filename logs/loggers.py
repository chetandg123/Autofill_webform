import logging

from reuse_funs import functions


class log_Details():

    @staticmethod
    def logen():
        dir = functions()
        file_path=dir.get_log_file_dir()+'/status.log'
        logging.basicConfig(filename=file_path,format='%(asctime)s : %(levelname)s : %(message)s',datefmt='%m-%d-%Y %I:%M:%S%p')
        logging.FileHandler(file_path,'w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger