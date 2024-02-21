# importing json library
from tinydb import TinyDB, Query
import time

def take_input():
    get_input = input("Tell about your day: ")
    return get_input

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
    doc_id = users_db.insert({'name': name})
    print(doc_id)
add_user("mar")

# write notes to db
def add_note(user_id, note):
    notes_db.insert({'user_id': user_id, 'note': note})

# write records to db
def add_record(user_id, note_id, mood, date):
    records_db.insert({'user_id': user_id, 'note_id': note_id, 'mood': mood, 'date': date})

# def save_note_details_to_DB(user_id):
#     add_note(user_id, take_input())
#     add_record(user_id, 1, "Happy", time.time())


# Fetch all documents from each database
all_users = users_db.all()
all_notes = notes_db.all()
all_tasks = records_db.all()

print("Users:", all_users)
print("Notes:", all_notes)
print("Tasks:", all_tasks)


