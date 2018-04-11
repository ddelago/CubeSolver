# Delago, Daniel
# 100-106-0927
# 2018-01-18

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been somewhat modified and updated by Brian A. Dalio for use
# in CSE 4303 / CSE 5365 in the 2018 Spring semester.

#----------------------------------------------------------------------
class cl_world :
    def __init__( self, objects = [], canvases = [] ) :
        self.objects = objects
        self.canvases = canvases

    def add_canvas( self, canvas ) :
        self.canvases.append( canvas )
        canvas.world = self

    def clear_canvas( self, canvas ) :
        canvas.delete( "all" )

    def create_graphic_objects( self, canvas, vertices, faces, world, screen ) :
        self.objects = []
        # Variables
        self.vertices = vertices
        self.faces = faces
        self.world = world
        self.screen = screen
        # Canvas variables
        self.width = int(canvas.cget( "width" ))
        self.height = int(canvas.cget( "height" ))
        # World variables
        self.w_xmin = world[0]
        self.w_ymin = world[1]
        self.w_xmax = world[2]
        self.w_ymax = world[3]
        # Screen variables
        self.s_xmin = screen[0]
        self.s_ymin = screen[1]
        self.s_xmax = screen[2]
        self.s_ymax = screen[3]
        # Point transformation variables
        self.fx = -self.w_xmin
        self.fy = -self.w_ymin
        self.gx = self.width * self.s_xmin
        self.gy = self.height * self.s_ymin
        self.sx = ( self.width * (self.s_xmax - self.s_xmin) ) / (self.w_xmax - self.w_xmin)
        self.sy = ( self.height * (self.s_ymax - self.s_ymin) ) / (self.w_ymax - self.w_ymin)

        # Draw faces
        for i in range(0, len(faces)):
            # Line 1
            self.objects.append( canvas.create_line(
                ( (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][0]-1][0] ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][0]-1][1] ) ),
                ( (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][1]-1][0] ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][1]-1][1] ) )
            ))
            # Line 2
            self.objects.append( canvas.create_line(
                ( (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][1]-1][0] ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][1]-1][1] ) ),
                ( (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][2]-1][0] ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][2]-1][1] ) )
            ))
            # Line 3
            self.objects.append( canvas.create_line(
                ( (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][2]-1][0] ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][2]-1][1] ) ),
                ( (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][0]-1][0] ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][0]-1][1] ) )
            ))
            
        # Display Screen View
        self.objects.append( canvas.create_line(
            ( self.s_xmin * self.width, self.s_ymin * self.height ),
            ( self.s_xmin * self.width, self.s_ymax * self.height ),
            ( self.s_xmax * self.width, self.s_ymax * self.height ),
            ( self.s_xmax * self.width, self.s_ymin * self.height ),
            ( self.s_xmin * self.width, self.s_ymin * self.height )
        ))

    def redisplay( self, canvas, event ) :
        if self.objects :
            # Recompute values
            self.width = int(canvas.cget( "width" ))
            self.height = int(canvas.cget( "height" ))
            self.gx = self.width * self.s_xmin
            self.gy = self.height * self.s_ymin
            self.sx = ( self.width * (self.s_xmax - self.s_xmin) ) / (self.w_xmax - self.w_xmin)
            self.sy = ( self.height * (self.s_ymax - self.s_ymin) ) / (self.w_ymax - self.w_ymin)
            # Update face
            i=0
            while(i < len(self.objects)-1):
                self.canvas.coords(self.objects[ i ], 
                     (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][0]-1][0]), 
                     (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][0]-1][1]),
                     (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][1]-1][0]), 
                     (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][1]-1][1]))
                self.canvas.coords(self.objects[ i + 1],
                     (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][1]-1][0]), 
                     (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][1]-1][1]),
                     (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][2]-1][0]), 
                     (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][2]-1][1]))
                canvas.coords(self.objects[ i + 2 ],
                     (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][2]-1][0]), 
                     (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][2]-1][1]),
                     (self.fx * self.sx) + self.gx + (self.sx * self.vertices[self.faces[i][0]-1][0]), 
                     (self.fy * self.sy) + self.gy + (self.sy * self.vertices[self.faces[i][0]-1][1]))
                i += 3
            canvas.coords(self.objects[ -1 ],
                 self.s_xmin * self.width, self.s_ymin * self.height ,
                 self.s_xmin * self.width, self.s_ymax * self.height ,
                 self.s_xmax * self.width, self.s_ymax * self.height ,
                 self.s_xmax * self.width, self.s_ymin * self.height ,
                 self.s_xmin * self.width, self.s_ymin * self.height )

#----------------------------------------------------------------------
