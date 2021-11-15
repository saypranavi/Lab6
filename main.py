import RPi.GPIO as GPIO
import sys

columnDataPin = 20
rowDataPin = 21
latchPIN = 17
clockPIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup((columnDataPin,rowDataPin,latchPIN,clockPIN),GPIO.OUT)

def shift_update_matrix(input_Col,Column_PIN,input_Row,Row_PIN,clock,latch):
  GPIO.output(clock,0)
  GPIO.output(latch,0)
  GPIO.output(clock,1)

  for i in range(7, -1, -1):
    GPIO.output(clock,0)
    GPIO.output(Column_PIN, int(input_Col[i]))
    GPIO.output(Row_PIN, int(input_Row[i]))
    GPIO.output(clock,1)

  GPIO.output(clock,0)
  GPIO.output(latch,1)
  GPIO.output(clock,1)

smile=[["11111111"],\
      ["11000011"],\
      ["10111101"],\
      ["01011010"],\
      ["01111110"],\
      ["01100110"],\
      ["10111101"],\
      ["11000011"]]

while True:
  try:
    RowSelect=[1,0,0,0,0,0,0,0]
    for i in range(0,8): 
      shift_update_matrix(''.join(map(str, smile[i])), columnDataPin,\
                          ''.join(map(str, RowSelect)),rowDataPin,clockPIN,latchPIN)

      RowSelect = RowSelect[-1:] + RowSelect[:-1]
  except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
