import os, json

with open('config/config.json') as config_json_file:
    config = json.load(config_json_file)
user = config['user']
password = config['pass']
db_name = config['db_name']
name_sql_file = config['name_sql_file']

cmd='mysql -u ' + user + ' --password=' + password + " " + db_name + ' < ' + name_sql_file + ".sql"
#Import
os.system(cmd)