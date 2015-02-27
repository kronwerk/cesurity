import web
import cgi
import sys
import view, config
from view import render

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, query):
        query = web.ctx.query
        print 'input index:', query
        if query:
            qdict = cgi.parse_qs(query[1:])
        else:
            qdict = {'id': 1, 'left_key': 1, 'right_key': sys.maxint, 'level': 1}
        return render.base(view.listing(**qdict))

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
