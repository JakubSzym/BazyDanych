###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #

class Book:

  def __init__(self, title, genre, year, mark, publisher, author, copies):
    self.title                 = title
    self.mark                  = mark
    self.year                  = year
    self.author                = author
    self.genre                 = genre
    self.publisher             = publisher
    self.copies                = copies