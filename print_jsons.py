from tinydb import TinyDB, Query

records_db = TinyDB('records_db.json')

def printAllRecords():
    all_records = records_db.all()
    for record in all_records:
        print("user: ", record["user_id"], "note: ", record["note_id"], "mood: ", record["mood"], "date: ", record["date"])

def printRecordsByUser(user_id):
    Record = Query()
    user_records = records_db.search(Record.user_id == user_id)
    print("Records for user ", user_id, ":")
    for record in user_records:
        print("note: ", record["note_id"], "mood: ", record["mood"], "date: ", record["date"])

def printRecordsByDateRange(start_date, end_date):
    Record = Query()
    date_records = records_db.search((Record.date >= start_date) & (Record.date <= end_date))
    print("Records between ", start_date, " and ", end_date, ":")
    for record in date_records:
        print("user: ", record["user_id"], "note: ", record["note_id"], "mood: ", record["mood"], "date: ", record["date"])
        
def printRecordsByUserAndDateRange(user_id, start_date, end_date):
    Record = Query()
    user_date_records = records_db.search((Record.user_id == user_id) & (Record.date >= start_date) & (Record.date <= end_date))
    print("Records for user ", user_id, "between ", start_date, " and ", end_date, ":")
    for record in user_date_records:
        print("note: ", record["note_id"], "mood: ", record["mood"], "date: ", record["date"])
