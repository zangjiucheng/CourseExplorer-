from ..Utiles.manageDBClass import connectDB


class dbClass:
    def __init__(self):
        self.ClassCollectionName = "Class2024Winter"



        self.url = "mongodb+srv://user:hCk2I9rMak6dMKpf@uwdatabase.kcmy6ok.mongodb.net/?retryWrites=true&w=majority"

        self.ClassDATABASE = connectDB(mongo_host=self.url)
        self.ClassDATABASE.connectDataBase('UWRegistrationDB')
        self.ClassDATABASE.selectCollection(self.ClassCollectionName)
        self.ClassSchedule = self.ClassDATABASE.mongo_collection

        self.CourseDetailDB = connectDB(mongo_host=self.url)
        self.CourseDetailDB.connectDataBase("UWRegistrationDB")
        self.CourseDetailDB.selectCollection("CourseDetail")
        self.CourseDescribe = self.CourseDetailDB.mongo_collection

    def switchCollection(self, collectionName):
        self.ClassCollectionName = collectionName
        self.ClassDATABASE.selectCollection(self.ClassCollectionName)
        self.ClassSchedule = self.ClassDATABASE.mongo_collection
