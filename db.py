import config

def listing(**k):
    #return config.DB.select('my_tree', **k)
    print 'db.listing 1', k
    for key,v in k.items():
        print 'db.listing 1.1', key, type(key), v, type(v)
    j = {key:int(v) for key,v in k.items() if type(v)==int or (type(v)==str or type(v)==unicode) and v.isnumeric()}
    print 'db.listing 2', j
    return config.DB.query("SELECT * FROM my_tree WHERE left_key >= $left_key AND right_key <= $right_key AND level = $level+1 ORDER BY left_key", vars=j)
