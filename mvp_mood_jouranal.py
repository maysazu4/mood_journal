# importing json library
from tinydb import TinyDB, Query
import time
import emotions_in_percent as eip
import datetime


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
    with open("notes.txt", "a") as file:
        file.write(str(note) + "\n")


# Create users Db
users_db = TinyDB("users_db.json")
notes_db = TinyDB("notes_db.json")
records_db = TinyDB("records_db.json")


# write users to db
def add_user(name):
    doc_id = users_db.insert({"name": name})
    users_db.update({"_id": doc_id}, doc_ids=[doc_id])
    return doc_id


# write notes to db
def add_note(user_id, note):
    doc_id = notes_db.insert({"user_id": user_id, "note": note})
    notes_db.update({"_id": doc_id}, doc_ids=[doc_id])
    return doc_id


# write records to db
def add_record(user_id, note_id, mood, date):
    doc_id = records_db.insert(
        {"user_id": user_id, "note_id": note_id, "mood": mood, "date": date}
    )
    records_db.update({"_id": doc_id}, doc_ids=[doc_id])
    return doc_id


# def save_note_details_to_DB(user_id):
#     note = take_input()
#     note_id = add_note(user_id, note)
#     note_moods = eip(note, eip.emotions_words)
#     for mood in note_moods:
#         add_record(user_id, note_id, mood, time.time())


# Fetch all documents from each database
all_users = users_db.all()
all_notes = notes_db.all()
all_tasks = records_db.all()

# print("Users:", all_users)
# print("Notes:", all_notes)
# print("Tasks:", all_tasks)


date = datetime.datetime.now()
t = date.strftime("%H:%M-%d-%m-%y")
add_record(2, note_id=1, mood="Happy", date=str(t))


def compare_entry_with_last():
    # all_tasks.
    length = len(all_tasks)
    if length >= 2:
        print(all_tasks[length - 1]["date"])
        new_record_date = all_tasks[length - 1]["date"]
        last_record_date = all_tasks[length - 2]["date"]
        date1 = datetime.datetime.strptime(new_record_date, "%H:%M-%d-%m-%y")
        date2 = datetime.datetime.strptime(last_record_date, "%H:%M-%d-%m-%y")
        if date1.weekday() == date2.weekday():
            return True
        return False
    return True


compare_entry_with_last("Sa")
