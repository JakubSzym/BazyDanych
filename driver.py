###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #

from tkinter import *

from library import Library
from book import *

class Driver:
  def __init__(self, root):
    self.lib  = Library()
    self.root = Canvas()
    self.root = root
    
    self.entryForBooks = Entry(self.root)

    self.entryForUsers = Entry(self.root)    

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.scrollbar = Scrollbar(self.root)
    self.list = Listbox(self.root, yscrollcommand=self.scrollbar.set)
  
  def search():
    return 0
  
  def insertBook():
    return 0
  
  def insertUser():
    return 0
  
  
  def searchUserButtonHandler(self):

    self.scrollbar.destroy()
    self.list.destroy()

    self.scrollbar = Scrollbar(self.root)
    self.scrollbar.pack(side=RIGHT, fill=Y)


    foundUsers = self.lib.selectUser(self.entryForUsers.get())

    self.list = Listbox(self.root, yscrollcommand=self.scrollbar.set, width=200)

    for user in foundUsers:
      self.list.insert(END, user)
      self.list.insert(END, "")

    self.list.pack(side=LEFT, fill=BOTH)
    self.scrollbar.config(command=self.list.yview)

  def searchBookButtonHandler(self):

    self.scrollbar.destroy()
    self.list.destroy()

    self.scrollbar = Scrollbar(self.root)
    self.scrollbar.pack(side=RIGHT, fill=Y)

    foundBooks = self.lib.selectBooks(self.entryForBooks.get())

    self.list = Listbox(self.root, yscrollcommand=self.scrollbar.set, width=200)
  
    for book in foundBooks:
      book.title.split()
      self.list.insert(END, "Tytuł: " + book.title)
      self.list.insert(END, "Autor: " + book.author)
      self.list.insert(END, "Gatunek: " + book.genre)
      self.list.insert(END, "Rok wydania: " + book.year)
      self.list.insert(END, "Wydawca: " + book.publisher)
      self.list.insert(END, "Ocena: " + str(book.mark))
      numberOfCopies = len(book.copies)
      availableCopies = 0
      for copy in book.copies:
        if copy.isRented == 0:
          availableCopies += 1
      self.list.insert(END, "Kopie: " + str(numberOfCopies) +
                            ", w tym dostępne: " + str(availableCopies))
      self.list.insert(END, "")

    self.list.pack(side=LEFT, fill=BOTH)
    self.scrollbar.config(command=self.list.yview)


  def addBookButtonHandler(self):
    self.canvas.destroy()

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.canvas.pack()

    self.lib.insertBook(self.author.get(), 
                        self.origin.get(), 
                        self.title.get(), 
                        self.year.get(),
                        self.genre.get(), 
                        self.publisherName.get(), 
                        self.publisherCity.get())

    Label(self.canvas, text="Książka została dodana do bazy").pack()
  
  ''' def addUserButtonHandler(self):
    self.canvas.destroy()

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.canvas.pack()

    self.data.clear()

    self.appendData(self.id.get())
    self.appendData(self.name.get())
    self.appendData(self.email.get())
    self.appendData(self.address.get())

    self.lib.addUser(self.data)

    Label(self.canvas, text="Użytkownik został dodany do bazy").pack()'''


  def searchBook(self):
    for widget in self.root.winfo_children():
      widget.destroy()

    self.entryForBooks = Entry(self.root)
    self.entryForBooks.pack()
    
    searchBookButton = Button(self.root,
                          text="Szukaj",
                          width=20, height=1,
                          fg="white", bg="#263D42",
                          command=self.searchBookButtonHandler)
    searchBookButton.pack()

  def searchUser(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    self.entryForUsers = Entry(self.root)
    self.entryForUsers.pack()

    searchUserButton = Button(self.root,
                          text = "Szukaj",
                          width=20, height=1,
                          fg="white", bg="#263D42",
                          command = self.searchUserButtonHandler)
    searchUserButton.pack()

  
  def addBook(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    

    Label(self.root, text="Autor").pack()

    self.author = Entry(self.root)
    self.author.pack()

    Label(self.root, text="Kraj pochodzenia autora").pack()
    self.origin = Entry(self.root)
    self.origin.pack()
    Label(self.root, text="Tytuł").pack()

    self.title = Entry(self.root)
    self.title.pack()

    Label(self.root, text="Rok wydania").pack()
 
    self.year = Entry(self.root)
    self.year.pack()
    
    Label(self.root, text="Gatunek").pack()

    self.genre = Entry(self.root)
    self.genre.pack()

    Label(self.root, text="Wydawca").pack()

    self.publisherName = Entry(self.root)
    self.publisherName.pack()

    Label(self.root, text="Miasto").pack()

    self.publisherCity = Entry(self.root)
    self.publisherCity.pack()

    addBookButton = Button(self.root,
                            text = "Dodaj",
                            width=20, height=1,
                            fg="white", bg="#263D42",
                            command=self.addBookButtonHandler)
    addBookButton.pack()

  '''def addUser(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    self.data.clear()
    
    Label(self.root, text="Imię i nazwisko").pack()

    self.name = Entry(self.root)
    self.name.pack()

    Label(self.root, text="Email").pack()

    self.email = Entry(self.root)
    self.email.pack()

    Label(self.root, text="Adres").pack()

    self.address = Entry(self.root)
    self.address.pack()

    Label(self.root, text="PESEL").pack()

    self.id = Entry(self.root)
    self.id.pack()

    addUserButton = Button(self.root,
                            text="Dodaj",
                            width=20, height=1,
                            fg="white", bg="#263D42",
                            command=self.addUserButtonHandler)
    addUserButton.pack()'''
    
  
  '''def edit(self):
    for widget in self.root.winfo_children():
      widget.destroy()

    Label(self.root, text="Już niedługo będzie można obsługiwać zwroty i wypożyczenia").pack()'''


  def infoPanel(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    Label(self.root, text="Jakub Szymkowiak, Jakub Schmid").pack()
    Label(self.root, text="E-Biblioteka 2022").pack()
  