import configparser
import os


class get_paths():

    def get_config_ini_path(self):
        cwd = os.path.dirname(__file__)
        ini = os.path.join(cwd,'config.ini')
        return ini

    def get_application_url(self):
        self.p = get_paths()
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['domain']

    def get_username(self):
        self.p = get_paths()
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['username']

    def get_password(self):
        self.p = get_paths()
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['password']