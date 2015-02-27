import web
DB = web.database(#dburl='postgres://web:"web"@localhost:5432/mydb',
dbn='postgres', db='mydb', user='web', pw='web', host='localhost', port=5432)
cache = False
