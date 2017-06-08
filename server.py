import cherrypy
from Backend.orm import *
from threading import Thread
from build_for import build_for

class Root(object):
	def __init__(self):
		self.api = Api()

	@cherrypy.expose
	def index(self):
		raise cherrypy.HTTPRedirect("/index.html")

class Api(object):
	def __init__(self):
		self.users = User()
		self.processor = Processor()

@cherrypy.popargs('handle')
class Processor(object):
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self, handle):
		thread = Thread(target = threaded_build_for, args = (handle, ))
		thread.start()
	index._cp_config = {'response.stream': True}

# For running build asynccher
def threaded_build_for(handle):
	try:
		before_request_handler()
		build_for(handle)
	finally:
		after_request_handler()

@cherrypy.popargs('uid')
class User(object):
	def __init__(self):
		self.tags = UserTags()

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self, uid=None):
		try:
			before_request_handler()
			if uid == None:
				return [ x for x in IGUsers.get_distinct_handles().dicts() ]
			else:
				return [ x for x in IGUsers.get_distinct_handles().where(IGUsers.uid == uid).limit(1).dicts() ]
		finally:
			after_request_handler()

@cherrypy.popargs('action')
class UserTags(object):
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self, uid, action=None):
		try:
			before_request_handler()
			if action == 'details':
				return Picture.get_with_tags(int(uid))
			else:
				return Tag.get_occurances_for(int(uid))
		finally:
			after_request_handler()


if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/', 'server.conf')