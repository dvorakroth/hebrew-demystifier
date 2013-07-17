hebrew-demystifier
==================

A small commandline program to ungarble "gibberish" Hebrew characters. (åäøé ãâîà)

License: WTFPLv2, see COPYING for the full license text.

Usage
-----

You can fire up the program with no arguments if you only need to re-encode Windows-1252 (Western European) as Windows-1255 (Hebrew, Logical). It'll prompt you for a line of text, and will demystify each one once you enter a carriage-return or similar.

There also exists the `--mac-archive` option which, when passed to the program, makes it demystify lines of text by re-encoding Mac-Roman into CP-856 instead. Apparently, OSX sometimes has trouble with archives containing Hebrew characters in filenames, and this is the way to de-garble them.

There should be a `--help` option, optionally shorthanded as `-h` with a basic help and usage screen, too.

The Fine Print™
---------------

* Only use Python >= 3
* Can only demystify one line at a time, because I'm lazy
