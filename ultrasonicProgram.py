from gpiozero import DistanceSensor
import time
import decimal
import subprocess


def speakIt(text):
      subprocess.call(['./espeakScript.sh', text])
      
def toString(x):
      n = decimal.Decimal(x)
      strN = str(round(n,2))
      return strN


#initialize sensors
s0 = DistanceSensor(echo=17, trigger=4)
s45 = DistanceSensor(echo=6, trigger=5)
s90 = DistanceSensor(echo=24, trigger=25)
s135 = DistanceSensor(echo=19, trigger=26)
s180 = DistanceSensor(echo=18, trigger=23)

#initialize threshold values
s0_s180_Thresh = .5
s45_s135_Thresh = .7
s90_Thresh = .7
refreshRate = .1

# detect objects
while True:
   print("s180 = " + toString(s180.distance) +"     s135 = " + toString(s135.distance) + "     s90 = " + toString(s90.distance) +"     s45 = "+ toString(s45.distance) + "     s0 = " + toString(s0.distance))
   time.sleep(refreshRate)
   if (s90.distance < s90_Thresh):
         speakIt("Stop! Object in front")
         time.sleep(1)
   elif(s45.distance < s45_s135_Thresh):
         speakIt("Object slight right")
         time.sleep(1)
   elif(s135.distance < s45_s135_Thresh):
         speakIt("Object slight left")
         time.sleep(1)
   elif(s0.distance < s0_s180_Thresh):
         speakIt("Object on right")
         time.sleep(1)
   elif(s180.distance < s0_s180_Thresh):
         speakIt("Object on left")
         time.sleep(1)
