from gpiozero import DistanceSensor
import time
import decimal

def toString(x):
      n = decimal.Decimal(x)
      strN = str(round(n,2))
      return strN

def printDistances():
      return 0


s0 = DistanceSensor(echo=17, trigger=4)
s45 = DistanceSensor(echo=6, trigger=5)
s90 = DistanceSensor(echo=24, trigger=25)
s135 = DistanceSensor(echo=19, trigger=26)
s180 = DistanceSensor(echo=18, trigger=23)

thisdict ={
      "s0": s0,
      "s90": s180,
      "s135": s135,
      "s180": s180
}


while True:
   print("s180 = " + toString(s180.distance) +"     s135 = " + toString(s135.distance) + "     s90 = " + toString(s90.distance) +"     s45 = "+ toString(s45.distance) + "     s0 = " + toString(s0.distance))
   time.sleep(1)
