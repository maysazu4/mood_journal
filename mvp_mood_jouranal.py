# importing json library
from tinydb import TinyDB, Query

def take_input():
    name = input("Please enter your name: ")
    get_input = input("Tell about your day: ")
    return get_input,name

# print(take_input())

moods = {
    "Happy": {"Happy", "Excited", "Delighted"},
    "Sadness": {"Unhappy", "Depressed", "Sorrowfull"},
    "Anger": {"Furious", "Annoyed", "Irritated"},
}

def mood_journal(note):
    with open('notes.txt', 'a') as file:
        file.write(str(note) + '\n')

# Create users Db
users_db = TinyDB('users_db.json')

# write users to db
def add_user_json(user):
    users_db.insert(user)

# Note = Query()