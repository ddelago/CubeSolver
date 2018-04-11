# Delago, Daniel
# 100-106-0927
# 2018-01-18

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been somewhat modified and updated by Brian A. Dalio for use
# in CSE 4303 / CSE 5365 in the 2018 Spring semester.

#----------------------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog

#----------------------------------------------------------------------
class cl_widgets :
    def __init__( self, ob_root_window, ob_world = [] ) :
        self.ob_root_window = ob_root_window
        self.ob_world = ob_world
        self.menu = cl_menu( self )
        self.toolbar = cl_toolbar( self )

        self.statusBar_frame = cl_statusBar_frame( self.ob_root_window )
        self.statusBar_frame.pack( side = tk.BOTTOM, fill = tk.X )
        self.statusBar_frame.set( "%s", "This is the status bar" )
        self.ob_canvas_frame = cl_canvas_frame( self )
        self.ob_world.add_canvas( self.ob_canvas_frame.canvas )

#----------------------------------------------------------------------
class cl_canvas_frame :
    def __init__( self, master ) :
        self.master = master
        self.canvas = tk.Canvas(
          master.ob_root_window, width=640, height=480, bg="yellow" )

        self.canvas.pack( expand=tk.YES, fill=tk.BOTH )
        self.canvas.bind( "<Configure>",       self.canvas_resized_callback )
        self.canvas.bind( "<ButtonPress-1>",   self.left_mouse_click_callback )
        self.canvas.bind( "<ButtonRelease-1>", self.left_mouse_release_callback )
        self.canvas.bind( "<B1-Motion>",       self.left_mouse_down_motion_callback )
        self.canvas.bind( "<ButtonPress-3>",   self.right_mouse_click_callback )
        self.canvas.bind( "<ButtonRelease-3>", self.right_mouse_release_callback )
        self.canvas.bind( "<B3-Motion>",       self.right_mouse_down_motion_callback )
        self.canvas.bind( "<Key>",             self.key_pressed_callback )
        self.canvas.bind( "<Up>",              self.up_arrow_pressed_callback )
        self.canvas.bind( "<Down>",            self.down_arrow_pressed_callback )
        self.canvas.bind( "<Right>",           self.right_arrow_pressed_callback )
        self.canvas.bind( "<Left>",            self.left_arrow_pressed_callback )
        self.canvas.bind( "<Shift-Up>",        self.shift_up_arrow_pressed_callback )
        self.canvas.bind( "<Shift-Down>",      self.shift_down_arrow_pressed_callback )
        self.canvas.bind( "<Shift-Right>",     self.shift_right_arrow_pressed_callback )
        self.canvas.bind( "<Shift-Left>",      self.shift_left_arrow_pressed_callback )
        self.canvas.bind( "f",                 self.f_key_pressed_callback )
        self.canvas.bind( "b",                 self.b_key_pressed_callback )

    def key_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Key pressed" )

    def up_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Up arrow pressed" )

    def down_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s","Down arrow pressed" )

    def right_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Right arrow pressed" )

    def left_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Left arrow pressed" )

    def shift_up_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Shift up arrow pressed" )

    def shift_down_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Shift down arrow pressed" )

    def shift_right_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Shift right arrow pressed" )

    def shift_left_arrow_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "Shift left arrow pressed" )

    def f_key_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "f key pressed" )

    def b_key_pressed_callback( self, event ) :
        self.master.statusBar_frame.set( "%s", "b key pressed" )

    def left_mouse_click_callback( self, event ) :
        self.master.statusBar_frame.set( "%s",
            "LMB clicked. (" + str( event.x ) + ", " + str( event.y ) + ")" )
        self.x = event.x
        self.y = event.y
        self.canvas.focus_set()

    def left_mouse_release_callback( self, event ) :
        self.master.statusBar_frame.set( "%s",
            "LMB released. (" + str( event.x ) + ", "+ str( event.y ) + ")" )
        self.x = None
        self.y = None

    def left_mouse_down_motion_callback( self, event ) :
        self.master.statusBar_frame.set( "%s",
            "LMB down motion. ("+ str( event.x ) + ", "+ str( event.y ) + ")" )
        self.x = event.x
        self.y = event.y

    def right_mouse_click_callback( self, event ) :
        self.master.statusBar_frame.set( "%s",
            "RMB clicked. (" + str( event.x ) + ", " + str( event.y ) + ")" )
        self.x = event.x
        self.y = event.y

    def right_mouse_release_callback( self, event ) :
        self.master.statusBar_frame.set( "%s",
            "RMB released. (" + str( event.x ) + ", " + str( event.y ) + ")" )
        self.x = None
        self.y = None

    def right_mouse_down_motion_callback( self, event ) :
        self.master.statusBar_frame.set( "%s",
            "RMB down motion. (" + str( event.x ) + ", " + str( event.y ) + ")" )
        self.x = event.x
        self.y = event.y

    def canvas_resized_callback( self, event ) :
        self.canvas.config( width = event.width-4, height = event.height-4 )

        self.master.statusBar_frame.pack( side = tk.BOTTOM, fill = tk.X )
        self.master.statusBar_frame.set( "%s",
            "Canvas width, height (" + str( self.canvas.cget( "width" ) ) +
            ", " + str( self.canvas.cget( "height" ) ) + ")" )

        self.canvas.pack()

        self.master.ob_world.redisplay( self.master.ob_canvas_frame.canvas, event )

#----------------------------------------------------------------------
class cl_statusBar_frame( tk.Frame ) :
    def __init__( self, master ) :
        tk.Frame.__init__( self, master )
        self.label = tk.Label( self, bd = 1, relief = tk.SUNKEN, anchor = tk.W )
        self.label.pack( fill = tk.X )

    def set( self, formatStr, *args ) :
        self.label.config( text = "(Daniel Delago) " + (formatStr % args))
        self.label.update_idletasks()

    def clear( self ) :
        self.label.config( text="" )
        self.label.update_idletasks()

#----------------------------------------------------------------------
class cl_menu :
    def __init__( self, master ) :
        self.master = master
        self.menu = tk.Menu( master.ob_root_window )
        master.ob_root_window.config( menu = self.menu )

        self.filemenu = tk.Menu( self.menu )
        self.menu.add_cascade( label = "File", menu = self.filemenu )
        self.filemenu.add_command( label = "New", command = self.menu_callback )
        self.filemenu.add_command( label = "Open...", command = self.menu_callback )
        self.filemenu.add_separator()
        self.filemenu.add_command( label = "Exit", command = self.menu_callback )

        self.dummymenu = tk.Menu( self.menu )
        self.menu.add_cascade( label = "Dummy", menu = self.dummymenu )
        self.dummymenu.add_command( label = "Item1", command = self.menu_item1_callback )
        self.dummymenu.add_command( label = "Item2", command = self.menu_item2_callback )

        self.helpmenu = tk.Menu( self.menu )
        self.menu.add_cascade( label = "Help", menu = self.helpmenu )
        self.helpmenu.add_command( label = "About...", command = self.menu_help_callback )

    def menu_callback( self ) :
        self.master.statusBar_frame.set( "%s", "called the menu callback!" )

    def menu_help_callback( self ) :
        self.master.statusBar_frame.set( "%s", "called the help menu callback!" )

    def menu_item1_callback( self ) :
        self.master.statusBar_frame.set( "%s", "called item1 callback!" )

    def menu_item2_callback( self ) :
        self.master.statusBar_frame.set( "%s", "called item2 callback!" )

#----------------------------------------------------------------------
class cl_toolbar :
    def __init__( self, master ) :
        self.master = master
        self.toolbar = tk.Frame( master.ob_root_window )
        self.var_filename = tk.StringVar()
        self.var_filename.set( "" )
        # Loaded object data
        self.vertices = []
        self.faces = []
        self.world = []
        self.screen = []

        # Create Clear Button
        self.button = tk.Button( self.toolbar, text = "Clear", command = self.toolbar_clear_callback )
        self.button.pack( side = tk.LEFT, pady = 2 )

        # Create Load Button
        self.file_dialog_button = tk.Button( self.toolbar, text = "Load", command = self.browse_file )
        self.file_dialog_button.pack( side = tk.LEFT )

        # Create Draw Button
        self.button = tk.Button( self.toolbar, text = "Draw", command = self.toolbar_draw_callback )
        self.button.pack( side = tk.LEFT, pady = 2 )
        self.toolbar.pack( side = tk.TOP, fill = tk.X )

    def toolbar_clear_callback( self ) :
        self.master.ob_world.clear_canvas( self.master.ob_canvas_frame.canvas )
        self.master.statusBar_frame.set( "%s", "Cleared the data" )

    def browse_file( self ) :
        fName = tk.filedialog.askopenfilename( filetypes = [ ( "allfiles", "*" ), ( "pythonfiles", "*.txt" ) ] )
        if ( len( fName ) == 0 ) :
            msg = "[Enter was cancelled]"
        else :
            self.var_filename.set( fName )
            self.load_file()
            msg = str(len(self.vertices)) + " vertices, " + str(len(self.faces)) + " faces" 

        self.master.statusBar_frame.set( "%s", msg )

    def load_file( self ):
        # First reset object values
        self.vertices = []
        self.faces = []
        self.world = []
        self.screen = []

        # Open file
        file = open( self.var_filename.get(),'r' )

        # Get data values
        for line in file:
            temp = line.strip().split(' ')
            char = temp[0]
            # If vertice
            if (char == 'v'):
                self.vertices.append([float(temp[1]),float(temp[2]),float(temp[3])])
            # If face
            elif (char == 'f'):
                self.faces.append([int(temp[1]),int(temp[2]),int(temp[3])])
            # If world
            elif (char == 'w'):
                self.world = [float(temp[1]),float(temp[2]),float(temp[3]),float(temp[4])]
            # If screen
            elif (char == 's'):
                self.screen = [float(temp[1]),float(temp[2]),float(temp[3]),float(temp[4])]

    def toolbar_draw_callback( self ) :
        self.master.ob_world.create_graphic_objects( self.master.ob_canvas_frame.canvas, self.vertices, self.faces, self.world, self.screen )
        self.master.statusBar_frame.set( "%s", "Drew the data" )

#----------------------------------------------------------------------
