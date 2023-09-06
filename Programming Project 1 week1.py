P-1.36: Write a Python program that inputs a list of words, separated by whitespace,and outputs how many times each word appears in the list. You dont need to worry about efficiency at this point, however, as this topic is something that will be addressed later in this book.



my_name = ""
# Assignment: Programming Project 1, P1.36
def count_words(words):
    word_count = {}
 # WRITE YOUR CODE HERE
    # Note: Output order does not matter because it is a dictionary
    return word_count
 
 
 
if __name__ == '__main__':
 
    words = "abc ab mno abc a vwx vwx stu mno abc"
    words2 = "abc abc abc"
    print(count_words(words)) # {'abc': 3, 'vwx': 2, 'a': 1, 'mno': 2, 'ab': 1, 'stu': 1}
    print(count_words(words2)) # {'abc': 3}
  


P-2.39: Develop an inheritance hierarchy based upon a Polygon class that has abstract methods area( ) and perimeter( ). In order to avoid less trivial math, let's just Implement classes RightTriangle, Square and Rectangle.



my_name = "XXYYZZ P2"
 
from abc import ABC, abstractmethod
import math
 
 
class Polygon(ABC):
    # YOUR CODE HERE
 
class RightTriangle(Polygon):
    # YOUR CODE HERE
 
class Rectangle(Polygon):
    # YOUR CODE HERE
 
class Square(Rectangle):  # A square is a specific type of rectangle
    # YOUR CODE HERE
 
 
if __name__ == "__main__":
    # create a right triangle with base 3 and height 4
    rt = RightTriangle(3, 4)
    print("Right Triangle area:", rt.area())
    print("Right Triangle perimeter:", rt.perimeter())
 
    # create a rectangle with width 3 and height 4
    rect = Rectangle(3, 4)
    print("Rectangle area:", rect.area())
    print("Rectangle perimeter:", rect.perimeter())
 
    # create a square with side 3
    sq = Square(3)
    print("Square area:", sq.area())
    print("Square perimeter:", sq.perimeter())
 


Note: submit the source code it MUST be free of any syntax errors and MUST run successfully, otherwise, automatic 0. Please, submit the source code (.py) file(s) in blackboard, email submissions will NOT be accepted. (If you have any issue with a code, feel free to write to me though an email, Blackboard messages or communicate with your classmates)

Submission Content
Submission Content
P-1.36:

words = input('Enter words:\n')
words=words.split(' ')
 
word_list = set(words)
word_count={}
for word in word_list:
    if word != '':
        word_count[word]=words.count(word)
 
print(word_count)
P-2.39:

# Import ABC module to define abstract class
 
from abc import ABC, abstractmethod
from math import sqrt
 
# Base class
class Polygon(ABC):
 
    @abstractmethod
    def area(self, side1, side2):
        pass
 
    @abstractmethod
    def perimeter(self, side1, side2):
        pass
 
 
class RightTriangle(Polygon):
    # default constructor
    def __init__(self, base, height):
        self.base = base
        self.height = height
 
    # overriding abstract method
    def area(self):
        # Return area
        return 0.5 * self.base * self.height
 
    def perimeter(self):
        # Return perimeter
        hyp = sqrt(self.base*self.base + self.height*self.height)
        return self.base + self.height + hyp
 
 
class Square(Polygon):
    # default constructor
    def __init__(self, side):
        self.side = side
 
    # overriding abstract method
    def area(self):
        # Return area
        return self.side * self.side
 
    def perimeter(self):
        # Return perimeter
        return 4 * self.side
 
 
class Rectangle(Polygon):
    # default constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width
 
    # overriding abstract method
    def area(self):
        # Return area
        return self.length * self.width
 
    def perimeter(self):
        # Return perimeter
        return 2 * (self.length + self.width)
 
 
# Driver code
# Instantiate class
t = RightTriangle(4, 5)
# Function calls
print('Right Triangle ->> Area      :', t.area())
print('Right Triangle ->> Perimeter :', t.perimeter())
 
# Instantiate class
s = Square(7)
# Function calls
print('\nSquare ->> Area      :', s.area())
print('Square ->> Perimeter :', s.perimeter())
 
# Instantiate class
r = Rectangle(3, 8)
# Function calls
print('\nRectangle ->> Area      :', r.area())
print('Rectangle ->> Perimeter :', r.perimeter())
