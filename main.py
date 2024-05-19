class Button(): #버튼 클래스
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def click_check(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #마우스 클릭
            if self.rect.collidepoint(event.pos): #마우스 위치
                return True

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Textnput_Box:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        font = pygame.font.SysFont("hancommalangmalang", 30, False, False)
        self.txt_surface = font.render(text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #클릭확인
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            
            if self.active: self.color = BLACK #활성화 따른 색 변화
            else: self.color = GRAY

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN: #엔터
                    self.active = False
                    return self.text
                elif event.key == pygame.K_BACKSPACE: #백스페이스
                    self.text = self.text[:-1]

                else: #나머지 키는 input
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, BLACK)

    def draw(self):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def add_word():
    global run
    add_running = True

    font = pygame.font.SysFont("hancommalangmalang", 50, False, False)
    title = font.render("원하는 단어를 추가하세요.", True, BLACK)
    word_input_box = Textnput_Box(200, 200, 1000, 60, "단어를 입력하세요")
    meaning_input_box = Textnput_Box(200, 300, 1000, 60, "뜻를 입력하세요")

    while add_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #종료코드
                add_running = False
                run = False 
            if exit_button.click_check(event): #뒤로가기
                add_running = False

            word_input_box.handle_event(event)
            meaning_input_box.handle_event(event)

        screen.fill(WHITE)
        exit_button.draw()
        word_input_box.draw()
        meaning_input_box.draw()
        screen.blit(title, (430, 70))
        pygame.display.update()

def memorize_word():
    global run
    add_running = True

    font = pygame.font.SysFont("hancommalangmalang", 50, False, False)
    title = font.render("단어 암기", True, BLACK)
    while add_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #종료코드
                add_running = False
                run = False
            if exit_button.click_check(event): #뒤로가기
                add_running = False

        screen.fill(WHITE)
        exit_button.draw()
        screen.blit(title, (430, 70))
        pygame.display.update()

def memorize_meaning():
    global run
    add_running = True

    font = pygame.font.SysFont("hancommalangmalang", 50, False, False)
    title = font.render("뜻 암기", True, BLACK)
    while add_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #종료코드
                add_running = False
                run = False 
            if exit_button.click_check(event): #뒤로가기
                add_running = False

        screen.fill(WHITE)
        exit_button.draw()
        screen.blit(title, (430, 70))
        pygame.display.update()


import pygame
from hangulinputBox import *


pygame.init() #초기화

screen_width = 1366
screen_height = 705
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기 설정
pygame.display.set_caption("Hello, World!") #창 이름

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (115,115,115)

exit_button = Button(10, 10, "club_project/images/go_back.PNG")
add_button = Button(140, 225, "club_project/images/add_word.png")
memorize_word_button = Button(510, 225, "club_project/images/memorize_word.png")
memorize_meaning_button = Button(880, 225, "club_project/images/memorize_meaning.png")

font = pygame.font.SysFont("hancommalangmalang", 50, False, False)
choose_function_tx = font.render("원하는 기능을 선택하세요", True, BLACK)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if add_button.click_check(event) == True: #단어추가 클릭
            add_word()
        if memorize_word_button.click_check(event) == True: #단어암기 클릭
            memorize_word()
        if memorize_meaning_button.click_check(event) == True: #뜻암기 클릭
            memorize_meaning()

    screen.fill(WHITE)
    screen.blit(choose_function_tx, (430, 70))
    add_button.draw()
    memorize_word_button.draw()
    memorize_meaning_button.draw()
    pygame.display.update()

pygame.quit()