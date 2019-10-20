# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
### Μάθημα : Πολυμέσα
## Kαθηγητής: Χωριανόπουλος Κωνσταντίνος 

### Στοιχεία φοιτητή : Χρίστος Δημοσθένους
## ΑΜ: Π2017175 

## Eργασία 1: Search, download and play (with the terminal) your favorite song of the month from youtube

### url asciinema: https://asciinema.org/a/ltN3WDWJ7uZiaUI6nzYrlocSU
 Για να το κάνω αυτό έχω χρησιμοποιήση το youtube-dl όπου κάνουμε αναζήτηση στο youtube και μπορέις να κατεβάσεις το video σε mp3 μορφή.
## youtube-dl -x --audio-format mp3 + link απο το youtube
 Στην ουσία με το παραπάνω επιλέγουμε να το κατεβάσουμε σε μορφή mp3 δηλαδή μόνο ήχο
 
 ## sudo apt-get install sox
 ## sudo apt-get install ffmpeg
 
 # Στο Video που έκανα αρχικά κατέβασα το τραγούδι σε mp3 μορφή μετά το βλέπουμε που κάνει download , αργότερα με το ls μου δείχνει όλα τα τραγούδια που είναι κατεβασμένα στον φάκελο μου. Στην συνέχεια με την εντολή play και το όνομα του αρχείου αρχίζει να παίζει ο ήχος.  
  
## Εργασία 2: Youtube video streaming 

### url asciinema: https://asciinema.org/a/4bhBBEJo5OqxWuX3uel1pFGek
## Εντολή : mplayer -fs -cookies -cookies -cookies-file /tmp/cookies.txt $(youtube-dl -g --cookies /tmp/cookies.txt " link apo youtube ")
# Με το -fs μπορούμε να βλέπουμε το video μας σε πλήρης εικόνα. Το -g είναι για να μην αποθηκευτεί το video και απλά να πάρουμε ένα link
