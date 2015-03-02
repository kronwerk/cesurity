import web
import urlparse
import sys
import cPickle
import view, config
from view import render


urls = (
    '/(.*)', 'index'
)


class path:
    def __init__(self):
        self.nodes = []

    def add_node(self, obj):
        print "to_node", obj, self.nodes
        if self.is_empty() or not self.is_empty() and obj != self.nodes[-1]:
            self.nodes.append(obj)
            return obj

    def is_empty(self):
        return len(self.nodes) == 0

    def root_only(self):
        return len(self.nodes) == 1

    def get(self):
        if self.root_only():
            return self.nodes[-1]
        else:
            return self.nodes.pop()

    def purge(self):
        while (not self.root_only()):
            _ = self.get()
        return self.get()


def pack(name, obj):
    return web.setcookie(name, cPickle.dumps(obj))

def unpack(name):
    #print 'unpack', web.cookies().get(name)
    return cPickle.loads(web.cookies().get(name))


class index:
    def GET(self, query):
        print '___before', web.cookies().get('nodepath')
        #print web.cookies(), unpack('nodepath')
        if web.cookies().get('nodepath') == None:
            pack('nodepath', path())
            print 'np 111', dir(path())
        query = web.ctx.query
        print '___after', web.cookies().get('nodepath')
        print 'nodepath', unpack('nodepath'), dir(unpack('nodepath'))
        print 'input index:', query, unpack('nodepath').nodes
        if query:
            response = urlparse.parse_qs(query[1:])
            qdict = {}
            for k,v in response.items():
               qdict[k] = v[-1]
            print "response", response, qdict
            #qdict = cgi.parse_qs(query[1:])
            print "type", qdict['type'], qdict['type'] == 'up'
            if qdict['type'] == 'up':
                print '_____________up', unpack('nodepath').nodes
                qdict = unpack('nodepath').get()
            #else:
            _ = unpack(('nodepath'))
            _.add_node(qdict)
            pack('nodepath', _)
        else:
            if unpack('nodepath').is_empty():
                for _ in config.DB.query("SELECT * FROM my_tree WHERE level = 1"):
                    qdict = _
                _ = unpack('nodepath')
                _.add_node(qdict)
                pack('nodepath', _)
            else:
                _ = unpack('nodepath')
                qdict = _.purge()
                pack('nodepath', _)
        print "GET", qdict, dir(qdict), unpack('nodepath').nodes
        return render.base(view.listing(**qdict), qdict)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
    print "__main__", web, dir(web)
