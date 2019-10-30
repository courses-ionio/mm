# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
### Μάθημα : Πολυμέσα
## Kαθηγητής: Χωριανόπουλος Κωνσταντίνος 

### Στοιχεία φοιτητή : Χρίστος Δημοσθένους
## ΑΜ: Π2017175 

## Eργασία 1: Search, download and play (with the terminal) your favorite song of the month from youtube

### url asciinema: https://asciinema.org/a/277023
 Χρησιμοποίησα το ddgr για να κάνει αναζήτηση στο τραγούδι που ήθελα. 

## youtube-dl -x --audio-format mp3 + link 
 Στην ουσία με το παραπάνω επιλέγουμε να το κατεβάσουμε σε μορφή mp3 δηλαδή μόνο ήχο
 
 ## sudo apt-get install sox
 ## sudo apt-get install ffmpeg
 
 # Στο Video που έκανα αρχικά χρησιμοποιήσα την μηχανή αναζήτησης ddgr έγραψα το τραγούδι που ήθελα και έκανα αναζήτηση. Πάτησα το x και ξανά έβαλα το όνομα του τραγουδιού για να μου εμφανίσει το link και μετά με την επόμενη εντολή άρχισε να το παίζει σε mp3
  
## Εργασία 2: Youtube video streaming 

### url asciinema: https://asciinema.org/a/4bhBBEJo5OqxWuX3uel1pFGek
## Εντολή : mplayer -fs -cookies -cookies -cookies-file /tmp/cookies.txt $(youtube-dl -g --cookies /tmp/cookies.txt " link apo youtube ")
# Με το -fs μπορούμε να βλέπουμε το video μας σε πλήρης εικόνα. To cookies-file δίνουμε δικαίωμα στο mplayer να χρησιμοποιήση cookies και το  -g είναι για να μην αποθηκευτεί το video και απλά να πάρουμε ένα link.
