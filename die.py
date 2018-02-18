#  Pygal Gallery

#  Goto http://www.pygal.org/; click Documentation and then
#     click Chart types. Each example includes source code 

#  This die class to be used for visualizations

#  The _init_() method takes one optional arg. With this 
#      class when an instance o our die is created, the number
#      of sides will always be six if no arg is included. If an
#      arg is included, that value is used to set the number of 
#      sides on the die
#  The roll() method uses the randit() function to return a 
#      random number btw 1 and the number of sides

#  Creating the Die Class

from random import randint

class Die():
    """class representing a single die"""

    def _init_(self, num_sides = 6):
        """assume a 6 sided die"""
        self.num_sides = num_sides

    def roll(self):
        """return a random value btw 1 and number of slides"""
       # return randit(1, self.num_sides)
        return randint(1, 6) 

