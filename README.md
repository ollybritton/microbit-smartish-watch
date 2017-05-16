# Microbit Smartish Watch
This is a tutorial on how to turn your BBC Microbit into a smart-ish watch. I say smart-ish as it can't actually tell the time. Why? I don't know how to implement it (if you feel you could code it in, please do a pull request!).

## Installation
To put this onto your own BBC Microbit, please copy and paste the following code into [this](http://python.microbit.org/editor.html) website. Then click on the top-left hand button labled download. A `.hex` file should appear in your downloads. Take the `.hex` file and drag it into the folder for your BBC Microbit.

If the folder for the Microbit doesn't show up, try using a different cable.

```
"""Microbit Watch v2.1"""

from microbit import *

logos = {
    "paint": "00000:00900:09990:00900:00000",
    "timer": "00000:00000:09090:00000:00000",
    "gofl": "00000:09900:09990:09990:00000",
    "dungeon": "00000:00990:09990:00990:00000",
    "dots1": "00000:00000:09000:00000:00000",
    "dots2": "00000:00000:09900:00000:00000",
    "dots3": "00000:00000:09990:00000:00000",
    "wip": "00900:00900:00900:00000:00900",
}

def colon(string):
    return ":".join([ string[ i:i+5 ] for i in range( 0, len( string ), 5 ) ])

def paint():
    memory = []
    pointer = 0

    while accelerometer.current_gesture() == "face down":
        display.show(Image(logos["dots3"]))

    for i in range(25):
        memory.append(0)

    def convert(last = False):
        result = ""

        if last != True:
            for i in range( len(memory) ):
                if memory[i] == 1:
                    result += "9"

                else:
                    result += "0"

        else:
            for i in range(len(memory)):
                if i == pointer:
                    if memory[i] == 1:
                        result += "9"

                    else:
                        result += "5"

                else:
                    if memory[i] == 1:
                        result += "9"

                    else:
                        result += "0"

        return colon(result)


    while True:
        if accelerometer.was_gesture("shake"):
            pointer = (pointer - 1) % 25

        elif button_a.is_pressed():
            pointer = (pointer + 1 ) % 25

            while button_a.is_pressed():
                pointer

        elif button_b.is_pressed():
            if memory[pointer] == 0:
                memory[pointer] = 1

                while button_b.is_pressed():
                    memory[pointer] = 1

            else:
                memory[pointer] = 0

                while button_b.is_pressed():
                    memory[pointer] = 03

            display.show(Image(convert()))

        elif accelerometer.current_gesture() == "face down":
            while accelerometer.current_gesture() == "face down":
                display.show(Image(logos["dots3"]))
            
            return None

        else:
            converted = convert(True)

            display.show(Image(converted))



def timer():
    seconds = 1

    while accelerometer.current_gesture() == "face down":
        display.show(Image(logos["dots3"]))
        
    display.show(Image("90000:00000:00000:00000:00000"))

    while True:
        seconds += 1
        binary_form = str("{0:b}".format(seconds)).replace("1", "9").replace("0","2")

        if(binary_form == "9999999999999999999999999"):
            print("Somehow, you've left the timer on for over a year. You should really go and reconsider your life.")
            break

        elif button_a.is_pressed():
            while True:
                if button_a.is_pressed():
                    sleep(5000)
                    return None

        elif accelerometer.current_gesture() == "face down":
            while accelerometer.current_gesture() == "face down":
                display.show(Image(logos["dots3"]))
            
            return None
                
                

        display.show( Image( ":".join( [ binary_form[ i:i+5 ] for i in range( 0, len( binary_form ), 5 ) ] ) ) )
        sleep(1000)

def gofl():
    while accelerometer.current_gesture() == "face down":
        display.show(Image(logos["wip"]))

    sleep(1000)

def dungeon():
    while accelerometer.current_gesture() == "face down":
        display.show(Image(logos["wip"]))

    sleep(1000)


def home():
    page = (logos["paint"] + logos["timer"] + logos["gofl"] + logos["dungeon"]).replace(":","")
    page = [ page[ i:i+5 ] for i in range( 0, len( page ), 5 ) ]

    position = 0
    curr_page = colon("".join(page[ position : position + 5]))

    while True:
        if button_a.is_pressed():
            position += 1

            if position < 0:
                position = 0

            elif position >= 15:
                position = 15

            curr_page = colon("".join(page[position:position+5]))

            display.show(Image(curr_page))

            while button_a.is_pressed():
                position

        elif button_b.is_pressed():
            position -= 1

            if position < 0:
                position = 0

            elif position >= 15:
                position = 15

            curr_page = colon("".join(page[position:position+5]))

            display.show(Image(curr_page))

            while button_b.is_pressed():
                position

        elif accelerometer.current_gesture() == "face down":
            if curr_page == colon("".join(page[0:5])):
                paint()
                break

            elif curr_page == colon("".join(page[5:10])):
                timer()
                break

            elif curr_page == colon("".join(page[10:15])):
                gofl()
                break

            elif curr_page == colon("".join(page[15:20])):
                dungeon()
                break



        else:
            display.show(Image(curr_page))

    display.show(Image(curr_page))

while True:
    home()

```

## Parts
There are currently only two main things on the watch. To navigate to these things, load up the Microbit. This page is the navigation section for the watch. To scroll down, use the `A (left)` button and to scroll up use the `B (right)` button. To activate one of these items, turn the Microbit completely upside down so that the LEDs are facing the floor. Upon turning it upright again, the item you selected should be running. 

### Paint
The first is a paint-style piece of software, which is labled `+` in the naviagtion screen. When it is loaded up, a small, faint dot should appear at the top left. This is the pointer. Is you press `A (left)`, the dot will move to the right. If you then press `B (right)` it will toggle the pixel on and off.

If you make a mistake and need to go back a pixel, just shake the device.

### Timer
This is the second item in the navigation, and upon opening a `9` will appear (this is currently a bug). It will then start counting up in binary, as it is too dificult to display the decimal representation of the time on the screen. If you then hold down `A (left)`, it will freeze the timer for 5 seconds before going to the navigation screen once again.

### Ideas
This section of the document is to house new ideas for the watch.

- A [Conway's Game Of Life simulator](https://en.m.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- A dungeon explorer.
- A gravity game, where you have to catch falling objects.
