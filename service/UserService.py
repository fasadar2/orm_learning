from models.UserModel import UserModel
class UserService:
    @staticmethod
    def create_user():
        user_name = input("Введите ФИО пользователя")
        user = UserModel().create(user_name=user_name)
        return user
