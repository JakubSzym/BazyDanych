#
# Autor: Jakub Szymkowiak
# class Driver
# frontend 🤬
#

from tkinter import *
from library import Library

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
  
  def appendData(self, item):
    if item != "":
      self.data.append(item)

  def searchUserButtonHandler(self):

    self.canvas.destroy()

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.canvas.pack()

    self.data.clear()

    self.appendData(self.name.get())
    self.appendData(self.email.get())
    self.appendData(self.address.get())
    self.appendData(self.id.get())

    foundUsers = self.lib.searchUser(self.data)

    for user in foundUsers:
      Label(self.canvas, text=user.name).pack()
      Label(self.canvas, text=user.email).pack()
      Label(self.canvas, text=user.address).pack()
      Label(self.canvas, text=user.id).pack()
      Label(self.canvas, text="------------------------------").pack()

  def searchBookButtonHandler(self):

    self.canvas.destroy()

    self.canvas = Canvas(self.root, height = 180, width = 500)
    self.canvas.pack()

    self.data.clear()

    self.appendData(self.author.get())
    self.appendData(self.title.get())
    self.appendData(self.year.get())
    self.appendData(self.genre.get())

    foundBooks = self.lib.searchBook(self.data)

    for book in foundBooks:
      Label(self.canvas, text=book.title).pack()
      Label(self.canvas, text=book.author).pack()
      Label(self.canvas, text=book.year).pack()
      Label(self.canvas, text=book.genre).pack()
      Label(self.canvas, text="-------------------------------").pack()


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
    
    Label(self.root, text="Już niedługo będzie to dodawanie książek").pack()

  def addUser(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    Label(self.root, text="Już niedługo będzie tu dodawanie użytkowników").pack()
  
  def changeUser(self):
    for widget in self.root.winfo_children():
      widget.destroy()

    Label(self.root, text="Już niedługo będzie można aktualizować użytkowników").pack()


  def infoPanel(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    
    Label(self.root, text="Autor: Jakub Szymkowiak").pack()
    Label(self.root, text="E-Biblioteka 2022").pack()
  