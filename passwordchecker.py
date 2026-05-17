import pygame, pygwidgets, sys
import pwdclass  # Import the PasswordChecker class


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
pink = (255, 182, 193)
dark_pink = (255, 105, 180)
green = (0, 255, 0)


# Window settings
window_width = 640
window_height = 480
frames_per_second = 30  # Controls the main loop speed



# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((window_width, window_height))  # Create window
pygame.display.set_caption("Password Strength Checker") # Set the window title
clock = pygame.time.Clock()  # Clock for controlling frames



# UI Elements

# Title at the top
title_text = pygwidgets.DisplayText(window, (120, 100), 'Password Strength Checker', fontSize=40, textColor=white)

# Instruction for user
enter_text = pygwidgets.DisplayText(window, (165, 145), 'Please enter your password:', fontSize=30, textColor=white)

# Input box for password entry
pwd_input = pygwidgets.InputText(window, (200, 175), focusColor=red, textColor=dark_pink, initialFocus=True)

# Button to submit password
enter_button = pygwidgets.TextButton(window, (450, 220), 'Enter')

# Stores feedback messages for password rule violations
feedback = []

# Stores the strength label returned by the strength() method
strength = ""

# Stores the display color corresponding to the strength level
color = ""




# Main loop
while True:
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle typing/backspace in input box
        pwd_input.handleEvent(event)
        pwd = pwd_input.getValue()  # Get current password string

        # Check if Enter button is pressed
        if enter_button.handleEvent(event):
            # Clear input box after Enter is pressed
            pwd_input.clearText()

            # Create a PasswordChecker instance
            pwd_instance = pwdclass.PasswordChecker(pwd)
            pwd_instance.analyze()  # Analyze the password

            # Get rule violations and strength
            feedback = pwd_instance.validate()
            strength = pwd_instance.strength()


    # Draw everything on screen
    window.fill(pink)  # Background color

    # Draw static elements
    title_text.draw()
    enter_text.draw()
    enter_button.draw()
    pwd_input.draw()

    # Draw feedback messages dynamically
    y = 260  # Starting y-position
    for line in feedback:

        text = pygwidgets.DisplayText(window, (55, y), line, fontSize=20, textColor=red)
        text.draw()
        y += 30  # Move down for the next message
    
    if strength:

        if strength == "Password is very strong!":
            color = green
        
        elif strength == "Password is moderate.":
            color = white
        
        elif strength == "Password is too weak!":
            color = red
            
        text = pygwidgets.DisplayText(window, (55, y), strength, fontSize=20, textColor=color)
        text.draw()

    # Update the display
    pygame.display.update()
    # Limit the loop speed
    clock.tick(frames_per_second)

