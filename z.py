from sense_hat import SenseHat
from time import sleep
sense = SenseHat ()
sense.show_letter("P", (100,22,45))
sleep (1)
sense.show_letter("U", (100,22,45))
sleep (1)
sense.show_letter("M", (100,22,45))
sleep (1)
sense.show_letter("P", (100,22,45))
sleep (1)
sense.show_letter("K", (100,22,45))
sleep (1)                                                                         
sense.show_letter("I", (100,22,45))
sleep(1)
sense.show_letter("N", (100,22,45))
sleep(1)
r = 225
g = 225
b = 225
sense.clear ((r,g,b))
red = (255,0,0)
blue = (0,0,255)
sense.set_pixel (0,2, blue)
sense.set_pixel (7,4, red)
sense.set_pixel (2,2, (225,0,255))
sense.set_pixel (4,2, (0,0,255))
sense.set_pixel (3,4, (100,0,0))
sense.set_pixel (1,5, (255,225,0))
sense.set_pizel (2,6, (255,0,0))