import pygame
import random
from collections import Counter

pygame.init()

win_width = 900
win_height = 600
initial_delay = 80
win = pygame.display.set_mode((win_width, win_height))

class Snake():
    def __init__(self):
        self.color = (30, 150, 45)
        self.x = win_width // 2
        self.y = win_height // 2
        self.width = 30
        self.height = 30
        self.direction = "STOP"
        self.rect_numbers = 3
        self.positions_list = self.positions()

    def positions(self):
        positions_list = []
        for i in range(self.rect_numbers):
            x = self.x - self.width * i
            y = self.y
            position = (x,y)
            positions_list.append(position)
        return positions_list


    def move_up(self):
        new_positions_list = []
        head_position = (self.positions_list[0][0], self.positions_list[0][1] - 30)
        for i in range(self.rect_numbers):
            if i == 0:
                new_positions_list.append(head_position)
            else:
                new_positions_list.append(self.positions_list[i-1])

        self.positions_list = new_positions_list

    def move_down(self):
        new_positions_list = []
        head_position = (self.positions_list[0][0], self.positions_list[0][1] + 30)
        for i in range(self.rect_numbers):
            if i == 0:
                new_positions_list.append(head_position)
            else:
                new_positions_list.append(self.positions_list[i-1])

        self.positions_list = new_positions_list

    def move_right(self):
        new_positions_list = []
        head_position = (self.positions_list[0][0] + 30, self.positions_list[0][1])
        for i in range(self.rect_numbers):
            if i == 0:
                new_positions_list.append(head_position)
            else:
                new_positions_list.append(self.positions_list[i-1])

        self.positions_list = new_positions_list

    def move_left(self):
        new_positions_list = []
        head_position = (self.positions_list[0][0] - 30, self.positions_list[0][1])
        for i in range(self.rect_numbers):
            if i == 0:
                new_positions_list.append(head_position)
            else:
                new_positions_list.append(self.positions_list[i-1])

        self.positions_list = new_positions_list

    def draw(self):
        for i in range(self.rect_numbers):
            x = self.positions_list[i][0]
            y = self.positions_list[i][1]
            pygame.draw.rect(win, self.color, (x, y, self.width, self.height))

snake = Snake()

class Food():
    def __init__(self):
        self.color = (0, 150, 250)
        self.width = 30
        self.height = 30
        # self.position = (750 + 120, 390)
        self.position = (390 + 60, 180)

    def change_position(self):
        x = random.randrange(0, win_width, 30)
        y = random.randrange(0, win_height, 30)
        position = (x,y)
        while position in snake.positions_list:
            x = random.randrange(0, win_width, 30)
            y = random.randrange(0, win_height, 30)
            position = (x,y)
        self.position = position

    def eating(self):
        if snake.positions_list[0] == self.position:
            snake.rect_numbers += 1
            return True


    def draw(self):
        if not self.eating():
            pygame.draw.rect(win, self.color, (self.position[0], self.position[1], self.width, self.height))
        else:
            self.change_position()
            pygame.draw.rect(win, self.color, (self.position[0], self.position[1], self.width, self.height))

food = Food()

def game_finished():

        snake_head = snake.positions_list[0]
        # for i in range(1, len(snake.positions_list)):
        #     if snake_head == snake.positions_list[i]:
        #         quit()

        if snake_head[0] >= win_width or snake_head[0] < 0:
            return True
        elif snake_head[1] < 0 or snake_head[1] >= win_height:
            return True
        else:
            return False

def main():
    final_score_font = pygame.font.SysFont("comicsansms", 30, True)
    score_font = pygame.font.SysFont("comicsansms", 30, True)
    game_over_font = pygame.font.SysFont("comicsansms", 50, True)
    count = 0
    run = True

    def redraw_game_window():
        win.fill((0,0,0))
        text = score_font.render("Score: " + str(snake.rect_numbers - 3), 1, (250, 250, 250))
        win.blit(text, (win_width - 150, 10))
        snake.draw()
        food.draw()

        pygame.display.update()

    def draw_gameover_window():
        win.fill((0,0,0))
        text = game_over_font.render("Game Over", 1, (250, 250, 250))
        final_score = final_score_font.render("Score: " + str(snake.rect_numbers - 3), 1, (250, 250, 250))
        win.blit(text, (int(win_width / 2 - 120), int(win_height / 2 - 50)))
        win.blit(final_score, (int(win_width / 2 - 50), int(win_height / 2 + 20)))
        pygame.display.update()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
                if event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                if event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"


        if snake.direction == "RIGHT":
            snake.move_right()
        if snake.direction == "LEFT":
            snake.move_left()
        if snake.direction == "UP":
            snake.move_up()
        if snake.direction == "DOWN":
            snake.move_down()

        pygame.time.delay(initial_delay - int(1.5 * snake.rect_numbers))

        snake_head = snake.positions_list[0]



        if game_finished():
            draw_gameover_window()
        else:
            redraw_game_window()
        for i in range(1, len(snake.positions_list)):
            if snake_head == snake.positions_list[i]:
                count += 1
        if count >= 1:
            draw_gameover_window()

main()
