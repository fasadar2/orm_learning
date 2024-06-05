#UserMarkDTO
class UserMarkDTO:
    def __init__(self,user_model):
        self.user_model = user_model
        self.marks = []
    def add_marks(self,mark):
        self.marks.append(mark)
    def get_username(self):
        return self.user_model.user_name