create table book(
book_id integer primary key,
label_id int,
language_id int,
location_id int,
book_title varchar(50),
notes varchar(50),  
foreign key (language_id) references language(language_id)
on delete cascade on update no action,
foreign key (location_id) references location(location_id)
on delete cascade on update no action,
foreign key (label_id) references language(language_id) 
on delete cascade on update no action);

create table author(
author_id integer primary key,
author_name varchar(20),
author_lastname varchar(20));

create table book_author(
author_id int,
book_id int,
primary key(book_id,author_id),
foreign key (author_id) references author(author_id)
on delete cascade on update no action,
foreign key (book_id) references book(book_id)
on delete cascade on update no action);

create table language(language_id integer primary key,
language_name varchar(20));

create table location(location_id integer primary key,
location_name varchar(20));

create table label(label_id integer primary key,
label_name varchar(20));