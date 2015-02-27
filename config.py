import web
DB = web.database(dbn='postgres', db='mydb', user='web', pw='web', host='localhost', port=5432)
cache = False
