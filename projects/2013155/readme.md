# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτητή  
### Νίκος ξαντινίδης
### ΑΜ: Π2013155

## Eργασία 1 search, download and play (with the terminal) your favorite song of the month from youtube

#### url asciinema to recorded terminal session: https://asciinema.org/a/l8QPkOrJE5PDd5FDg8RZAjfr4
Για το συγκεκριμένη εργασία χρησιμοποιήθηκε το youtube-dl απο το οποίο μπορείς να κάνεις οποιαδήποτε αναζήτηση στο youtube και να κατεβάσεις το βίντεο ή μόνο τον ήχο σε οποιαδήποτε μορφή. Επέλεξα ν ακαταβάσω το the show must go on απο Queen.

```
youtube-dl -x --audio-format mp3 -o choosename.mp3 ytsearch$1:"$search term
```

Διαλέγουμε δηλαδή μόνο τον ήχο ως mp3, επιλέγουμε να όνομα για να αποθηκεύσουμε το αρχείο, στο $1 λέμε οτι θέλουμε να κατεβάσουμε μόνο ένα αποτέλεσμα απο το search και στη συνέχεια γράφουμε τον όρο αναζήτησης. Το αρχείο κατεβαίνει στο directory που βρισκόμαστε.

Για την αναπαραγωγή του αρχείου mp3, χρησιμοποίησα τον mplayer αντί για το mpv.Η εγκατάσταση του mplayer σε debian γίνετε με την παρακάτω εντολή.

```
sudo apt-get install mplayer
```
και η αναπαραγωγή

```
mplayer /path/to/file.mp3
```

Στην περίπτωση που λέιπουν κάποιες επεκτάσεις όπως στην περίπτωση μου μπορούν να εγκατασταθούν.

```
sudo apt-get install ffmpeg
```
