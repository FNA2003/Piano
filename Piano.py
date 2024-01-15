import pygame
import sys
import random

from notesObject import KEYS




# Background color
colors = [0] * 3

# Number of notes that can be played at the same time (If this is a big number, then we will get a lot of optimization problems)
MAX_NOTES = 4
# Queue of notes that are actually playing
notesQueue = []

# Start pygame
pygame.init()
# Pygame window
width, height = 250, 250
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Piano")
# Font config
font = pygame.font.Font(None, 36)
font_color = (255, 255, 255)
text = "Bb1, Db2, Eb2, Gb1"


# Main loop
while True:
    # Look for the events list of pygame
    for event in pygame.event.get():
        # Quit if the user pressed the "X" of the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Play the key that we press (If we can)
        if event.type == pygame.KEYDOWN:
            try:
                # Max notes security
                notesQueue.append(event.key)
                while len(notesQueue) > MAX_NOTES:
                    KEYS[notesQueue[0]][0].stop()
                    notesQueue = notesQueue[1:]
                

                # Update the text where we can see the notes that we actually playing
                text = ""
                for i in notesQueue:
                    text += KEYS[i][1] + ","
                text=text[0:-1]


                # Play the current pressed note
                KEYS[event.key][0].stop()
                KEYS[event.key][0].play()                


                # Make an RGB random color pick
                colors[0] = random.randint(0, 255)
                colors[1] = random.randint(0, 255)
                colors[2] = random.randint(0, 255)
                # Change the background color :D
                window.fill((
                        colors[0], colors[1], colors[2]
                ))


                # Render the text
                text_surface = font.render(text, True, font_color)
                # Adjust the frame of the text
                text_rect = text_surface.get_rect()
                text_rect.center = (width // 2, height // 2)
                # Draw the text
                window.blit(text_surface, text_rect)

                # Update the screen
                pygame.display.flip()
            except KeyError:
                pass