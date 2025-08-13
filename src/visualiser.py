"""
Visualiser for Sudoku solving steps using pygame.
"""
import pygame
import sys
import time
class Visualiser:
    def __init__(self, original,solved,cell_size=60,delay=0.05):
        self.original = original
        self.solved = solved
        self.cell_size = cell_size
        self.delay = delay
        self.width = cell_size*9
        self.height = cell_size*9
        self.screen = None
        self.font = None

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Sudoku Visualiser')
        self.font = pygame.font.SysFont('arial',self.cell_size//2)
        self.draw_board(self.original)
        pygame.display.flip()
        time.sleep(1)

        for i in range(9):
            for j in range(9):
                if self.original[i][j] == 0:
                    self.draw_cell(i,j,self.solved[i][j],color=(0,128,0))
                    pygame.display.flip()
                    time.sleep(self.delay)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            time.sleep(0.1)

    def draw_board(self, board):
        self.screen.fill((255,255,255))
        for line in range(10):
            width = 3 if line%3 == 0 else 1
            pygame.draw.line(self.screen,(0,0,0),(0,line*self.cell_size),(self.width,line*self.cell_size),width)
            pygame.draw.line(self.screen,(0,0,0),(line*self.cell_size,0),(line*self.cell_size,self.height),width)
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    text = self.font.render(str(board[i][j]),True,(0,0,0))
                    x = j*self.cell_size + self.cell_size//3
                    y = i*self.cell_size + self.cell_size//4
                    self.screen.blit(text,(x,y))

    def draw_cell(self,i,j,value,color=(0,0,255)):
        rect = pygame.Rect(j*self.cell_size,i*self.cell_size,self.cell_size,self.cell_size)
        pygame.draw.rect(self.screen,(255,255,255),rect)
        pygame.draw.rect(self.screen,color,rect,2)
        text = self.font.render(str(value),True,color)
        x = j * self.cell_size + self.cell_size//3
        y = i * self.cell_size + self.cell_size//4
        self.screen.blit(text,(x,y))
