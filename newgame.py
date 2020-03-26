from time import *
options= input("Hello Player.Press ENTER to continue.But if you dont want to press ENTER due to a diffrent device, say 'switch'")
if options == "switch":
  a = input("Hello Player, Please Enter a name.")
  if a == "":
    a = " "
  print("so i will call you",a,"?")
  sleep(0.5)
  print("Alrighty mate, get ready for a ride!")
if options == "":
  a = input("Hello Player, Please Enter a name.")
  if a == "":
    a = " "
  print("so i will call you",a,"?")
  sleep(0.5)
  print("Alrighty mate, get ready for a ride!")
  



