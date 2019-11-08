# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  

## Στοιχεία φοιτητή  
### Αθανάσης Παπαπέτρου
### ΑΜ: Π2017149

## Eργασία 1 search, download and play (with the terminal) your favorite song of the month from youtube

## asciinema URL: https://asciinema.org/a/276971

## Τα προγράμματα που χρησιμοποίησα:

# ddgr
sudo apt-get install ddgr

# youtube-dl
sudo apt-get install youtube-dl

# sox
sudo apt-get install sox

# ffmpeg
sudo apt-get install ffmpeg


## Οι εντολές που χρησιμοποίησα στο video:

# Για να κάνω search το Link από τον browser 
```
ddgr
nf mansion youtube
x
nf mansion youtube
```

# Για να κατεβάσω το τραγούδι σε mp3
```
youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=XBp88RoxSPY
```
# Για να δω τα αρχεία που είναι στον φάκελο 
```
ls
```
# Για τα αρχίσει τα παίζει το τραγούδι με το sox
```
play 'NF - Mansion-XBp88RoxSPY.mp3'
```

## Eργασία 2 youtube video streaming

## asciinema URL: https://asciinema.org/a/277787

## Τα προγράμματα που χρησιμοποίησα:

# MPlayer
Οι εντολές που χρησιμοποίησα για να κάνω το install το MPlayer:
```
sudo add-apt-repository universe
```
```
sudo apt update
```
```
sudo apt install mplayer mplayer-gui
```

Για να ξεκινήσει το video να κάνει streaming:
```
mplayer -fs -cookies -cookies -cookies-file /tmp/videos.txt $(youtube-dl -g --cookies /tmp/videos.txt "https://www.youtube.com/watch?v=m_qlgFQs7E4")
```
Το -fs είναι για να παίξει το video σε full screen

Το 1ο cookies είναι για να δείξω στο mplayer ότι θέλω να χρησιμοποιήσει cookies  

Το 2ο cookies είναι για να δείξω το path του cookies αρχείου 

Tο -g είναι για να μην κατεβάσει το video 

Το --cookies /tmp/videos.txt ειναι το path και μετά το Youtube Link



