"""Microbit Watch v2"""

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
                        result += "8"

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
                pass

        elif button_b.is_pressed():
            if memory[pointer] == 0:
                memory[pointer] = 1

                while button_b.is_pressed():
                    memory[pointer] = 1

            else:
                memory[pointer] = 0

                while button_b.is_pressed():
                    memory[pointer] = 1

            display.show(Image(convert()))

        elif accelerometer.current_gesture() == "face down":
            while accelerometer.current_gesture() == "face down":
                display.show(Image(logos["dots3"]))
            
            return

        else:
            converted = convert(True)

            display.show(Image(converted))


while True:
    paint()
