# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτητή  
### Φοίβος Αργυρίδης
### ΑΜ: Π2013041

## Εισαγωγή
Υλοποίησα συνολικά 4 ασκήσεις, οι οποίες έγιναν σε περιβάλλον linux με τη βοήθεια του terminal. Δούλεψα σε windows 10 με wsl (ubuntu). Όλα τα recorded sessions είναι στον προσωπικό μου λογαριασμό asciinema και τα link βρίσκονται παρακάτω στην ανάλυση της κάθε εργασίας, καθώς επίσης και url απο σελίδες ή βίντεο που άντλησα πλήροφορίες για την υλοποίησή τους.

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


## Άσκηση 4. Batch image conversion. Convert your image files to different sizes and formats.
#### asciinema: https://asciinema.org/a/nYxoD4BmPgbOKcESSYv0lzcha
Για την άσκηση αυτή δημιουργησα directory askisi4 και προσθεσα εικόνες που είχα στον υπολογιστή μου. Εγκατέστησα το imagemagick.

```
sudo apt-get install imagemagick
```

Δηιούργησα νέο directory για να αποθηκεύσω τις επεξεργασμένες εικόνες.

```
mkdir new_images
```

χρησιμοποιόντας την εντολή mogrify του imagemagick μείωσα το μέγεθος των εικόνων και τις μετέτρεψα σε png απο jpg.
Πετάει κάποιο error, αλλα τρέχει κανονικά.

```
mogrify -path new_images -adaptive-resize 40% -quality 50% -format png *
```

Οι αλλαγές επιβεβαιώνονται και στα δύο directories με την εντολή

```
ls -lh
```

## Πηγές
https://imagemagick.org/script/mogrify.php


## Συμπεράσματα
Με την υλοποίηση των παραπάνω ασκήσεων έμαθα να χρησιμοποιώ σημαντικά εργαλεία του linux terminal. Η δουλειά γίνετε γρηγορότερα πχ στην επεξεργασία εικόνων με το imagemagick αν το συγκρίνω με το photoshop. To γραφικό περιβάλλον έχει το συν ότι βλέπεις τι κάνεις (δεν χεριάζετε πάντα) αλλά τρώει αρκετή ram. Έτσι αν θέλεις κάτι γρήγορο μπορείς να χρησιμοποιήσεις τα εργαλεία του command line, τα οποία πολλές φορές μπορείς να τα επεκτείνεις και να τα κάνεις καλύτερα ώστε να σου δίνουν καλύτερο outout με το τι συμβαίνει. Μέσα απ’ όλη τη διαδικασία έμαθα αρκετές εντολές του linux terminal τις οποίες σκοπεύω να χρησιμοποιώ από δω και πέρα.
