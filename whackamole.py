import pygame
import random


def draw_grid(screen):
    """Draw a 20x16 grid on the screen with 32x32 squares."""
    grid_color = (0, 0, 0)  # Black color for grid lines
    for x in range(0, 641, 32):  # Vertical lines
        pygame.draw.line(screen, grid_color, (x, 0), (x, 512))
    for y in range(0, 513, 32):  # Horizontal lines
        pygame.draw.line(screen, grid_color, (0, y), (640, y))


def get_random_position():
    """Generate a random grid-aligned position."""
    x = random.randrange(0, 20) * 32  # 20 columns
    y = random.randrange(0, 16) * 32  # 16 rows
    return x, y


def main():
    try:
        pygame.init()

        # Initialize screen and mole image
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole")
        mole_image = pygame.image.load("mole.png")

        # Initialize mole position
        mole_position = (0, 0)  # Start in the top-left square

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole is clicked
                    mouse_x, mouse_y = event.pos
                    mole_rect = pygame.Rect(mole_position[0], mole_position[1], 32, 32)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        mole_position = get_random_position()

            # Fill the screen with light green
            screen.fill("light green")

            # Draw the grid
            draw_grid(screen)

            # Draw the mole
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
