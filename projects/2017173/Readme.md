# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ Πολυμέσα 

## Στοιχεία φοιτητή  
### Χαράλαμπος Στυλιανού
### ΑΜ: Π2017173

## Πρώτο Παραδοτέο : 
###  search, download and play (with the terminal) your favorite song of the month from youtube
### Asciinema URL : https://asciinema.org/a/JhtxwhNAsw1MhHkq6ishe52G7

### Τα προγράμματα που χρειάζονται

```
sudo apt-get install youtube-dl
sudo apt-get install sox
sudo apt-get install ffmpeg
```

### Οι εντολές που χρησιμοποίησα :

```
youtube-dl --extract-audio --audio-format mp3 <link of the music you want to download>
play 'Song name.mp3'
```
