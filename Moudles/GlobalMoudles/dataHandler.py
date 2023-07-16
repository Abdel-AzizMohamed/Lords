import sqlite3
import json


def createDb():
    db = sqlite3.connect("mainDb.db")
    cr = db.cursor()

    cr.execute("CREATE TABLE IF NOT EXISTS ()")

    closeCommit(db)

def addData(path, table, data_name, data):
    if path == "":
        db = sqlite3.connect("mainDb.db")
        cr = db.cursor()
    else:
        db = sqlite3.connect(f"{path}\\mainDb.db")
        cr = db.cursor()

    if len(data_name) == 1 and len(data) == 1:
        cr.execute(f"INSERT INTO {table} ({data_name[0]}) VALUES ('{data[0]}')")

    closeCommit(db)

def deleteData(path, table, fillter_name, fillter_data):
    if path == "":
        db = sqlite3.connect("mainDb.db")
        cr = db.cursor()
    else:
        db = sqlite3.connect(f"{path}\\mainDb.db")
        cr = db.cursor()
    db.execute("PRAGMA foreign_keys = 1")

    if len(fillter_name) == 1 and len(fillter_data) == 1:
        cr.execute(f"DELETE FROM {table} WHERE {fillter_name[0]}='{fillter_data[0]}'")

    closeCommit(db)

def readData(path, table, data_name, fillter_name, fillter_data):
    if path == "":
        db = sqlite3.connect("mainDb.db")
        cr = db.cursor()
    else:
        db = sqlite3.connect(f"{path}\\mainDb.db")
        cr = db.cursor()

    if len(data_name) == 1 and len(fillter_name) == 0:
        readed_data = cr.execute(f"SELECT {data_name[0]} FROM {table}").fetchall()

    closeCommit(db)

    return readed_data

def updateData(path, table, data_name, data, fillter_name, fillter_data):
    if path == "":
        db = sqlite3.connect("mainDb.db")
        cr = db.cursor()
    else:
        db = sqlite3.connect(f"{path}\\mainDb.db")
        cr = db.cursor()
    db.execute("PRAGMA foreign_keys = 1")

    if len(data_name) == 1 and len(fillter_name) == 1:
        cr.execute(f"UPDATE {table} SET {data_name[0]}='{data[0]}' WHERE {fillter_name[0]}='{fillter_data[0]}'")

    closeCommit(db)

def closeCommit(db):
    db.commit()
    db.close()

################### Json ###################
def readJson(file):
    with open(file) as f:
        readed_data = json.load(f)

    return readed_data

def SaveJson(file, new_data):
    with open(file, "w") as w:
        json.dump(new_data, w, indent=2)
