# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ-ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος
## Στοιχεία φοιτητή
### ΖΕΡΒΑΣ ΔΙΟΝΥΣΙΟΣ ΘΕΩΝΑΣ
### ΑΜ: Π2017105

## Εργασία 1η: Search, download and play (with the terminal) your favorite song of the month from youtube

### URL Asciinema: https://asciinema.org/a/277177
Για την εργασία χρησιμοποίησα το youtube-dl μέσω του οποίου σου παρέχεται η δυνατότητα να πραγματοποιήσεις αναζήτηση στο youtube και να κατεβάσεις είτε ολόκληρο το βίντεο είτε μόνο τον ήχο σε οποιαδήποτε μορφή επιθυμείς (πχ mp3). Στα πλαίσια της εργασίας επέλεξα να κατεβάσω το "Tones and I-Dance monkey"

```
youtube-dl -x --audio-format mp3 -o choosefilename.mp3 ytsearch$1:"$search term
```

Γράφοντας την εντολή αυτη στο terminal επιλεγουμε ότι θέλουμε μόνο τον ήχο σε μορφή mp3 και επιλέγουμε το όνομα του αρχείου που θα αποθηκεύσουμε. Ακόμη με το $1 υποδηλώνουμε πως θέλουμε να κατεβάσουμε μόνο ενα αποτέλεσμα από το search.

Για την αναπαραγωγή του τραγουδιού επέλεξα να χρησιμοποιήσω το mpv. 

Για την εγκατάσταση των προγραμμάτων youtube-dl & mpv χρησιμοποίησα τις παρακάτω εντολές:

Για το youtube-dl ακολούθησα της οδηγίες που δίνει ο καταστευαστής μεσα στο official github page τους 
URL https://github.com/ytdl-org/youtube-dl/blob/master/README.md#how-do-i-update-youtube-dl

```
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```
Για την εγκατάσταση του mpv χρησιμοποίησα τον εντολή 

```
sudo apt-get install mpv
```

## Εργασία 2η: Download a torrent

### URL asciinema: https://asciinema.org/a/280050
Για την εργασία αυτή χρησιμοποίησα το [rTorrent] μέσω του οποίου σου παρέχετε η δυνατότητα να πραγματοποιήσης τη λήψη ενός torrent αρχείου με διάφορους τρόπους (URL link, Magnet link κ.α.) Για τη διεκπεραίωση της εργασίας διάλεξα να χρησιμοποιήσω τον τρόπου του magnet link.
Έγκατάσταση rTorrent
```
sudo apt-get install rtorrent
```
Aρχικά καλείς από τον τερματικό το rTorrent με την εντολή
```
rTorrent
```
Στη συνέχεια εμφανίζεται ενα νέο περιβάλλον στο οποίο καλείται ο χρήστης να εισάγει το torrent που θέλει να κατεβάσει. Για να γίνει αυτο ο χρήστης πρέπει να πατήσει ENTER και στη συνέχεια να προσθέσει το Link το οποιο αντισοιχεί στο αρχείο που θέλει να "κατεβάσει"
Έπειτα ο χρήστης πρέπει να διαλέξει με τα βελάκια του πληκτρολογίου ποίο αρχείο επιθυμεί να προχωρίσει σε λήψη και στη συνέχεια να πατήσεις CTRL+S έτσι ώστε να αρχίσει η λήψη του αρχείου.


## Συμμετοχικό Υλικό- Α'Παραδοτέο
 
 # Link του βιβλίου (https://mibook.org/gr/)
 
  Για την ανάρτηση του περιεχομένου του βιβλίου [mibook/gr](https://mibook.org/gr/) με τρόπο εκπαιδευτικό και ευχάριστο, χρησιμοποίησα το [Twitter] (https://twitter.com/DionisisZervas).

Για το πρώτο παραδοτέο υλοποίησα συνολικά οτκώ δημοσιεύσεις ( 3 για το Β παραδοτέο) στις οποίες προσθάθησα να "εκμεταλλευτώ" όλες τις δυνατότητες του κοινωνικού αυτού δικτύου (text, images, gif, mention, hashtags,polls etc).

Link πρώτης ανάρτησης [Ορισμός multimedia] https://twitter.com/DionisisZervas/status/1193896683807166464

Link δεύτερης ανάρτησης [Street Maps] https://twitter.com/DionisisZervas/status/1193901779962015744

Link τρίτης ανάρτησης [GitHub] https://twitter.com/DionisisZervas/status/1193903829248626693

Link τέταρτης ανάρτησης [Apple-I-Computer] https://twitter.com/DionisisZervas/status/1193905369791246336

Link πέμπτης ανάρτησης [Google Search Engine] https://twitter.com/DionisisZervas/status/1193907509733609474

Link έκτης ανάρτησης [Google Assistant] https://twitter.com/DionisisZervas/status/1193909993571045377

Link έβδομης ανάρτησης [Windows 1] https://twitter.com/DionisisZervas/status/1193913421751836672

Link όγδοης ανάρτησης [Virtual Reality into Military Training] https://twitter.com/DionisisZervas/status/1193914889502416896  


## Εργασία 4η: Edit a spreadsheet

### URL asciinema: https://asciinema.org/a/284111

 Για την εργασία αυτή χρησιμοποίησα την εφαρμογή SC μέσω της οποίας μπορεί κάποιος να δημιουργήσει, να διαβάσει, να επεξεργαστεί και να διαγράψει αρχεια spreadsheet. ( http://manpages.ubuntu.com/manpages/xenial/man1/sc.1.html)
 
 Στο παραπάνω βίντεο επεξεργάζομαι ενα αρχείο scv το οποίο ονόμασα ergasia.scv μέσα στο οποίο αλλάζω τιμές σε διάφορες καταχωρίσεις καθώς επίσης καθορίζω και τον τρόπο σύνταξης του κειμένου (στο κεντρο, δεξιά, αριστερά κλπ). Η μεταφορά από καταχώρηση σε καταχώρηση γίνεται είτε με τα πλήκτρα h j k l όπου h μας μεταφέρει στην αριστερά καταχώρηση j στην άνω καταχώρηση k στην κάτω καταχώρηση και l στην δεξιά. Για την ευκολότερη χρήση του προγράμματος προτείνεται ο χρήστης να διατρέξει στο manual της εφαρμογής πατώντας το ? και στη συνέχεια να διατρέξει στους τομείς που τον ενδιαφέρουν και να διαβάσει της εντολές.
 
 Εφόσον έχει γίνει ορθή εγκατάσταση του προγράμματος ο χρήστης με την εντολή 
 ```
 sc FileName
 ```
 ανοίγει το πρόγραμμα και μπαίνει αυτόματα στο περιβάλλον εργασίας του.
 
 
 
 
 
 
 
 
 
