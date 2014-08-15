#GradHack

A comical roguelike based on graduate school

This uses classical vi keybindings. When on stairs use "." to ascend or descend. Pick up the thesis with "." as well. I'll eventually have one more key use for item useage when that gets implemented.

More specifically:

* h,j,k,l,y,u,b,n for movement (use it! the game should basically be impossible if you use arrow keys)
* 0, 1, 2 for special skills
* . for doing things that appear on screen (up/down stairs, use book, use item)
* ! indicates an item
* ~ indicates a book

This is a very preliminary sketch of the final game. To run you will need pygame and python 3 (maybe earlier versions will work?). You do not need to make anything. 

Steps to play:

* Open a terminal
* type "git clone http://github.com/wardm4/gradhack" 
* type "python gradhack.py"

## Note to pre-alpha testers:

Experiment at your own risk. This is only about halfway to the first alpha release. If you find clear bugs that you think I might not know about, I would be ever grateful if you told me.

Known bugs:

* Diagonal around some corners doesn't work
* Up and down stairs can spawn on top of each other

