import os, json

with open('config/config.json') as config_json_file:
    config = json.load(config_json_file)
name_container = 'mysql_container'
password = config['pass']
db_name = config['db_name']
name_sql_file = config['name_sql_file']


cmd='docker run --name ' + 'radmin_data' + ' e MYSQL_ROOT_PASSWORD=' + password + " -d -p 3306:3306 mysql"


cmd_import = 'docker exec -i' + 'radmin_data' + 'mysql -uroot -p' + password + ' ' + db_name + ' --force < ' + name_sql_file + '.sql'

#Import
#docker exec -i container mysql -uroot -pContrasena databasename --force < file.sql
os.system(cmd)