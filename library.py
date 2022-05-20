###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #

from SQLConnector import *
from author import Author
from book import Book
from user import User

class Library:

  def __init__(self):
    self.connection = connect(host="127.0.0.1", 
                              username="root",
                              password="iamgroot",
                              database="baza_test4")
  
  def selectBooks(self, userdata):
    allResults = []

    query = f"SELECT * FROM Book WHERE title='{str(userdata)}';"
    foundBooks = readData(self.connection, query)
    if len(foundBooks) != 0:
      for item in foundBooks:
        allResults.append(item)
    
    query = f"""SELECT * FROM Author WHERE surname='{str(userdata)}';"""
    foundAuthors = readData(self.connection, query)

    if len(foundAuthors) != 0:
      for item in foundAuthors:
        allResults.append(item)
    
    query = f"""SELECT * FROM Author WHERE origin='{str(userdata)}';"""
    foundAuthors = readData(self.connection, query)

    if len(foundAuthors) != 0:
      for item in foundAuthors:
        allResults.append(item)
    
    query = f"SELECT * FROM PublisherHouse WHERE publisher='{str(userdata)}'"
    foundPublishers = readData(self.connection, query)
    if len(foundPublishers) != 0:
      for item in foundPublishers:
        allResults.append(item)
    return allResults
  
  def selectUser(self, userdata):
    allResults = []
    query = f"SELECT * FROM Reader WHERE surname='{str(userdata)}';"
    foundUsers = readData(self.connection, query)
    if len(foundUsers) != 0:
      for user in foundUsers:
        allResults.append(user)
    
    query = f"SELECT * FROM Reader WHERE email='{str(userdata)}';"
    foundUsers = readData(self.connection, query)
    if len(foundUsers) != 0:
      for user in foundUsers:
        allResults.append(user)
    
    return allResults


































  
  def insertBook(self, userdata):
    return 0
  
  def insertUser(self, userdata):
    return 0
  
  def insertCopy(userdata):
    return 0
