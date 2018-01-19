# Pacman - MM Project 2017-2018

Όνομα: **Ξυπολιτόπουλος Κωνσταντίνος**

ΑΜ: **Π2014116**

[Github Pages Αναφοράς](https://constantinexipol.github.io/mm/)

[Fork του αποθετηρίου του παιχνιδιού](https://github.com/ConstantineXipol/pacman)

[Εδώ τρέχει το παιχνίδι](https://constantinexipol.github.io/pacman)

# Τελική Αναφορά - Συμπεράσματα

Το παρόν github page αποτελεί την τελική αναφορά της εργασίας εξαμήνου του μαθήματος Πολυμέσα με θέμα "Pacman".
Εκπόνηθηκε από τον Κωνσταντίνο Ξυπολιτόπουλο με αριθμό μητρώου Π2014116 για το χειμερινό εξάμηνο του ακαδημαικού έτους 2017-2018.
Η εργασία έχει να κάνει με την αλλαγή και επέκταση ενος παιχνίδιου κλόνου του κλασσικού Pacman. Η διαδικασία της εργασίας εξαμήνου ακολούθησε την πορεία 4 παραδοτέων: αρχικά την δήλωση θέματος, έπειτα την δημιουργία καινούργιας πίστας για το παιχνίδι, την πρόσθεση μουσικής και μουσικών εφέ, αλλαγή του sprite του χαρακτήρα, προσθήκη φόντου, και τα λοιπά. 
Η πίστα δημιουργήθηκε χρησιμοποιόντας το εργαλέιο ανοιχτού κώδικα "Tiled", το οποίο είναι διάσημο στον χώρο των 2D και ισομετρικών (isometric 2D) κύκλων από ερασιτέχνες game devs.
Το παιχνίδι είναι χτίσμένο πάνω στην βιβλιοθήκη "Phaser" που είναι φτιαγμένη για native HTML5 παιχνίδια που τρέχουν σε φυλλομετρητές.

Μέσω της φετινής εργασίας έμαθα να δουλέυω καλήτερα το github, κατάλαβα την λειτουργεία της βιβλιοθήκης HTML5 Phaser και το πως τρέχουν εφαρμογές από τοπικούς server (xampp).

## Παραδοτεο 1
Δήλωση θέματος εργασίας: Pacman

Έχει γίνει fork του αποθετηρίου του παιχνιδιού και έγιναν οι αλλαγές που χρειάζονται για να τρέχει απο το προσωπικό αποθετήριο μου μεσω github pages.

[Fork του αποθετηρίου του παιχνιδιού:](https://github.com/ConstantineXipol/pacman)

[Εδώ τρέχει το παιχνίδι:](https://constantinexipol.github.io/pacman)

## Παραδοτεο 2

Ο χαρακτήρας του pacman έχει αλλαχτεί με τον αιώνιο αντιπαλό του, το κόκκινο φάντασμα.
![Screenshot](https://i.imgur.com/43EqTCv.png)

Το κόκκινο φάντασμα έχει και ένα random animation στο στόμα του που έφτιαξα μέσω του gimp, όταν παίζεις το παιχνίδι φαίνεται πολύ καλήτερο από ότι στις εικόνες.
![Screenshot](https://i.imgur.com/hsnZiVe.png)

Οι κλασσικές "βουλίτσες" που τρώει ο pacman έχουν αλλάξει τώρα και είναι οι μακρινοί συγγενείς του pacman.

![Screenshot](https://i.imgur.com/NQIcwjZ.png)

Εχουν προσθεθεί επίσης "bonus" στις 4 άκρες του χάρτη όπως το κλασσικό pacman. Τρωγοντάς τα δίνουν ένα μπόνους 15 βαθμών. Τα 4 bonus επαναφέρονται μονο μαζί με ολες τις άλλες βουλίτσες όταν φαγωθούν όλες από τον παίχτη. 

![Screenshot](https://i.imgur.com/q3RoU5t.png)

Δημιούργησα μια καινούργια πίστα χρησιμοποιώντας το Tiled, βασισμένος στην κλασσική του pacman, αλλα με διάφορες αλλαγές και προσαρμογές του layout προσπαθώντας να κρατήσω όμοια την αρχική όψη και αίσθηση της κλασσικής πίστας.

![Screenshot](https://i.imgur.com/DjnSCtU.png?1)

Δυστυχώς δεν μπόρεσα να χρησιμοποιήσω ενα διαφορετικό "RPG" tileset που έφτιαξα σε χάρτη που ήθελα λόγο του ότι δεν μπορούσα να το κάνω να δουλέψει με το phaser με τίποτα, αλλά εδώ είναι το αποτέλεσμα της προσπάθειας στο tiled μέσα.

![Screenshot](https://i.imgur.com/Pgx8IlF.png)

Επίσης έχει προστεθεί ένα φόντο πίσω από το frame του παιχνιδιού για καλήτερη αισθητική.

![Screenshot](https://i.imgur.com/h5hzMep.png)

Υπάρχουν τώρα μετρητές για το σκόρ, bonus σκόρ, ζωές, και χρόνος παιχνιδιού κάτω απο τήν πίστα:

![Screenshot](https://i.imgur.com/j4ip6fV.png)

Τελικά προσέθεσα ήχο όταν ο χαρακτήρας τρώει τους πόντους, διαφορετικό ήχο για οταν τρώει τα bonus, και ένα τραγούδι chiptune που παίζει σε loop σαν μουσικό θέμα του παιχνιδιού.

## Παραδοτέο 4 - Τελική Αναφορά

Έχει προτεθεί πίστα στο κεντρικό αποθετήριο του παιχνιδιού branch: gh-pages και στο φάκελο: extensions. 
Link του pull request: https://github.com/ioniodi/pacman/pull/52

Quote από το FAQ του μαθήματος *"Η τελική αναφορά μπορεί να αποτελείται από τα διορθωμένα προηγούμενα παραδοτέα με όσες αλλαγές έγιναν και την προσθήκη τίτλου, σύνοψης, συμπερασμάτων, και αναφορές σε σχετικές-παρόμοιες εργασίες."*

Έγινε ένα γενικό "streamline" των παραδοτέων μέχρι τώρα, ξεκαθαρίστηκαν κάποιες προτάσεις και προστέθηκαν ενδεικτικές εικόνες. Παραπάνω δουλεία στον κώδικα του 4ου παραδοτέου δεν θα γινει, αυτό το readme/github page είναι η τελική αναφορά της εργασίας.