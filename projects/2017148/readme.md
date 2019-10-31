## ΜΑΘΗΜΑ: Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτητή  
### Αντρέας Παππούτας
### ΑΜ: Π2017148

## Παραδοτέο 1
### download mp3 - search, download and play (with the terminal) your favorite song of the month from youtube

Σε αυτή τη εργασία κατέβασα ενα τραγούδι απο το terminal σε μορφή mp3 με το youtube-dl. Με το εργαλείο mpv κατάφερα να 
τρέξω το mp3 αρχείο μέσα στο terminal.

## [Asciinema Recording URL: https://asciinema.org/a/VYVtnnYotgjyRvJECRBhw0njt](https://asciinema.org/a/VYVtnnYotgjyRvJECRBhw0njt)

### Για τη αλλαγή του terminal έγινε χρήση της εντολής

```
sudo gedit ~/.bashrc
```
## Έγινε εγκατάσταση των παρακάτω

### PYTHON

```
sudo apt-get install python3.6
```

### YOUTUBE-DL

```
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```


### MPV

```
sudo add-apt-repository ppa:mc3man/mpv-tests
sudo apt-get install mpv
```

### FFMPEG

```
sudo apt install ffmpeg
```

### Μέσο του youtube-dl κατέβασα το τραγούδι σε μορφή mp3

```
youtube-dl --extract-audio --audio-format mp3 --output song.mp3 <url>
```

### Για την αναπαραγωγή του τραγουδιού χρησημοποίησα το mpv

```
mpv song.mp3
```





## Παραδοτέο 2
### download a torrent

Σε αυτή το παραδοτέο έκανα χρήση του rtorrent. Όταν ανοίξεις το rtorrent βάζεις το url ή directory του torrent σου και πατάς enter. Για να αρχίσεις να κατεβάζεις επιλέγεις το torrent και πατάς ctrl+s. Για να σταματήσει ctrl+d και για να διαγραφτεί ctrl+d(x2) .

## [Asciinema Recording URL: https://asciinema.org/a/277309](https://asciinema.org/a/277309)

### Εγκατασταση του rtorrent

```
sudo apt-get install rtorrent
```


### Keybindings για το rtorrent
```
ctrl+S = start torrent
ctrl+D = stop torrent
ctrl+D(x2) = delete torrent
```
