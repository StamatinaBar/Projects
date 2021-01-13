from utils.database_manager import DatabaseManager

class Database:
    @classmethod
    def database_exists(cls):
        with DatabaseManager() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS Patients(
                        Last_Name TEXT PRIMARY KEY,
                        First_Name TEXT,
                        Age TEXT,
                        Telephone INT,
                        Address TEXT,
                        Cause_of_Examination TEXT,
                        Date INT,
                        Summary TEXT
                     )'''
            cursor.execute(sql)

    @classmethod
    def show_all(cls):
        with DatabaseManager() as cursor:
            cursor.execute("SELECT * FROM Patients")
            patients = cursor.fetchall()
            return patients

    @classmethod
    def insert(cls,surname,name,age,telephone,address,cause,date,summary):
        with DatabaseManager() as cursor:
            sql = "INSERT INTO Patients VALUES(?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (surname, name, age, telephone, address, cause, date, summary))

    @classmethod
    def search(cls,surname):
        with DatabaseManager() as cursor:
            cursor.execute("SELECT * FROM Patients WHERE Last_Name=?", (surname,))
            patients = cursor.fetchall()
            items = [record[7] for record in patients]
            return patients,items

    @classmethod
    def delete(cls, surname):
        with DatabaseManager() as cursor:
            cursor.execute("DELETE FROM Patients WHERE Last_Name=?", (surname,))






