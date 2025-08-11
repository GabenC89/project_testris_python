import pygame

from game.board import GameBoard

class Engine:

    def __init__(self):
        self.window_width = 800
        self.window_height = 800
        self.window_fillcolor = (0, 0, 0)

        self.game_window = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()

        self.game_board = GameBoard(10, 0, 15, 20)
        print(self.game_board)

    def get_close_keyevent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        return False
    
    def draw_objects(self):
        #objects to draw:
        self.game_window.fill(self.window_fillcolor)

        pygame.display.update()

    def run_game_loop(self):
        while True:
            events = pygame.event.get()

            #Event Handling loop
            for event in events:
                if event.type == pygame.QUIT or self.get_close_keyevent(event):
                    return
            
            #Common logic

            #Draw objects
            self.draw_objects()

            self.clock.tick(60)