import sqlite3

def DBControl(kategoriSayisi):
    if(kategoriSayisi) == 0:
        print("Kategori bulunamadı")
        return False



class Category:
    def __init__(self,_name,_description):
        self.Name  = _name
        self.Description = _description
    def __str__(self):
        return "Kategori ismi:{}, Aciklama: {}".format(self.Name,self.Description)






class DataBase:
    def __CreateConnection(self):
        self.Connection = sqlite3.connect("CategorySim.db")
        self.Cursor = self.Connection.cursor()
        __query = "create table if not exists Categories (id integer primary key autoincrement,Name text,Description text)"
        self.Cursor.execute(__query)
        self.Connection.commit()
    def __init__(self):
        self.__CreateConnection()
    def CloseConnection(self):
        self.Connection.close()
    def ShowCategories(self):
        __query = "select * from Categories"
        self.Cursor.execute(__query)
        __categoryList= self.Cursor.fetchall()
        if (DBControl(len(__categoryList))) == None:
            for k  in __categoryList:
                kategori = Category(k[1],k[2])
                print(kategori)
    def FindCategory(self,_name):
        __query = "select * from Categories where Name = ?"
        self.Cursor.execute(__query,(_name,))
        __categoryDefault = self.Cursor.fetchall()
        if DBControl(len(__categoryDefault))==None:
            kategori  = Category(__categoryDefault[0][1],__categoryDefault[0][2])
            print(kategori)
    def AddCategory(self,veri:Category):
        __query = "insert into Categories (Name,Description) values (?,?)"
        self.Cursor.execute(__query,(veri.Name,veri.Description))
        self.__Commit()
    def __Commit(self):
         __result = input("İşlemi gercekleştirmek istediginize emin misiniz?(E/H)")
         if __result == "E":
             self.Connection.commit()
         else:
             print("İşlem iptal edildi")
    def DeleteCategory(self,_name):
        __categoryDefault = self.FetchDefault(_name)
        if (DBControl(len(__categoryDefault)))==None:
            __query ="delete from Categories where Name=?"
            self.Cursor.execute(__query,(_name,))
            self.__Commit()
    def UpdateCategory(self,_name,newName,newDescription):
        __categoryDefault = self.FetchDefault(_name)
        if(DBControl(len(__categoryDefault)))==None:
            __query="update Categories set Name = ?, Description = ? where Name = ?"
            self.Cursor.execute(__query,(newName,newDescription,_name))
            self.__Commit()
    def FetchDefault(self,_name):
        __categoryDefault = "select * from Categories where Name= ?"
        self.Cursor.execute(__categoryDefault,(_name,))
        __categoryDefault = self.Cursor.fetchall()
        return __categoryDefault




