import cherrypy
from Backend.orm import *

class Root(object):
	def __init__(self):
		self.api = Api()

	@cherrypy.expose
	def index(self):
		raise cherrypy.HTTPRedirect("/index.html")

class Api(object):
	def __init__(self):
		self.users = User()

@cherrypy.popargs('uid')
class User(object):
	def __init__(self):
		self.tags = UserTags()

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self, uid=None):
		if uid == None:
			return [ x for x in IGUsers.select().dicts() ]
		else:
			return [ x for x in IGUsers.select().where(IGUsers.uid == uid).limit(1).dicts() ]

class UserTags(object):
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self, uid):
		return [ (x[0], int(x[1])) for x in Tag.get_occurances_for(int(uid)) ]

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'server.conf')