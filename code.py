# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

sponge_bob_b = digitalio.DigitalInOut(board.BUTTON_B)
sponge_bob_b.direction = digitalio.Direction.INPUT
sponge_bob_b.pull = digitalio.Pull.DOWN


def main():
    print(dir(board))
    print('')
    print(dir(digitalio))
    print('')
    print(dir(led))
    print('')
    print(dir(led.direction))
    while True:
        led.value = sponge_bob_b.value
        if led.value == True:
            print("Your LED lit up")
        else:
            print("The LED isn't lit")
        
    
main()