import pygame, datetime

pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Часы Мики")

# Загрузка и изменение изображений
MikiClock = pygame.image.load("img/mainclock.png")
mainClock = pygame.transform.scale(MikiClock, (width, height))

RightHand = pygame.image.load("img/rightarm.png")
FirstHandOriginal = pygame.transform.scale(RightHand, (width, height))  # Теперь это часовая стрелка

LeftHand = pygame.image.load("img/leftarm.png")
SecondHandOriginal = pygame.transform.scale(LeftHand, (25, 300))  # Минутная стрелка

rotation_center = (width // 2, height // 2)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    hour = now.hour % 12 + now.minute / 60  # Приводим часы к 12-часовому формату 
    minute = now.minute + now.second / 60  # Добавляем минуты для плавности

    # Рассчитываем углы поворота
    angle_hour = (hour * 30) % 360
    angle_minute = (minute * 6) % 360

    # Вращаем стрелки
    FirstHand = pygame.transform.rotate(FirstHandOriginal, -angle_hour)  # Часовая стрелка
    new_rect_hour = FirstHand.get_rect(center=rotation_center)
    SecondHand = pygame.transform.rotate(SecondHandOriginal, -angle_minute)  # Минутная стрелка
    new_rect_minute = SecondHand.get_rect(center=rotation_center)

    screen.fill((0, 0, 0))  # Очищаем экран
    screen.blit(mainClock, (0, 0))
    screen.blit(FirstHand, new_rect_hour.topleft)  # Часовая стрелка
    screen.blit(SecondHand, new_rect_minute.topleft)  # Минутная стрелка

    pygame.display.flip()

pygame.quit()