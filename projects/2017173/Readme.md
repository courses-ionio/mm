# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ Πολυμέσα 

## Στοιχεία φοιτητή  
### Χαράλαμπος Στυλιανού
### ΑΜ: Π2017173
https://twitter.com/P17styl

## Πρώτο Παραδοτέο : 
###  search, download and play (with the terminal) your favorite song of the month from youtube
### Asciinema URL : https://asciinema.org/a/WpyFWm3eNmY5rSkdvfjgvqMKJ
### Τα προγράμματα που χρειάζονται

```
sudo apt-get install youtube-dl
sudo apt-get install sox
sudo apt-get install ffmpeg
sudo apt-get install ddgr
```

### Οι εντολές που χρησιμοποίησα :

```
youtube-dl --extract-audio --audio-format mp3 <link of the music you want to download>
play 'Song name.mp3'
```
## Δεύτερο Παραδοτέο : 
### youtube video streaming
### Asciinema URL : https://asciinema.org/a/280073

Ακριβός όπως το πρώτο παραδοτέο έτσι και στο δεύτερο κάνουμε αναζήτηση του βίντεο που θέλουμε και με την πιο κάτω εντολή ανοίγει ένα παράθυρο και παίζει το βίντεο κανονικά χωρίς να χρειάζεται να τα κατεβάσεις.
```
mplayer -cookies -cookies-file /tmp/cookie.txt $(youtube-dl -g --cookies /tmp/cookie.txt "video link you want to stream")
```
Επειδή το youtube κάνει χρήση τον cookies για βεβαιωθεί ότι κάνεις χρήση κάποιου broswer ,
με τη χρήση του -cookies λες του mplayer να κάνει χρήση τον cookies. Μετά με τη χρήση του -cookies-file του λες που βρίσκεται το αρχείο με τα cookies.
Το youtube-dl μπορεί να δημιουργήσει cookies για εμάς με τη χρήση
```
$(youtube-dl -g --cookies /tmp/cookie.txt "video link you want to stream")
```
Το -g είναι για να μην κατεβάσει το βίντεο αλλά απλά να μας δώσει το link.
Το path /tmp/cookie.txt πρέπει να είναι το ίδιο και στα δύο. 

