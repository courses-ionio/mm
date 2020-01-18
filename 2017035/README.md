apt-get install youtube-dl
apt-get install mplayer 
mplayer -fs -cookies -cookies-file /tmp/cookie.txt $(youtube-dl -g --cookies /tmp/cookie.txt "https://www.youtube.com/watch?v=_Yhyp-_hX2s")
