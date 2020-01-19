# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτητή  
### Φοίβος Αργυρίδης
### ΑΜ: Π2013041

## Άσκηση 1. Search, download and play (with the terminal) your favorite song of the month from youtube.
#### asciinema: https://asciinema.org/a/eDpKh5BJxEvNRrBhJVsPhc4IR
Εγκατέστησα το youtube-dl

```
sudo apt-get install youtube-dl
```

Δημιούργησα directory music

```
mkdir music
```

Εψαξα και κατέβασα σε μορφή mp3 το nothing else matters των metallica με τη χρήση του youtube-dl στο music directory που δημιούργησα

```
youtube-dl -x --audio-format mp3 -o music/nothin_else_matters.mp3 ytsearch$1:"Metallica: Nothing Else Matters"
```

Έκανα αναπαραγωγή του τραγουδιού με τον mpv player

```
cd music
mpv nothin_else_matters.mp3
```

## Πηγές

https://www.youtube.com/watch?v=9A-HLSvtBWc

https://askubuntu.com/questions/178481/how-to-download-an-mp3-track-from-a-youtube-video

https://askubuntu.com/questions/630134/how-to-specify-a-filename-while-extracting-audio-using-youtube-dl

https://askubuntu.com/questions/643286/can-i-download-videos-from-a-youtube-search-query-using-youtube-dl



## Άσκηση 2. Manage torrent files. Search and download a torrent.
#### asciinema: https://asciinema.org/a/BFOukKNf4sCsHCYmr0CaAOnMs
Χρησιμοποίησα το we-get γαι να κανω αναζήτηση του torrent, και το rtorrent για να κατεβάσω το magnet.
Η εγκατάσταση του we-get γινετε μέσω pip και απαιτεί python > 3.5.

```
sudo pip3 install git+https://github.com/rachmadaniHaryono/we-get
sudo apt-get install rtorrent
```

Η αναζήτηση με το we-get γινετε με την εντολή:

```
we-get --search "Thunderstruck" --target  the_pirate_bay
show <επιλογή όνομα torrent>
```

ξεκινάμε τον rtorrent

```
rtorrent

backspace
paste magnet
```

## Πηγές
https://www.ostechnix.com/search-torrents-command-line-linux/

https://www.linuxtechi.com/rtorrent-command-line-bittorrent-client-ubuntu-linux/


## Άσκηση 3. Manage your music library. Import your music library, add tags and delete/add songs.
#### asciinema: https://asciinema.org/a/XXaSLzm2FOiE8rKUDkzYYjbDt

Εγκατέστησα το beets

```
sudo apt-get install beets
```

επεξεργαστηκα το configuration file του για να ορισω τα path

Δημιουργησα directories για το beets

```
mkdir beets_m
mkdir beets_l
```

```
beet config -p
sudo nano /home/fivos/.config/beets/config.yaml

directory: ~/beets_m
library: ~/beets_l/library.blb
import:
   move: yes
   copy: no
```

Πρόσθεσα μουσική, tags και έσβησα απο τη λιστα του beets.
```
beet import music/mymusic
beet ls
beet modify <you can modify as you want here>
beet remove title:'you song title'
```

## Πηγές
https://beets.readthedocs.io/en/v1.3.17/reference/query.html




