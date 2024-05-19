import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Korean Text Input")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# 폰트 설정 (한글 지원 폰트 사용)
font = pygame.font.Font(None, 36)

# 한글 조합 로직
CHOSUNG_LIST = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
JUNGSUNG_LIST = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
JONGSUNG_LIST = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

def is_hangul(char):
    return char in CHOSUNG_LIST or char in JUNGSUNG_LIST or char in ''.join(JONGSUNG_LIST)

def combine_hangul(chosung, jungsung, jongsung):
    if chosung is None or jungsung is None:
        return ''
    chosung_index = CHOSUNG_LIST.index(chosung)
    jungsung_index = JUNGSUNG_LIST.index(jungsung)
    jongsung_index = JONGSUNG_LIST.index(jongsung) if jongsung else 0
    return chr(0xAC00 + (chosung_index * 21 + jungsung_index) * 28 + jongsung_index)

class TextInputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        self.txt_surface = font.render(text, True, BLACK)
        self.active = False

        self.chosung = None
        self.jungsung = None
        self.jongsung = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = BLACK if self.active else GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    if self.jongsung:
                        self.jongsung = None
                    elif self.jungsung:
                        self.jungsung = None
                    elif self.chosung:
                        self.chosung = None
                    else:
                        self.text = self.text[:-1]
                else:
                    char = event.unicode
                    if char in CHOSUNG_LIST:
                        if self.chosung is None:
                            self.chosung = char
                        else:
                            self.text += combine_hangul(self.chosung, self.jungsung, self.jongsung)
                            self.chosung = char
                            self.jungsung = None
                            self.jongsung = None
                    elif char in JUNGSUNG_LIST:
                        if self.chosung is not None:
                            self.jungsung = char
                        else:
                            self.text += char
                    elif char in ''.join(JONGSUNG_LIST):
                        if self.chosung is not None and self.jungsung is not None:
                            self.jongsung = char
                    else:
                        self.text += char
                self.txt_surface = font.render(self.text + combine_hangul(self.chosung, self.jungsung, self.jongsung), True, BLACK)
        return None

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def main():
    clock = pygame.time.Clock()
    input_box = TextInputBox(100, 100, 600, 50)
    input_boxes = [input_box]
    words_and_meanings = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in input_boxes:
                result = box.handle_event(event)
                if result is not None:
                    words_and_meanings.append(result)
                    box.text = ''
                    box.chosung = None
                    box.jungsung = None
                    box.jongsung = None
                    box.txt_surface = font.render(box.text, True, BLACK)

        screen.fill(WHITE)
        for box in input_boxes:
            box.draw(screen)

        y_offset = 200
        for text in words_and_meanings:
            word_surface = font.render(text, True, BLACK)
            screen.blit(word_surface, (100, y_offset))
            y_offset += 40

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
