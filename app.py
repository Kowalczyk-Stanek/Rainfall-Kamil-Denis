import pygame
import random

# Inicjalizacja modułu pygame
pygame.init()

# Ustawienia ekranu
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animacja Kropli Deszczu")

# Kolory
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Definicja klasy kropli deszczu
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)  # losowa pozycja x
        self.y = random.randint(-SCREEN_HEIGHT, 0)  # losowa pozycja y (poza ekranem)
        self.speed = random.randint(5, 15)  # losowa prędkość spadania

    def fall(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-SCREEN_HEIGHT, 0)  # resetuj kroplę na górze ekranu
            self.x = random.randint(0, SCREEN_WIDTH)  # losowa pozycja x

    def draw(self, screen):
        pygame.draw.line(screen, BLUE, (self.x, self.y), (self.x, self.y + 5), 1)

# Definicja klasy wody na dole ekranu
class WaterSplash:
    def __init__(self):
        self.drops = []

    def add_drop(self, x, y):
        # Dodaj krople wody w okolicy punktu (x, y)
        for _ in range(20):
            drop_x = random.randint(x - 10, x + 10)
            drop_y = random.randint(y - 10, y + 10)
            self.drops.append((drop_x, drop_y))

    def draw(self, screen):
        for drop in self.drops:
            pygame.draw.circle(screen, BLUE, drop, 2)

        # Utrzymuj rozmiar listy kropli w granicach umożliwiających efekt
        self.drops = [drop for drop in self.drops if drop[1] < SCREEN_HEIGHT]

# Lista kropli deszczu
raindrops = [Raindrop() for _ in range(100)]

# Obiekt wody na dole ekranu
water_splash = WaterSplash()

# Główna pętla gry
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # wypełnij ekran biały

    for raindrop in raindrops:
        raindrop.fall()
        raindrop.draw(screen)

        # Sprawdź czy kropla dotyka dolnej części ekranu
        if raindrop.y > SCREEN_HEIGHT - 20:
            water_splash.add_drop(raindrop.x, SCREEN_HEIGHT)  # dodaj kroplę do wody na dole ekranu

    water_splash.draw(screen)  # rysuj efekt wody na dole ekranu

    pygame.display.flip()  # odśwież ekran

    clock.tick(30)  # ogranicz do 30 klatek na sekundę

pygame.quit()  # zakończ pygame
