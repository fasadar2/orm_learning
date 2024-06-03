#service.UserMarkService
from models.UserModel import UserModel
from models.UserMarkModel import UserMarkModel
from models.MarkModel import MarkModel
class UserMarkService:
    @staticmethod
    def add_mark_to_user(user_id,mark):
        mark_model = MarkModel().select().where(MarkModel.mark_name == mark).get()
        user_model = UserModel().select().where(UserModel.user_id == user_id).get()
        user_mark = UserMarkModel().create(user_id=user_model,mark_id = mark_model)
        return user_mark