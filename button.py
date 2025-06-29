import pygame

# Button class
class Button:
    def __init__(self, x, y, image, scale):
        # Load and scale the image
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()  # Get mouse position

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
                print("Button clicked!")  # Debugging line

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action  # Ensure this is inside the draw method

