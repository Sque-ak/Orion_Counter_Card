import configparser, os

config = configparser.ConfigParser()

if not os.path.isfile("config.ini"):
    # add a new section and server values
    config.add_section('Server')
    config.set('Server', 'host_db', 'localhost')
    config.set('Server', 'user_db', 'sa')
    config.set('Server', 'password_db', '123456')
    config.set('Server', 'name_db', 'database_05_04_22')
    config.set('Server', 'port_db', '2001')

    config.add_section('DataBase')
    config.set('DataBase', 'path_db_local', '')

    config.add_section('DataUser')
    config.set('DataUser', 'company_name', 'Nezumi')

    # add a new section and display values
    config.add_section('Display')
    config.set('Display', 'size_window_w', '1280')
    config.set('Display', 'size_window_h', '800')


    file = open("config.ini",mode="w")
    config.write(file)
    print('Config created succeed. \a')

# parse existing file
config.read('config.ini')

# read values from a section Server
host_db = config.get('Server', 'host_db')
user_db = config.get('Server', 'user_db')
password_db = config.get('Server', 'password_db')
name_db = config.get('Server', 'name_db')
port_db = config.get('Server', 'port_db')

# read values from a section DataBase
path_db_local = config.get('DataBase', 'path_db_local')

# read values from a section DataUser
company_name = config.get('DataUser', 'company_name')

# read values from a section Display
size_window_w = config.getint('Display', 'size_window_w')
size_window_h = config.getint('Display', 'size_window_h')