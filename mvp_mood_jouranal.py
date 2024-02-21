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
    users_db.update({'_id': doc_id}, doc_ids=[doc_id])
add_user("name1")

# write notes to db
def add_note(user_id, note):
    doc_id = notes_db.insert({'user_id': user_id, 'note': note})
    notes_db.update({'_id': doc_id}, doc_ids=[doc_id])
add_note(3, "I am happy")

# write records to db
def add_record(user_id, note_id, mood, date):
    doc_id = records_db.insert({'user_id': user_id, 'note_id': note_id, 'mood': mood, 'date': date})
    records_db.update({'_id': doc_id}, doc_ids=[doc_id])
add_record(3, 1, "Happy", time.time())

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


