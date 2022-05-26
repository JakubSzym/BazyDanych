###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #

from SQLConnector import *
from book import Book
from user import User
from copy import Copy
from datetime import datetime, timedelta

class Library:

  def __init__(self):
    self.connection = connect(host="127.0.0.1", 
                              username="root",
                              password="iamgroot",
                              database="bazadanych")
  
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
  
  def insertBook(self, authorName, authorOrigin, title, year, genre, publisherName, publisherCity, numberOfCopies):
    query = f"""SELECT surname FROM Author WHERE surname='{authorName}';"""
    foundAuthor = readData(self.connection, query)
    if len(foundAuthor) == 0:
      query = f"""INSERT INTO Author (surname, origin) VALUES ('{authorName}', '{authorOrigin}');"""
      ret = executeQuery(self.connection, query)
    
    query = f"""SELECT publisher FROM PublisherHouse WHERE publisher='{publisherName}';"""
    foundPublisher = readData(self.connection, query)
    if len(foundPublisher) == 0:
      query = f"""INSERT INTO PublisherHouse (publisher, city) VALUES ('{publisherName}', '{publisherCity}');"""
      ret = executeQuery(self.connection, query)
    
    query = f"""SELECT title FROM Book WHERE title='{title}' AND yearPublish={year} AND genre='{genre}';"""
    foundBook = readData(self.connection, query)
    if len(foundBook) == 0:
      query = f"""SELECT idPublisher FROM PublisherHouse WHERE publisher='{publisherName}' AND city='{publisherCity}';"""
      idPublisher = readData(self.connection, query)
      query = f"""SELECT idAuthor FROM Author WHERE surname='{authorName}' AND origin='{authorOrigin}';"""
      idAuthor = readData(self.connection, query)
      query = f"""INSERT INTO Book (title, genre, yearPublish, mark, PublisherHouse_idPublisher, Author_idAuthor) 
                  VALUES ('{title}', '{genre}', '{year}', 0, '{idPublisher[0][0]}', '{idAuthor[0][0]}');"""
      executeQuery(self.connection, query)
      query = f"""SELECT idBook FROM Book WHERE title='{title}' AND yearPublish={year} AND genre='{genre}';"""
      idBook = readData(self.connection, query)
      idBook = idBook[0][0]
      i = 0
      today =  datetime.now()
      deadline = today + timedelta(days=30)
      for i in range(int(numberOfCopies)):
        query = f"""INSERT INTO Copy (dateRent, dateReturn, isRented, Reader_idReader, Book_idBook) 
                    VALUES ('{today.strftime("%Y-%m-%d")}', '{deadline.strftime("%Y-%m-%d")}', 0, 1, {idBook});"""
        executeQuery(self.connection, query)
  
  def insertUser(self, userdata):
    return 0
  
  def insertCopy(userdata):
    return 0
