import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Window dimensions
width = 1280
height = 720

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nether Serpent")

clock = pygame.time.Clock()

# Initialize the pygame.mixer module and load background music
pygame.mixer.init()
background_music = pygame.mixer.Sound("background_music.mp3")

# Load enemy images
enemy_images = [
    pygame.image.load("enemy1.png"),
    pygame.image.load("enemy2.png"),
    pygame.image.load("enemy3.png"),
    pygame.image.load("enemy4.png"),
    pygame.image.load("enemy5.png")
]

# Class representing the snake
class Snake:
    def __init__(self):
        self.size = 2
        self.radius = 20
        self.x = width // 2
        self.y = height // 2
        self.speed = 9
        self.direction = "right"
        self.body = []
        self.color = green

    def draw(self):
        for block in self.body:
            pygame.draw.circle(window, self.color, (block[0], block[1]), self.radius)

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed

        self.body.append([self.x, self.y])

        if len(self.body) > self.size:
            del self.body[0]

    def check_collision(self):
        if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
            return True

        for block in self.body[:-1]:
            if block[0] == self.x and block[1] == self.y:
                return True

        return False

    def eat_food(self, food):
        if abs(self.x - food.x) < self.radius and abs(self.y - food.y) < self.radius:
            self.size += 1
            return True
        return False


# Class representing an enemy
class Enemy:
    def __init__(self, image):
        self.radius = 20
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.speed = 1
        self.image = pygame.transform.scale(image, (self.radius * 2, self.radius * 2))

    def draw(self):
        window.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def move(self, target_x, target_y, enemies):
        if self.x < target_x:
            self.x += self.speed
        elif self.x > target_x:
            self.x -= self.speed

        if self.y < target_y:
            self.y += self.speed
        elif self.y > target_y:
            self.y -= self.speed

        # Check collision with other enemies and repel
        for enemy in enemies:
            if enemy != self:
                distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
                if distance < self.radius + enemy.radius:
                    dx = self.x - enemy.x
                    dy = self.y - enemy.y
                    angle = math.atan2(dy, dx)
                    new_x = enemy.x - math.cos(angle)
                    new_y = enemy.y - math.sin(angle)
                    enemy.x = new_x
                    enemy.y = new_y


# Class representing food
class Food:
    def __init__(self):
        self.radius = 10
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.color = red

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


# Class representing a star
class Star:
    def __init__(self):
        self.radius = 2
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed = random.randint(1, 3)

    def draw(self):
        pygame.draw.circle(window, white, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0


# Class representing a boss
class Boss:
    def __init__(self):
        self.radius = 80
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.speed = 3
        self.image = pygame.image.load("boss.png")
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))

    def draw(self):
        window.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def move(self, target_x, target_y, enemies):
        if self.x < target_x:
            self.x += self.speed
        elif self.x > target_x:
            self.x -= self.speed

        if self.y < target_y:
            self.y += self.speed
        elif self.y > target_y:
            self.y -= self.speed

        # Check collision with other enemies and repel
        for enemy in enemies:
            if enemy != self:
                distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
                if distance < self.radius + enemy.radius:
                    dx = self.x - enemy.x
                    dy = self.y - enemy.y
                    angle = math.atan2(dy, dx)
                    new_x = enemy.x - math.cos(angle)
                    new_y = enemy.y - math.sin(angle)
                    enemy.x = new_x
                    enemy.y = new_y


# Class representing boss 2
class Boss2:
    def __init__(self):
        self.radius = 70
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.speed = 3
        self.image = pygame.image.load("boss2.png")
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))

    def draw(self):
        window.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def move(self, target_x, target_y, enemies):
        if self.x < target_x:
            self.x += self.speed
        elif self.x > target_x:
            self.x -= self.speed

        if self.y < target_y:
            self.y += self.speed
        elif self.y > target_y:
            self.y -= self.speed

        # Check collision with other enemies and repel
        for enemy in enemies:
            if enemy != self:
                distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
                if distance < self.radius + enemy.radius:
                    dx = self.x - enemy.x
                    dy = self.y - enemy.y
                    angle = math.atan2(dy, dx)
                    new_x = enemy.x - math.cos(angle)
                    new_y = enemy.y - math.sin(angle)
                    enemy.x = new_x
                    enemy.y = new_y


# Class representing boss 3
class Boss3:
    def __init__(self):
        self.radius = 70
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.speed = 3
        self.image = pygame.image.load("boss3.png")
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))

    def draw(self):
        window.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def move(self, target_x, target_y, enemies):
        if self.x < target_x:
            self.x += self.speed
        elif self.x > target_x:
            self.x -= self.speed

        if self.y < target_y:
            self.y += self.speed
        elif self.y > target_y:
            self.y -= self.speed

        # Check collision with other enemies and repel
        for enemy in enemies:
            if enemy != self:
                distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
                if distance < self.radius + enemy.radius:
                    dx = self.x - enemy.x
                    dy = self.y - enemy.y
                    angle = math.atan2(dy, dx)
                    new_x = enemy.x - math.cos(angle)
                    new_y = enemy.y - math.sin(angle)
                    enemy.x = new_x
                    enemy.y = new_y


# Function to check collision between the snake and an enemy
def check_collision(snake, enemy):
    distance = ((snake.x - enemy.x) ** 2 + (snake.y - enemy.y) ** 2) ** 0.5
    if distance < snake.radius + enemy.radius:
        return True
    return False


# Function to display the "Game Over" screen
def show_game_over_screen():
    game_over = True

    # Stop playing background music
    background_music.stop()

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # If Enter key is pressed
                    game_over = False

                elif event.key == pygame.K_ESCAPE:  # If Esc key is pressed
                    pygame.quit()
                    quit()

        window.fill(black)

        game_over_text = font.render("Game Over!", True, white)
        game_over_text_rect = game_over_text.get_rect(center=(width // 2, height // 2 - 50))
        window.blit(game_over_text, game_over_text_rect)

        continue_text = font.render("Press Enter to Continue", True, white)
        continue_text_rect = continue_text.get_rect(center=(width // 2, height // 2 + 10))
        window.blit(continue_text, continue_text_rect)

        exit_text = font.render("Press Esc to Exit", True, white)
        exit_text_rect = exit_text.get_rect(center=(width // 2, height // 2 + 50))
        window.blit(exit_text, exit_text_rect)

        pygame.display.update()
        clock.tick(30)


# Rest of the game code
snake = Snake()
food = Food()
enemies = []
stars = []
boss = None
boss_appeared = False
boss2 = None
boss2_appeared = False
boss3 = None
boss3_appeared = False
num_enemies = 15
num_stars = 25

for i in range(num_enemies):
    enemy_image = enemy_images[i % len(enemy_images)]
    enemy = Enemy(enemy_image)
    enemies.append(enemy)

for i in range(num_stars):
    star = Star()
    stars.append(star)

score = 0
font = pygame.font.Font(None, 36)
pause_image = pygame.image.load("pause_image.png")
pause_image = pygame.transform.scale(pause_image, (width, height))

# Start playing background music
background_music.play(-1)

while True:
    game_over = False
    is_paused = False
    score = 0

    snake = Snake()
    food = Food()
    enemies = []
    stars = []
    boss = None
    boss_appeared = False
    boss2 = None
    boss2_appeared = False
    boss3 = None
    boss3_appeared = False

    for i in range(num_enemies):
        enemy_image = enemy_images[i % len(enemy_images)]
        enemy = Enemy(enemy_image)
        enemies.append(enemy)

    for i in range(num_stars):
        star = Star()
        stars.append(star)

    # Start playing background music
    background_music.play(-1)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # If Esc key is pressed
                    is_paused = not is_paused  # Toggle pause state
                    if is_paused:
                        pygame.mixer.music.pause()  # Pause background music
                    else:
                        pygame.mixer.music.unpause()  # Unpause background music
                elif not is_paused:  # Process controls only if not paused
                    if event.key == pygame.K_RIGHT and snake.direction != "left":
                        snake.direction = "right"
                    elif event.key == pygame.K_LEFT and snake.direction != "right":
                        snake.direction = "left"
                    elif event.key == pygame.K_UP and snake.direction != "down":
                        snake.direction = "up"
                    elif event.key == pygame.K_DOWN and snake.direction != "up":
                        snake.direction = "down"

        if not is_paused:
            window.fill(black)

            snake.move()
            if snake.check_collision():
                game_over = True

            if snake.eat_food(food):
                score += 1
                food = Food()

            snake.draw()
            food.draw()

            for enemy in enemies:
                enemy.draw()
                enemy.move(snake.x, snake.y, enemies)

                if check_collision(snake, enemy):
                    game_over = True

                if enemy.x <= enemy.radius or enemy.x >= width - enemy.radius:
                    enemy.speed *= -1
                if enemy.y <= enemy.radius or enemy.y >= height - enemy.radius:
                    enemy.speed *= -1

            for star in stars:
                star.draw()
                star.move()

            # Boss1
            if score == 5 and not boss_appeared:
                boss = Boss()
                boss_appeared = True
                # Load and play boss music
                boss_music = pygame.mixer.Sound("boss_music.mp3")
                boss_music.play(-1)

            if boss:
                boss.draw()
                boss.move(snake.x, snake.y, enemies)
                if check_collision(snake, boss):
                    game_over = True

            if boss_appeared and (score >= 10 or game_over):
                boss_appeared = False
                boss = None
                # Stop music after boss disappears
                boss_music.stop()

                # Boss2
            if score == 20 and not boss2_appeared:
                boss2 = Boss2()
                boss2_appeared = True
                # Load and play boss music
                boss_music = pygame.mixer.Sound("boss2_music.mp3")
                boss_music.play(-1)

            if boss2:
                boss2.draw()
                boss2.move(snake.x, snake.y, enemies)
                if check_collision(snake, boss2):
                    game_over = True

            if boss2_appeared and (score >= 25 or game_over):
                boss2_appeared = False
                boss2 = None
                # Stop music after boss disappears
                boss_music.stop()

            # Boss3
            if score == 30 and not boss3_appeared:
                boss3 = Boss3()
                boss3_appeared = True
                # Load and play boss music
                boss_music = pygame.mixer.Sound("boss3_music.mp3")
                boss_music.play(-1)

            if boss3:
                boss3.draw()
                boss3.move(snake.x, snake.y, enemies)
                if check_collision(snake, boss3):
                    game_over = True

            if boss3_appeared and (score >= 35 or game_over):
                boss3_appeared = False
                boss3 = None
                # Stop music after boss disappears
                boss_music.stop()

            score_text = font.render("Score: " + str(score), True, white)
            window.blit(score_text, (10, 10))

        else:
            window.blit(pause_image, (0, 0))

            pause_text = font.render("Paused", True, white)
            pause_text_rect = pause_text.get_rect(center=(width // 2, height // 4))
            window.blit(pause_text, pause_text_rect)

        pygame.display.update()
        clock.tick(30)

    # Stop playing background music
    pygame.mixer.music.stop()

    show_game_over_screen()
