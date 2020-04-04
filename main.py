import pygame
import random
from pygame import mixer

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
lightRed = (200, 0, 0)
green = (0, 255, 0)
lightGreen = (50, 205, 50)
blue = (0, 0, 255)
lightBlue = (0, 191, 200)
purple = (128, 0, 128)
orchid = (186, 85, 211)
yellow = (255, 255, 0)
gold = (255, 215, 0)
turquoise = (0, 168, 243)

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Guess It Now")

background_img = pygame.image.load('main.jpg')
background_img = pygame.transform.scale(background_img, (600, 600))
mixer.music.load('demo.wav')
mixer.music.play(-1)
game_img = pygame.image.load("background1.jpg")
game_img = pygame.transform.scale(game_img, (600, 600))
setting_img = pygame.image.load("settings.jpg")

small_font = pygame.font.SysFont("Calibri", 18)
button_font = pygame.font.SysFont("Calibri", 24)
medium_font = pygame.font.SysFont("Calibri", 50)
large_font = pygame.font.SysFont("Calibri", 60, bold=True)

difficulty = "E"
turns = 10


def text_objects(msg, color, size="small"):
    text_surface = button_font.render(msg, True, color)
    if size == "medium":
        text_surface = medium_font.render(msg, True, color)
    elif size == "large":
        text_surface = large_font.render(msg, True, color)

    return text_surface, text_surface.get_rect()


def msg_screen(msg, color, size, y_movement=0, x_movement=0):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = 300 + x_movement, 300 + y_movement
    window.blit(text_surf, text_rect)


# Function which prints text on button
def text_button(msg, color, b_x, b_y, b_length, b_height):
    text_surf, text_rect = text_objects(msg, color)
    text_rect.center = (b_x + b_length / 2), (b_y + b_height / 2)
    window.blit(text_surf, text_rect)


def disp_turn(val):
    text = button_font.render("Remaining Turns: " + str(val), True, black)
    window.blit(text, (80, 410))


def disp_win_msg(given_word):
    window.fill(turquoise)
    mixer.music.load('win.wav')
    mixer.music.play()
    msg_screen("You have won ", black, "medium", -50)
    msg_screen("The Word is: " + given_word, black, "medium", 80)


def disp_lost_msg(given_word):
    window.fill(turquoise)
    mixer.music.load('loose.wav')
    mixer.music.play()
    msg_screen("You have Lost ", black, "medium", -50)
    msg_screen("Correct Word was: " + given_word, black, "medium", 80)


# ****************************MAIN GAME LOGIC*****************************


def gameplay_logic():
    words = ['rainbow', 'computer', 'science', 'python', 'mathematics', 'player', 'condition', 'programming',
             'reverse', 'water', 'board', 'geeks']
    word = random.choice(words)

    global difficulty
    global turns

    if difficulty == "E":
        turns = 10
    elif difficulty == "M":
        turns = 7
    elif difficulty == "X":
        turns = 5

    temp = turns

    guesses = ''
    while temp > 0:
        guess = ""
        window.blit(game_img, (0, 0))
        str1 = ""
        failed = 0
        for char in word:
            if char in guesses:
                str1 += char
            else:
                str1 += " _ "
                failed += 1
        print("Current String: ", str1)

        disp_turn(temp)
        if failed == 0:
            disp_win_msg(word)
            break

        text = button_font.render("Your Word ", True, black)
        window.blit(text, (80, 290))

        text = button_font.render(str1, True, black)
        window.blit(text, (80, 340))

        text = medium_font.render("Guess", True, black)
        window.blit(text, (60, 30))

        text = medium_font.render("a", True, black)
        window.blit(text, (100, 75))

        text = medium_font.render("character!! ", True, black)
        window.blit(text, (30, 120))
        # pygame.display.update()

        for event in pygame.event.get():  # Getting the input from user
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    guess = "a"
                elif event.key == pygame.K_b:
                    guess = "b"
                elif event.key == pygame.K_c:
                    guess = "c"
                elif event.key == pygame.K_d:
                    guess = "d"
                elif event.key == pygame.K_e:
                    guess = "e"
                elif event.key == pygame.K_f:
                    guess = "f"
                elif event.key == pygame.K_g:
                    guess = "g"
                elif event.key == pygame.K_h:
                    guess = "h"
                elif event.key == pygame.K_i:
                    guess = "i"
                elif event.key == pygame.K_j:
                    guess = "j"
                elif event.key == pygame.K_k:
                    guess = "k"
                elif event.key == pygame.K_l:
                    guess = "l"
                elif event.key == pygame.K_m:
                    guess = "m"
                elif event.key == pygame.K_n:
                    guess = "n"
                elif event.key == pygame.K_o:
                    guess = "o"
                elif event.key == pygame.K_p:
                    guess = "p"
                elif event.key == pygame.K_q:
                    guess = "q"
                elif event.key == pygame.K_r:
                    guess = "r"
                elif event.key == pygame.K_s:
                    guess = "s"
                elif event.key == pygame.K_t:
                    guess = "t"
                elif event.key == pygame.K_u:
                    guess = "u"
                elif event.key == pygame.K_v:
                    guess = "v"
                elif event.key == pygame.K_w:
                    guess = "w"
                elif event.key == pygame.K_x:
                    guess = "x"
                elif event.key == pygame.K_y:
                    guess = "y"
                elif event.key == pygame.K_z:
                    guess = "z"

                mixer.music.load('success.wav')
                mixer.music.play()

        guesses += guess
        print("Before: ", temp)
        if guess not in word:
            temp -= 1
            disp_turn(temp)

        print("After: ", temp)
        if temp == 0:
            disp_lost_msg(word)
            break

        button("Home", lightRed, red, 210, 490, 120, 50, "Back")
        pygame.display.update()

    run_status = True
    while run_status:
        for value in pygame.event.get():
            if value.type == pygame.QUIT:
                run_status = False
        button("Home", lightRed, red, 100, 490, 120, 50, "Back")
        button("Quit", lightRed, red, 380, 490, 120, 50, "Quit")
        pygame.display.update()


def game_instructions():  # Add Instructions here
    window.fill(white)
    run_status = True
    while run_status:
        for value in pygame.event.get():
            if value.type == pygame.QUIT:
                run_status = False
        msg_screen("INSTRUCTIONS", black, "large", -250)
        msg_screen("1. Enter a letter to check it's presence in the word.", black, "small", 5)
        msg_screen("2. Fill the letter in the blanks if the players guess correctly. ", black, "small", 30)
        msg_screen("3. Reduce the number of turns when the players guess wrong. ", black, "small", 55)
        msg_screen("4. The players win when they guess the correct word. ", black, "small", 80)

        button("Home", lightRed, red, 230, 490, 120, 50, "Back")
        pygame.display.update()


def game_setting():
    window.blit(setting_img, (0, 0))
    run_status = True
    while run_status:
        for value in pygame.event.get():
            if value.type == pygame.QUIT:
                run_status = False
        msg_screen("Game Settings", black, "large", -250, 110)
        msg_screen("Difficulty : ", black, "medium", -80, -35)
        button("Easy", gold, yellow, 430, 200, 120, 50, "Easy")
        button("Medium", gold, yellow, 430, 280, 120, 50, "Med")
        button("Expert", gold, yellow, 430, 360, 120, 50, "Exp")
        button("Home", lightRed, red, 230, 490, 120, 50, "Back")
        pygame.display.update()


def button(msg, b_color, b_color_active, b_x, b_y, b_length, b_height, action="None", color_text=white):
    cursor_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    global difficulty
    if cursor_pos[0] in range(b_x, b_x + b_length) and cursor_pos[1] in range(b_y, b_y + b_height):
        pygame.draw.rect(window, b_color_active, (b_x, b_y, b_length, b_height))
        if mouse_click[0] == 1 and action != "None":
            if action == "Back":
                main()
            elif action == "Easy":
                difficulty = "E"
                pygame.draw.rect(window, black, (b_x, b_y, b_length, b_height), 6)
                pygame.draw.rect(window, turquoise, (430, 280, 120, 50), 6)  # Med Rect
                pygame.draw.rect(window, turquoise, (430, 360, 120, 50), 6)  # Exp Rect
                pygame.display.update()
            elif action == "Med":
                difficulty = "M"
                pygame.draw.rect(window, black, (b_x, b_y, b_length, b_height), 6)
                pygame.draw.rect(window, turquoise, (430, 200, 120, 50), 6)  # Easy Rect
                pygame.draw.rect(window, turquoise, (430, 360, 120, 50), 6)  # Exp Rect
                pygame.display.update()
            elif action == "Exp":
                difficulty = "X"
                pygame.draw.rect(window, black, (b_x, b_y, b_length, b_height), 6)
                pygame.draw.rect(window, turquoise, (430, 200, 120, 50), 6)  # Easy Rect
                pygame.draw.rect(window, turquoise, (430, 280, 120, 50), 6)  # Med Rect
                pygame.display.update()
            elif action == "Quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(window, b_color, (b_x, b_y, b_length, b_height))
    text_button(msg, color_text, b_x, b_y, b_length, b_height)


# ''' *******************************MAIN FUNCTION**************************** '''


def main():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = pygame.mouse.get_pos()
                if cursor_pos[0] in range(100, 220) and cursor_pos[1] in range(310, 360):
                    gameplay_logic()
                elif cursor_pos[0] in range(100, 220) and cursor_pos[1] in range(370, 420):
                    game_instructions()
                elif cursor_pos[0] in range(100, 220) and cursor_pos[1] in range(430, 480):
                    game_setting()

        window.blit(background_img, (0, 0))
        button("Play Game", lightGreen, green, 100, 310, 120, 50, "Play")
        button("Instructions", blue, lightBlue, 100, 370, 120, 50, "Instruct")
        button("Settings", purple, orchid, 100, 430, 120, 50, "Settings")
        button("Quit", lightRed, red, 100, 490, 120, 50, "Quit")
        pygame.display.update()

    pygame.quit()
    quit()


main()
