# file txt
# revesh sakht file txt dar python
f = open('bardia.txt','a') # mode  a --> append
#  mode a --> dar in mode ma dakhel file ra hazf nemikonad balkeh edameh file minevisad 
#  revesh neveshtan dar file txt

text = """
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.
"""
f.write('bardia kemaei ')  # write() --> string migirad 
f.write('')
f.write('sajjad\n')
f.write(text)
