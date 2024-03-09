import configparser
 
 
def create_config():
    config = configparser.ConfigParser()
 
    # Add sections and key-value pairs
    config['General'] = {'debug': True, 'log_level': 'info'}
    config['POSTGRES'] = {'database': 'postgres',
                          'user': 'postgres', 
                          'pwd' : 'VolpPost2023$',
                          'port': '5432',
                          'host' : '192.168.0.200'}
 
    # Write the configuration to a file
    with open('../private.cfg', 'w') as configfile:
        config.write(configfile)
 
 
if __name__ == "__main__":
    create_config()