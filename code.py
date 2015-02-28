import web
import cgi
import sys
import view, config
from view import render

urls = (
    '/(.*)', 'index'
)


class path:
    def __init__(self):
        self.nodes = []

    def add_node(self, obj):
        print "to_node", obj
        return obj

    def is_empty(self):
        return len(self.nodes == 0)

    def root_only(self):
        return len(self.nodes == 1)

    def get(self):
        if self.root_only():
            return self.nodes[-1]
        else:
            return self.nodes.pop()


class index:
    def __init__(self):
        self.path = path()

    def GET(self, query):
        query = web.ctx.query
        print 'input index:', query
        if query:
            qdict = cgi.parse_qs(query[1:])
            self.path.add_node(qdict)
        else:
            if self.path.is_empty():
                qdict = config.DB.query("SELECT * FROM my_tree WHERE level = 1")
                self.path.add_node(qdict)
            else:
                qdict = self.path.get()
        print "GET", qdict, self.path
        return render.base(view.listing(**qdict))

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
