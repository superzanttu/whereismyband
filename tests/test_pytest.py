import sys
import os
print ("Adding previous folder into path")
current = os.path.dirname(os.path.realpath(__file__))
print("  Current folder:",current)
parent = os.path.dirname(current)
print("  Parent folder:",parent)
sys.path.append(parent)


from inc_dec import *
 
def test_kaa():
    assert True == True

def test_increment():
    assert increment(3) == 4

def test_decrement():
    assert decrements(3) == 4
