#models.UserModel
from models.BaseModel import BaseModel
from peewee import PrimaryKeyField,CharField
class UserModel(BaseModel):
    user_id = PrimaryKeyField(primary_key=True,column_name="user_id")
    user_name = CharField(max_length=511,column_name="user_name")

    class Meta:
        table_name = "user"