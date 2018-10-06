from gpiozero import DistanceSensor
import time
import decimal

def toString(x):
      n = decimal.Decimal(x)
      strN = str(round(n,2))
      return strN

s0 = DistanceSensor(echo=17, trigger=4)
s90 = DistanceSensor(echo=24, trigger=25)
s180 = DistanceSensor(echo=18, trigger=23)
s135 = DistanceSensor(echo=19, trigger=26)


while True:
   print("s180 = " + toString(s180.distance) +"     s135 = " + toString(s180.distance) + "     s90 = " + toString(s90.distance) + "     s0 = " + toString(s0.distance))
   time.sleep(1)
