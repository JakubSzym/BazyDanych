#!/usr/bin/env python3

#
# Autor: Jakub Szymkowiak, 2022
# Main program
# frontend 🤬
#

from tkinter import *

from library import Library
from driver import Driver

lib = Library()

lib.readBooksFromDatabase()
lib.readUsersFromDatabase()

root = Tk()
root.title("Biblioteka")
root.geometry('800x800')

canvas = Canvas(root, height = 180, width = 500)

driver = Driver(canvas, lib)
driver.infoPanel()

infoPanel = Button(root,
                   text = "Informacje o aplikacji",
                   width=20, height=1,
                   fg="white", bg="#263D42",
                   command = driver.infoPanel)
infoPanel.pack()

bookSearcher = Button(root, 
                      text = "Szukaj książek", 
                      width = 20, height = 1, 
                      fg = "white", bg = "#263D42", 
                      command = driver.searchBook)
bookSearcher.pack()

userSearcher = Button(root, 
                      text = "Szukaj użytkowników", 
                      width = 20, height = 1, 
                      fg = "white", bg = "#263D42",
                      command = driver.searchUser)
userSearcher.pack()

changeUser = Button(root, 
                    text = "Zmień użytkownika książki", 
                    width  = 20, height = 1, 
                    fg = "white", bg = "#263D42",
                    command = driver.changeUser)
userSearcher.pack()

addBook = Button(root, 
                 text = "Dodaj nową książkę", 
                 width = 20, height = 1, 
                 fg = "white", bg = "#263D42",
                 command = driver.addBook)
addBook.pack()

addUser = Button(root, 
                 text = "Dodaj nowego użytkownika", 
                 width = 20, height = 1, 
                 fg = "white", bg = "#263D42",
                 command = driver.addUser)
addUser.pack()

driver.root.pack()

root.mainloop()

lib = driver.lib

lib.saveBooksToDatabase()
lib.saveUsersToDatabase()