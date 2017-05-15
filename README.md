# Microbit Smartish Watch
This is a tutorial on how to turn your BBC microbit into a smartish watch.

## Parts

WIP, so this is just here.

```
import time as t

seconds = 0

while True:
  seconds += 1
  binary_form = str("{0:b}".format(seconds)).replace("1", "9")
  
  if(binary_form == "9999999999999999999999999"):
    break
  
  print( ":".join( [ binary_form[ i:i+5 ] for i in range( 0, len( binary_form ), 5 ) ] ) )
  t.sleep(0.0000001)
  
print("Somehow, you've left the timer on for over a year. You should really go and reconsider your life.")
```
