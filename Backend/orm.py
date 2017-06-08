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
		return Tag.select().join(PicTags).join(Picture).where(Picture.uid == uid).group_by(Tag.tag_text).select(Tag.tag_text, fn.Sum(Tag.percent).alias('percent')).order_by('percent').tuples()

class Picture(BaseModel):
	pid = PrimaryKeyField()
	uid = ForeignKeyField(IGUsers)
	url = CharField()

class PicTags(BaseModel):
	ptid = PrimaryKeyField()
	pid = ForeignKeyField(Picture)
	tid = ForeignKeyField(Tag)

db.connect()

db.create_tables([ IGUsers, Tag, Picture, PicTags ], safe=True)

# TODO do stuff