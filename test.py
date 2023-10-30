import pygame

def main():
    pygame.init()

    # Initialize the joystick module
    pygame.joystick.init()

    # Check how many joysticks are available
    joystick_count = pygame.joystick.get_count()

    if joystick_count == 0:
        print("No joystick found.")
        return

    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Joystick Name: {joystick.get_name()}")

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    # Handle joystick axis motion events
                    axis = event.axis
                    value = event.value
                    if axis == 1:
                        print(f"Axis {axis}: {value}")
                elif event.type == pygame.JOYBUTTONDOWN:
                    # Handle joystick button press events
                    button = event.button
                    print(f"Button {button} pressed")
                elif event.type == pygame.JOYBUTTONUP:
                    # Handle joystick button release events
                    button = event.button
                    print(f"Button {button} released")

    except KeyboardInterrupt:
        pygame.quit()

if __name__ == "__main__":
    main()
