###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #

class Copy:
  def __init__(self, dateOfReturn, isRented, idBook) -> None:
      self.dateOfReturn = dateOfReturn
      self.isRented = isRented
      self.book_IdBook = idBook