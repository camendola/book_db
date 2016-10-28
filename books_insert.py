import sqlite3

sqlite_file = 'books.db'
table_book = 'book'
column_book = 'book_title'
column_notes = 'notes'
table_author = 'author'
column1_author = 'author_name'
column2_author = 'author_lastname'
table_book_author = 'book_author'
table_language = 'language'
column_language =  'language_name'
table_label = 'label'
column_label = 'label_name'
table_location = 'location'
column_location = 'location_name'
book_id = 'book_id'
author_id = 'author_id'
book_author_id = 'book_author_id'
language_id = 'language_id'
label_id = 'label_id'
location_id = 'location_id'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

title = raw_input("Book title: ").split(' ')
title = ' '.join(title)
title = title.replace("'", "`")
title ="'"+title+"'"

author_input = raw_input("Author: ").split(' ')
author_input[0]="'"+author_input[0]+"'"
author_input[1]="'"+author_input[1]+"'"

c.execute("SELECT * FROM book,author WHERE book_title={value} AND author_lastname={value2};".format(value = title,value2=author_input[1]))
data = c.fetchall()
if data:
    abort = 'N'
    proceed = 'Y' 
    answer = raw_input("This book is already in the database. Continue? (Y/N) ")    
    if answer==abort:
        exit()        

label_input = raw_input("Editor: ").split(' ')
label_input = ' '.join(label_input)
label_input = label_input.replace("'", "`")
label_input ="'"+label_input+"'"

language_input = raw_input("Language: ").split(' ')
language_input = ' '.join(language_input)
language_input = language_input.replace("'", "`")
language_input ="'"+language_input+"'"

location_input = raw_input("Location: ").split(' ')
location_input = ' '.join(location_input)
location_input = location_input.replace("'", "`")
location_input ="'"+location_input+"'"

notes_input = raw_input("Notes: ").split(' ')
notes_input = ' '.join(notes_input)
notes_input = notes_input.replace("'", "`")
notes_input ="'"+notes_input+"'"


c.execute("SELECT * FROM author WHERE author_name={value} AND author_lastname={value2};".format(value = author_input[0],value2=author_input[1]))
data = c.fetchall()
if not data:
    c.execute("INSERT INTO {table}({column},{column2}) VALUES({value},{value2});".format(table = table_author, column = column1_author,column2=column2_author, value=author_input[0], value2=author_input[1]))

c.execute("SELECT * FROM label WHERE label_name={value};".format(value = label_input))
data = c.fetchall()
if not data:
    c.execute("INSERT INTO {table}({column}) VALUES({value});".format(table = table_label, column = column_label, value = label_input))
if label_input:
    c.execute("SELECT label_id FROM label WHERE label_name={value};".format(value = label_input))
    labelID_tuple = c.fetchall()
    labelID=int(labelID_tuple[0][0])

c.execute("SELECT * FROM language WHERE language_name={value};".format(value = language_input))
data = c.fetchall()
if not data:
    c.execute("INSERT INTO {table}({column}) VALUES({value});".format(table = table_language, column=column_language,value = language_input))
if language_input:
    c.execute("SELECT language_id FROM language WHERE language_name={value};".format(value = language_input))
    languageID_tuple = c.fetchall()
    languageID=int(languageID_tuple[0][0])

c.execute("SELECT * FROM location WHERE location_name={value};".format(value = location_input))
data = c.fetchall()
if not data:
    c.execute("INSERT INTO {table}({column}) VALUES({value});".format(table = table_location, column= column_location, value = location_input))
if location_input:
    c.execute("SELECT location_id FROM location WHERE location_name={value};".format(value = location_input))
    locationID_tuple = c.fetchall()
    locationID=int(locationID_tuple[0][0])

c.execute("INSERT INTO book(book_title, language_id, label_id, location_id, notes) VALUES({value},{value2},{value3},{value4},{value5});".format(value=title, value2 = languageID, value3 = labelID, value4 = locationID, value5= notes_input))

c.execute("SELECT {column} FROM book,author WHERE book_title={value} AND author_lastname={value2};".format(column=book_id, value = title,value2 = author_input[1]))
bookID_tuple = c.fetchall()
bookID=int(bookID_tuple[0][0])

c.execute("SELECT {column} FROM author WHERE author_name={value} AND author_lastname={value2};".format(column=author_id, value = author_input[0],value2 = author_input[1]))
authorID_tuple = c.fetchall()
authorID=int(authorID_tuple[0][0])

c.execute("INSERT INTO book_author(book_id, author_id) VALUES({value},{value2});".format(value = bookID, value2=authorID))





conn.commit()
conn.close()
