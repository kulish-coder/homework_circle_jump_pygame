import pygame


SIZE = W, H = 500, 500
pygame.init()
screen = pygame.display.set_mode((SIZE))

class Circle:
    def __init__(self, x, y, rad, speed):
        self.x = x
        self.y = y
        self.rad = rad
        self.speed = speed
        self.color = [(202, 12, 240), (240, 149, 12), 
                            (146, 238, 240), (242, 12, 116), 
                                (35, 242, 12), (0, 0, 0)]

    def draw(self):
        self.color_c = self.color[-1]
        pygame.draw.circle(screen, self.color_c, (self.x, self.y), self.rad)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        jump_counter = 10
        is_jump = False
        if keys[pygame.K_SPACE]:
            is_jump = True
        if is_jump is True:
            if jump_counter >= -1:
                self.y -= jump_counter
                jump_counter -= 2
                for i in range(0, 5):
                    self.color_c = self.color[i]
            else:
                jump_counter = 10
                is_jump = False

circle = Circle(W // 2, H // 2, 50, 0.8)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
    screen.fill((225, 225, 225))
    circle.draw()
    circle.update()
    pygame.display.flip()
    pygame.display.update()
