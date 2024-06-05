from service.UserService import UserService
from repos.UserRepos import UserRepos
from service.UserMarkService import UserMarkService
if __name__ == "__main__":
    users = []
    while True:
        user_chose = int(input("1-Добавить пользователя\n2-Просмотреть всех пользователей\n0-Выйти\n3-Добавить оценку\n4-Просмотреть оценки для пользователя\n"))
        if user_chose == 0:
            break
        elif user_chose == 1:
            UserService.create_user()
        elif user_chose == 2:
            users = UserRepos.get_users()
            for user in users:
                print(f"{user.user_id} {user.user_name}")
        elif user_chose == 3:
            user_id = int(input("Введите id пользователя"))
            mark = input("Введите оценку")
            UserMarkService.add_mark_to_user(user_id, mark)
        elif user_chose == 4:
            user_id = int(input("Введите id пользователя"))
            user_marks = UserMarkService.get_marks_for_user(user_id)
            print(f"Оценки {user_marks.get_username()}:")
            for mark in user_marks.marks:
                print(mark.mark_name)