Slayaway Camp Bruteforce Solver
===============================

This is a bruteforce solver (and, completely incidentally, commandline
version of) the excellent puzzle game "Slayaway Camp", by Blue Wizard
Digital: http://store.steampowered.com/app/530390/Slayaway_Camp/

I believe I started on this when I got stuck on one of the "NC-17"
levels and figured I'd try my hand at writing a bruteforce solver for
the game.  Along the way I had so much fun putting it together that
it became a fully-fledged console version of the game, in addition to
having level definitions for basically the entire base game.

The console version certainly leaves quite a lot to be desired from
a UI perspective, since it's really only in there because I wanted a
way to easily test out functionality.  It'll look like this:

![Interactive Mode](screenshot.png)

When run in non-interactive mode, you'll get output like this:

    $ ./solve.py -l s2_s04
    Winning moves (11) for Slayaway Camp 2, Scene 4 - Triple Truncheon:
            1. South
            2. East
            3. North
            4. West
            5. South
            6. South
            7. East
            8. North
            9. West
            10. South
            11. North
    $

The game has levels defined for all of the "main" Slayaway Camp levels
(ie: Slayaway Camp 1 through Slayaway Camp X), plus the NC-17 levels for
Slayaway Camp 1.

Usage
=====

Slayaway Solver was written in Python.  It should work in Python 2.7 or Python 3.x
without problems, though it's mostly just been run in 3.  I recommend using
PyPy/PyPy3, though performance is generally fine using plain ol' CPython.

Slayaway Solver requires the `colorama` Python module, to make the interactive
output a little more palatable.  If you want to use PyPy3, an easy way to get
this installed appropriately is using virtualenvs:

    $ pypy3 -m venv_slayaway
    $ . venv_slayaway/bin/activate
    (venv_slayaway) $ pip install colorama
    (venv_slayaway) $ ./solve.py

Commandline usage is pretty simple:

	usage: solve.py [-h] [-i | -t] [-l LEVELNAME]

	Play or solve Slayaway Camp levels

	optional arguments:
	  -h, --help            show this help message and exit
	  -i, --interactive     Run interactively rather than in solver mode (default:
							False)
	  -t, --test            Generate python code suitable for a unit test
							(default: False)
	  -l LEVELNAME, --level LEVELNAME
							Level name to run (use "list" to get a list) (default:
							s1_s01)

As mentioned, to get a list of all levels that it knows about, specify
`--level list` or `-l list` as an argument.

The `-t`/`--test` argument is mostly just for my own purposes to add it into
our unit test area.  They aren't actually real unit tests; rather it just checks
each level against previously-found solutions.

Performance
===========

Performance is actually quite good when using PyPy3 instead of CPython.  (And in
general it's not bad even when using CPython).  Our test suite, which tests all
levels except `s10_d4` versus known solutions, completes in just under fifteen
seconds on my system.  They complete in 52 seconds using CPython.

"Slayaway Camp X, Deleted Scene 4" (`s10_d4`) is currently the longest to solve,
clocking in at at a little over 1 minute, on my CPU (using PyPy3).  Its solve
time goes up to 4:20 or so when using CPython.

Interactive Use
===============

The interactive UI for this definitely takes a bit of getting used to.  Your
available commands are just `n`, `e`, `w`, and `s` (for north, east, west, and
south).  You can also undo moves with `u`, reset to the initial state with `r`,
and quit with `q`.

The symbols used in the UI to indicate the map:

* `P` - Player
* `V` - Victim
* `E` - Exit
* `C` - Cat
* `L` - Police (will use `←↑→↓` to show which way they're facing)
* `S` - SWAT Cop (will use `←↑→↓` to show which way they're facing)
* `O` - Police targeting reticle
* `H` - Hazard (pit, fire, etc)
* `M` - Mine
* `1`/`2`/`3` - Phones
* `|` - Bookcase/Cabinet which can be knocked over west or east
* `=` - Bookcase/Cabinet which can be knocked over north or south
* `X` - Bookcase/Cabinet which has been knocked over
* `^` `>` `V` `<` - Escapes (only along map edges)
* `~~~` - Light switches
* `▒` - Gum (sticky patch)
* `◉` `◧` `◈` - Teleporters (matched by symbol)

A bit of coloration is used to help distinguish things as well.  The game
map will use a yellow checkerboard pattern to distinguish cells.  The exit
will be magenta until all victims have been killed, and blue/green afterwards.
Half-height walls are in red.  Police/SWAT targeting reticles are in red.
Electric walls will be bright cyan if active, or blue otherwise.  Sticky
Goo will be magenta.
