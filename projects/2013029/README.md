# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτήτριας  
### Μαρία Δήμα
### ΑΜ: Π2013029

## Άσκηση 1. Search, download and play (with the terminal) your favorite song of the month from youtube.
#### asciinema https://asciinema.org/a/QDPfqsqwPdNcsvp21O3DkJXTd
Χρησιμοποιήθηκε το youtube-dl
```
sudo apt-get install youtube-dl
```

Επέλεξα να κατεβάσω το fix you απο Coldplay https://www.youtube.com/watch?v=k4V3Mo61fJM 

```
youtube-dl -x --audio-format mp3 -o fixyou.mp3 ytsearch$1:"$Coldplay - Fix You"
```

Για την αναπαραγωγή χρησιμοποίησα τον mpv player

```
sudo apt-get install mpv
mpv fixyou.mp3
```

#### Πηγές άσκησης
https://askubuntu.com/questions/178481/how-to-download-an-mp3-track-from-a-youtube-video
https://askubuntu.com/questions/643286/can-i-download-videos-from-a-youtube-search-query-using-youtube-dl
https://askubuntu.com/questions/630134/how-to-specify-a-filename-while-extracting-audio-using-youtube-dl

## Άσκηση 2. Manage your music library. Import your music library, add tags and delete/add songs.
#### asciinema https://asciinema.org/a/y9ThdSWKMS1JWtkWHsHuLZRIT
Εκκατέστησα το beets

```
sudo apt-get install beets
```
Στη συνέχεια προσθεσα στο config.yaml του beets τα path για την αποθήκευση των κομματιών και της βιβλιοθήκης.

```
sudo nano .config/beets/config.yaml
```

```
directory: ~/beets_music
library: ~/beets_library/library.blb
import:
    move: no
    copy: yes
```
Δημιούργησα τα δύο νέα directories για να λειτουργήσει το beets. 

```
sudo mkdir beets_music
sudo mkdir beets_library
```

Επειδή το beets δεν είχε πρόσβαση στα directories αυτά άλλαξα τα permitions.

```
sudo chmod -R 777 beets_music
sudo chmod -R 777 beets_library
```

Για να προσθέσω κομμάτια είχα δημιουργήσει 2 directories music1 και music2 με διαφορα τραγούδια.

```
beet import music1
beet import music2
```

modify (add edit tags)

```
beet modify <artist or other tag> <tag>="new tag"
```

delete

```
beet remove title:'song title'
```

Για να δεί κανεις κομμάτια με συγκεκριμένες λέξεις κλειδιά πχ tags

```
beet ls <tag or artist or anything>
```

### Πηγές άσκησης
https://www.youtube.com/watch?v=-eVTV3npXZQ

https://beets.readthedocs.io/en/v1.3.17/reference/query.html

