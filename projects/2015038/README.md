----------------------

**ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ**


Πολυμέσα (MM)

Super-Mario

ΠΙΠΛΙΚΑΤΣΗΣ ΑΘΑΝΑΣΙΟΣ	
Π2015038

## Παραδοτέο 1

Ο σύνδεσμος της σελίδας (git-page) μου με την εφαρμογή:
https://sakis475.github.io/Super-Mario/

Για την αλλαγή του ***χαρακτήρα***,***νομίσματος*** ανέβασα 2 νέες φωτογραφίες
και έβαλα τα σωστά arguments στις μεθόδους:

> this.load.spritesheet('mario', 'assets/**ash.png**', 16, 16, **13**);
> this.load.spritesheet('coin', 'assets/**coin2.png**', 16, 16);


Αλλαγή coins.callAll(...) [0, 0, 1, 2] σε [ 0, 0, 1, 2, 3, 4, 5, 6, 7 ]
Αφού το αρχείο coin2 έχει 8 tiles αντί για 3. 

> coins.callAll('animations.add', 'animations', 'spin',
> 					**[ 0, 0, 1, 2, 3, 4, 5, 6, 7 ]**, 6, true);

					
Για τη ***δημιουργία καινούργιου χάρτη***, χρησιμοποίησα το tiled 
και έκανα εξαγωγή σε json. Από εκεί έθεσα τα σωστά arguments στο κώδικα:
> this.load.tilemap('level', 'assets/**super_mario_map1.json**', null,
> 					Phaser.Tilemap.TILED_JSON);


Όλα  αυτά στο αρχείο index.html : 
[sakis475/Super-Mario/paradoteo2/index.html](https://github.com/sakis475/Super-Mario/blob/paradoteo1/index.html)


## Παραδοτέο 2

Οι 3 πρώτες απαιτήσεις υπάρχουν στο Παραδοτέο 1, επειδή το ανέβασα πριν μεταφέρετε κάποιες αλλαγές στο Παραδοτέο 2. Έτσι αφού τα έχω πραγματοποιήση ήδη, συνεχίζω με μερικές διευκρινήσεις και τα υπόλοιπα του Παραδοτέου 2.

Σημείωση: Yπάρχει αναλυτικός σχολιασμός στο κώδικα για όλες τις αλλαγές.
Κώδικας: [Super-Mario/index.html](https://github.com/sakis475/Super-Mario/blob/paradoteo2/index.html)

-Προσθήκη ήχων και μουσικής :

Αρχικά ανέβασα όλα τα αρχεία της μουσικής και εφέ (.wav) στο φάκελο 

[Super-Mario/audio](https://github.com/sakis475/Super-Mario/tree/paradoteo2/audio)

coin.wav -> Όταν ο χαρακτήρας παίρνει ένα νόμισμα

jump.wav -> Όταν ο χαρακτήρας πηδάει.

death.wav -> Όταν ο χαρακτήρας πεθαίνει

stomp.wav -> Όταν ένα goomba πεθαίνει

gameTheme.wav -> Η μουσική που παίζει κατά τη διάρκεια του παιχνιδιού

bump.wav -> Όταν ο παίκτης χάσει μια ζωή

bonusLife.wav -> Όταν ο παίκτης πάρει μια μπόνους ζωή



-Έπειτα ανέβασα τις εικόνες και το json αρχείο στο φάκελο 

[Super-Mario/assets](https://github.com/sakis475/Super-Mario/tree/paradoteo2/assets)

Ένα τμήμα του καινούργιου χάρτη  
![map2](https://raw.githubusercontent.com/sakis475/mm/paradoteo2/projects/2015038/map_scr.png)

assets/super_mario_map2.json -> Ουσιαστικά είναι σχεδόν ίδιος με τον map1 από το Παραδοτέο 1, απλά πρόσθεσα τα pokeballs

super_mario_tiles.png -> Προσθήκη pokeball στη θέση 3 όπου είναι το αντικείμενο που θα δίνει bonus life

bonus.png -> Είναι και αυτό pokeball που χρησιμοποιήθηκε σαν spritesheet για να το κάνω enable στο physics.arcade του Phaser

ash.png -> Είναι ο κύριος χαρακτήρας του παιχνιδιού (ο Ash Ketchum από το pokemon) όπου και αντικαθιστά το super-mario.

Τέλος, προστέθηκαν στο παιχνίδι score και ζωές, στο πάνω μέρος της οθόνης.

![scoreLives](https://raw.githubusercontent.com/sakis475/mm/paradoteo2/projects/2015038/ScoreLives.png)

Ο παίκτης χάνει μια ζωή όταν ακουμπάει ένα goomba (το goomba πεθαίνει), και κερδίζει μια ζωή όταν παίρνει ένα pokeball.
Ο παίκτης κερδίζει ένα πόντο για κάθε νόμισμα που μαζέυει και 5 πόντους για κάθε goomba που πατάει.


