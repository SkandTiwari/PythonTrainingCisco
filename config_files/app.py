import configparser
 
config = configparser.ConfigParser()
config.read("config_files\config.ini", encoding="utf-8")  #Always use relative path along with encoding scheme
print(config['Product']['Name'])
print(config.sections())

# Adding section

"""config.add_section('Product IV')
config.set('Product IV', 'Name', 'Cisco ASR')
config.set('Product IV', 'Name', 'Cisco ISR')"""


"""with open('config_files\config.ini', 'w') as file:
    config.write(file)"""

config.remove_option('Product III', 'Name')

print("Removed!")
