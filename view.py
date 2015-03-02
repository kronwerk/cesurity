import web
import db
import config

t_globals = dict(
  datestr=web.datestr,
)
render = web.template.render('templates/', cache=config.cache, 
    globals=t_globals)
render._keywords['globals']['render'] = render

def listing(**k):
    l = db.listing(**k)
    print "view.listing 1", dir(l)
    lst = []
    for _ in l:
        print "view.listing", _
        lst.append(_)
    return render.listing(lst)
