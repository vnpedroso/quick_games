#Importing required packages:
import os
import platform

#Creating instructions:
def instructions():
   print('Hey, hope you enjoy the game!')
   print('Step1: import the tic_tac_toe module')
   print('Step2: create an instance of TicTacToe() class')
   print('Step3: call the start() method on your created instance to start the game')
   print('Step4: call the play_again() method on your created instance to allow replay')
   print('Have fun ^^')

# Creating TicTacToe game:
class TicTacToe():

   def __init__(self):
      self.tile = ['-']*10

   def header(self): 
      print('Welcome to TicTacToe! \nOur keyboard simulates an standard calculator: \n')
      print(' 1',' 2',' 3 ',' ',' -'*3)
      print(' 4',' 5',' 6 ','=',' -'*3)
      print(' 7',' 8',' 9 ',' ',' -'*3)
      print('\n Player X starts!')

   def refresh_screen(self):
      if platform.system == 'Windows':
         os.system('cls')
      else:
         os.system('clear')
               
   def display_board(self):
      print(self.tile[1],self.tile[2],self.tile[3])
      print(self.tile[4],self.tile[5],self.tile[6])
      print(self.tile[7],self.tile[8],self.tile[9])

   def get_input(self):
      while True:
         try:
            position = int(input('Please select a position from 1 to 9: '))
            if position in list(range(1,10)) and self.tile[position] not in ['X','O']:
               return position
               break
            elif position in list(range(1,10)):
               print('This position number is taken!')
            else:
               print('This value position number is out of the 1 to 9 range')
         except ValueError:
            print('Please enter a valid number position!')

   def select_move(self,position,player):
      self.tile[position] = player

   def end_conditions(self):
      if  (self.tile[1] == self.tile[2] == self.tile[3]== 'X' or
         self.tile[4] == self.tile[5] == self.tile[6]== 'X' or
         self.tile[7] == self.tile[8] == self.tile[9]== 'X' or
         self.tile[1] == self.tile[4] == self.tile[7]== 'X' or
         self.tile[2] == self.tile[5] == self.tile[8]== 'X' or
         self.tile[3] == self.tile[6] == self.tile[9]== 'X' or
         self.tile[1] == self.tile[5] == self.tile[9]== 'X' or
         self.tile[3] == self.tile[5] == self.tile[7]== 'X'):
         self.refresh_screen()
         return 'X'
      elif (self.tile[1] == self.tile[2] == self.tile[3]== 'O' or
         self.tile[4] == self.tile[5] == self.tile[6]== 'O' or
         self.tile[7] == self.tile[8] == self.tile[9]== 'O' or
         self.tile[1] == self.tile[4] == self.tile[7]== 'O' or
         self.tile[2] == self.tile[5] == self.tile[8]== 'O' or
         self.tile[3] == self.tile[6] == self.tile[9]== 'O' or
         self.tile[1] == self.tile[5] == self.tile[9]== 'O' or
         self.tile[3] == self.tile[5] == self.tile[7]== 'O'):
         self.refresh_screen()
         return 'O'
      else:
         if '-' not in self.tile[1:]:
            return 'D'
         else:
            return 'N'

   def start(self):
      self.refresh_screen()
      self.header()
      self.display_board()
      player = 'X'
      while self.end_conditions() == 'N':
         if player == 'X':
            self.select_move(self.get_input(),'X')
            self.display_board()
            self.end_conditions()
            player = 'O'
         else:
            self.select_move(self.get_input(),'O')
            self.display_board()
            self.end_conditions()
            player = 'X'
      else:
         self.refresh_screen()
         if self.end_conditions() == 'X':
            print('X has won!')
         elif self.end_conditions() == 'O':
            print('O has won!')
         else:
            print('Its a draw!')

   def play_again(self):
      while True:
         replay = input('Do you want to play again? Y=Yes, N=No: ').upper()
         if replay not in ['Y','N']:
            print('Please answer with Y for yes and N for no')
         elif replay == 'Y':
            self.tile = ['-']*10
            self.start()
         else:
            print('Goodbye!')
            break

#Enabling the code above as an module
if __name__ == '__main__':
   #Playing TicTacToe Game directly from file:
   Game = TicTacToe()
   Game.start()
   Game.play_again()
   
   
