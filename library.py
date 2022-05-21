###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #

from SQLConnector import *
from book import Book
from user import User
from copy import Copy

class Library:

  def __init__(self):
    self.connection = connect(host="127.0.0.1", 
                              username="root",
                              password="iamgroot",
                              database="baza_test4")
  
  def selectBooks(self, userdata):
    allResults = []

    query = f"""SELECT * FROM Book WHERE title='{str(userdata)}' OR genre='{str(userdata)}';"""
    foundBooks = readData(self.connection, query)
    if len(foundBooks) != 0:
      for item in foundBooks:
        id = item[0]
        title = str(item[1])
        genre = item[2]
        year = item[3]
        mark = item[4]
        publisherID = item[5]
        authorID = item[6]
        query = f"""SELECT publisher FROM PublisherHouse WHERE idPublisher={str(publisherID)}"""
        publisher = readData(self.connection, query)
        query = f"""SELECT surname FROM Author WHERE idAuthor={str(authorID)}"""
        author = readData(self.connection, query)
        query = f"""SELECT * FROM Copy WHERE Book_idBook={str(id)}"""
        copiesRaw = readData(self.connection, query)
        copies = []
        for item in copiesRaw:
          idCopy = item[0]
          dateRent = item[1]
          dateReturn = item[2]
          isRented = item[3]
          copies.append(Copy(dateReturn, dateRent, isRented, idCopy))
        author = author[0][0]
        publisher = publisher[0][0]
        allResults.append(Book(title, genre, str(year), mark, publisher, author, copies))

    query = f"""SELECT idAuthor, surname FROM Author WHERE surname='{str(userdata)}' OR origin='{str(userdata)}';"""
    foundAuthors = readData(self.connection, query)
    if len(foundAuthors) != 0:
      for item in foundAuthors:
        id = item[0]
        author = item[1]
        query = f"""SELECT * FROM Book WHERE Author_idAuthor='{str(id)}';"""
        foundBooks = readData(self.connection, query)
        for item in foundBooks:
          idBook = item[0]
          title = str(item[1])
          genre = item[2]
          year = item[3]
          mark = item[4]
          publisherID = item[5]
          query = f"""SELECT publisher FROM PublisherHouse WHERE idPublisher={str(publisherID)}"""
          publisher = readData(self.connection, query)
          query = f"""SELECT * FROM Copy WHERE Book_idBook={str(idBook)}"""
          copiesRaw = readData(self.connection, query)
          copies = []
          for item in copiesRaw:
            idCopy = item[0]
            dateRent = item[1]
            dateReturn = item[2]
            isRented = item[3]
            copies.append(Copy(dateReturn, dateRent, isRented, idCopy))
          publisher = publisher[0][0]
          allResults.append(Book(title, genre, str(year), mark, publisher, author, copies))
    query = f"""SELECT idPublisher, publisher FROM PublisherHouse WHERE publisher='{str(userdata)}';"""
    foundPublishers = readData(self.connection, query)
    if len(foundPublishers) != 0:
      for item in foundPublishers:
        id = item[0]
        publisher = item[1]
        query = f"""SELECT * FROM Book WHERE PublisherHouse_idPublisher='{str(id)}';"""
        foundBooks = readData(self.connection, query)
        for item in foundBooks:
          idBook = item[0]
          title = str(item[1])
          genre = item[2]
          year = item[3]
          mark = item[4]
          authorID = item[6]
          query = f"""SELECT surname FROM Author WHERE idAuthor='{str(authorID)}';"""
          author = readData(self.connection, query)
          query = f"""SELECT * FROM Copy WHERE Book_idBook={str(idBook)}"""
          copiesRaw = readData(self.connection, query)
          copies = []
          for item in copiesRaw:
            idCopy = item[0]
            dateRent = item[1]
            dateReturn = item[2]
            isRented = item[3]
            copies.append(Copy(dateReturn, dateRent, isRented, idCopy))
          author = author[0][0]
          allResults.append(Book(title, genre, str(year), mark, publisher, author, copies))
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
