use baza_test4;

load data infile '/var/lib/mysql-files/authors.csv'
into table Author
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

load data infile '/var/lib/mysql-files/publishers.csv'
into table PublisherHouse
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

load data infile '/var/lib/mysql-files/users.csv'
into table Reader
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

load data infile '/var/lib/mysql-files/books.csv'
into table Book
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

load data infile '/var/lib/mysql-files/copies.csv'
into table Copy
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

load data infile '/var/lib/mysql-files/librarians.csv'
into table Librarian
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;