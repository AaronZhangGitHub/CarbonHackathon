from peewee import *

password = input("Database password: ")
db = MySQLDatabase('carbondb', host='carboncoderhackathon.caqu9lasjuwn.us-east-1.rds.amazonaws.com', user='zhangster', passwd=password)

class BaseModel(Model):
	class Meta:
		database=db

class Users(BaseModel):
	uid = PrimaryKeyField()

class Tag(BaseModel):
	tid = PrimaryKeyField()
	tag_text = CharField()
	percent = IntegerField()

class Picture(BaseModel):
	pid = PrimaryKeyField()
	uid = ForeignKeyField(Users)
	latitude = DoubleField()
	longitude = DoubleField()

class PicTags(BaseModel):
	pid = ForeignKeyField(Picture)
	tid = ForeignKeyField(Tag)

	class Meta:
		primary_key = CompositeKey('pid','tid')

db.connect()

# TODO do stuff