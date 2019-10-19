# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  

## Στοιχεία φοιτητή  
### Αθανάσης Παπαπέτρου
### ΑΜ: Π2017149

## Eργασία 1 search, download and play (with the terminal) your favorite song of the month from youtube

## asciinema URL: https://asciinema.org/a/mMVDOLmCMoKBVljDo4M3YrflA

## Τα προγράμματα που χρησιμοποίησα:

# youtube-dl
sudo apt-get install youtube-dl

# sox
sudo apt-get install sox

# ffmpeg
sudo apt-get install ffmpeg


## Οι εντολές που χρησιμοποίησα στο video

# Για να κατεβάσω το τραγούδι σε mp3
```
youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=ibWdgkv1LSA
```
# Για να δω τα αρχεία που είναι στον φάκελο 
```
ls
```
# Για τα αρχίσει τα παίζει το τραγούδι με το sox
```
play 'Mansion - NF (Lyrics)-ibWdgkv1LSA.mp3'
```
