if __name__=="__main__":
  import sys, os
  src = ""
  with open(sys.argv[1]) as f:
      for line in f.readlines():
          src += line
  #src=${src//.i.in /for i in }
  def replace(one,two):
    global src
    src=src.replace(one,two)
  replace(".fi.in.range","for i in range(")
  #src=${src//.fi.in.range /for i in range(}
  replace(".fi.in ","for i in ")
  #src=${src//.j.in /for j in }
  replace(".j.in ","for j in ")
  #src=${src//.fj.in.range /for j in range(}
  replace(".fj.in.range ","for j in range ")
  #src=${src//.k.in /for k in }
  replace(".k.in ","for k in range ")
  #src=${src//.fk.in.range /for k in range(}
  replace(".fk.in.range ","for k in range ")
  #src=${src//.fl.in /for l in }
  replace(".fl.n ","for l in ")
  #src=${src//.fl.in.range /for l in range(}
  replace(".fl.in.range ","for l in range(")
  #src=${src//==>/:}
  #src=${src//_use./import }
  replace("_use.","import ")
  #src=${src//4evr==>/while True:}
  replace("4evr:","while True:")
  replace("&&",";")
  replace("|","()")
  replace("__func","def")
  replace("[+]-","#")
  replace(".make_var.str",'=""')
  replace(".make_var.int","=0")
  replace(".make_var.float.","=0.0")
  replace(".eq","==")
  replace("repeat","for i in range(1,")
  replace(".append ","+=")
  replace(".as."," as ")
  replace("~~~","pass")
  replace("exception?:","except Exception as e:")
  replace("main?:","if __name__=='__main__'")
  replace("__1","sys.argv[1]")
  replace("__2","sys.argv[2]")
  replace("__3","sys.argv[3]")
  replace("__4","sys.argv[4]")
  replace("__5","sys.argv[5]")
  replace("__6","sys.argv[6]")
  replace("__7","sys.argv[7]")
  replace("__8","sys.argv[8]")
  replace("__9","sys.argv[9]")
  replace("~~>","):")
  lib = """
import time,os
def _install(it):
  os.system("pip install " + it)
# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def _clear(): 
	# for windows 
	if name == 'nt': 
		os.system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		os.system('clear') 
def echo(it):
  print(it)
def __wait(seconds):
  time.sleep(seconds)
"""
  exec(lib + src)
