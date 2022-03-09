#
# Autor: Jakub Szymkowiak
# class Driver
# frontend 🤬
#

from tkinter import *

from library import Library
from book import *

class Driver:
  def __init__(self, root, lib):
    self.lib  = Library()
    self.lib  = lib
    self.root = Canvas()
    self.root = root
    self.data = []

    self.author = Entry(self.root)
    self.title  = Entry(self.root)
    self.year   = Entry(self.root)
    self.genre  = Entry(self.root)

    self.name    = Entry(self.root)
    self.email   = Entry(self.root)
    self.address = Entry(self.root)
    self.id      = Entry(self.root)

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.scrollbar = Scrollbar(self.root)
    self.list = Listbox(self.root, yscrollcommand=self.scrollbar.set)
  
  def appendData(self, item):
    if item != "":
      self.data.append(item)

  def searchUserButtonHandler(self):

    self.scrollbar.destroy()
    self.list.destroy()

    self.scrollbar = Scrollbar(self.root)
    self.scrollbar.pack(side=RIGHT, fill=Y)

    self.data.clear()

    self.appendData(self.name.get())
    self.appendData(self.email.get())
    self.appendData(self.address.get())
    self.appendData(self.id.get())

    foundUsers = self.lib.searchUser(self.data)

    self.list = Listbox(self.root, yscrollcommand=self.scrollbar.set, width=200)

    for user in foundUsers:
      self.list.insert(END, user.name + ", " +
                            user.email + ", " +
                            user.address + ", " +
                            user.id)
      self.list.insert(END, "")

    self.list.pack(side=LEFT, fill=BOTH)
    self.scrollbar.config(command=self.list.yview)

  def searchBookButtonHandler(self):

    self.scrollbar.destroy()
    self.list.destroy()

    self.scrollbar = Scrollbar(self.root)
    self.scrollbar.pack(side=RIGHT, fill=Y)

    self.data.clear()

    self.appendData(self.author.get())
    self.appendData(self.title.get())
    self.appendData(self.year.get())
    self.appendData(self.genre.get())

    foundBooks = self.lib.searchBook(self.data)

    self.list = Listbox(self.root, yscrollcommand=self.scrollbar.set, width=200)

    for book in foundBooks:
      self.list.insert(END, book.title + ", " + 
                            book.author + ", " + 
                            book.year + ", " + 
                            book.genre)

      if book.status == BookStatus.AVAILABLE:
        self.list.insert(END, "Dostępna")
      elif book.status == BookStatus.RENTED:
        self.list.insert(END, "Wypożyczona")

      self.list.insert(END, "")

    self.list.pack(side=LEFT, fill=BOTH)
    self.scrollbar.config(command=self.list.yview)


  def addBookButtonHandler(self):
    self.canvas.destroy()

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.canvas.pack()

    self.data.clear()

    self.appendData(self.author.get())
    self.appendData(self.title.get())
    self.appendData(self.year.get())
    self.appendData(self.genre.get())

    self.lib.addBook(self.data)

    Label(self.canvas, text="Książka została dodana do bazy").pack()
  
  def addUserButtonHandler(self):
    self.canvas.destroy()

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.canvas.pack()

    self.data.clear()

    self.appendData(self.id.get())
    self.appendData(self.name.get())
    self.appendData(self.email.get())
    self.appendData(self.address.get())

    self.lib.addUser(self.data)

    Label(self.canvas, text="Użytkownik został dodany do bazy").pack()


  def searchBook(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    self.data.clear()

    Label(self.root, text="Autor").pack()

    self.author = Entry(self.root)
    self.author.pack()

    Label(self.root, text="Tytuł").pack()

    self.title = Entry(self.root)
    self.title.pack()

    Label(self.root, text="Rok wydania").pack()
 
    self.year = Entry(self.root)
    self.year.pack()
    
    Label(self.root, text="Gatunek").pack()

    self.genre = Entry(self.root)
    self.genre.pack()
    
    searchBookButton = Button(self.root,
                          text="Szukaj",
                          width=20, height=1,
                          fg="white", bg="#263D42",
                          command=self.searchBookButtonHandler)
    searchBookButton.pack()

  def searchUser(self):
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

    searchUserButton = Button(self.root,
                          text = "Szukaj",
                          width=20, height=1,
                          fg="white", bg="#263D42",
                          command = self.searchUserButtonHandler)
    searchUserButton.pack()

  
  def addBook(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    self.data.clear()

    Label(self.root, text="Autor").pack()

    self.author = Entry(self.root)
    self.author.pack()

    Label(self.root, text="Tytuł").pack()

    self.title = Entry(self.root)
    self.title.pack()

    Label(self.root, text="Rok wydania").pack()
 
    self.year = Entry(self.root)
    self.year.pack()
    
    Label(self.root, text="Gatunek").pack()

    self.genre = Entry(self.root)
    self.genre.pack()

    addBookButton = Button(self.root,
                            text = "Dodaj",
                            width=20, height=1,
                            fg="white", bg="#263D42",
                            command=self.addBookButtonHandler)
    addBookButton.pack()

  def addUser(self):
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
    addUserButton.pack()
    
  
  def changeUser(self):
    for widget in self.root.winfo_children():
      widget.destroy()

    Label(self.root, text="Już niedługo będzie można aktualizować użytkowników").pack()


  def infoPanel(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    Label(self.root, text="Autor: Jakub Szymkowiak").pack()
    Label(self.root, text="E-Biblioteka 2022").pack()
    Label(self.root, text="W bazie jest " + str(self.lib.countBooks) + " książek i " + str(self.lib.countUsers) + " użytkowników").pack()
  