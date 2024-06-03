#repos.UserRepos
from models.UserModel import UserModel
class UserRepos:
    @staticmethod
    def get_users():
        #SELECT * FROM user ORDER BY user_id
        return UserModel.select().order_by(UserModel.user_id)