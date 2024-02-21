import random


class Note:
    def __init__(self, mood, text, date, user_id):
        self.id = date
        self.date = date
        self.text = text
        self.mood = mood
        self.user_id = user_id

    def get_record(self):
        return self.date, self.text
