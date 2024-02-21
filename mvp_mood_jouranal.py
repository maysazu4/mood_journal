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
notes_db = TinyDB('notes_db.json')
records_db = TinyDB('records_db.json')

# write users to db
def add_user(name):
    users_db.insert({name})

# write notes to db
def add_note(user_id, note):
    notes_db.insert({user_id, note})

# write records to db
def add_record(user_id, note_id, mood, date):
    records_db.insert({user_id, note_id, mood, date})


# Fetch all documents from each database
all_users = db_users.all()
all_notes = db_notes.all()
all_tasks = db_tasks.all()

print("Users:", all_users)
print("Notes:", all_notes)
print("Tasks:", all_tasks)