## Παραδοτέο 2
#### Τίτλος: download a torrent
#
#### Για την εκπόνηση της άσκησης, ακολουθήσαμε τα εξής βήματα:
##### α) Εγκατάσταση του S/W 'asciinema', ώστε να γίνει καταγραφή του terminal (χρήση flag -i=0.2 για την αποφυγή καταγραφής κενών διαστημάτων). Για την σκοπό της άσκησης δημιουργήσαμε και λογαριασμό στο www.asciinema.org
###### sudo apt-get install asciinema
##### β) Τροποποίηση του .bashrc, ώστε το bash prompt να δείχνει τον Α.Μ. μας.
###### vi .bashrc
##### γ) Εγκατάσταση  'terminaltables' packet απο πακέτο pip3. Χρειάζεται για την σωστή εκτέλεση του παρακάτω script.
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
#### 
#
#### link στο αποθετήριο του κώδικα:
#### 
#### link στο κλαδί του κώδικα που αντιστοιχεί στο κάθε παραδοτέο:
#### 
#### link στο εκτελέσιμο:

















