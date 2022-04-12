CREATE DATABASE baza_test4;
USE baza_test4;

CREATE TABLE Author (idAuthor int primary key, 
surname varchar(45), 
origin varchar(45));

CREATE TABLE PublisherHouse (idPublisher int primary key,
 publisher varchar(45),  
 city varchar(45));

CREATE TABLE Reader (idReader int primary key, 
surname varchar(45), 
email varchar(45), 
address varchar(45), 
phoneNumber varchar(45));

CREATE TABLE Book (idBook int primary key, 
title varchar(45), 
genre varchar(45), 
yearPublish int, 
mark double,
PublisherHouse_idPublisher int,
Author_idAuthor int);

CREATE TABLE Copy (idCopy int primary key, 
dateRent datetime, 
dateReturn datetime, 
isRented boolean, 
Reader_idReader int, 
Book_idBook int);


alter table Copy add foreign key (Reader_idReader) REFERENCES Reader (idReader) ON UPDATE CASCADE ON DELETE CASCADE;
alter table Book add foreign key (Author_idAuthor) REFERENCES Author (idAuthor) ON UPDATE CASCADE ON DELETE CASCADE;
alter table Book add foreign key (PublisherHouse_idPublisher) REFERENCES PublisherHouse (idPublisher) ON UPDATE CASCADE ON DELETE CASCADE;
alter table Copy add foreign key (Book_idBook) REFERENCES Book (idBook) ON UPDATE CASCADE ON DELETE CASCADE;

CREATE TABLE Librarian (idLibrarian int,
surname varchar(45),
login varchar(45), 
passwd varchar(45)); 