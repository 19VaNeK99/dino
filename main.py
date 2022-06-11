import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = [0, 0]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]


pygame.init()
screen = pygame.display.set_mode([600, 400])

groups_cacti = pygame.sprite.Group()

dinosaur = Sprite(100, 100, 50, 'dinosaur.png')
cactus = Sprite(620, 240, 30, 'cactus.png')
cactus.speed = [-5, 0]

groups_cacti.add(cactus)

result = 0
next_boost = 5

font = pygame.font.Font(None, 32)

runnning = True
while runnning:

    if cactus.rect.x < 0:
        cactus.rect.x = 620
        result += 1

    if dinosaur.rect.y > 200:
        dinosaur.speed = [0, 0]
    else:
        dinosaur.speed[1] += 1

    if result >= next_boost:
        cactus.speed[0] -= 3
        next_boost += 5

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            runnning = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                dinosaur.speed[1] = -15

    if pygame.sprite.spritecollide(dinosaur, groups_cacti, False):
        runnning = False

    dinosaur.update()
    cactus.update()

    screen.fill([200, 200, 200])
    screen.blit(font.render(f'Счет: {result}', True, (0, 0, 0), [200, 200, 200]), (40, 40))
    screen.blit(pygame.image.load('ground.png'), [0, 250])
    screen.blit(dinosaur.image, dinosaur.rect)
    screen.blit(cactus.image, cactus.rect)
    pygame.display.flip()
    pygame.time.delay(20)


pygame.quit()
print(f'Счет: {result}')
