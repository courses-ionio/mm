
# Multimedia

  ## Αναφορά:

Όνομα: Πολίτης Αλέξανδρος
AM: Π2017202


  ## Άσκηση 1 Multimedia
   ## Search, Download and Play mp3
   ### Youtube-dl
   
   Στην πρώτη εργασία σκοπός είναι η εύρεση, αποθήκευση και αναπαραγωγή ενός τραγουδιού.
   
   
   Για τον σκοπό αυτό εγκαταστάθηκε το [youtube-dl](https://github.com/ytdl-org/youtube-dl") για την εύρεση και την αποθήκευση του τραγουδιού.
   
   
   Επίσης έγινε εγκατάσταση και του [ffmpeg](https://www.ffmpeg.org/) ώστε να γίνει εξαγωγή ο ήχος απο το αρχείο " .mkv" σε αρχείο " .mp3"
   Tέλος με το [mkv player](https://github.com/mpv-player/mpv) έγινε η αναπαραγωγή του αρχείου του τραγουδιού " .mp3".
   
   Me το asciinema καταγράφηκε μια επιτυχημένη
   * Aναζήτηση
   * Aποθήκευση
   * Εξαγωγή ήχου
   * Αναπαραγωγή
  
   
   [Link asciinema](https://asciinema.org/a/8haJ9uf622aphIyZLqHqeCIMF)
   
   ### MPS-youtube
  Ένα ακόμα εργαλείο που μπορεί να χρησιμοποιηθεί αντί του youtube-dl είναι το [mps-youtube](https://github.com/mps-youtube/mps-youtube).
  Με το εργαλείο αυτό γίνεται αναζήτηση και εμφανίζει λίστα με τα διαθέσιμα προς αναπαραγωγή ή αποθήκευση τραγούδια.
  
  
  [Link asciinema](https://asciinema.org/a/zo5gxZeH9cT3VkpLMAaQhCbuo) 




  ## Άσκηση 2 Multimedia
   ## Download a torrent
   ### Transmission
   
   Στην δεύτερη εργασία γίνεται download ενός αρχείου **torrent**.
   
   
   Για τον σκοπό αυτό εγκαταστάθηκε το [Transmission](https://wiki.archlinux.org/index.php/Transmission) το οποίο είναι ενα ελαφρύ *cross-platform BitTorrent Client*.
   
   ### Torque 
    
   To [Torque](https://github.com/dylanaraps/torque) είναι TUI client που μας επιτρέπει την καλύτερη οπτική απεικόνιση των αρχείων που κάνουμε download (με χρήση του Transmission). Επίσης δίνει την επιλογή μέσω του δικού του interface να γίνει προσθήκη, διαγραφή, έναρξη, παύση των .torrent αρχείων.
   
   Το αρχείο asciinema που δίχνει την επιτυχημένη καταγραφή της χρήσης Transmission-Torque
   [Link asciinema](https://asciinema.org/a/9t9iMk6tFcMpkZ0tcy5uOyC1D).
  
  ### we-get
  
  Με το [we-get](https://github.com/rachmadaniHaryono/we-get) δίνεται η δυνατότητα για εύρεση .torrent links σε διάφορα site. Καθώς υπάρχει μια πολιτική προστασίας της εκάστοτε χώρας για την προστασία απο κάποια site διακίνησης .torrent η εμφάνιση των links διαφέρει.
  
  Όπως μπορούμε να δούμε γίνεται αναζήτηση μέσω [we-get](#we-get) και χρήση του link στο [Transmission](#Transmission) για να γίνει download.
  
  [Link asciinema](https://asciinema.org/a/EkzTDiStqqrRM1AUuE7I5qW9g)
  
### Aria2

 Ένα πολύ χρήσιμο *multi-protocol & multi-source command-line download utility* είναι το [Aria2](https://aria2.github.io/) το οποίο υποστηρίζει και BitTorrent.Στο αρχείο asciinema που ακολουθεί γίνεται εύρεση Link με το [we-get](#we-get) και download με το [Aria2](#Aria2)
 
 [Link asciinema](https://asciinema.org/a/vc8YqIqCLQBaF6lC6Zmpz7DgH)
 
 
## Συμμετοχικό Υλικό

[Link αντιγράφου αποθετηρίου](https://github.com/AlexandrosP38/gr)

   Μέρος της εργασίας στα Multimedia είναι η χρήση ενός κοινωνικού δικτύου για παρουσίαση του βιβλίου ["O Προγραμματισμός της Διάδρασης"](https://mibook.org/gr/)
   
   Για τον σκοπό αυτό χρησιμοποιήθηκε το Twitter.
   
   [Link Tweet#1](https://twitter.com/38Alexandros/status/1192544391740702720)
   
   [Link Tweet#2](https://twitter.com/38Alexandros/status/1192555364602040320)
   
   [Link Tweet#3](https://twitter.com/38Alexandros/status/1192558765591187456)
   
   [Link Tweet#4](https://twitter.com/38Alexandros/status/1192585188053786624)
   
   [Link Tweet#5](https://twitter.com/38Alexandros/status/1192586315923111936)
   
   [Link Tweet#6](https://twitter.com/38Alexandros/status/1192587782000201729)
   
   [Link Tweet#7](https://twitter.com/38Alexandros/status/1192588428145287168)
   
   [Link Tweet#8](https://twitter.com/38Alexandros/status/1192588998319001602)
   
   [Link Tweet#9](https://twitter.com/38Alexandros/status/1215747741239906306)
   
   [Link Tweet#10](https://twitter.com/38Alexandros/status/1215748473657667584)
   
   
   ## Άσκηση 3 Multimedia
   ## Create a simple website with a static generator
   ### Requirements
   
   Στόχος της εργασίας είναι με χρήση του Jekyll και του πακέτου εργαλείων του να δημιουργήσουμε ένα στατικό website.
   Κάνουμε εγκατάσταση των Ruby,RubyGems,GCC και Make
   >sudo apt-get install ruby-full build-essential
   
   >gem install jekyll bundler
   
   >jekyll new politisalexandros-P2017202-github
   
   ### Jekyll
   
   Στη συνέχεια δημιουργούμε τον χώρο στον υπολογιστή που περιέχει τα αρχεία του site μας
   
   >bundle exec jekyll build
    
   Τώρα ανοίγουμε τον server που πλέον δείχνει το site μας μέσα στον browser (http://localhost:4000)
   
   >jekyll serve
    
   Στο main directory (και οχι στο "sites") δημιουργούμε το αρχείο index.html. Το επεξεργαζόμαστε όπως θέλουμε και το Jekyll κάνει αυτόματα update την σελιδα.Οι αλλαγές που γίνονται φαίνονται και στο terminal log
   ![Site Up](https://imgur.com/LO4oruG.png)
   
   [Creating and using Jekyll](https://asciinema.org/a/yRdogWHplhe2eRNM5FvYpmhOf)
   
   [Editing index.html](https://asciinema.org/a/908ma2e88UxrxVa3cTSpDAwRV)
   
   ## Άσκηση 4 Multimedia
   ## Visualize a large text file with a word cloud
   ### Requirements
   
   Το Word Cloud επιτρέπει στον χρήστη να οπτικοποιήσει κείμενο δημιουργώντας εικόνες απο text.
   Για τον σκοπό αυτό εγκαθιστούμε το wordcloud.py 
   
   >pip install wordcloud
   
   Επίσης θα χρησιμοποίησουμε και το curl ώστε να κατεβάσουμε ένα δωρεάν βιβλίο απο το [Project Gutenberg](https://www.gutenberg.org/)
   
   ### Word Cloud
   
   To βιβλίο που επιλέξαμε για την εργασία είναι το [The Adventures of Sherlock Holmes](https://www.gutenberg.org/files/1661/1661-0.txt) του Arthur Conan Doyle με τον γνωστό ντετέκτιβ.
   
   Κατεβάζουμε το βιβλίο σε μορφή .txt (το Project Gutenberg παρέχει τα βιβλία νόμιμα και δωρεάν) 
   >curl https://www.gutenberg.org/files/1661/1661-0.txt --output SherlockBook.txt
   
   Στη συνέχεια κάνουμε mask το περιεχόμενο του βιβλίου χρησιμοποιώντας το [Word Cloud](http://amueller.github.io/word_cloud/auto_examples/index.html)
   
   >wordcloud_cli --text wordcloud.txt --imagefile cover.jpg --mask sherlock.jpg

  To αποτέλεσμα εμφανίζεται παρακάτω ![Link to image](https://imgur.com/VZxyste.png)

   
   
   
