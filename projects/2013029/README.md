# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτήτριας  
### Μαρία Δήμα
### ΑΜ: Π2013029

## Άσκηση 1. Search, download and play (with the terminal) your favorite song of the month from youtube.
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

