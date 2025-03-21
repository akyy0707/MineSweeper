import pygame
import sys
import textwrap
from button import Button

pygame.init()
pygame.mixer.init() 

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

pygame.mixer.music.load("Menu/assets/nhac_nen.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

BG = pygame.image.load("Menu/assets/Background.png")
BG = pygame.transform.scale(BG, (1280, 720))

def get_font(size):
    return pygame.font.Font("Menu/assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("gray")

        EASY_BUTTON = Button(image=pygame.image.load("Menu/assets/Play Rect.png"), pos=(640, 100), 
                            text_input="EASY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MEDIUM_BUTTON = Button(image=pygame.image.load("Menu/assets/Options Rect.png"), pos=(640, 250), 
                            text_input="MEDIUM", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON = Button(image=pygame.image.load("Menu/assets/Quit Rect.png"), pos=(640, 400), 
                            text_input="HARD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("Menu/assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    return 

        pygame.display.update()

def draw_volume_slider(volume):
    SLIDER_X = 340 
    SLIDER_WIDTH = 600 
    
    pygame.draw.rect(SCREEN, (100, 100, 100), (SLIDER_X, 350, SLIDER_WIDTH, 10))  
    pygame.draw.circle(SCREEN, (255, 0, 0), (SLIDER_X + int(volume * SLIDER_WIDTH), 355), 15)

    volume_text = get_font(50).render(f"Volume: {int(volume * 100)}%", True, "black")
    SCREEN.blit(volume_text, (370, 250))


import textwrap

def show_tutorial_box():
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Minesweeper Tutorial")

    running = True
    font = pygame.font.SysFont("comicsansms", 20, bold=True)

    tutorial_rect = pygame.Rect(100, 80, 1080, 500)
    TUTORIAL_TEXT = font.render("INSTRUCTION", True, "black")
    TUTORIAL_RECT = TUTORIAL_TEXT.get_rect(center=(640, 50))

    BACK_BUTTON = Button(image=pygame.image.load("Menu/assets/Quit Rect.png"), pos=(640, 650),
                         text_input="BACK", font=pygame.font.Font(None, 50), base_color="black", hovering_color="White")

    GUIDE_TEXT = [
        "Minesweeper Game Guide",
        "Game Objective",
        "Your goal is to uncover all the safe tiles without triggering any mines!",

        "Basic Rules",
        "1. At the start, you will see a grid of squares (size depends on the game mode).",
        "2. Left-click on a tile to reveal it:",
        "   - If it's a number: It shows how many mines are adjacent to it.",
        "   - If it's an empty tile: It will expand and reveal surrounding empty tiles.",
        "   - If it's a mine: You lose!",
        "3. Right-click to place a flag on a tile you suspect has a mine.",
        "4. You win when all non-mine tiles are revealed!",

        "Meaning of Numbers",
        "When you uncover a tile, if you see a number from 1 to 8, it represents the number of mines in the surrounding 8 tiles.",
        "Example: If a tile has a '2', there are two mines nearby.",

        "Pro Tips",
        "Start from the center or a corner to reveal more tiles quickly.",
        "If you see numbers like 1, 2, 3...  Use logic to locate mines.",
        "Place flags on suspected mine tiles before clicking others.",
        "If you're sure a tile is safe, open it to save time.",
        "When only mines remain unopened, you've won!",

        "Have fun and conquer Minesweeper!"
    ]

    scroll_y = 0  
    max_scroll = max(0, len(GUIDE_TEXT) * 30 - 450)

    while running:
        SCREEN.fill("gray")
        pygame.draw.rect(SCREEN, (200, 200, 200), tutorial_rect, border_radius=10)
        SCREEN.blit(TUTORIAL_TEXT, TUTORIAL_RECT)

        y_offset = 100 - scroll_y  
        line_spacing = 30  

        for line in GUIDE_TEXT:
            wrapped_lines = textwrap.wrap(line, width=80)
            for wrapped_line in wrapped_lines:
                if 100 <= y_offset <= 550:
                    text_surface = font.render(wrapped_line, True, "black")
                    SCREEN.blit(text_surface, (120, y_offset))
                y_offset += line_spacing

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    return  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scroll_y = max(0, scroll_y - 30)
                elif event.key == pygame.K_DOWN:
                    scroll_y = min(max_scroll, scroll_y + 30)
            elif event.type == pygame.MOUSEWHEEL:
                scroll_y = max(0, min(max_scroll, scroll_y - event.y * 30)) 
  


def options():
    volume = pygame.mixer.music.get_volume()  
    dragging = False  

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("gray")

        OPTIONS_TEXT = get_font(75).render("OPTIONS", True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        draw_volume_slider(volume)  

        GUIDE_BUTTON = Button(image=pygame.image.load("Menu/assets/Options Rect.png"), pos=(640, 450),
                              text_input="INSTRUCTION", font=get_font(50), base_color="black", hovering_color="White")

        BACK_BUTTON = Button(image=pygame.image.load("Menu/assets/Quit Rect.png"), pos=(640, 600),
                             text_input="BACK", font=get_font(75), base_color="black", hovering_color="White")

        GUIDE_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        GUIDE_BUTTON.update(SCREEN)
        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    show_tutorial_box()
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    return  
                if 300 <= OPTIONS_MOUSE_POS[0] <= 900 and 340 <= OPTIONS_MOUSE_POS[1] <= 370:  
                    dragging = True  
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False  
            if event.type == pygame.MOUSEMOTION and dragging:
                volume = (OPTIONS_MOUSE_POS[0] - 400) / 400  
                volume = max(0, min(1, volume))  
                pygame.mixer.music.set_volume(volume)  

        pygame.display.update()
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "red")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Menu/assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Menu/assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Menu/assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()