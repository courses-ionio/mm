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
