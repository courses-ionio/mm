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


## Άσκηση 3. Manage torrent files. Search and download a torrent.
#### asciinema https://asciinema.org/a/c3WFsJAatANVYD3Zuw6KUFZZL
Για την άσκηση αυτή χρησιμοποίησα δύο εργαλεία. Για την αναζήτηση του torrent χρησιμοποίσησα το we-get, και για να κατεβάσω το torrent χρησιμοποίησα το deluge. Η εγκατάσταση του we-get εγινε μέσω pip.

```
sudo pip3 install git+https://github.com/rachmadaniHaryono/we-get
```

Αμέσως μετά εγκατέστησα το deluge.

```
sudo apt-get install deluge deluged deluge-console
```

Επέλεξα να κατεβάσω το Lubuntu linux οπότε με τη βοήθεια του we-get έψαξα για το Lubuntu στο pirate bay

```
we-get --search "Lubuntu" --target the_pirate_bay
```

Στη συνέχεια για να δώ το magnet link απο τα αποτελέσματα αναζήτησης...

```
show lubuntu-16.10-desktop-i386.iso
```

Τέλος κλείνοντας το we-get άνοιξα το console to deluge, και προσθεσα το magnet link

```
deluge-console
add -p /home/maria/downloads <magnet link>
```

### Πηγές άσκησης
https://www.ostechnix.com/search-torrents-command-line-linux/

https://askubuntu.com/questions/315113/how-to-run-deluge-from-cli


## Άσκηση 4. Batch image conversion. Convert your image files to different sizes and formats
#### asciinema https://asciinema.org/a/2hSTASx15pGnOMpgLSNdxOx6F
Αρχικά δημιουργησα directory images, όπου έβαλα 4 images που κατέβασα απο https://www.stockvault.net/c/nature/landscape.
Τις εικόνες της πέρασα απο τον explorer των windows κάνωντας browse το filesystem μου με την εντολή.

```
exploer.exe .
```
Εγκατέστησα το imagemagick.

```
sudo apt-get install imagemagick
```

Δημιουργησα directory μεσα στο images με ονομασία resized, και είδα τις εικόνες με το μέγεθός τους

```
cd images
mkdir resized
ls -lh
```
Στη συνέχεια έτρεξα το conversion του imagmagick με την εντολή mogrify. Μείωσα το μέγεθος αρχείου όλων των εικόνων και τις μετέτρεψα σε .png απο .jpg

```
mogrify -path resized -adaptive-resize 50% -quality 60% -format png *
```

Πάλι επιβεβαίωσα τις αλλαγες

```
cd resized
ls -lh
```



