from models.UserMarkModel import UserMarkModel
class UserMarkModelsRepos:
    @staticmethod
    def get_user_mark_by_user_id(user_id):
        #SELECT * FROM user_mark
        # JOIN user on user_mark.user_id = user.user_id
        # JOIN mark on user_mark.mark_id = mark.mark_id
        # WHERE user_mark.user_mark_id = ?;
        return UserMarkModel.select().where(UserMarkModel.user_id == user_id)