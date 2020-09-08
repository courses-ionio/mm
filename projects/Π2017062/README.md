# ΜΑΘΗΜΑ: ΠΟΛΥΜΕΣΑ

### ΥΠΕΥΘΥΝΟΣ ΚΑΘΗΓΗΤΗΣ: Κ. ΧΩΡΙΑΝΟΠΟΥΛΟΣ
### ΕΞΑΜΗΝΟ ΦΟΙΤΗΣΗΣ: Ε'
### ΟΝΟΜΑΤΕΠΩΝΥΜΟ: ΛΑΣΟΠΟΥΛΟΥ ΒΑΛΕΡΙΑ
### ΑΜ: Π2017Ο62
#
#
## ΑΣΚΗΣΗ 1
### Τίτλος: Download mp3
#
#### 1ος Τρόπος
  Στην συγκεκριμένη άσκηση κληθήκαμε να ψάξουμε, να κατεβάσουμε καθώς και να αναπαράξουμε ένα αρχείο mp3 από το YouTube. Τα βήματα 
 που ακολούθησα για την πραγματοποήση της είναι τα εξής:
 
   1) Λήψη του terminal session recorder Asciinema, το οποίο μας επιτρέπει με την πληκτρολόγηση των κατάλληλων εντολών στον 
   τερματικό του Ubuntu, να δούμε τις εντολές που χρειάζονται για να ολοκληρωθεί η άσκηση σε μορφή βίντεο. Δημιουργία λογαριασμού
   στην ομώνυμη ιστοσελίδα.
       - sudo apt-get install asciinema
   2) Λήψη του MPS-youtube το οποίο αναπαράγει, ψάχνει και κατεβάζει βίντεο καθώς και ηχητικά κλιπ από το YouTube. Για την ορθή λειτουργία του χρειάζονται τα εξής βήματα:
       - sudo apt-get update ,ώστε να αναβαθμίσουμε το target system
       - Εγκατάσταση του ίδιου του πακέτου MPS-youtube με την εντολή: sudo apt-get install mps-youtube
       - Εγκατάσταση του πακέτου Mplayer (πάνω στο οποίο βασίστηκε το mpv) με την εντολή: sudo apt-get mplayer
 Για την ορθή λειτουργία του πακέτου αυτού είναι απαραίτητο να προσθέσουμε το ~/.local/bin στο PATH.
   3) Λήψη του εργαλείου ffmpeg για την μετατροπή των βίντεο απο m4a σε mp3.
       - sudo apt-get install ffmpeg
   4) Λήψη του media player mpv με τη βοήθεια του οποίου θα μπορέσουμε να ακούσουμε τα τραγούδια που κατεβάσαμε και μετατρέψαμε σε mp3.
       - sudo apt-get install mpv
    
  ##### Link βίντεο στο οποίο απεικονίζεται το play, search και download: https://asciinema.org/a/MDkQybmvnmriQ9EYbygxQuwFE
 
 
  #### 2ος Τρόπος 
  
   1) Εγκαθιστούμε τη μηχανη αναζήτησης DuckDuckGo στο τερματικό μας και στην συνέχεια πληκτρολογούμε το όνομα του τραγουδιού που θέλουμε στην συνέχεια να κατεβάσουμε:
   
     - sudo add-apt-repository ppa:twodopeshaggy/jarun
     - sudo apt-get update
     - sudo apt-get install ddgr
     - ddgr name_of_the_song
        
   2) Αντιγράφουμε το link που μας ενδιαφέρει με την εντολή c number_of_link.
   3)Εγκαθιστούμε και χρησιμοποιούμε την τερματική εφαρμογή youtube-dl ώστε να κατεβάσουμε το τραγούδι που επιλέξαμε σε μορφή mp3.
   
     - sudo apt-get youtube-dl
     - youtube-dl --extract-audio --audio-format mp3 link_of_choice
        
   4) Με την εφαρμογή mpv ακούμε το τραγούδι που μόλις κατεβάσαμε.
   
   ##### Αναλυτικά τα βήματα παρουσιάζονται στο link: https://asciinema.org/a/kveqsjaNXUzlm3dQoNJKcSve6
   #
   ##### Links που βοήθησαν στην επίλυση της άσκησης:
         - https://ytdl-org.github.io/youtube-dl/download.html
         - https://github.com/ytdl-org/youtube-dl
         - https://github.com/mps-youtube/mps-youtube
         - https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats
         - https://launchpad.net/~mc3man/+archive/ubuntu/mpv-tests
         - http://tipsonubuntu.com/2018/07/27/install-mpv-0-29-ubuntu-18-04-lts/
   
## ΑΣΚΗΣΗ 2
### Τίτλος: Visualize an mp3
   
 Για την υλοποίηση του συγκεκριμένου ζητήματος επέλεξα να χρησιμοποιήσω το ncmpcpp που είναι client του Music Player Deamon (MPD). Για
 να επιτύχω την εγκατάσταση και την ορθή λειτουργία του ακολούθησα τα εξής βήματα:
 
  1) Εγκατάσταση των MPD, ncmpcpp και MPC (client πρόγραμμα που μπορεί να ελέγχει τον MPD).
          - sudo apt-get install mpd mpc ncmpcpp
  2) Για να δούμε τι χρειάζεται για το configuration του mpd ανοίγουμε το file mpd.conf που βρίσκεται στο directory /etc. Στην συνέχεια ελέγχουμε αν η εγκατάσταση του προγράμματος δημιούργησε τους αναγκαίους φακέλους στους σωστούς καταλόγους. Στη δική μου περίπτωση έπρεπε να προσθέσω τον φάκελο mpdstate στο var/lib/mpd καθώς και να αλλάξω το όνομα του music directory σε αυτό που υπήρχε στο δικό μου υπολογιστή. Έπειτα δημιουργούμε directories τα οποία χρειάζεται το MPD ώστε να τρέξει σωστά, ένα default configurations directory  και ένα playlist directory. 
  
          - mkdir -p ~/.mpd/playlists/
          - nano ~/.mpd/mpd.conf
          
 Στο mpd file που δημιουργήσαμε μέσα στο mpd προσθέτουμε το παρακάτω:
 
         bind_to_address "127.0.0.1"
         #bind_to_address "~/.mpd/socket"
         music_directory "~/Music"
         playlist_directory "~/.mpd/playlists"   
         db_file      "~/.mpd/mpd.db"  
         log_file      "~/.mpd/mpd.log"  
         pid_file      "~/.mpd/mpd.pid"  
         state_file     "~/.mpd/mpdstate"  
         
         audio_output {
         type             "alsa"
         name            "Alsa for audio sound card"
         mixer_type      "software"      # optional }

         audio_output {
             type                    "fifo"
             name                    "my_fifo"
             path                    "/tmp/mpd.fifo"
             format                  "44100:16:2 }
             
  3) Για το configuration του ncmpcpp χρειάστηκε να δημιουργήσουμε ένα lyrics directory καθώς και ένα ncmpcpp config file όπως και προηγουμένως με το mpd.
  
          - mkdir -p ~/.ncmcpp/lyrics
          - nano ~/.ncmpcpp/config
          
 Στο config file που δημιουργήσαμε μέσα στο directory ncmpcpp προσθέτουμε:
        
        mpd_music_dir = "~/Music"  
        lyrics_directory  = ~/.ncmpcpp/lyrics
        ncmpcpp_directory  = ~/.ncmpcpp
        mpd_host = "localhost"
        mpd_port = "6600"  
        visualizer_fifo_path = "/tmp/mpd.fifo"
        visualizer_output_name = "my_fifo"
        visualizer_in_stereo = yes
        visualizer_sync_interval = 10
        visualizer_type = wave_filled
        visualizer_look = +|
   
   4) Πληκτρολογούμε ncmpcpp στον τερματικό για να "ανοίξουμε¨ την εφαρμογή και στην συνέχεια πατάμε "u" για συγχρονισμό ώστε το ncmpcpp να προσθέσει τα τραγούδια που έχουμε αποθηκευμένα στον φάκελο της μουσικής μας στη βάση δεδομένων του. Πατώντας τα αριθμημένα κουμπιά στο πάνω μέρος του πληκτρολογίου μας μεταφερόμαστε στις διάφορες σελίδες με διαφορετικές επιλογές που προσφέρει το ncmpcpp. Για να δούμε τον Music Visualizer πιέζουμε τον αριθμό "8¨.
  
  
Αντιμετώπισα κάποια προβλήματα με τη λειτουργία του Visualizer σε αυτήν την άσκηση η λύση των οποίων είχε να κάνει κυρίως με την ενεργοποίηση του mpd, καθώς και ορισμένες επιπλέον τροποποιήσεις σε φακέλους όπως πρότειναν ορισμένα από τα άρθρα που περιέχονται στα links που αναφέρονται παρακάτω.

  ##### To Visualization φαίνεται στο link: https://asciinema.org/a/CcS4E199RQ3JV4zHELfkDsk43
  #
  ##### Links που βοήθησαν στην επίλυση της άσκησης: 
   
         - https://wiki.archlinux.org/index.php/Music_Player_Daemon#Setup
         - https://wiki.archlinux.org/index.php/Music_Player_Daemon/Troubleshooting
         - https://computingforgeeks.com/how-to-configure-mpd-and-ncmpcpp-on-linux/
         - https://www.reddit.com/r/linuxquestions/comments/anlfi5/ncmpcpp_visualizer_not_working_configured_as_per/
         - https://wiki.archlinux.org/index.php/ncmpcpp
         - https://www.musicpd.org/doc/html/user.html
   
   
## ΑΣΚΗΣΗ 3
### Τίτλος: Manage torrent files

  Για την επίλυση αυτής της άσκησης επέλεξα να εγκαταστήσω τον BitTorrent client [Transmission-Cli](https://cli-ck.io/transmission-cli-user-guide/). Μιας και η άσκηση ζητούσε αναζήτηση και εγκατάσταση torrent file, προσπάθησα να κάνω το search μέσω του τερματικού εγκαθιστώντας το [Googler](https://github.com/jarun/googler) ωστόσο τόσο αυτό όσο και το ddgr που έχω αναφέρει παραπάνω δεν εμφάνιζαν αποτελέσματα, οπότε προχώρησα με την μηχανή αναζήτησης που χρησιμοποιώ σε καθημερινή βάση για να βρω το torrent site και να αντιγράψω τον σύνδεσμο των torrent αρχείων που επιθυμούσα να κατεβάσω. Το Transmission-cli μας παρέχει επίσης ένα web interface στο οποίο μπορούμε να παρακολουθήσουμε την πορεία των αρχείων που κατεβάζουμε.  Σε αυτό μπορούμε να σταματήσουμε και να ξεκινήσουμε τη διαδικασία του κατεβάσματος και να κάνουμε εν ολίγοις ότι θα μπορούσαμε να κάνουμε χρησιμοποιώντας τη γραμμή εντολών.
  
  ![alt text](https://github.com/p17laso/mm/blob/%CE%A02017062/projects/%CE%A02017062/torrentdownload.png)

  
 ##### Αναλυτικά τα βήματα παρουσιάζονται στο link: https://asciinema.org/a/o1Xg88k1cRTEjc1uaCcjUrioJ
 ##### Links που βοήθησαν στην επίλυση της άσκησης: 
 
          - https://www.youtube.com/watch?v=NVOLRXFhczU
          - https://www.youtube.com/watch?v=spqTxmr3NHM
          - https://www.youtube.com/watch?v=ee4XzWuapsE&t=16s
          - https://www.omgubuntu.co.uk/2017/08/search-google-from-the-command-line]
          
          
## ΑΣΚΗΣΗ 4
### Τίτλος: Create your own static site and blog generator


Για τη δημιουργία στατικού site επέλεξα να χρησιμοποιήσω το Static Site Generator [Ηugo](https://gohugo.io/getting-started/quick-start/). Για την επίλυση συτής της άσκησης μια επίσης καλή επιλογή είναι η χρήση του Jekyll ωστόσο το Hugo μου φάνηκε γρηγορότερο και ευκολότερο στη χρήση.

Για να χρησιμοποιήσουμε το Hugo θα πρέπει να εγκαταστήσουμε το Homebrew package manager. Για την εγκατάσταση του:

1. Αντιγράφουμε στο τερματικό την εξής εντολή:
```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
``` 
2. Μόλις ολοκληρωθεί η εγκατάσταση πληκτρολογούμε τις εξής εντολές αφού πρώτα τις έχουμε διαμορφώσει για τα ταιριάζουν στο λειτουργικό σύστημα που χρησιμοποιούμε. Στη δική μου περίπτωση δουλεύω με Ubuntu οπότε οι εντολές γίνονται:

```
    test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
    test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
    test -r ~/.profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
    echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
```
Με τη χρήση του Ηugo δημιούργησα μια στατική σελίδα στην οποία πρόσθεσα δημοσιεύσεις και θέμα της αρεσκείας μου. Tο θέμα που επέλεξα είχε πολλα features τα οποία επέτρεπαν εύκολη εισαγωγή εικόνων στην σελίδα μου καθώς και την αυτόματη μετάβαση στους προσωπικούς μου λογαριασμούς σε μέσα κοινωνικής δικτύωσης (FaceBook, Twitter, Github). Οι μετατροπές που χρειάστηκε να κάνω για να φτάσω στο τελικό αποτέλεσμα φαίνονται στον παρακάτω σύνδεσμο.

#### Asciinema link:

[Create your own static site and blog generator](https://asciinema.org/a/Uz3pi0Z2G6x0Nllc1A4fBk4MK)

### Απεικόνιση σελίδας

1. Μετά την εισαγωγή θέματος χωρίς ωστόσο να έχει γίνει καμία αλλαγή στο default config.toml του.

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/static-site-before.png)

2. Μετά τις μετατροπές που υπέστη τόσο το config.toml όσο και το layouts για να προσαρμοστεί το θέμα στις προτιμήσεις του χρήστη. Επιπρόσθετα έχουν προστεθεί και 2 δημοσιεύσεις.

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/static-site-final.png)

![alt text](https://github.com/p17laso/sw/blob/2017062/P2017062/static-site-final2.png)

[Σύνδεσμος με πληροφορίες για το θέμα που επέλεξα](https://github.com/eueung/hugo-casper-two)

Οι φωτογραφίες που χρησιμοποιήθηκαν για την σελίδα δεν υπόκεινται σε πνευματικά δικαιώματα και πάρθηκαν από το site:

  * https://www.pexels.com/
  

## ΑΣΚΗΣΗ 5
### Τίτλος: Visualize git commits

Για την επίλυση της συγκεκριμένης άσκησης δεν απαιτούνται πολλές ενέργειες. Αρκεί μονάχα να γίνει η εγκατάσταση του εργαλείου [git-bars](https://github.com/knadh/git-bars) και η κλωνοποίηση του repository που θέλουμε να ελέγξουμε τοπικά. Το δυσάρεστο με το συγκεκριμένο εργαλείο είναι πως δεν είναι ευρέως γνωστό επομένως μαθαίνουμε τις δυνατότητες του μόνο μέσω εμπειρίας και ανάγνωσης των οδηγιών που προσφέρει με την εντολή:

   ``
   git-bars --help
   ``
  #### Asciinema link:

[Visualise git commits](https://asciinema.org/a/5pSDePfbaukWwarBVDSh0dVQV)
  


## ΑΣΚΗΣΗ 6
### Τίτλος: Use color to improve your cli tools

Για την ολοκλήρωση αυτής της άσκησης είναι απαραίτητη η εγκατάσταση του εργαλείου γραμμής εντολών [pastel](https://github.com/sharkdp/pastel). To pastel είναι ένα σχετικά εύκολο εργαλείο για κατανόηση αν και όπως το git-bars δεν είναι ιδιαίτερα διαδεδομένο. Όλες οι εντολές που πραγματοποίησα φαίνονται στο παρακάτω link:

  #### Asciinema link:

[Use color to improve your cli tools](https://asciinema.org/a/lExHpUZUjvnS6KRDu8pfNxdVn)


## ΣΥΜΜΕΤΟΧΙΚΟ ΠΕΡΙΕΧΟΜΕΝΟ

### 2A

Για την εργασία αυτή επέλεξα να ποστάρω τις 10 δημοσιεύσεις μου στο Twitter, ένα social media γνωστό για το μικρή έκταση των post, την χρήση #, την αναφορά σε άλλα άτομα χρησιμοποιώντας @ καθώς και την χρήση gif, εικόνων και βίντεο.

[Λογαριασμός Twitter](https://twitter.com/valery_las)

[1o Tweet](https://twitter.com/valery_las/status/1192573181279768576)

[2o Tweet](https://twitter.com/valery_las/status/1192826188089249795)

[3o Tweet](https://twitter.com/valery_las/status/1192845171953733633)

[4o Tweet](https://twitter.com/valery_las/status/1192985622727798784)

[5o Tweet](https://twitter.com/valery_las/status/1193335627141582848)

[6o Tweet](https://twitter.com/valery_las/status/1193550034668867584)

[7o Tweet](https://twitter.com/valery_las/status/1193676728742424576)

[8o Tweet](https://twitter.com/valery_las/status/1193688401653968898)

[9o Tweet](https://twitter.com/valery_las/status/1193696721676705792)

[10o Tweet](https://twitter.com/valery_las/status/1193959652762869764)


### 2Β

Για την διεκπεραίωση του Β συμμετοχικού περιεχομένου πρόσθεσα μια στήλη με τις αναρτήσεις μου στο Twitter στη θέση του τρίτου section της αρχικής σελίδας της ιστοσελίδας του βιβλίου. Αυτό πραγματοποιείται εύκολα με την αντικατάσταση των δύο τελευταίων γραμμών (που αναφέρονται στο τμήμα που ήθελα να αντικαταστήσω) του φακέλου index.md με την εξής εντολή:

  <a class="twitter-timeline" data-width="400" data-height="600"  href="https://twitter.com/valery_las">Tweets by valery_las</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
  
  ![alt text](https://github.com/p17laso/mm/blob/%CE%A02017062/projects/%CE%A02017062/twitter_column.png)
  

  Παρόλο που δεν συνάντησα προβλήματα στη διεκπεραίωση των 2 προηγούμενων ζητημάτων το github μου έβγαζε συνεχώς σφάλματα (GitHub Pages failed to build your site) όταν προσπαθούσα να προσθέσω τα δικά μου διαδραστικά παραδείγματα και τη βιογραφία. 
  Εμφάνισα την ιστοσελίδα μέσω netlify, όπως ανέφεραν οι οδηγίες και όπως είπα προηγουμένως δεν αντιμετώπισα προβλήματα στην εμφάνιση της στήλης με τις αναρτήσεις μου, ωστόσο μόλις προσπαθούσα να ανεβάσω κάποια δική μου ανάρτηση το github με προειδοποιούσε πως υπάρχουν σφάλματα στην ιστοσελίδα.
  
 ![alt text](https://github.com/p17laso/mm/blob/%CE%A02017062/projects/%CE%A02017062/all_checks_have_failed.png)
  
  Προσπάθησα επιφυλακτικά να τα διορθώσω μιας και ήταν σε φακέλους που υπήρχαν εξαρχής στην σελίδα και δε δημιούργησα εγώ, χωρίς αποτέλεσμα. Μόλις διόρθωνα ένα σφάλμα εμφάνιζε ειδοποίηση πως υπάρχει κάποιο άλλο μέσα στην σελίδα. 
  
  ![alt text](https://github.com/p17laso/mm/blob/%CE%A02017062/projects/%CE%A02017062/error_correction1.png)
  
  Μετά τη διόρθωση:
  
  ![alt text](https://github.com/p17laso/mm/blob/%CE%A02017062/projects/%CE%A02017062/error_correction2.png)
  
  Στη προσωπική μου ιστοσελίδα εμφανίζει μόνο το όνομα της δημοσίευσης μου καθώς και μια σύντομη περιγραφή στο search bar
  
  ![alt text](https://github.com/p17laso/mm/blob/%CE%A02017062/projects/%CE%A02017062/search_bar.png)
  
  ωστόσο όταν προσπαθώ να μπώ στις αντίστοιχες πληροφορίες λέει πως η σελίδα δε μπορεί να βρεθεί. 
 
 ![alt text](https://github.com/p17laso/mm/blob/%CE%A02017062/projects/%CE%A02017062/loading_error.png)
  
  ### 1B
  
[Link Βιβλίου](https://github.com/pibook/site)

[Link Προσωπικού Αποθετηρίου του Βιβλίου](https://github.com/p17laso/site)

[Εκτελέσιμο Προσωπικό Link Βιβλίου](https://lucid-franklin-28216b.netlify.app/)
