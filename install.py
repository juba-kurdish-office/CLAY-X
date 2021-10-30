import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

yellow="\033[1;33m"
blue="\033[1;34m"
nc="\033[00m"

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input(f"{yellow}Do you want to install CLAY-X [Y/n]> {nc}")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/CLAY-X"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/CLAY-X")
          os.system(system.sudo+" cp -r modules core CLAY-X.py "+system.conf_dir+"/CLAY-X")
          os.system(system.sudo+" cp -r core/CLAY-X "+system.bin)
          os.system(system.sudo+" cp -r core/clayx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/CLAY-X")
          os.system(system.sudo+" chmod +x "+system.bin+"/clayx")
          os.system("cd .. && "+system.sudo+" rm -rf CLAY-X")
          if os.path.exists(system.bin+"/CLAY-X") and os.path.exists(system.conf_dir+"/CLAY-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}CLAY-X{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}CLAY-X{nc}@{blue}space {yellow}$ {nc}")
            break
        else:
          if os.path.exists(system.conf_dir+"/CLAY-X"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/CLAY-X")
          os.system("cp -r modules core CLAY-X.py "+system.conf_dir+"/CLAY-X")
          os.system("cp -r core/CLAY-X "+system.bin)
          os.system("cp -r core/clayx "+system.bin)
          os.system("chmod +x "+system.bin+"/CLAY-X")
          os.system("chmod +x "+system.bin+"/clayx")
          os.system("cd .. && rm -rf CLAY-X")
          if os.path.exists(system.bin+"/CLAY-X") and os.path.exists(system.conf_dir+"/CLAY-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}CLAY-X{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}CLAY-X{nc}@{blue}space {yellow}$ {nc}")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
