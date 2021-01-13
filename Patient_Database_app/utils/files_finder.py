import os
import shutil

#find files related to a specific patient only

class FilesFinder:
    def __init__(self,surname):
        self.surname=surname
        self.dir=f"C:/Users/user/Desktop/{self.surname}"

    def make_dir(self):
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
            self.dir = f"C:/Users/user/Desktop/{self.surname}"

    def search_files(self):
        entries = os.listdir("C:/Users/user/Desktop/Patient_Examinations")
        for entry in entries:
            if entry.endswith('.docx') and entry.startswith("Examination"):
                shutil.copy(f"C:/Users/user/Desktop/Patient_Examinations/{entry}", self.dir)
        if not os.listdir(self.dir):
            raise FileNotFoundError
