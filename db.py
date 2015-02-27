import config

def listing(**k):
    #return config.DB.select('my_tree', **k)
    print k
    return config.DB.query("SELECT * FROM my_tree WHERE left_key >= $left_key AND right_key <= $right_key AND level = $level+1 ORDER BY left_key", vars=k)
