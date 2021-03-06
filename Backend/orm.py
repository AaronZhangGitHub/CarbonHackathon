from peewee import *

my_db = input("Database name: ")
my_host = input("Database hostname: ")
my_user = input("Database username: ")
my_password = input("Database password: ")
db = MySQLDatabase(my_db, host=my_host, user=my_user, passwd=my_password)

class BaseModel(Model):
	class Meta:
		database=db

class IGUsers(BaseModel):
	uid = PrimaryKeyField()
	handle = CharField()

	@staticmethod
	def get_by_handle(handle):
		return IGUsers.select().where(IGUsers.handle == handle).order_by(IGUsers.uid.desc()).get()

	@staticmethod
	def get_distinct_handles():
		join_query = IGUsers.select(IGUsers.handle, IGUsers.uid)
		join_query = join_query.alias('jq')
		query = IGUsers.select().join(join_query, on=(IGUsers.handle == join_query.c.handle)).group_by(IGUsers.handle).select(IGUsers.handle, fn.Max(join_query.c.uid).alias('uid')).order_by(IGUsers.handle)
		return query

class Tag(BaseModel):
	tid = PrimaryKeyField()
	tag_text = CharField()
	percent = IntegerField()

	@staticmethod
	def get_occurances_for(uid):
		query = Tag.select().join(PicTags).join(Picture).where(Picture.uid == uid).group_by(Tag.tag_text).select(Tag.tag_text, fn.Sum(Tag.percent).alias('spercent')).order_by(SQL('spercent').desc())
		return [ (x[0], int(x[1])) for x in query.tuples() ]

class Picture(BaseModel):
	pid = PrimaryKeyField()
	uid = ForeignKeyField(IGUsers)
	url = CharField()

	@staticmethod
	def get_with_tags(uid):
		pictures = []
		for picture in Picture.select().where(Picture.uid == uid):
			picture_dict = dict()
			picture_dict['url'] = picture.url
			picture_dict['tags'] = [ (x[0], int(x[1])) for x in Tag.select().join(PicTags).where(PicTags.pid == picture.pid).select(Tag.tag_text, Tag.percent).order_by(SQL('percent').desc()).tuples() ]
			pictures.append(picture_dict)
		return pictures

class PicTags(BaseModel):
	ptid = PrimaryKeyField()
	pid = ForeignKeyField(Picture)
	tid = ForeignKeyField(Tag)

def before_request_handler():
    db.connect()

def after_request_handler():
    db.close()

# db.connect()

# db.create_tables([ IGUsers, Tag, Picture, PicTags ], safe=True)
