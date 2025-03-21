import pygame
import sys
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
    pygame.draw.rect(SCREEN, (100, 100, 100), (400, 350, 400, 10))
    pygame.draw.circle(SCREEN, (255, 0, 0), (400 + int(volume * 400), 355), 15)
    volume_text = get_font(40).render(f"Volume: {int(volume * 100)}%", True, "black")
    SCREEN.blit(volume_text, (400, 300))

def options():
    volume = pygame.mixer.music.get_volume() 
    dragging = False 

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("gray")

        OPTIONS_TEXT = get_font(75).render("OPTIONS", True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("Menu/assets/Quit Rect.png"), pos=(640, 550), 
                             text_input="BACK", font=get_font(75), base_color="black", hovering_color="White")
        
        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        draw_volume_slider(volume)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    return  
                if 400 <= OPTIONS_MOUSE_POS[0] <= 800 and 340 <= OPTIONS_MOUSE_POS[1] <= 360:
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
