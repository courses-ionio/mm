# Μάθημα: Πολυμέσα
#
## Προσωπικά Στοιχεία:
#### A.M.: Π2017203
#### Όνομα: Ανδρέας
#### Επώνυμο: Καγκελάρης
#
## Παραδοτέο 1
#### Τίτλος: download mp3 
#### Ζητούμενα: 
#### 1) search, download and play (with the terminal) your favorite song of the month from youtube
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση του S/W 'youtube-dl' ώστε να κάνουμε download το επιθυμητό link με την χρήση terminal. Η εγκατάσταση του πακέτου έγινε απο την σελίδα του δημιουργού και όχι απο τον Ubuntu server, λόγω γνωστού προβλήματος στην έκδοση του Ubuntu Server (https://github.com/ytdl-org/youtube-dl/issues/21952). 
###### sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
###### sudo chmod a+rx /usr/local/bin/youtube-dl
##### δ) Εγκατάσταση του front end 'mps-youtube', ώστε να κάνουμε search και download το αρχείο που θέλουμε.
###### sudo apt install mps-youtube
##### ε) Εκτέλεση του mpsyt. Download το βέλτιστο audio αρχείο (και όχι video για οικονομία χρόνου). 
##### στ) Εγκατάσταση του πακέτου 'ffmpeg', ώστε να μετατρέψουμε το αρχείο που κατεβάσαμε (.m4a) σε μορφή .mp3.
###### sudo apt-get install ffmpeg
##### ζ) Μετατροπή του αρχείου σε .mp3
###### ffmpeg -i 'Dmitri Shostakovich -  Waltz No. 2.m4a' -acodec libmp3lame -aq 2 'Dmitri Shostakovich -  Waltz No. 2.mp3'
##### η) Εγκατάσταση του S/W 'mpv', ώστε να γίνει απο εκεί η αναπαραγωγή του .mp3 αρχείου.
###### sudo apt-get install mpvsudo apt-get install mpv
##### θ) Αναπαραγωγή του .mp3 αρχείου απο terminal. Η αναπαραγωγή τερματίστηκε μετά απο λίγα δευτερόλεπτα, για οικονομία χρόνου.
###### mpv 'Dmitri Shostakovich -  Waltz No. 2.mp3'
#
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο παρακάτω link:
#### https://asciinema.org/a/275789
#
#### link στο αποθετήριο του κώδικα:
#### https://github.com/p17kagk/mm/tree/master
#### link στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### https://github.com/p17kagk/mm/tree/P2017203
#### link στο εκτελέσιμο:
#### https://asciinema.org/a/275789
#
## Παραδοτέο 2
#### Τίτλος: download a torrent
#
###### Σημείωση: Κατά την εκπόνηση της εργασίας, διαπιστώθηκε οτι ένας μεγάλος αριθμός απο τα γνωστά cli torrent search λογισμικά (torrench, we-get, rtorrent) έχει σταματήσει να αναπτύσσεται και να υποστηρίζεται απο τα τέλη περίπου του 2017, όπου δηλαδή η πληθώρα των torrent trackers μετέβη στο 'https'. Για τον λόγο αυτό, το κομμάτι της άσκησης που αφορά την αναζήτηση αρχείου δεν υλοποιήθηκε με κάποιο απο αυτα τα εργαλεία, αλλά με την χρήση python script.
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση  'terminaltables' packet απο πακέτο pip3. Χρειάζεται για την σωστή απεικόνιση των αποτελεσμάτων του παρακάτω script.
###### pip3 install terminaltables
##### δ) Δημιουργία python script με όνομα 'torrent_search', που θα εκτελείται απο κονσόλα, κάνει αναζήτηση σε torrent server και θα επιστρέφει τα αποτελέσματα στο τερματικό. Ο κώδικας προέρχεται απο αναζήτηση στον διαδίκτυο.
###### vi torrent_search 
###### (o κώδικας του αρχείου μπήκε σε ξεχωριστό αρχείο, για λόγους ομοιομορφίας. Το αρχείο είναι το torrent_search που βρίσκεται στον ίδιο φάκελο με το readme.md)
##### Για να μην χρειάζεται κάθε φορά να καλούμε το script μέσα απο το full path της python, δίνουμε το χαρακτηριστικό python στο script, προσθέτοντας στην πρώτη γραμμή του αρχείου το shebang:
###### #!/usr/bin/env python3
##### ε) Μετατροπή του αρχείου σε εκτελέσιμο. 
###### chmod +χ torrent_search
##### H σύνταξη για την εκτέλεση είναι:
###### ./torrent_search name
##### στ) Εγκατάσταση του cli torrent client "transmission "repository
###### sudo add-apt-repository ppa:transmissionbt/ppa 
##### Ενημέρωση των πακέτων αναζήτησης (στην ουσία προσθέτω το repository που μόλις έβαλα)
###### sudo apt-get update
##### εγκατάσταση των πακέτων που θα χρειαστω: transmission-cli, transmission-common, tranmission-daemon.
###### sudo apt-get install transmission-cli transmission-common tranmission-daemon
##### ζ) Σταματάω τον daemon και προσθέτω τον Ubuntu user μου (andreas) στους Authenticated χρήστες του Transmission. Στην συνέχεια ξαναξεκινώ τον daemon
###### sudo service transmission -daemon stop
###### sudo usermode -a -G debian-transmission andreas
###### sudo service transmission -daemon start
##### η) Κάνω την αναζήτησή μου (keyword="wind")
###### ./torrent_search wind
##### Επιλέγω  ένα απο τα αποτελέσματα, και παίρνω απο εκει το magnetic link. Στην συνέχεια το βάζω στον torrent client
###### transmission-remote -a "magnetic link"
##### και στην συνέχεια βλέπω οτι όντως προστέθηκε:
###### transmission-remote -l
##### Για να δείξουμε οτι τα παραπάνω δεν δουλεύουν μόνο για magnetic links, αλλά και για αρχεία torrents, εκτελούμε την ίδια εντολή και για ένα αρχείο .torrent που έχουμε κατεβάσει απο το διαδίκτυο.
###### transmission-remote -a ".torrent file"
##### Eπιβεβαίωση
###### transmission-remote -l
##### και τέλος μεταβαίνουμε στο download path και επιβεβαιώνουμε την ύπαρξη των των αρχείων:
###### cd /var/lib/transmission-daemon/downloads
###### ls 
#
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο παρακάτω link:
#### https://asciinema.org/a/277131 (still private)
#
#### link στο αποθετήριο του κώδικα:
#### https://github.com/p17kagk/mm/tree/master
#### link στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### https://github.com/p17kagk/mm/tree/P2017203
#### link στο εκτελέσιμο:
##### https://asciinema.org/a/277131
































