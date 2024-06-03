#models.UserMarkModel
from models.BaseModel import BaseModel
from models.UserModel import UserModel
from models.MarkModel import MarkModel
from peewee import PrimaryKeyField,ForeignKeyField
class UserMarkModel(BaseModel):
    user_mark_id = PrimaryKeyField(primary_key=True,column_name="user_mark_id")
    user_id = ForeignKeyField(UserModel,column_name="user_id")
    mark_id = ForeignKeyField(MarkModel,column_name="mark_id")
    class Meta:
        table_name = 'user_mark'