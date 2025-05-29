# reaction_game.py
import pygame
import random
import time

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🧠 Reaction Time Tester")

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Game variables
waiting = True
reaction_start = 0
reaction_time = 0
best_time = None
bg_color = (30, 30, 30)

# Game loop
running = True
state = "waiting"
delay = random.uniform(2, 5)  # Random wait time
start_time = time.time()

while running:
    screen.fill(bg_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if state == "ready" and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reaction_time = round((time.time() - reaction_start) * 1000)
            if best_time is None or reaction_time < best_time:
                best_time = reaction_time
            state = "show_result"
            bg_color = (30, 30, 30)

    # Timing logic
    if state == "waiting" and (time.time() - start_time) > delay:
        state = "ready"
        bg_color = (0, 255, 0)  # Flash green
        reaction_start = time.time()

    # Display messages
    if state == "waiting":
        msg = font.render("Wait for the screen to turn GREEN...", True, (255, 255, 255))
    elif state == "ready":
        msg = font.render("PRESS SPACE NOW!", True, (0, 0, 0))
    elif state == "show_result":
        msg = font.render(f"Reaction Time: {reaction_time} ms", True, (255, 255, 255))
        info = small_font.render("Press R to try again or ESC to quit", True, (200, 200, 200))
        screen.blit(info, (WIDTH // 2 - info.get_width() // 2, HEIGHT // 2 + 50))

    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

    if best_time:
        best = small_font.render(f"Best Time: {best_time} ms", True, (255, 255, 0))
        screen.blit(best, (10, 10))

    pygame.display.flip()
    clock.tick(60)

    # Handle keypress to restart
    keys = pygame.key.get_pressed()
    if state == "show_result":
        if keys[pygame.K_r]:
            state = "waiting"
            delay = random.uniform(2, 5)
            start_time = time.time()
            reaction_time = 0
            bg_color = (30, 30, 30)
        elif keys[pygame.K_ESCAPE]:
            running = False

pygame.quit()
j
