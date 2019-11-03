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
  2) Για να δούμε τι χρειάζεται για το configuration του mpd ανοίγουμε το file mpd.conf που βρίσκεται στο directory /etc. Στην συνέχεια ελέγχουμε αν η εγκατάσταση του προγράμματος δημιούργησε τους αναγκαίους φακέλους στα σωστά αποθετήρια. Στη δική μου περίπτωση έπρεπε να προσθέσω τον φάκελο mpdstate στο var/lib/mpd καθώς και να αλλάξω το όνομα του music directory σε αυτό που υπήρχε στο δικό μου υπολογιστή. Έπειτα δημιουργούμε directories τα οποία χρειάζεται το MPD ώστε να τρέξει σωστά, ένα default configurations directory  και ένα playlist directory. 
  
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
          
 Στο config file που δημιουργήσαμε μέσα στο αποθετήριο ncmpcpp προσθέτουμε:
        
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
   
   
   
   
     
 
