import time
import board
import neopixel
from random import randint
# Declare Any Global Variables

def main():
    print("Starting Code Challenge")
    # Declare Any main() Variables - (Not Global)
    
    # list 'pixels' of indexable neopixles
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
    pixels.fill((0, 0, 0))
    while True:
        time.sleep(0.5)
        pixels[0]=(255, 0, 0)
        time.sleep(0.25)
        pixels[1]=(200,50 , 0)
        time.sleep(0.25)
        pixels[2]=(150, 100,0)
        time.sleep(0.25)
        pixels[3]=(50,255,0)
        time.sleep(0.25)
        pixels[4]=(0, 255, 0)
        time.sleep(0.25)
        pixels[5]=(0,200,50)
        time.sleep(0.25)
        pixels[6]=(0, 150, 100)
        time.sleep(0.25)
        pixels[7]=(0,50,200)
        time.sleep(0.25)
        pixels[8]=(0, 0, 255)
        time.sleep(0.25)
        pixels[9]=(150,0,100)
        time.sleep(0.25)
        pixels.fill((0, 0, 0))
        time.sleep(0.5)
        
        red_part = [0,1,8,9]
        white_part = [2,7]
        blue_part = [3,4,5,6]
        
        for i in range(5):
            for a in red_part:
                pixels[a]=(255,0,0)
            for b in white_part:
                pixels[b]=(150,150,150)
            for c in blue_part:
                pixels[c]=(0,0,255)
            time.sleep(0.1)
            pixels[0:10]=(0,0,0)*10
            i = i + 1
            time.sleep(0.1)
      
            
    print("Ending Code Challenge")

main()
