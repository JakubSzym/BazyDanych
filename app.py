#!/usr/bin/env python3

###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #


from tkinter import *

from library import Library
from driver import Driver

root = Tk()
root.title("Biblioteka")
root.geometry('800x800')

canvas = Canvas(root, height = 180, width = 500)

driver = Driver(canvas)
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
                      text="Przeglądanie użytkowników",
                      width = 20, height = 1, 
                      fg = "white", bg = "#263D42", 
                      command = driver.searchUser)
userSearcher.pack()

driver.root.pack()

root.mainloop()
