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
Ο παίκτης κερδίζει ένα πόντο για κάθε νόμισμα που μαζεύει και 5 πόντους για κάθε goomba που πατάει.


## Παραδοτέο 3

Σε αυτό το παραδοτέο, έχει γίνει γενική αναδιαμόρφωση του κώδικα. Αρχικά για να κάνω πιο καθαρό το κώδικα και δεύτερον για να χρησιμοποιήσω το [Phaser.State](https://phaser.io/docs/2.4.4/Phaser.State.html) που προσφέρει η βιβλιοθήκη Phaser. Χώρισα το κώδικα σε states, με αυτό το τρόπο μπορώ να πηδάω από state σε state κάνοντας το κώδικα πιο εύκαμπτο, προσιτό σε αλλαγές/προσθήκες, και κυριότερα ευκολοδιάβαστο. 

[**index.html**](https://github.com/sakis475/Super-Mario/blob/paradoteo3/index.html)
Στο html αρχείο ξεχώρισα το script και το έβαλα σε ένα νέο αρχείο index.js
Επίσης ανέβασα το [phaser.min.js](https://github.com/sakis475/Super-Mario/blob/paradoteo3/phaser.min.js) αρχείο στο git ώστε να μην χρειάζετε να το φορτώνει από εξωτερική πηγή.

 [**index.js**](https://github.com/sakis475/Super-Mario/blob/paradoteo3/index.js) 
**Σημείωση: Για περισσότερες πληροφορίες υπάρχει σχολιασμός κώδικα μέσα στο αρχείο index.js .**
 
 Στο JavaScript αρχείο η σημαντικότερη αλλαγή  που έκανα ήταν να βάλω όλες τις μεθόδους μέσα σε μεταβλητές, για να τις ελέγχω σαν states μέσω του phaser. Έτσι ώστε όταν ξεκινάω πχ τη loadState να εκτελέσει ότι υπάρχει μέσα στη μεταβλητή loadState. 

    var loadState = {
        //code...
    }
    game.state.add('load', loadState);
    game.state.start('load');

**loadState** 

Σε αυτό το state απλά γίνονται load όλα τα αρχεία και ορίζονται κάποιες σημαντικές παραμέτρους που χρειάζονται για να τρέξει η εφαρμογή.  

**menuState**

Στο menu υπάρχει η επιλογή level Α,Β για αρχή, όπου Α είναι το τωρινό map και Β θα είναι το επόμενο map που θα δημιουργήσω στο επόμενο παραδοτέο.
![menu](https://raw.githubusercontent.com/sakis475/mm/paradoteo3/projects/2015038/menu.png)

**gameOverState**

Αυτό το state εμφανίζετε όταν ο παίκτης πεθαίνει. Δίνει τη επιλογή στο χρήστη για να κάνει restart το game, όπου τον πηγαίνει πίσω στο menuState.
![gameover](https://github.com/sakis475/mm/blob/paradoteo3/projects/2015038/gameover.png?raw=true)

**mainState**

Εδώ υπάρχει όλη η λογική του παιχνιδιού. Έχω προσθέσει 4 καινούργιες μεθόδους

 1. turtleOverlap (νέος εχθρός) ![turtle](https://raw.githubusercontent.com/sakis475/Super-Mario/paradoteo3/assets/turtle.png)
 2. endLevelOverlap (το animation στο τέλος)
 3. teleportOverlap (η τηλεμεταφορά σε σημείο του χάρτη)
 4. handleDeath  
 
 
1.Όταν γίνετε overlap παίκτη με τη χελώνα τότε ο παίκτης πεθαίνει ακαριαία.
 
2.Όταν ο παίκτης ακουμπάει το δοκάρι της σημαίας στο τέλος, ο παίκτης πέφτει με αργή κίνηση προς το έδαφος, και πηγαίνει προς τη είσοδο του κάστρου όπου και περνάει στο επόμενο level.
![flagpole](https://raw.githubusercontent.com/sakis475/mm/paradoteo3/projects/2015038/flagpole.png)
3.Όταν ο παίκτης είναι πάνω από το πράσινο σωλήνα και πατηθεί το κάτω βελάκι, γίνετε τηλεμεταφορά σε καινούργιο σημείο της πίστας.
![newdungeon](https://raw.githubusercontent.com/sakis475/mm/paradoteo3/projects/2015038/newdungeon.png)
4.Το handleDeath καλείτε όταν ο χρήστης πεθαίνει. Απλά το έβαλα για να κάνω πιο καθαρό το κώδικα (OOP friendly) και να μη βάζω 2 φορές το ίδιο κώδικα (στη goombaOverlap & turtleOverlap).

**Assets**

-Αρχικά πρόσθεσα καινούργιο tileset (**super_mario_tiles2.png**)
![tileSet](https://github.com/sakis475/Super-Mario/blob/paradoteo3/assets/super_mario_tiles2.png?raw=true)
Τη σημαία, το κάστρο, τη χελώνα, και το πίκατσου

-Πρόσθεσα καινούργια πίστα **super_mario_map15.json**, όπου είναι προέκταση της προηγούμενης. Εδώ έχουν προσθεθεί o καινούργιος εχθρός, το κάστρο στο τέλος του level και στη αρχή του επόμενου, και η σημαία για το animation στο τέλος του level, και το μέρος όπου γίνετε τηλεμεταφορά από το πράσινο σωλήνα. 

**Sounds**

Στο φάκελο audio πρόσθεσα το levelCompleted.wav όπου παίζει στο animation στο τέλος της πίστας.

 
