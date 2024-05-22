class Button(): #버튼 클래스
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def click_check(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #마우스 클릭
            if self.rect.collidepoint(event.pos): #마우스 위치
                return True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
def add_word():
    global run
    add_running = True

    word_input_box = HangulInputBox("hancommalangmalang", 30, 15, BLACK, "단어를 입력하세요", False)
    word_input_box.rect.center = (1366/4, 300)
    meaning_input_box = HangulInputBox("hancommalangmalang", 30, 15, BLACK, "뜻을 입력하세요", True)
    meaning_input_box.rect.center = (1366/4*3, 300)
    add_button = Button(583, 550, "club_project/images/add_button.png")
    added_button = Button(583, 550, "club_project/images/added_button.png")
    font = pygame.font.SysFont("hancommalangmalang", 50, False, False)
    title = font.render("원하는 단어를 추가하세요.", True, BLACK)
    word = font.render("단어", True, BLACK)
    meaning = font.render("뜻", True, BLACK)

    checked_time = 0
    while add_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #종료코드
                add_running = False
                run = False 
            if exit_button.click_check(event): #뒤로가기
                add_running = False
            if add_button.click_check (event): #추가 버튼 클릭
                with open("club_project/words.txt", 'a', encoding='utf-8') as file:  # 'a'는 파일 끝에 내용 추가
                    file.write(f"{word_input_box.update(event)}: {meaning_input_box.update(event)}\n")
                checked_time = time.time()

            word_input_box.update(event)
            meaning_input_box.update(event)

        screen.fill(WHITE)
        exit_button.draw(screen)
        if time.time()-checked_time < 1:
            added_button.draw(screen)
        else:
            add_button.draw(screen)
        word_input_box.draw(screen)
        meaning_input_box.draw(screen)
        screen.blit(title, (427, 70))
        screen.blit(word, (120, 200))
        screen.blit(meaning, (805, 200))
        pygame.display.update()

def read_words(filename):
    words_li = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if ": " in line:
                word, meaning = line.strip().split(": ")
                words_li.append((word, meaning))
    return words_li

def memorize_word():
    global run
    memorize_running = True

    font = pygame.font.SysFont("hancommalangmalang", 50, False, False)
    title = font.render("단어 암기", True, BLACK)
    answer_check_button = Button(363, 550, "club_project/images/answer_check_button.png")
    next_button = Button(363, 550, "club_project/images/next_button.png")
    i_dont_know_button = Button(803, 550, "club_project/images/i_dont_know_button.png")
    answer_input = HangulInputBox("hancommalangmalang", 50, 10, BLACK, "정답을 입력하세요", False)
    answer_input.rect.topleft = (800, 300)
    notice = font.render("", True, BLACK)
    
    words_li = read_words("club_project/words.txt")
    
    i = 0
    is_correct = False
    real_answer = ""
    checked_time = 0
    while memorize_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #종료코드
                memorize_running = False
                run = False
            elif exit_button.click_check(event): #뒤로가기
                memorize_running = False

            elif answer_check_button.click_check(event) and is_correct == False:
                answer = answer_input.update(event)
                if answer == real_answer:
                    is_correct = True
                    notice = font.render("맞았습니다!", True, GREEN)
                    checked_time = time.time()
                else:
                    is_correct = False
                    notice = font.render("틀렸습니다!", True, RED)
                    checked_time = time.time()
            elif next_button.click_check(event) and is_correct:
                i += 1
                is_correct = False
            elif i_dont_know_button.click_check(event):
                i += 1
                is_correct = False #todo 모르는 단어에 대한 처리 추가
            
            answer_input.update(event)

        
        if i >= len(words_li): #todo 결과화면
            memorize_running = False
        else:
            meaning = font.render(f"{words_li[i][1]}", True, BLACK)
            real_answer = words_li[i][0]

        screen.fill(WHITE)
        exit_button.draw(screen)
        if is_correct: 
            next_button.draw(screen)
        else:
            answer_check_button.draw(screen)
        answer_input.draw(screen)
        i_dont_know_button.draw(screen)
        screen.blit(title, (588, 70))
        screen.blit(meaning, (300, 300))
        if time.time() - checked_time < 1:
            screen.blit(notice, (570, 150))

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
        exit_button.draw(screen)
        screen.blit(title, (611, 70))
        pygame.display.update()


from hangulinputBox import *


pygame.init() #초기화

screen_width = 1366
screen_height = 705
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기 설정
pygame.display.set_caption("Hello, World!") #창 이름

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (115,115,115)
RED = (253,138,105)
GREEN = (129,255,184)

exit_button = Button(10, 10, "club_project/images/go_back.PNG")
add_button = Button(140, 225, "club_project/images/add_word.png")
memorize_word_button = Button(510, 225, "club_project/images/memorize_word.png")
memorize_meaning_button = Button(880, 225, "club_project/images/memorize_meaning.png")

font = pygame.font.SysFont("hancommalangmalang", 50, False, False)
title = font.render("원하는 기능을 선택하세요", True, BLACK)

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
    screen.blit(title, (427, 70))
    add_button.draw(screen)
    memorize_word_button.draw(screen)
    memorize_meaning_button.draw(screen)
    pygame.display.update()

pygame.quit()