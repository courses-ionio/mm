# ΙΟΝΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ, ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ 
## ΜΑΘΗΜΑ
### Πολυμέσα  

## Στοιχεία φοιτητή  
### Αθανάσης Παπαπέτρου
### ΑΜ: Π2017149

## Eργασία 1 search, download and play (with the terminal) your favorite song of the month from youtube

## asciinema URL: https://asciinema.org/a/YKK6GNcR1kZxiOXB39AiIoBeS?fbclid=IwAR2oWtiO3TAI2xS1Fsrd0A3YBSNuPoFOkGTKnH6uykzpx0VgvNM76sJF71k

## Τα προγράμματα που χρησιμοποίησα:

# youtube-dl
sudo apt-get install youtube-dl

# sox
sudo apt-get install sox

# ffmpeg
sudo apt-get install ffmpeg


## Οι εντολές που χρησιμοποίησα στο video

#Για να κατεβάσω το τραγούδι σε mp3
```
youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=HKS6cp5OGMo
```
#Για να δω τα αρχεία που είναι στον φάκελο 
```
ls
```
#Για να αρχίσει τα παίζει το τραγούδι με το sox
```
play 'Mansion - NF (Lyrics)-ibWdgkv1LSA.mp3'
```
