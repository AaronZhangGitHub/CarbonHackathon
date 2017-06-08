import cherrypy

class Root(object):
    @cherrypy.expose
    def api(self):
        return "Hello World!"
    @cherrypy.expose
    def index(self):
    	raise cherrypy.HTTPRedirect("/index.html")

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'server.conf')