import mysql.connector
 
## ACA EL CODIGO SE CONCECCTA CON LA BDD

class DataBase:
  def __init__(self):
      self.connection=mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database='virtuapet2'
        )  
      self.cursor=self.connection.cursor()