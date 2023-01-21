#!/usr/bin/python3 
 """initialize"""
 
 
 def read_file(filename=""): 
     """create function that read atext file""" 
     with open(filename, encoding="UTF8") as f: 
         line = f.read() 
     print(line, end="") 
     f.close()
