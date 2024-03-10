#File:CS112_A1_T1_Game3_20230414.py
#purpose: A subtract square . each player should play numbers that have a square root which is less than the number of coins . who take last wins
#Author: malk ahmed fouad mohamed
#ID: 20230414
'''#subtract a square :this is a two-player mathematical game of strategy. It is played by two 
people with a pile of coins (or other tokens) between them. The players take turns removing 
coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). 
The player who removes the last coin wins.'''

print("welcome to subtract a square ")
import math 
def is_perfect_square(z):      # to check square root                                                                                                                                                                                                       
     sqrt_z=math.sqrt(z)
     return sqrt_z.is_integer()

while True:
    user_choice =str(input("Please choose between A) user and B) randam: "))
    if user_choice == 'A' or user_choice == 'B':
        print("Thank you for choosing", user_choice)
        break  
    else:
        print("Invalid choice. Please choose between A and B.")
if user_choice =='A':# if the user is the one who will enter the number of coins 

  while True:
   n_coins=int(input("enter the number of coins"))
   if not is_perfect_square(n_coins):
    print("Thank you for choosing not square number")
    break  
   else:
        print("Invalid choice. Please choose not square number  .")
#game playing     
 
  while n_coins>0:
    while True:
      try:
         choice_player1=int(input("player 1 enter a number :"))
         is_perfect_square(choice_player1)
      except ValueError: # if player does not insert an integer
        print("please enter an integer")
        continue
      if not is_perfect_square(choice_player1):
         print("invalid,player 1 please insert a valid number")
         continue
      n_coins-=choice_player1
      print(f'Now we have{n_coins}')
      if n_coins<0 :
          print("n_coins are negative. please try again")
          n_coins+=choice_player1  #return the withdrawn value 
          continue
          
      if n_coins==0:
         print("player1 is winner")
      break
    while n_coins>0:
      try:
        choice_player2=int(input("player 2  enter a number:"))
        is_perfect_square(choice_player2)
      except ValueError: # if player does not insert an integer
        print("please enter an integer")
        continue
      if not is_perfect_square(choice_player2):
         print("invalid,player 2 please insert a valid number")
         continue
      n_coins-=choice_player2
      print(f'Now we have{n_coins}')
      if n_coins <0 :
        print("n_coins are negative. please try again ")
        n_coins+=choice_player2  #return the withdrawn value 

        continue 
      if n_coins==0:
        print("player 2 is a winner")
      break
   
if user_choice=='B':
  n_coins2=20
  print('number of n_coins2 = 20 ')
  #game playing
  while n_coins2>0:
    while True:
      try:                       # to check if user enter string or integer 
        choice_player1=int(input("player 1 enter a number :"))
        is_perfect_square(choice_player1)
      except ValueError:
        print("please enter an integer")
        continue
      
      if not is_perfect_square(choice_player1):
         print("invalid,player 1 please insert a valid number")
         continue
      n_coins2-=choice_player1
      print(f'Now we have{n_coins2}')
      if n_coins2<0 :
          print("n_coins are negative. please try again")
          n_coins2+=choice_player1 #return the withdrawn value 
          continue
      if n_coins2 ==0:
        print("player1 is winner")
      break
    while n_coins2>0:
      try:        # to check if user enter string or integer 
        choice_player2=int(input("player 2  enter a number:"))
        is_perfect_square(choice_player2)
      except ValueError: # if player does not insert an integer
        print("please enter an integer")
        continue

      if not is_perfect_square(choice_player2):
         print("invalid,player 2 please insert a valid number")
         continue
      n_coins2-=choice_player2
      print(f'Now we have{n_coins2}')
      if n_coins2 <0 :
        print("n_coins are negative. please try again")
        n_coins2+=choice_player2  #return the withdrawn value 
        continue
      if n_coins2==0 :
         print("player 2 is a winner")
      break



