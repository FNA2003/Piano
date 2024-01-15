
## IMPORTANT!

In order to run this project you **must** download the following library:
- Pygame, i used 2.0.2

### Buttons

Here you'll see a list of the buttons that i used for the piano and the corresponding notes.

*If you want to change the button used for a note, then, go to the **notesObject** file and change the code number of the key asociated with the note, for example, the note 'Ab3' is asociated to the code '57' wich is the number '9' (I'll help you get the key code, you may see it at the bottom).*


| KEY SYMBOL| NOTE |
|---|---|
| F1 | C2 |
| F2 | Db2 |
| F3 | D2 |
| F4 | Eb2 |
| F5 | E2 |
| F6 | F2 |
| F7 | Gb2 |
| F8 | G2 |
| F9 | Ab2 |
| F10 | A2 |
| F11 | Bb2 |
| F12 | B2 |
| 1 | C3 |
| 2 | Db3 |
| 3 | D3 |
| 4 | Eb3 |
| 5 | E3 |
| 6 | F3 |
| 7 | Gb3 |
| 8 | G3 |
| 9 | Ab3 |
| 0 | A3 |
| ' | Bb3 |
| ¿ | B3 |
| q | C4 |
| w | Db4 |
| e | D4 |
| r | Eb4 |
| t | E4 |
| y | F4 |
| u | Gb4 |
| i | G4 |
| o | Ab4 |
| p | A4 |
| ´ | Bb4 |
| + | B4 |
| a | C5 |
| s | Db5 |
| d | D5 |
| f | Eb5 |
| g | E5 |
| h | F5 |
| j | Gb5 |
| k | G5 |
| l | Ab5 |
| ñ | A5 |
| { | Bb5 |
| } | B5 |
| < | C6 |
| z | Db6 |
| x | D6 |
| c | Eb6 |
| v | E6 |
| b | F6 |
| n | Gb6 |
| m | G6 |
| , | Ab6 |
| . | A6 |
| - | Bb6 |
| RShift | B6 |
---
*Note:* You may see some keys that your keyboard doesn't have or are not direct keys (you have to make a combination to reach them), and, that is because i have an Argentinian keyboard.


####  Button key code

You can get the key-code of 'x' button by a script that you have to run on a **new** python file and then, copy the codes that the console will write.

---
Again, if it is not clear enought, the file where you should paste the code of the key will be the 'notesObject' file, and so you can see it clear:
```
{
	# [...]
	# The number of bellow its the code of a key in pygame   
	1073741887: 
        [mixer.Sound(MUSIC_ROUTE+"F2.mp3"), "F2"]
    ,
    1073741888: 
	    [mixer.Sound(MUSIC_ROUTE+"Gb2.mp3"), "Gb2"] # The second element its the note name
    ,
	# [...]
}
```
---

This is the code that you have to paste in a **NEW** python file and remember, the key code will be in the terminal:
```
import pygame
import sys  


# Start pygame
pygame.init()
# Pygame window
width, height =  250,  250
window = pygame.display.set_mode((width, height))

# Main loop
while  True:
	# Look for the events list of pygame
	for event in pygame.event.get():
		# Quit if the user pressed the "X" of the window
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# Print if we press a key
		if event.type == pygame.KEYDOWN:
			print(event.key)
```