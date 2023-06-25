def calculate_revolutions(song_length):
    ticks_per_revolution = 4
    return song_length / ticks_per_revolution


song_length = int(input())
revolutions = calculate_revolutions(song_length)
print(revolutions)
