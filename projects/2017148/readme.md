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
sudo getdit ~/.bashrc
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

