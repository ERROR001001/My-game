import BaggageClaim
import sys
from os import system, name
import time
def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
Red = "\033[0;31m"
Green = "\033[0;32m"
Blue = "\033[0;34m"
Reset = "\033[0;37m"
print(Blue+"Robotic voice: You have arrived"+Reset)
time.sleep(2)
print(Green+"\nYou hear the shuttle doors slide open")
time.sleep(1)
loop1 = True
while loop1:
  Choice1 = input("\nYou walk out of the shuttle and see two places you could go:\n"+Blue+"1. The Baggage Claim Zone"+Red+"\n2. The Employies Only Area"+Reset+"\nWhere do you go (1/2): ")
  if Choice1 == "1":
    loop1 = False
  elif Choice1 == "2":
    print("\nYou walk towards the employies only area and open the door, on the other side of the door is a the employies only restroom and an employee who forgot to lock the door. ")
    sys.exit(Red+"\nYou got caught.")
  else:
    pass