# Delago, Daniel
# 100-106-0927
# 2018-01-18

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been somewhat modified and updated by Brian A. Dalio for use
# in CSE 4303 / CSE 5365 in the 2018 Spring semester.

#----------------------------------------------------------------------
# The initialization of tkinter is deeply recursive.  On Ubuntu, the
# limit is too low for tkinter to succeed.  Trial-and-error has shown
# that 2000 seems to work.  If a more complex program starts failing,
# the limit might have to be even higher.
import sys
_RECURSION_LIMIT = 2000

if ( sys.getrecursionlimit() < _RECURSION_LIMIT ) :
    print ( 'System recursion limit was %d, setting to %d.' % ( sys.getrecursionlimit(), _RECURSION_LIMIT ) )
    sys.setrecursionlimit( _RECURSION_LIMIT )

#----------------------------------------------------------------------
import tkinter as tk
import myWidgets
import myGraphics

ob_root_window = None

#----------------------------------------------------------------------
def onClosing() :
    if tk.messagebox.askokcancel( "Really Quit?", "Do you really wish to quit?" ) :
        tk.Tk().quit()

#----------------------------------------------------------------------
def main() :
    global ob_root_window

    ob_root_window = tk.Tk()
    ob_root_window.protocol( "WM_DELETE_WINDOW", onClosing )

    ob_world = myGraphics.cl_world()

    myWidgets.cl_widgets( ob_root_window, ob_world )

    ob_root_window.mainloop()
    print( '... mainloop has exited.' )

if ( __name__ == "__main__" ) :
  main()

#----------------------------------------------------------------------
