import configparser
import io

# load the configuration file
config = configparser.ConfigParser()
config.read('./config.ini')

section = config.sections()[0]
nginx_log_file_path = config.get(section, 'nginx_log_file_path')
host = config.get(section, 'host')
port = config.get(section, 'port')
admin = config.get(section, 'admin')
password = config.get(section, 'password')
