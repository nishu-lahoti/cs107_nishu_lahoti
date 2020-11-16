#Coder, Listener, Sharer: Drew Pendergrass, Blake Bullwinkel, Nishu Lahoti

#Points of discussion: Discussed use of SQL import option, but it didn't work. Opted to do it manually

# Utilizing Python SQL
import sqlite3

# Created candidates db
db = sqlite3.connect('candidates_db.sqlite') # Create a connection to the database
cursor = db.cursor() 
cursor.execute("DROP TABLE IF EXISTS candidates") # Convenient in case you want to start over

# Creating frame for candidates table
cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_name TEXT, 
               party TEXT NOT NULL)''')

db.commit() # Commit changes to the database

file = open("candidates.txt", "r")

# Looping through the .txt file to extract candidate information
for ind,line in enumerate(file):
    if ind==0: # Skip the header
        continue
    line = line.strip('\n') #Newline character is annoying; get rid of it
    vals = line.split('|') #split string for processing as table input
    candidate_id = int(vals[0]) #cast as int to match with expected table format
    candidate_firstname = vals[1]
    candidate_lastname = vals[2]
    candidate_middlename = vals[3]
    candidate_party = vals[4]
    #add line to the SQL database
    cursor.execute('''INSERT INTO candidates
               (id, first_name, last_name, middle_name, party)
               VALUES (?, ?, ?, ?, ?)''', 
                (candidate_id, candidate_firstname, candidate_lastname, candidate_middlename, candidate_party))
    db.commit() #commit change

# Print out all rows of the table
cursor.execute("SELECT * FROM candidates")
all_rows = cursor.fetchall()
print(all_rows)