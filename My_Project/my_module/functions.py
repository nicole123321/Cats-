import random
import string

from time import sleep
from IPython.display import clear_output
from Animal import *

"""method from A4 assignment- unchanged"""
def check_bounds(position, size):
    for item in position:
        if item<0 or item>= size:
            return False
    return True

"""" Method from A4 assignment- unchanged"""
def add_lists(list1, list2):
    output=[]
    for it1, it2 in zip(list1, list2):
        value= it1+it2
        output.append(value)
    
    return output

""""this method will show position of the animals on the list"""
def element_count(animal_positions, number):
    x=animal_positions[number]
    list_to_return=[]
    for i in range(len(animal_positions)):
        if x==animal_positions[i] and i !=number:
            list_to_return.append(i)
    
    return list_to_return 

"""" this method inputs the all the animal positions, and animal fight moves
list and checks which animal is at the same position as the current one. 
It then appends the corresponding fight move to a list which is then returned. """
    
#in the same grid position
def check_elements(animal_positions, animal_fights, number):
    list_to_return=[]
    x=animal_positions[number]
    list_to_return=[]
    for i in range(len(animal_positions)):
        if x==animal_positions[i] and i is not number:
            list_to_return.append(animal_fights[i])

    return list_to_return 
       
import random
import string

from time import sleep
from IPython.display import clear_output
""" The basics of the board is from A4."""
def play_board(animals, n_iter=25, grid_size=5, sleep_time=0.3):
    """Run a bot across a board.
    
    Parameters
    ----------
    bots : Animal() type or list of Animal() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
    """
    
    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(animals, list):
        animals = [animals]
    """ A4"""
    # Update each bot to know about the grid_size they are on
    for animal in animals:
        animal.grid_size = grid_size
    for animal in animals:
        print(animal.position)
        print('in position')    
    
    #saves the coordinates of where food is on the grid 
    
   
     
    """ My code- made the board differently- so it is able to add a character representing
     food (*) create grid that food can be placed on randomly no more than 25% of board."""
    for it in range(n_iter):
        grid_list=[]
        food_coordinate=[]
        
        for x in range(grid_size):
            grid_list.append([])
            for y in range(grid_size):
                probability= random.randrange(1,5,1)
                if probability==1:
                    character= '*'
                    food_coordinate.append([x,y])
                
                if probability>1:
                    character='.'
                                  
                grid_list[x].append(character)
       
        #update each bot to know what coordinates are the food coordinate
        for animal in animals:
            animal.food_coordinate= food_coordinate
          
        # Add bot(s) to the grid
        """A4"""
        animal_p_list=[]
        animal_second_list=[]
        """modified with variables to save positions of animal, and their attributes"""
        for animal in animals:
            #want to save position of animals and check which ones are on the same place
            grid_list[animal.position[0]][animal.position[1]] = animal.character
            animal_p_list.append(animal.position)
            animal_second_list.append(animal.fight_move)
            
        """My code- list with position and name, which can then be zipped through for loop  
        This is where animals who are on the same spot will fight, by calling class 
        fight function. If animal is killed, it will be removed from lists
        result of this should be updates on animal list"""
        
        for animal, position in zip(animals, range(len(animals))):
            if it>10:
                animal.position_in_list=position
                #using methods created to generate fight list
                fight_list= check_elements(animal_p_list,animal_second_list,position)
                position_list= element_count(animal_p_list,position)
                animal.fight_list= fight_list
                animal.position_list=position_list
                if fight_list !=[]:
                    
                    update_list= animal.fight1()
                    #update list 
                    for item in update_list:
                        del animals[item]
                        del animal_p_list[item]
                        del animal_second_list[item]
            
        """ this will make the animal eat when it comes across food, which results in 
        change of moves for the animal"""
        for animal,position in zip(animals, range(len(animals))):
            animal.position_in_list= position
            if animal.position in food_coordinate:                 
                animal.eat()
                      
        """From A4"""
        # Clear the previous iteration, print the new grid (as a string), and wait
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)

        # Update bot position(s) for next turn
        for animal in animals:
            animal.move()