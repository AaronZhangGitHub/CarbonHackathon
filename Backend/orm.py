from peewee import *

password = "abcd1234" # input("Database password: ")
db = MySQLDatabase('carbondb', host='carboncoderhackathon.caqu9lasjuwn.us-east-1.rds.amazonaws.com', user='zhangster', passwd=password)

class BaseModel(Model):
	class Meta:
		database=db

class IGUsers(BaseModel):
	uid = PrimaryKeyField()
	handle = CharField()

class Tag(BaseModel):
	tid = PrimaryKeyField()
	tag_text = CharField()
	percent = IntegerField()

	@staticmethod
	def get_occurances_for(uid):
		query = Tag.select().join(PicTags).join(Picture).where(Picture.uid == uid).group_by(Tag.tag_text).select(Tag.tag_text, fn.Sum(Tag.percent).alias('spercent')).order_by(SQL('spercent').desc())
		print(query)
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

db.connect()

db.create_tables([ IGUsers, Tag, Picture, PicTags ], safe=True)

# TODO do stuff