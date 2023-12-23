import pygame
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")

# Police de texte
font = pygame.font.Font(None, 36)

# Variables du jeu
clock = pygame.time.Clock()
running = True
score = 0
words = ['hello', 'world', 'python', 'game', 'keyboard', 'difficult', 'challenge', 'programming']  # Liste de mots à taper
current_word = random.choice(words)
input_text = ''
input_font = font.render(input_text, True, BLACK)
word_x, word_y = 300, 200
input_x, input_y = 300, 400
word_speed = 2
game_over = False

# Temps de frappe par mot
time_limit = 10  # Limite de temps en secondes
start_time = pygame.time.get_ticks()  # Temps de départ du mot courant

# Boucle principale du jeu
while running:
    screen.fill(WHITE)
    
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                current_time = pygame.time.get_ticks()
                elapsed_time = (current_time - start_time) / 1000  # Temps écoulé en secondes
                
                if input_text == current_word and len(input_text) == len(current_word) and elapsed_time < time_limit:
                    score += 1
                    current_word = random.choice(words)
                    input_text = ''
                    start_time = pygame.time.get_ticks()  # Réinitialiser le temps de départ pour le nouveau mot
                else:
                    game_over = True
            else:
                input_text += event.unicode
    
    # Affichage du mot à taper
    word_font = font.render(current_word, True, BLACK)
    screen.blit(word_font, (word_x, word_y))
    
    # Affichage du texte saisi par le joueur
    input_font = font.render(input_text, True, BLACK)
    screen.blit(input_font, (input_x, input_y))
    
    # Vérification de la victoire ou de la défaite
    if game_over:
        text = font.render("Game Over! Score: {}".format(score), True, BLACK)
        screen.blit(text, (300, 300))
        pygame.display.update()
        pygame.time.wait(2000)
        game_over = False
        score = 0
        current_word = random.choice(words)
        input_text = ''
    
    # Mise à jour de l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
