import os, json


with open('config/config.json') as config_json_file:
    config = json.load(config_json_file)
user = config['user']
password = config['pass']
db_name = config['database_name']
name_sql_exported = config['name_sql_exported']

#En raspberry origen python -m SimpleHTTPServer 5004
#En device destino wget http://ip:5004/file.sql
cmd='mysqldump --skip-triggers --routines -u ' + user + ' --password=' + password + " " + db_name + ' > ' + name_sql_exported + ".sql"
#Export
os.system(cmd)  
