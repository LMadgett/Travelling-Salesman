import pygame

class City:
    def __init__(self, pos):
        self.pos = pos
        self.visited = False

def calculate_distance(loc1, loc2):
    return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5

def run():
    pygame.init()
    screen = pygame.display.set_mode((1024, 1024))
    pygame.display.set_caption("Travelling Salesman Problem Visualization")
    running = True
    optimising = False

    cities = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if not optimising:
                        pos = pygame.mouse.get_pos()
                        city = City(pos)
                        cities.append(city)
                        pygame.draw.circle(screen, (0, 255, 0), pos, 5)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    optimising = True
        if optimising:
            screen.fill((0, 0, 0))
            for city in cities:
                pygame.draw.circle(screen, (0, 255, 0), city.pos, 5)
            #TODO implement the TSP algorithm here