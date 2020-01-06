# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτήτριας  
### Ιωάννα Ξυγκώρου
### ΑΜ: Π2014215

### Προσωπικό αποθετήριο https://github.com/p2014xygk/mm

## Εισαγωγή
Έγιναν 4 ασκήσεις σε linux terminal όπως περιγραφονται στις οδηγίες του μαθήματος. Οι εργασίες όλλες υλοποιήθηκαν σε raspberry pi, με λειτουργικό raspbian buster. Κάθε άσκηση περιέχει σχετικό link στο asciinema όπου φαινεται η διαδικασία υλοποίησης, καθώς και πηγες άντλησης δεδομένων και βοήθειας για τα εργαλέια που χρησιμοποιήθηκαν.

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

### Άσκηση 4. Batch image conversion. Convert your image files to different sizes and formats.

#### url asciinema: https://asciinema.org/a/XD5Pde6qThhZ60h0CjmISTx6l

Για την άσκηση αυτή χρησιμοποίησα το imagemagick. Και μείωσα το μέγεθος όλων των εικόνων μέσα στον φάκελο images κατα 50%. H πρακτική αυτή είναι ιδανική όταν δουλεύεις με περιεχόμενο το οποίο πρέπει να ανέβει σε μια ιστοσελίδα, Θες οι εικόνες να είναι οσο το δυνατόν μικρότερες σε μέγεθος χωρίς να χάσουν αισθητά την ποιότητά τους. Συνήθως η δουλειά αυτή γίνετε με λογισμικά όπως το photoshop. Με το imagemagick είναι πολύ πιο εύκολο. Εγκατέστησα το imagemagick με την εντολή

```
sudo apt-get install imagemagick
```

Δημιούργησα νέο φάκελο resized_images μεσα στον φάκελο images, όπου είναι οι εικόνες και χρησιμοποίησα την εντολή mogrify.

```
mogrify -path resized_images -adaptive-resize 50% -quality 60% *
```
Στην παραπάνω εντολή δίνουμε το όνομα του directory που θέλουμε να αποθηκευτούνε ει εικόνες μας, ορίζουμε το ποσοστό του resize και της ποιότητας που θέλουμε (κάτι σαν το save for web and devices του photoshop).

Η διαφορά στα μεγέθη των αρχείων φαίνεται ξεκάθαρα με την εντολή

```
ls -lh
```

Τέλος επέλεξα μία εικόνα απο τις νέες εικόνες που δημιουργήθηκαν για να την μετατρέψω απο jpg σε png. Για τον σκοπό αυτό δημιούργησα νέο directory PNG μεσα στο resized_images, και ετρεξα την εντολή

```
convert name.jpg PNG/name.png
```

Πηγές άντλησης δεδομένων και βοήθειας:
https://www.youtube.com/watch?v=-hPleOyZJr4


## Συμπεράσματα
Μέσα από τη διαδικασία υλοποίησης των 4 ασκήσεων εξοικειώθηκα με το terminal των linux, και έμαθα να χρησιμοποιώ σημαντικά εργαλεία, αλλα και πως λειτουργεί γενικά το σύστημα. file structure, δικαιώματα χρηστών κ.α. Απο τις αναζητήσεις στο internet σχετικά με την εγκατάσταση και την λειτουργία των εργαλέιων κατάλαβα ότι πολλά πραγματα διαφέρουν σε κάθε σύστημα (linux distribution). Οι γνώσεις που αποκτήθηκαν είναι σημαντικές καθώς πολλές διαδικτυακές εφαρμογές τρέχουν σε linux, και είναι σημαντικό να γνωριζεις πως λειτουργεί το συστημα, κυρίως μέσω terminal.
