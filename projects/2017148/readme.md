## ΜΑΘΗΜΑ: Πολυμέσα  
Επιβλέπων καθηγητής: Χωριανόπουλος Κωνσταντίνος 

## Στοιχεία φοιτητή  
### Αντρέας Παππούτας
### ΑΜ: Π2017148

## Συμμετοχικό Υλικό

## [Twitter Profile : https://twitter.com/p17papp1](https://twitter.com/p17papp1)

#### [Skype](https://twitter.com/p17papp1/status/1193272511997390852)
#### [Windows 10](https://twitter.com/p17papp1/status/1193269938565369857)
#### [Linux](https://twitter.com/p17papp1/status/1193270222679093248)
#### [Eclipse IDE](https://twitter.com/p17papp1/status/1193270675525554182)
#### [Social Media](https://twitter.com/p17papp1/status/1193270776532733953)
#### [Google Assistant](https://twitter.com/p17papp1/status/1193270898645708800)
#### [App](https://twitter.com/p17papp1/status/1193271203148029957)
#### [Raspberry Pi](https://twitter.com/p17papp1/status/1193271635106811905)
#### [Google Search Engine](https://twitter.com/p17papp1/status/1193271820763455488)
#### [Modern mouse](https://twitter.com/p17papp1/status/1193272109776228352)


## Παραδοτέο 1
### download mp3 - search, download and play (with the terminal) your favorite song of the month from youtube

Σε αυτή τη εργασία κατέβασα ενα τραγούδι απο το terminal σε μορφή mp3 με το youtube-dl. Με το εργαλείο mpv κατάφερα να 
τρέξω το mp3 αρχείο μέσα στο terminal.

## [Asciinema Recording URL: https://asciinema.org/a/VYVtnnYotgjyRvJECRBhw0njt](https://asciinema.org/a/VYVtnnYotgjyRvJECRBhw0njt)

### Για τη αλλαγή του terminal έγινε χρήση της εντολής

```
sudo gedit ~/.bashrc
```
## Έγινε εγκατάσταση των παρακάτω

### PYTHON

```
sudo apt-get install python3.6
```

### YOUTUBE-DL

```
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```


### MPV

```
sudo add-apt-repository ppa:mc3man/mpv-tests
sudo apt-get install mpv
```

### FFMPEG

```
sudo apt install ffmpeg
```

### Μέσο του youtube-dl κατέβασα το τραγούδι σε μορφή mp3

```
youtube-dl --extract-audio --audio-format mp3 --output song.mp3 <url>
```

### Για την αναπαραγωγή του τραγουδιού χρησημοποίησα το mpv

```
mpv song.mp3
```





## Παραδοτέο 2
### download a torrent

Σε αυτή το παραδοτέο έκανα χρήση του rtorrent. Όταν ανοίξεις το rtorrent βάζεις το url ή directory του torrent σου και πατάς enter. Για να αρχίσεις να κατεβάζεις επιλέγεις το torrent και πατάς ctrl+s. Για να σταματήσει ctrl+d και για να διαγραφτεί ctrl+d(x2) .

## [Asciinema Recording URL: https://asciinema.org/a/277309](https://asciinema.org/a/277309)

### Εγκατασταση του rtorrent

```
sudo apt-get install rtorrent
```


### Keybindings για το rtorrent
```
ctrl+S = start torrent
ctrl+D = stop torrent
ctrl+D(x2) = delete torrent
```

## Παραδοτέο 3
### edit a spreadsheet - edit values and formulas

Κατέβασα τα δεδομένα απο το ΕΛΣΤΑΤ και τα έβαλα στο sc-im. Άλλαξα τοποθεσία μιας στήλης με τη χρήση του visual mode και yank. Δημιούργισα νεές γραμμές με το ir και έβαλα επικεφαλιδες πανω απο τα δεδομενα με το \"@upper("text"). Βρήκα το μεσο ορο με τη φόρμουλα =@avg(B3:B6) και το σύνολο με =@sum(B2:G2).

## [Asciinema Recording URL: https://asciinema.org/a/278021](https://asciinema.org/a/278021)

### Εγκατασταση του sc-im

```
git clone https://github.com/andmarti1424/sc-im.git
$ cd sc-im/src
$ make
$ sudo make install
```


### Keybindings για το sc-im
```
v  -> Visual
y  -> Yank
p  -> Paste
u  -> Undo
x  -> Delete
> or < or \ -> Write text
=  -> Write numbers
aa -> Show the whole text
fl -> Increase column width
fh -> Decrease column width
ir -> Insert row
dc -> Delete column
:w  -> Save
:q  -> Quit

```

## Παραδοτέο 4
### manage your music library	- import your music library, add tags and delete/add songs

## [Asciinema Recording URL: https://asciinema.org/a/277344](https://asciinema.org/a/277344)

Αρχικά έκανα επεξεργασία του αρχείου config.yml όπου έβαλα το φάκελο τις μουσικής και το library για το beets.
Ακολούθως έβαλα τη μουσική μου μέσα στο φάκελο που είναι το library του beets μέσο της εντολής:
```
beet import ~/Music/Mousikiold
```
Πρόσθεσα tags σε ένα από τα τραγούδια με τη εντολή:
```
beet modify song artists="" tags="" title=""
```
Για να αφαιρέσεις ή προσθέσεις τραγούδια:
```
beet remove title:""
beet import
```
Εντολή για να δεις τη λίστα με τα τραγούδια
```
beet ls
```


## Παραδοτέο 5
### Visualize an mp3: demonstrate album art and visualizations with an mp3 player and various songs.

## [Asciinema Recording URL: https://asciinema.org/a/BldMvAjOoEmS9gvAd1X2XvjJg](https://asciinema.org/a/BldMvAjOoEmS9gvAd1X2XvjJg)

Με τη χρήση του cmus μπορείς να διαχειριστείς μέσα στο linux τεράστιες βιβλιοθήκες μουσικής χωρίς κανένα πρόβλημα. Μπορείς να προσθέσεις και να ταξινομήσεις χιλιάδες τραγούδια γρηγορότερα από άλλα προγράμματα. 

### Το cmus είναι χωρισμένο σε 7 διαφορετικά views:

```
1. Library
2. Sorted Library
3. Playlist
4. Play Queue
5. Browser
6. Filters
7. Settings
```
### Εγκατάσταση cmus
```
sudo apt-get install cmus
```
### Keybindings:
```
x = play song
c = pause
v = stop
```
### Για να βάλεις μουσική:
```
:add ~Music/Library
```
