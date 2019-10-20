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
## Δεύτερο Παραδοτέο : 
### youtube video streaming
### Asciinema URL : https://asciinema.org/a/6XFGTmom7fwg0GNfQcL4v7VM3

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

## Τρίτο Παραδοτέο :
### download a torrent
### Asciinema URL : https://asciinema.org/a/glt3cwe9kjMnOCQ4q5chESmsJ

```
sudo apt-get install rtorrent
```
```
rtorrent
```
Πατάμε τα βελάκια πάνω ή κάτω.
Κάνουμε αντιγραφή το link του να κατεβάσεις ένα torrent αρχείο και πατάμε enter.
Μετά θα εμφανιστεί το όνομα του torrent που θέλουμε να κατεβάσουμε.
Με τα βελάκια διαλέγεις πιο torrent θες να διαλέξεις και εμφανίζονται * διπλά από αυτό πού είναι επιλεγμένο
Με τη χρήση του CTRL+S ξεκινά να κατεβάζει το torrent και με το CTRL+D το κάνει παύση . 
Αν κάνεις δυο φορές CTRL+D τότε διαγράφεται to torrent.


## Τέταρτο Παραδοτέο :
### demonstrate album art and visualizations with an mp3 player and various songs
### Asciinema URL :https://asciinema.org/a/NFhmJ5TYmL44RavqELDUrYogI\
Tο cmus μας βοηθά στη δημιουργία album τραγουδιών και να κάνουμε δικά μας playlists.
Είναι χωρισμένο σε 7 views : 
1 - Library
2 - Sorted library
3 - Playlist
4 - Play Queue
5 - Browser
6 - Filters
7 - Settings
Αλλάζεις το view σου πιέζοντας τους αριθμούς που βρίσκονται δίπλα από το όνομα του συγκεκριμένου view.Υπάρχουν και keybindings που μας βοήθα να κερδίζουμε χρόνο και επίσης μπορείς να αλλάξεις τα keybindings όπως σε βολεύει.
Με τη χρήση του :add κανείς προσθήκη τα τραγούδια που βρίσκονται σε εκείνο το αρχείο.
```
:add ~/Music
```
Μετά με τη χρήση κάποιων keybindings επεξεργαζόμαστε τη σειρά του playlists που έχουμε κάνει.
```
e = add to queue
a = add to playlist
p = move down the song in playlist or queue
P = move up the song in playlist or queue
```
