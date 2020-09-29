list1=list(input("enter your list: "))
print ("you enter list : ",list1)
def menu():
   print ("--------------")
   print ("[  your list ]")
   print ("--------------")
   print ("1) add element")
   print ("2) del element")
   print ("3) index value")
   print ("4) print list ")
   print ("5) quit list  ")
   print ("----------------------------------------")
   return int(input("Ro706#~ choose your option: "))

#NOW THE PROGRAM REALLY STARTS,AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
  choice = menu()
  if choice == 1:
      a = input("element add :")
      list1.append(a)
      print ("your list",list1)
  elif choice == 2:
      n=input("element del : ")
      list1.remove(n)
      print (list1)
  elif choice == 3:
      n=input("enter element: ")
      print (list1.index(n))
  elif choice == 4:
      print (list1)
  elif choice == 5:
      loop = 0
print ("made by Ro706")
