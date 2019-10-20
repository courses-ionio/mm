## ΜΑΘΗΜΑ: Πολυμέσα  
## Παραδοτέο 1ο
### download mp3 - search, download and play (with the terminal) your favorite song of the month from youtube.

Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος
 
## Στοιχεία φοιτητή 
## Όνομα: Χρήστος Δήμας
## Α.Μ.: Π2017204

Asciinema URL: https://asciinema.org/a/LzIEgPe6Zvtg61N8DdWKWcqy2

## Για να επιτευχθεί η εργασία χρειάστηκε να γίνει η εγκατάσταση των παρακάτω με τις εξής εντολές:

### PYTHON
 
```
sudo apt-get install python
```

### YOUTUBE-DL
 
```
sudo apt-get install youtube-dl
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

## Για να γίνει η μετατροπή του τραγουδιού απο το youtube σε μορφή mp3 γίνεται με την παρακάτω εντολή:

### YOUTUBE-DL
 
```
youtube-dl --extract-audio --audio-format mp3 --prefer-ffmpeg
```
