import pygame 
pygame.init()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = (255,255,255)
        if color:
            self.fill_color = color


    def color(self, new_color):
        self.fill_color = new_color


    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)


    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)       


    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    


#класс для объектов-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width,height))
        
    def draw(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
def update_go():
    if event.key == pygame.K_w:
        player_1.rect.y -= 30
    if event.key == pygame.K_s:
        player_1.rect.y += 30
    if event.key == pygame.K_UP:
        player_2.rect.y -= 30
    if event.key == pygame.K_DOWN:
        player_2.rect.y += 30
    


dx = -3
dy = -2
window = pygame.display.set_mode((500,500))
window.fill((0,0,0))
clock = pygame.time.Clock()
player_1 = Picture("platforma.png",0,250,20,340)
player_2 = Picture("platforma.png",490,250,20,340)
ball = Picture("mon.png",200,250,50,50)

while True:
    window.fill((0,0,0))
    player_1.draw()
    player_2.draw()
    ball.draw()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                update_go()
    if player_1.collidepoint(ball.rect.x,ball.rect.y):
        dx *= -1
        dy *= -1
    if player_2.collidepoint(ball.rect.x,ball.rect.y):
        dx *= -1
        dy *= -1
    ball.rect.x +=dx
    ball.rect.y +=dy
    clock.tick(40)
    pygame.display.update()
