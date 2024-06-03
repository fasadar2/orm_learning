#models.MarkModel
from models.BaseModel import BaseModel
from peewee import PrimaryKeyField, CharField


class MarkModel(BaseModel):
    mark_id = PrimaryKeyField(primary_key=True, column_name="mark_id")
    mark_name = CharField(max_length=7, column_name="mark_name")

    class Meta:
        table_name = "mark"