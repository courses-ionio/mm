# ΠΟΛΥΜΕΣΑ-MULTIMEDIA 

### First Assignment- Download mp3

Εργαλεία: 
          
          youtube-dl

          mpv player
          
          ffmpeg(for the convertion)
          
          asciinema
          
          terminal in Kali Linux(Virtual Box)
          
          
Για την πρώτη εργασία στο μάθημα "Πολυμέσα" του Ε' εξαμήνου χρησιμοποιήθηκαν τα παραπάνω εργαλεία για την αναζήτηση, το κατέβασμα και το παίξιμο ενός τραγουδιου.

Αρχικά με όπως φαίνεται και στο [λινκ](https://asciinema.org/a/Y48NlruYBUNCsIg3OtDeOHyDv) χρησιμοποιήθηκε η εντολή **PS1="P2017070-> "**
ετσι ώστε το command prompt να είναι ο ΑΜ μου.

Στη συνέχεια, χρησιμοποιείται η εντολή **youtube-dl ytsearch:(song-name)** για την αναζήτηση και κατέβασμα του επιθυμητού τραγουδιου απο το youtube.

Το αρχείο που δημιουργήθηκε, για να μετατραπεί σε μορφή .mp3 και να μπορεί να ακούγεται ο ήχος χρησιμοποιήθηκε η εντολή **ffmpeg -i "" mysong.mp3**

Tέλος για να ξεκινήσει το τραγούδι να "παίζει" χρησιμοποιήθηκε η εντολή **mpv mysong.mp3""

Βοηθητικα λινκς και ιστότοποι: https://asciinema.org/
                               Stackoverflow
                               https://ytdl-org.github.io/youtube-dl/index.html
                               https://www.ostechnix.com/hide-modify-usernamelocalhost-part-terminal/
                               Github
                               
[Link asciinema for the first assignment](https://asciinema.org/a/Y48NlruYBUNCsIg3OtDeOHyDv)                               
                               

## Συμμετοχικό Εκπαιδευτικό Υλικό

Για να επικοινωνήσω το περιεχόμενο του βιβλίου με τρόπο εκπαιδευτικό, ευχάριστο, χρησιμοποίηθηκε ως κοινωνικό μέσο το Twitter.

Ταυτόχρονα χρησιμοποιήθηκαν τα κατάλληλα tags, mention, giphy κ.α. για πιο ευχάριστο τρόπο επικοινωνίας με το κοινό. 
Το ύφος των δημοσιεύσεων είναι άμεσο και απεθύνεται στους χρήστες με τέτοιο τρόπο που να τους ωθεί στο να αναζητήσουν και οι ίδιοι το κάθε θέμα εκτενέστερα. Τα λινκ που οδηγούν στις δημοσιεύσεις είναι τα παρακάτω

[Λινκ για την ιστοσελιδα του βιβλιου/twitter](https://twitter.com/farmaki4/status/1192180854409367553)

[Λινκ για το Dynabook του Alan Kay/twitter](https://twitter.com/farmaki4/status/1192473400012353537)

[Λινκ για το Google Assistant/twitter](https://twitter.com/farmaki4/status/1193275189028642817)

[Λινκ για το home programming/twitter](https://twitter.com/farmaki4/status/1193277159378444289)

[Λινκ για το Aspen Movie Map/twitter](https://twitter.com/farmaki4/status/1193352436070731776)

[Λινκ για το Sword of Damocles/twitter](https://twitter.com/farmaki4/status/1193496946482335744)

[Λινκ Videoplace/twitter](https://twitter.com/farmaki4/status/1193507880089145344)

[Λινκ για wiki-edit](https://twitter.com/farmaki4/status/1193524594256338946)


### Second Assignment- Download a torrent

Εργαλεία: 
          
          links

          rtorrent
          
          asciinema 
         
         
Για το δεύτερο παραδοτέο τα βήματα που ακολούθησα ήταν τα εξής:

- asciinema rec --idle-time-limit=0.3 για την γρηγορότερη ροή του βίντεο

- PS1="P2017070-> " για να μετατρέψω το όνομα του prompt στο όνομα Α.Μ. 

- Εγκατάσταση της εντολής "links" με στόχο να αναζητήσω το λινκ μέσω command line. (apt-get install links)

- Εγκατάσταση της εντολής "rtorrent".

- Αναζήτηση μέσω του "links" στο site eztv.io, το οποίο περιλαμβάνει αρχεία torrent. (links eztv.io)

- Επιλογή του κατάλληλου λινκ μέσω των πλήκτρων. (Down, Up, Enter)

- Υλοποίηση της εντολής rtorrent

- Ctrl-D για διακοπή του download

- Ctrl-Q για έξοδο

[Link asciinema of Second assignment](https://asciinema.org/a/OMdqkJgfkkp0aFEdJN52VDS7p)

### Third Assignment- Youtube video streaming with asciiart

Εργαλεία: 

          ddgr
          
          mpv player
          
          libcaca
          
          asciinema
          
       
Για το τρίτο παραδοτέο τα βήματα που ακολούθησα ήταν τα εξής:

- Εγκατάσταση της μηχανής αναζήτησης "ddgr" με την εντολή "apt-get install ddgr".

- Εγκατάσταση της βιβλιοθήκης "libcaca" η οποία μετατρέπει τις εικόνες σε μορφή colored Asciiart μέσω της εντολής "apt-get --yes install caca-utils".

- Εγκατάσταση του mpv player για να παίξει το βίντεο.

- Εκτέλεση εντολής asciinema rec --idle-time-limit=0.3 για την γρηγορότερη ροή του βίντεο.

- PS1="P2017070-> " για να μετατρέψω το όνομα του prompt στο όνομα Α.Μ.

- Εκτέλεση εντολής "ddgr Sometimes james " για την αναζήτηση του τραγουδιού.

- c 1 για την αντιγραφή του επιθυμητού link

- DISPLAY= mpv --quiet -vo caca 'λινκ τραγουδιού'. Το DISPLAY χρησιμοποιείται ετσι ώστε το τραγούδι να μην ανοίξει σε παραθυρικό περιβάλλον αλλά στο ίδιο παράθυρο όπου εκτελούνται οι εντολές. Το caca χρησιμεύει στο να μην είναι ασπρομαυρο το περιβάλλον.

- q για έξοδο από το περιβάλλον ascii

- exit για εξοδο απο asciinema rec.

[Link asciinema for the third assignment](https://asciinema.org/a/pQHmZaSY0yHWkYKv9F2lUkCdw)

Παρατήρηση! Η εργασία μπορεί να δεχτεί διορθώσεις όσο αναφορά την ποιότητα και την εμφάνιση του βίντεο σε ascii , ώστε να φαίνεται πιο καθαρά.


### Fourth Assignment- Edit a Spreadsheet





