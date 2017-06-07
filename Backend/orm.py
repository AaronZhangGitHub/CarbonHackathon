from peewee import *

class Users(Model):
	uid = PrimaryKeyField()

class Tag(Model):
	tid = PrimaryKeyField()
	tag_index = IntegerField()
	tag_text = CharField()
	percent = IntegerField()

class Picture(Model):
	pid = PrimaryKeyField()
	uid = ForeignKeyField(Users)
	latitude = DoubleField()
	longitude = DoubleField()

class PicTags(Model):
	pid = ForeignKeyField(Picture)
	tid = ForeignKeyField(Tag)

	class Meta:
		primary_key = CompositeKey('pid','tid')