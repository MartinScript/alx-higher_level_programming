#!/usr/bin/python3 
 """module 0-read_file.py 
 """ 
  
  
 def read_file(filename=""):
    """Function reads a text file (UTF8) and prints it to stdout.
        Args: 
     filename: file to open 
     Return: 
     file contents
     """ 
     with open(filename, encoding="utf-8") as f_obj: 
         file_content = f_obj.read() 
         print(file_content, end="")
    