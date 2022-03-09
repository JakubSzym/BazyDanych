#
# Autor: Jakub Szymkowiak, 2022
# class Library
# backend 😍
#

import csv

from user import User
from book import Book, BookStatus

class Library:

  def __init__(self):
    self.books = []
    self.users = []
    self.countBooks = 0
    self.countUsers = 0

  def readBooksFromDatabase(self):
    with open('database_books.csv', 'r', encoding='utf-8') as csvfile:
      csvbooks = csv.DictReader(csvfile, delimiter=',')
      for book in csvbooks:
        item  = Book(book['ID'], book['Title'], book['Year'], book['Author'], book['Genre'], book['UserID'])
        self.books.append(item)
        self.countBooks += 1


  def readUsersFromDatabase(self):
    with open('database_users.csv', 'r', encoding='utf-8') as csvfile:
      csvusers = csv.DictReader(csvfile, delimiter=',')
      for user in csvusers:
        item = User(user['ID'], user['Name'], user['Email'], user['Address'])
        self.users.append(item)
        self.countUsers += 1
  
  def saveBooksToDatabase(self):
    with open('database_books.csv', 'w', encoding='utf-8') as csvfile:
      fieldnames = ['ID', 'Title', 'Year', 'Author', 'Genre', 'UserID']
      csvbooks = csv.DictWriter(csvfile, fieldnames=fieldnames)

      csvbooks.writeheader()

      for book in self.books:
        item = {'ID'     : book.id, 
                'Title'  : book.title, 
                'Year'   : book.year, 
                'Author' : book.author, 
                'Genre'  : book.genre, 
                'UserID' : book.uid
               }
        csvbooks.writerow(item)

  def saveUsersToDatabase(self):
    with open('database_users.csv', 'w', encoding='utf-8') as csvfile:
      fieldnames = ['ID', 'Name', 'Email', 'Address']
      csvusers = csv.DictWriter(csvfile, fieldnames=fieldnames)

      csvusers.writeheader()

      for user in self.users:
        item = { 'ID'      : user.id,
                 'Name'    : user.name,
                 'Email'   : user.email,
                 'Address' : user.address
               }
        csvusers.writerow(item)
  
  def searchBook(self, bookdata):
    result = []
    for item in bookdata:
      for book in self.books:
        if item == book.author or item == book.title or item == book.year or item == book.genre:
          result.append(book)
    
    return result

  def searchUser(self, userdata):
    result = []
    for item in userdata:
      for user in self.users:
        if item == user.name or item == user.address or item == user.email or item == user.id:
          result.append(user)
    
    return result
  
  def changeUser(self, bookdata, userdata):
    for item in self.books:
      if item == bookdata:
        item.uid = userdata.id

  def addBook(self, bookdata):
    self.countBooks += 1
    book = Book(self.countBooks, bookdata[0], bookdata[1], bookdata[2], bookdata[3], "0")
    
    self.books.append(book)

  def addUser(self, userdata):
    self.countUsers += 1
    user = User(userdata[0], userdata[1], userdata[2], userdata[3])

    self.users.append(user)
