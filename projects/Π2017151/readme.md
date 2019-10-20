## ΜΑΘΗΜΑ: Πολυμέσα  
 
### ONOMA ΦΟΙΤΗΤΗ: Χαράλαμπος Θεοδούλου
### ΑΜ: Π2017151

## Παραδοτέο 1
### κατεβάστε και παίξτε μέσο του τέρμιναλ το αγαπημένο σας τραγούδι του μήνα.

## [Asciinema URL](http://asciinema.org/a/qxybfXGWa4Pyo4zbJNCgJM01m)


# ΕΝΤΟΛΕΣ ΠΟΥ ΧΡΗΣΙΜΟΠΟΙΗΘΗΚΑΝ 




### FFMPEG

```
sudo apt install ffmpeg
```


### MPV

```
sudo add-apt-repository ppa:mc3man/mpv-tests
sudo apt-get install mpv
```

### YOUTUBE-DL

```
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```


### χρησιμοποιήθηκε  η παρακάτω εντολή για λήψη σε mp3. μορφη

```
youtube-dl --extract-audio --audio-format mp3 -o onemoreligh.mp3 <url>
```

### χρησιμοποιήθηκε η παρακάτω εντολή για την εκτέλεση του τραγουδιού μέσα στο τέρμιναλ 

```
mpv onemoreligh.mp3
```
