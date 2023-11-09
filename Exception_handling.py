# Exception Handling.


while(True):
  try :
    userdata  =  input("Enter a number:  ")
    userdata = int(userdata)
  except  ValueError:
      print("Not a number. Try again")
  else :
    break
