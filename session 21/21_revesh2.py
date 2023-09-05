# format dovom kar ba file haye txt dar python 
with open ('kemaei.txt','a') as f: 
     # as yani dadan name mostear 
    text="""
    Python can be used on a server to create web applications.
    Python can be used alongside software to create workflows.
    Python can connect to database systems. It can also read and modify files.
    Python can be used to handle big data and perform complex mathematics.
    Python can be used for rapid prototyping, or for production-ready software development.
    """
    f.write(text)