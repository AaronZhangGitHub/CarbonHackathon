import cherrypy

class Root(object):
	pass
	
if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'server.conf')