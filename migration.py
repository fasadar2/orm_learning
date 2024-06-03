from models.UserModel import UserModel
from models.MarkModel import MarkModel
from models.UserMarkModel import UserMarkModel
def apply():
    UserModel.create_table()
    MarkModel.create_table()
    UserMarkModel.create_table()
def fillData():
    for i in range(2,6):
        mark = MarkModel()
        mark.mark_name = str(i)
        mark.save()
if __name__ == "__main__":
    apply()
    fillData()