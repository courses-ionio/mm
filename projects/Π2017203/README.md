# Μάθημα: Πολυμέσα
#
## Προσωπικά Στοιχεία:
#### A.M.: Π2017203
#### Όνομα: Ανδρέας
#### Επώνυμο: Καγκελάρης
#
## Άσκηση 1
#### Τίτλος: download mp3 
#### Ζητούμενα: 
#### 1) search, download and play (with the terminal) your favorite song of the month from youtube
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση του S/W 'youtube-dl' ώστε να κάνουμε download το επιθυμητό link με την χρήση terminal. Η εγκατάσταση του πακέτου έγινε απο την σελίδα του δημιουργού και όχι απο τον Ubuntu server, λόγω γνωστού προβλήματος στην έκδοση του Ubuntu Server https://github.com/ytdl-org/youtube-dl/issues/21952. 
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
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/275789) 
#
#### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
#### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### [link](https://asciinema.org/a/275789) στο εκτελέσιμο:
#
## Άσκηση 2
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
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/277131 )
#
#### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
#### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### [link](https://asciinema.org/a/277131) στο εκτελέσιμο:
#
## Συμμετοχικό εκπαιδευτικό υλικό - 1
#
#### [Link](https://mibook.org/gr/) του mibook.org
#### [Link](https://github.com/p17kagk/gr) του προσωπικού αποθετηρίου του βιβλίου
#
#### Αναρτήσεις του περιεχομένου του mibook.org/gr/ με τρόπο εκπαιδευτικό και ευχάριστο! 
#### Για τις αναρτήσεις έγινε χρήση των κοινωνικών δικτύων facebook και tweeter.
#
#### [Ανάρτηση 1](https://www.facebook.com/andreas.kagkelaris/posts/10156381743652414)
#### [Ανάρτηση 2](https://www.facebook.com/andreas.kagkelaris/videos/10156381702157414/)
#### [Ανάρτηση 3](https://www.facebook.com/andreas.kagkelaris/videos/10156381718967414/)
#### [Ανάρτηση 4](https://www.facebook.com/andreas.kagkelaris/videos/10156381756957414/)
#### [Ανάρτηση 5](https://www.facebook.com/andreas.kagkelaris/videos/10156381726337414/)
#### [Ανάρτηση 6](https://twitter.com/kagelaris3/status/1192932196157468673)
#### [Ανάρτηση 7](https://twitter.com/kagelaris3/status/1192930702200889344)
#### [Ανάρτηση 8](https://twitter.com/kagelaris3/status/1192929617251840005)
#### [Ανάρτηση 9](https://twitter.com/kagelaris3/status/1192928238240194563)
#### [Ανάρτηση 10](https://twitter.com/kagelaris3/status/1192927744604196864)
#### [Ανάρτηση 11](https://twitter.com/kagelaris3/status/1192925222904705026)
#
## Άσκηση 3
#### Τίτλος: edit a spreadsheet
#### Ζητούμενα: 
#### 1) edit values and formulas
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση του S/W 'sc' ώστε να επεξεργαστούμε ένα spreadsheed. 
###### sudo apt install sc
##### δ) Εκκίνηση του επεξεργαστή 'sc'. Πραγματοποιήθηκαν οι παρακάτω λειτουργίες:
###### hjkl — keys motion
###### gX00 - go to cell
###### ir — insert row
###### dr — delete row
###### = — enter a numeric value
###### = (@sum(A2:A145)) enter a formula
###### e — edit a numeric value
###### e — edit a formula
###### P<ΜΜ.sc> — write an .sc file
###### q=quite
#
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/281721)
#
#### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
#### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### [link](https://asciinema.org/a/281721) στο εκτελέσιμο:
#
## Άσκηση 4
#### Τίτλος: watch video
#### Ζητούμενα: youtube video streaming with asciiart
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση του S/W 'youtube-dl' ώστε να κάνουμε download το επιθυμητό link με την χρήση terminal. Η εγκατάσταση του πακέτου έγινε απο την σελίδα του δημιουργού και όχι απο τον Ubuntu server, λόγω γνωστού προβλήματος στην έκδοση του Ubuntu Server https://github.com/ytdl-org/youtube-dl/issues/21952. 
###### sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
###### sudo chmod a+rx /usr/local/bin/youtube-dl
##### δ) Εγκατάσταση των βιβλιοθηκών [link](https://launchpad.net/ubuntu/+source/libcaca)'libcaca' και [link](https://launchpad.net/ubuntu/+source/aalib)'AAlib'. Η βιβλιοθήκη AAlib μετατρέπει την έξοδο του σήματος που δέχεται απο pixels σε ασπρόμαυρους ASCII χαρακτήρες. Αντίστοιχα, η βιβλιοθήκη libcaca μετατρέπει την έξοδο του σήματος που δέχεται απο pixels σε έγχρωμους ASCII χαρακτήρες. Και οι 2 βιβλιοθήκες εγκαταστάθηκαν κάνοντας build και install στο τερματικό μας:
###### ./configure && make && sudo make install
##### ε) Εκτέλεση της εντολής: 
###### mplayer -vo aa -cookies -cookies-file /tmp/cookie.txt $(youtube-dl -g -f best --cookies /tmp/cookie.txt "https://www.youtube.com/watch?v=EKkzbbLYPuI") 
##### όπου:
###### mplayer: o player που χρησιμοποιούμε
###### -vo: για να οδηγήσουμε την έξοδο σε περιβάλλον X11 (παράθυρο)
###### aa: για να μετατρέψουμε τα pixels σε ASCII χαρακτήρες.
###### -cookies -cookies-file /tmp/cookie.txt: για να δηλώσουμε οτι θα χρησιμοποιήσουμε cookies (απαραίτητα για την λειτουργία του youtube). τα οποία και θα βρίσκονται στο δηλωθέν path.
###### $(youtube-dl): η είσοδος του mplayer θα είναι η έξοδος απο την εκτέλεση του youtube-dl
###### youtube-dl -g: για να κανουμε real time streaming και όχι download.
###### -f best: επιλέγουμε βέλτιστη ανάλυση
###### --cookies /tmp/cookie.txt: χρήση cookies
###### "https://www.youtube.com/watch?v=EKkzbbLYPuI": το url μας.
#
#### Αντίστοιχα, για να έχουμε το ίδιο αποτέλεσμα με έγχρωμους ASCII χαρακτήρες, η εντολή που εκτελέσαμε ήταν: 
###### mplayer -vo caca -cookies -cookies-file /tmp/cookie.txt $(youtube-dl -g -f best --cookies /tmp/cookie.txt "https://www.youtube.com/watch?v=EKkzbbLYPuI") 
##### όπου αντικαθιστώντας στην παραπάνω εντολή το "aa" με "caca" πετυχαίνουμε τον χρωματισμό των ASCII χαρακτήρων
#### όλα τα παραπάνω βήματα φαίνονται αναλυτικά στο [link](https://asciinema.org/a/291335)
#
#### [link](https://github.com/p17kagk/mm/tree/master) στο αποθετήριο του κώδικα:
#### [link](https://github.com/p17kagk/mm/tree/P2017203) στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### [link](https://asciinema.org/a/291335) στο εκτελέσιμο:
#
































