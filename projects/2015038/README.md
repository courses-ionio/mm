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
[sakis475/Super-Mario/blob/master/index.html](https://github.com/sakis475/Super-Mario/blob/master/index.html)






