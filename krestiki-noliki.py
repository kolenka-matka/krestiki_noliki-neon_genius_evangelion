import pygame
import random

pygame.init()


def check_win(board, sign):
    zero_count = 0
    for row in board:
        zero_count += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if (board[0][col] == sign) and (board[1][col] == sign) and (board[2][col] == sign):
            return sign
    if (board[0][0] == sign) and (board[1][1] == sign) and (board[2][2] == sign):
        return sign
    if (board[0][2] == sign) and (board[1][1] == sign) and (board[2][0] == sign):
        return sign
    if zero_count == 0:
        return 'Ничья'
    return False


class Board():
    def __init__(self, width, height):
        self.width = 30 * 3  # длина
        self.height = 30 * 3  # высота
        self.cell_size = 30
        self.board = [[0] * (self.width // self.cell_size) for i in
                      range(self.height // self.cell_size)]  # матрица нулей размером с нашу доску (квадратики)
        self.count_step = 0
        self.flag = False
        self.win = ''

    def render(self):
        x, y = 0, 0
        for i in range(self.height // self.cell_size):
            for j in range(self.width // self.cell_size):

                if self.win:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)  # перерисовывается пустая ячейка
                    if self.win == 'x':
                        LIGHT_BLUE = (64, 128, 255)  # заливается голубым  (крестик)
                        pygame.draw.line(screen, LIGHT_BLUE, [x, y + self.cell_size], [x + self.cell_size, y], 4)  # из левого нижнего в правый верхний
                        pygame.draw.line(screen, LIGHT_BLUE, [x, y], [x + self.cell_size, y + self.cell_size], 4)  # из левого нижнего в правый верхний
                    else:
                        RED = (200, 35, 55)  # заливается красным (нолик)
                        pygame.draw.circle(screen, RED, (x + self.cell_size // 2, y + self.cell_size // 2), self.cell_size // 2, 2)

                elif self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)  # последний параметр - ширина рамки без заливки
                elif self.board[i][j] == 'x':
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size),1)  # перерисовывается пустая ячейка
                    LIGHT_BLUE = (64, 128, 255)  # заливается голубым  (крестик)
                    pygame.draw.line(screen, LIGHT_BLUE, [x, y + self.cell_size], [x + self.cell_size, y], 4)  # из левого нижнего в правый верхний
                    pygame.draw.line(screen, LIGHT_BLUE, [x, y], [x + self.cell_size, y + self.cell_size], 4)  # из левого нижнего в правый верхний
                elif self.board[i][j] == 'o':
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)  # перерисовывается пустая ячейка
                    RED = (200, 35, 55)  # заливается красным (нолик)
                    pygame.draw.circle(screen, RED, (x + self.cell_size // 2, y + self.cell_size // 2), self.cell_size // 2, 2)
                x += self.cell_size
            y += self.cell_size
            x = 0


    def on_click(self, x, y):
        self.count_step += 1
        i, j = x // self.cell_size, y // self.cell_size  # номер клетки по горизонтали, номер клетки по вертикали
        if self.board[j][i] == 0:
            if self.count_step % 2 != 0:
                self.board[j][i] = 'x' # крестик
            else:
                self.board[j][i] = 'o' # нолик
        if (self.count_step - 1) % 2 == 0: # крестик
            self.win = check_win(self.board, 'x')
        else:
            self.win = check_win(self.board, 'o')

    def pomogite(self):
        return self.flag


x, y = 170, 230
screen = pygame.display.set_mode((x, y))

main_board = Board(x, y)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                k1, k2 = event.pos[0], event.pos[1]
                main_board.on_click(k1, k2)
        if main_board.pomogite():
            running = False
    screen.fill((0, 0, 0))
    main_board.render()
    pygame.display.flip()
