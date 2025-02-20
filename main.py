import pygame

pygame.init()
window = pygame.display.set_mode(size=(600, 480))

while True:
    menu = Menu(self.window)
    menu.run()
    pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()  # end pygame




from code.Game import Game

game = Game()
game.run()