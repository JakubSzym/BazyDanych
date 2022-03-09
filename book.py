#
# Autor: Jakub Szymkowiak, 2022
# class Book
# backend 😍
#

from enum import IntFlag

class BookStatus(IntFlag):
  AVAILABLE = 0
  RENTED    = 1

class Book:

  def __init__(self, id, title, year, author, genre, uid):
    self.title       = title
    self.year        = year
    self.author      = author
    self.genre       = genre
    self.id          = id
    self.uid         = uid
    if self.uid == "0":
      self.status = BookStatus.AVAILABLE
    else:
      self.status = BookStatus.RENTED

  def __eq__(self, other):
    if self.id == other.id:
      return True
    return False

  
