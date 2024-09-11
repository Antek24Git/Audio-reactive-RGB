# Audio reactive RGB

## initial setup
To get the reactive rgb to work the process is slightly complicated, the reason for this is  your audio output must be recognized as a input by the program, i reccomend using Voicemeeter Banana along with VB Audio Cable. once you have these installed open up voicemeeter Banana, under A1 select your speaker, for A2 and A3 select VB audio cable, then under hardware input select VB audio cable, if done correctly it should look like this. ![voicemeeter demo.png](voicemeeter%20demo.png)
## Hardware setup
Now we will be connecting the rgb to the arduino, now this may seem wrong but you must connect the 5v on the led strip to the ground on the arduino, next connect the red pin to pin 9 on arduino green on 10 and blue on 11
## Arduino Setup
To  setup the arduino you must run the [ arduino code for audo resposive rgb.ino ] file and then **close arduino ide**.
if you wish to edit the color of the rgb you can change it by editing lines 24-26 of the ino file
## Finishing up
the last thing left to do is to run the python file and play some audio, if setup done correctly you should now have audio reactive rgb.