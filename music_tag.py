"""
This script loads an MP3 file using the music_tag library and extracts
the composer, title, and artist information from the file name.
It then updates the corresponding tags in the MP3 file and saves the changes.
"""

import music_tag as mt

f = mt.load_file("./Beethoven - Coriolan Overture, Op 62 - Muti.mp3")

file = str(f['title'])
print('Title:', file)
composer, title, artist = file.split('-')
composer = composer.strip()
title = title.strip()
artist = artist.strip()
print(f"{composer}\t\t{title}\t\t{artist}")

f['composer'] = composer
f['title'] = title
f['artist'] = artist
f.save()
