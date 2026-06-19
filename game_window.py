import pygame
from ui.textbox import TextBox
from chapters.chapter1_data import LESSON_PAGES
from chapters.chapter1_quiz import QUIZ_QUESTIONS
from chapters.chapter2_data import LESSON_PAGES as CHAPTER2_PAGES
from chapters.chapter2_quiz import QUIZ_QUESTIONS as CHAPTER2_QUIZ

pygame.init()

# ======================
# WINDOW
# ======================

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Quest")

# ======================
# FONTS
# ======================

title_font = pygame.font.Font(None, 70)
text_font = pygame.font.Font(None, 40)

# ======================
# BUTTONS
# ======================

start_button = pygame.Rect(300, 250, 200, 60)

next_button = pygame.Rect(320, 500, 160, 50)

submit_button = pygame.Rect(320, 450, 160, 50)

continue_button = pygame.Rect(
    300,
    450,
    200,
    60
)


# ======================
# TEXTBOX
# ======================

textbox = TextBox(
    200,
    330,
    400,
    50
)

# ======================
# GAME STATE
# ======================

running = True

current_screen = "menu"

lesson_index = 0
quiz_index = 0

player_xp = 0

# ======================
# MAIN LOOP
# ======================

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        textbox.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:

            # ==================
            # MENU
            # ==================

            if current_screen == "menu":

                if start_button.collidepoint(event.pos):

                    lesson_index = 0
                    quiz_index = 0
                    player_xp = 0
                    textbox.text = ""

                    current_screen = "lesson"

            # ==================
            # LESSONS
            # ==================

            elif current_screen == "lesson":

                if next_button.collidepoint(event.pos):

                    lesson_index += 1

                    if lesson_index >= len(LESSON_PAGES):

                        quiz_index = 0
                        textbox.text = ""

                        current_screen = "quiz"

            # ==================
            # QUIZ
            # ==================

            elif current_screen == "quiz":

                if submit_button.collidepoint(event.pos):

                    answer = textbox.text.strip()

                    current_question = QUIZ_QUESTIONS[quiz_index]

                    if answer == current_question["answer"]:

                        player_xp += 100

                        quiz_index += 1

                        textbox.text = ""

                        if quiz_index >= len(QUIZ_QUESTIONS):

                            current_screen = "success"
                            
            elif current_screen == "success":

                if continue_button.collidepoint(event.pos):

                    current_screen = "chapter2"
    # ======================
    # DRAW
    # ======================

    screen.fill((30, 30, 30))

    # ======================
    # MENU
    # ======================

    if current_screen == "menu":

        title = title_font.render(
            "Python Quest",
            True,
            (255, 255, 255)
        )

        screen.blit(title, (180, 120))

        pygame.draw.rect(
            screen,
            (0, 150, 255),
            start_button
        )

        start_text = text_font.render(
            "Start Game",
            True,
            (255, 255, 255)
        )

        screen.blit(
            start_text,
            (325, 268)
        )

    # ======================
    # LESSON SCREEN
    # ======================

    elif current_screen == "lesson":

        page = LESSON_PAGES[lesson_index]

        title = title_font.render(
            page["title"],
            True,
            (255, 255, 255)
        )

        screen.blit(
            title,
            (100, 100)
        )

        lesson = text_font.render(
            page["text"],
            True,
            (255, 255, 255)
        )

        screen.blit(
            lesson,
            (60, 260)
        )

        pygame.draw.rect(
            screen,
            (0, 150, 255),
            next_button
        )

        next_text = text_font.render(
            "Next",
            True,
            (255, 255, 255)
        )

        screen.blit(
            next_text,
            (360, 512)
        )

    # ======================
    # QUIZ SCREEN
    # ======================

    elif current_screen == "quiz":

        current_question = QUIZ_QUESTIONS[quiz_index]

        title = title_font.render(
            "Quiz",
            True,
            (255, 255, 255)
        )

        screen.blit(
            title,
            (280, 100)
        )

        question = text_font.render(
            current_question["question"],
            True,
            (255, 255, 255)
        )

        screen.blit(
            question,
            (120, 220)
        )

        textbox.draw(screen)

        pygame.draw.rect(
            screen,
            (0, 150, 255),
            submit_button
        )

        submit_text = text_font.render(
            "Submit",
            True,
            (255, 255, 255)
        )

        screen.blit(
            submit_text,
            (340, 462)
        )

        xp_text = text_font.render(
            f"XP: {player_xp}",
            True,
            (255, 255, 255)
        )

        screen.blit(
            xp_text,
            (650, 30)
        )

    # ======================
    # SUCCESS SCREEN
    # ======================

    elif current_screen == "success":

        success = title_font.render(
            "Chapter Complete!",
            True,
            (0, 255, 0)
        )

        screen.blit(
            success,
            (120, 150)
        )

        xp = text_font.render(
            f"Total XP: {player_xp}",
            True,
            (255, 255, 255)
        )

        screen.blit(
            xp,
            (280, 280)
        )

        chapter = text_font.render(
            "Variables Mastered!",
            True,
            (255, 255, 255)
        )

        screen.blit(
            chapter,
            (220, 350)
        )
        pygame.draw.rect(
            screen,
            (0, 150, 255),
            continue_button
        )

        continue_text = text_font.render(
            "Chapter 2",
            True,
            (255, 255, 255)
        )

        screen.blit(
            continue_text,
            (330, 465)
        )

    pygame.display.update()

pygame.quit()