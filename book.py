#
# Autor: Jakub Szymkowiak, 2022
# class Book
# backend 😍
#

from user import User

class Book:

  def __init__(self, id, title, year, author, genre, uid):
    self.title       = title
    self.year        = year
    self.author      = author
    self.genre       = genre
    self.id          = id
    self.uid         = uid

  def __eq__(self, other):
    if self.id == other.id:
      return True
    return False

  
