import pygame
import random

class City:
    def __init__(self, pos):
        self.pos = pos
        self.visited = False

def calculate_distance(loc1, loc2):
    return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5

def find_nearest_city(current_city, cities):
    nearest_city = None
    min_distance = float('inf')
    for city in cities:
        if not city.visited:
            distance = calculate_distance(current_city.pos, city.pos)
            if distance < min_distance:
                min_distance = distance
                nearest_city = city
    return (nearest_city, min_distance)

def run():
    pygame.init()
    x_size = 800
    y_size = 800
    screen = pygame.display.set_mode((x_size, y_size))
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
                        pygame.display.flip()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    optimising = True
                    drawn = False
        if optimising:
            #nearest neightbour algorithm
            if len(cities) > 0:
                min_distance = float('inf')
                for city in cities:
                    current_city = city
                    complete = False
                    total_distance = 0
                    route = []
                    while not complete:
                        current_city.visited = True
                        route.append(current_city)
                        (next_city, distance) = find_nearest_city(current_city, cities)
                        if distance != float('inf'):
                            total_distance += distance
                        if next_city is None:
                            complete = True
                            optimising = False
                            for c in cities:
                                c.visited = False
                            if total_distance < min_distance:
                                min_distance = total_distance
                                best_route = route
                            #print(f"starting at city {cities.index(city)} with distance {total_distance}")
                        else:
                            pygame.draw.line(screen, (255, 0, 0), current_city.pos, next_city.pos, 2)
                            current_city = next_city
                
                if not drawn:
                    screen.fill((0, 0, 0))
                    for city in cities:
                        pygame.draw.circle(screen, (0, 255, 0), city.pos, 5)
                    for i in range(len(best_route)):
                        if i < len(best_route) - 1:
                            pygame.draw.line(screen, (255, 0, 0), best_route[i].pos, best_route[i + 1].pos, 2)
                    font = pygame.font.SysFont(None, 36)
                    text = font.render(f"Total Distance: {min_distance:.2f}", True, (255, 255, 255))
                    screen.blit(text, (10, 10))
                    pygame.display.flip()
                    drawn = True

run()