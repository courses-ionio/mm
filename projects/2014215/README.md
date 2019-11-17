# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτήτριας  
### Ιωάννα Ξυγκώρου
### ΑΜ: Π2014215

### Άσκηση 1. Search, download and play (with the terminal) your favorite song of the month from youtube.

#### url asciinema: https://asciinema.org/a/GFoZ3wMsXTZkP2atO7kkKXl22

Για την άσκηση αυτή χρησιμοποίησα το youtube-dl και τον mpv player. Έκανα εγκατάσταση το youtube-dl και μαζί εγκαταστάθηκε και ο mplayer.

```
sudo apt-get install youtube-dl
```

Το τραγούδι που επέλεξα να κατεβάσω είναι το Shallow (Lady Gaga, Bradley Cooper) https://www.youtube.com/watch?v=bo_efYhYU2A, και το κατέβασα με την εντολή

```
youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=bo_efYhYU2A
```

Έκανα αναπαργωγή του τραγουδιού με τον mpv με πληκτρολογώντας

```
mpv <filename>
```

Οδηγίες σχετικά με τη χρήση του youtube-dl βρηκα απο το παρακάτω url
https://www.tecmint.com/download-mp3-song-from-youtube-videos/

### Άσκηση 2. Download a torrent

#### url asciinema: https://asciinema.org/a/lkQD9eFiqlLW9CIcghx9ln7KN

Για την άσκηση αυτή χρησιμοποίησα το aria. Οδηγίες και βοήθεια σχετικά με την εγκατάσταση και λειτουργία βρήκα στο https://www.addictivetips.com/ubuntu-linux-tips/download-torrents-from-the-command-line-linux/

Η εγκατασταση έγινε με την εντολή 

```
sudo apt-get install aria
```

και το torrent κατέβηκε με την εντολή

```
aria2c <url or magnet>
```

Επέλεξα να κατεβάσω το λειτουργικό raspbian noobs lite για το raspberry pi το οποίο βρήκα στην διεύθυνση https://www.raspberrypi.org/downloads/noobs/

### Άσκηση 3. Manage your music library. Import your music library, add tags and delete/add songs.

#### url asciinema: https://asciinema.org/a/1CkoGY32Uhp8TJXoT4Djg6LDv

Για την άσκηση αυτή χρησιμοποιήθηκε το beets. Και για τις ανάγκες της εργασίας πριν αρχίσω το recording εφτιαξα δύο directories music και more_music στα οποία έβαλα μουσική για να εισάγω στο beets. H εγκατάσταση του beets έγινε με την εντολή

```
sudo apt-get install beets
```

στη συνέχεια δημιούργησα άλλα δυο directories. new_music, όπου μεταφέρονται τα imported κομμάτια στο beets και ένα library όπου θα υπάρχει το database του beets. Για να ρυθμίσεις σε ποιον φάκελο θα είναι η database και τα κομμάτια πρέπει να επεξεργαστείς το config.yaml του beets. για να βρώ που είναι το αρχείο έτρεξα την εντολή

```
beet config -p
```

και προσθεσα

```
directory: ~/new_music
library: ~/library/library.blb
import:
    move: no
    copy: yes
```

παραπάνω λέμε στο beets που θα αποθηκεύσει τη βάση και τα κομμάτια καθώς και ότι δεν θέλουμε να μεταφέρει τα κομμάτια αλλα να τα αντιγράψει ώστε να υπάρχουν και στον αρχικό μας φάκελο.

για να εισάγεις κομμάτια στο beets πληκτρολογείς την εντολή

```
beet import /path/to/your/music/folder
```

Το beets βρίσκει απο μόνο του όλα τα απαραίτητα tags και τα προσθέτει αυτόματα, οστόσο μπορείς να προσθέσεις η να τα αλλάξεις με την εντολή 

```
beet modify <artist> <tag>="new tag"
```

Μπορείς να διαγράψεις κομμάτι με την εντολή

```
beet remove title:'song title'
```




