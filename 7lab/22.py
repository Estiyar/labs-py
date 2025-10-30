import pygame
import random
pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Музыкальный плеер")

def play_next_song():
    global _currently_playing_song, songs
    next_index = (songs.index(_currently_playing_song) + 1) % len(songs)
    _currently_playing_song = songs[next_index]
    pygame.mixer.music.load(f'Sounds/{_currently_playing_song}')
    pygame.mixer.music.play(1)
    
def play_previous_song():
    global _currently_playing_song, songs
    previous_index = (songs.index(_currently_playing_song) - 1) % len(songs)
    _currently_playing_song = songs[previous_index]
    pygame.mixer.music.load(f'Sounds/{_currently_playing_song}')
    pygame.mixer.music.play(1)


_currently_playing_song = '1.mp3'
done = False
songs = ['1.mp3', '2.mp3', '3.mp3']
SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(f'sounds/{_currently_playing_song}')
pygame.mixer.music.play(1)

font = pygame.font.SysFont(None, 24)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            play_next_song()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                play_next_song()
            elif event.key == pygame.K_LEFT:
                play_previous_song()
            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
            
                

    screen.fill((0, 0, 0))
    text = font.render(f'Сейчас играет: {_currently_playing_song}', True, (255, 255, 255))
    screen.blit(text, (50, height // 2))
    
    pygame.display.flip()

pygame.quit()