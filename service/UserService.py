from models.UserModel import UserModel
class UserService:
    @staticmethod
    def create_user():
        user_name = input("Введите ФИО пользователя")
        user = UserModel().create(user_name=user_name)
        return user

    @staticmethod
    def update_user(user_id):
        user = UserModel.select().where(UserModel.user_id == user_id).get()
        new_name = input("Введите новое имя")
        user.user_name = new_name
        user.save()

    @staticmethod
    def delete_user(user_id):
        user = UserModel.select().where(UserModel.user_id == user_id).get()
        user.delete_instance()