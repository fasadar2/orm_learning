#service.UserMarkService
from models.UserModel import UserModel
from models.UserMarkModel import UserMarkModel
from models.MarkModel import MarkModel
from DTO.UserMarkDTO import UserMarkDTO
class UserMarkService:
    @staticmethod
    def add_mark_to_user(user_id,mark):
        mark_model = MarkModel().select().where(MarkModel.mark_name == mark).get()
        user_model = UserModel().select().where(UserModel.user_id == user_id).get()
        user_mark = UserMarkModel().create(user_id=user_model,mark_id = mark_model)
        return user_mark
    @staticmethod
    def get_marks_for_user(user_id):
        user_model = UserModel().select().where(UserModel.user_id == user_id).get()
        user_mark_dto = UserMarkDTO(user_model)
        user_marks = UserMarkModel.select().where(UserMarkModel.user_id == user_id)
        for user_mark in user_marks:
            user_mark_dto.add_marks(user_mark.mark_id)
        return user_mark_dto
