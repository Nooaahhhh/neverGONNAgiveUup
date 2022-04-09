import pygame
import sys
import time, pyautogui
import webbrowser


class Button:
    def __init__(self, text, width, height, pos):
        # core attributes
        self.pressed = False

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (128, 128, 128)
        # Text
        self.text_surf = gui_font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=8)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (60, 60, 60)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    # start function after clicking

                    chrome = 'C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s'
                    webbrowser.get(chrome).open_new('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

                    self.pressed = False
        else:
            self.top_color = (128, 128, 128)


# main
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('HAHAHAHHAHAHAHAHAHAHHA')
gui_font = pygame.font.Font(None, 30)

button1 = Button('Click me', 150, 40, (175, 390))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Displayed:
    screen.fill((255, 255, 255))
    button1.draw()
    pygame.display.update()


