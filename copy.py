###########################################
# DATA BASE APP                           #
# NAME: E-LIBRARY 2022                    #
# AUTHORS: JAKUB SZYMKOWIAK, JAKUB SCHMID #
######################################### #

class Copy:
  def __init__(self, dateOfReturn, dateRent, isRented, idCopy) -> None:
      self.dateOfReturn = dateOfReturn
      self.dateRent = dateRent
      self.isRented = isRented
      self.idCopy   = idCopy