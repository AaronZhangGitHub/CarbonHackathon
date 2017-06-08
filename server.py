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

@cherrypy.popargs('action')
class UserTags(object):
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self, uid, action=None):
		if action == 'details':
			return Picture.get_with_tags(int(uid))
		else:
			return Tag.get_occurances_for(int(uid))


if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'server.conf')