from pprint import pprint
file_name = 'new.txt'
file_name = open(file_name, mode='rb')
file_content = file_name.read()
file_name.close()
pprint(file_content)