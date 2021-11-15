# LEDdisplay class

import time
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  numbers = [ 
    0b11111100, # 0
    0b01100000, # 1
    0b11011010, # 2
    0b11110010, # 3
    0b01100110, # 4
    0b10110110, # 5
    0b10111110, # 6
    0b11100000, # 7
    0b11111110, # 8
    0b11100110] # 9

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    self.shifter.shiftByte(LEDdisplay.numbers[num])
  

dataPin, latchPin, clockPin = 23, 24, 25

# Pick a number sequence
sequence = [8, 6, 7, 5, 3, 0, 9]

theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)

while True:
  for n in range(len(sequence)):
    theLEDdisplay.setNumber(sequence[n])
    time.sleep(0.4)