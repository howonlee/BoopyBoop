Auto Awesome
======

Automatically make awesome names that will also not collide too much.

Interface is simple. Create the object BoopyBoop (it will convert mongoids by default, but you can use any old number), and then pop out the human-friendly names with `BoopyBoop.id_to_string(words, settings)`

By "not collide too much", I mean "someone can probably figure it out, depending on how many of the words you use and how strong, etc your hash or whatever is in the first place". This is not really an encryption anything, really.
