# Delago, Daniel
# 100-106-0927
# 2018-01-18

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been somewhat modified and updated by Brian A. Dalio for use
# in CSE 4303 / CSE 5365 in the 2018 Spring semester.

#----------------------------------------------------------------------
import numpy as np
import copy
import CohenSutherland

class cl_world :
    def __init__( self, objects = [], canvases = [] ) :
        self.objects = objects
        self.canvases = canvases

    def add_canvas( self, canvas ) :
        self.canvases.append( canvas )
        canvas.world = self

    def clear_canvas( self, canvas ) :
        canvas.delete( "all" )

    def create_graphic_objects( self, canvas, vertices, faces, world, screen, euler_angles, object_center ) :
        self.objects = []
        # Variables
        self.vertices = copy.deepcopy(vertices)
        self.vertices = self.euler_rotation(self.vertices, euler_angles, object_center)
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
            # Apply Cohen Sutherland Algorithm before drawing
            do_draw, x1, y1, x2, y2 = self.check_cohen_sutherland( self.vertices[self.faces[i][0]-1][0], self.vertices[self.faces[i][0]-1][1], 
                                                                   self.vertices[self.faces[i][1]-1][0], self.vertices[self.faces[i][1]-1][1])
            if do_draw: 
                self.objects.append( canvas.create_line(x1, y1, x2, y2))

            # Line 2
            # Apply Cohen Sutherland Algorithm before drawing
            do_draw, x1, y1, x2, y2 = self.check_cohen_sutherland( self.vertices[self.faces[i][1]-1][0], self.vertices[self.faces[i][1]-1][1], 
                                                                   self.vertices[self.faces[i][2]-1][0], self.vertices[self.faces[i][2]-1][1]) 
            if do_draw:
                self.objects.append( canvas.create_line(x1, y1, x2, y2))

            # Line 3
            # Apply Cohen Sutherland Algorithm before drawing
            do_draw, x1, y1, x2, y2 = self.check_cohen_sutherland( self.vertices[self.faces[i][2]-1][0], self.vertices[self.faces[i][2]-1][1], 
                                                                   self.vertices[self.faces[i][0]-1][0], self.vertices[self.faces[i][0]-1][1])
            if do_draw:
                self.objects.append( canvas.create_line(x1, y1, x2, y2))
            
        # Display Screen View
        self.objects.append( canvas.create_line(
            ( self.s_xmin * self.width, self.s_ymin * self.height ),
            ( self.s_xmin * self.width, self.s_ymax * self.height ),
            ( self.s_xmax * self.width, self.s_ymax * self.height ),
            ( self.s_xmax * self.width, self.s_ymin * self.height ),
            ( self.s_xmin * self.width, self.s_ymin * self.height )
        ))

    def euler_rotation( self, vertices, euler_angles, object_center ):
        # The Euler angles. Convert from degree to radians
        phi, theta, psi = ( np.radians(euler_angles[0]), np.radians(euler_angles[1]), np.radians(euler_angles[2]) )

        # The object center.
        tx, ty, tz  = ( object_center[0], object_center[1], object_center[2] )

        # The points to transform.
        points = vertices

        # Step One -- Compute the r00 through r22 values.
        # First, get the cosine and sine values for the Euler angles.
        cosPhi,   sinPhi   = np.cos( phi ),   np.sin( phi )
        cosTheta, sinTheta = np.cos( theta ), np.sin( theta )
        cosPsi,   sinPsi   = np.cos( psi ),   np.sin( psi )

        # Now, compute the nine r values.
        # These four factors get used twice, so reuse them to save
        # four multiplications.
        cPhiXcPsi = cosPhi*cosPsi
        cPhiXsPsi = cosPhi*sinPsi
        sPhiXcPsi = sinPhi*cosPsi
        sPhiXsPsi = sinPhi*sinPsi

        # The r00 through r22 values.
        r00 = cosPsi * cosTheta
        r01 = -cosTheta * sinPsi
        r02 = sinTheta

        r10 = cPhiXsPsi + sPhiXcPsi*sinTheta
        r11 = cPhiXcPsi - sPhiXsPsi*sinTheta
        r12 = -cosTheta*sinPhi

        r20 = -cPhiXcPsi*sinTheta + sPhiXsPsi
        r21 = cPhiXsPsi*sinTheta + sPhiXcPsi
        r22 = cosPhi*cosTheta

        # Display the r values _rounded to three places_.
        # print( 'For ϕ %7.3f (%8.3f°), θ %7.3f (%8.3f°), ψ %7.3f (%8.3f°),' % (
        #   phi, np.rad2deg( phi ), theta, np.rad2deg( theta ), psi, np.rad2deg( psi ) ) )
        # print( '  r00 %7.3f, r01 %7.3f, r02 %7.3f' % ( r00, r01, r02 ) )
        # print( '  r10 %7.3f, r11 %7.3f, r12 %7.3f' % ( r10, r11, r12 ) )
        # print( '  r20 %7.3f, r21 %7.3f, r22 %7.3f' % ( r20, r21, r22 ) )

        # Step Two -- Compute the ax, ay, and az values.
        ax  = -r00*tx - r01*ty - r02*tz + tx
        ay  = -r10*tx - r11*ty - r12*tz + ty
        az  = -r20*tx - r21*ty - r22*tz + tz

        # Display the ax, ay, and az values _rounded to three places_.
        # print()
        # print( 'For t = ( %7.3f, %7.3f, %7.3f ),' % ( tx, ty, tz) )
        # print( '  ax  %7.3f, ay  %7.3f, az  %7.3f' % ( ax, ay, az ) )

        # Step Three -- Transform the points.
        points[:] =[[r00*x + r01*y + r02*z + ax, r10*x + r11*y + r12*z + ay, r20*x + r21*y + r22*z + az] for x, y, z in points]
        
        return points

    def check_cohen_sutherland(self, x1,y1,x2,y2):
        return(
            CohenSutherland.clipLine(
                ( (self.fx * self.sx) + self.gx + (self.sx * x1 ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * y1 ) ),
                ( (self.fx * self.sx) + self.gx + (self.sx * x2 ) ), 
                ( (self.fy * self.sy) + self.gy + (self.sy * y2 ) ),
                [self.s_xmin * self.width, self.s_ymin * self.height, self.s_xmax * self.width, self.s_ymax * self.height]
            )
        )

    def redisplay( self, canvas, event ) :
        if self.objects :
            # Recompute values
            self.width = int(canvas.cget( "width" ))
            self.height = int(canvas.cget( "height" ))
            self.gx = self.width * self.s_xmin
            self.gy = self.height * self.s_ymin
            self.sx = ( self.width * (self.s_xmax - self.s_xmin) ) / (self.w_xmax - self.w_xmin)
            self.sy = ( self.height * (self.s_ymax - self.s_ymin) ) / (self.w_ymax - self.w_ymin)
            # Update faces
            canvas.coords(self.objects[ -1 ],
                 self.s_xmin * self.width, self.s_ymin * self.height ,
                 self.s_xmin * self.width, self.s_ymax * self.height ,
                 self.s_xmax * self.width, self.s_ymax * self.height ,
                 self.s_xmax * self.width, self.s_ymin * self.height ,
                 self.s_xmin * self.width, self.s_ymin * self.height )
            i = 0
            while(i < len(self.faces)):
                # Line 1
                do_draw, x1, y1, x2, y2 = self.check_cohen_sutherland( self.vertices[self.faces[i][0]-1][0], self.vertices[self.faces[i][0]-1][1], 
                                                                       self.vertices[self.faces[i][1]-1][0], self.vertices[self.faces[i][1]-1][1])
                if do_draw:
                    canvas.coords(self.objects[ i*3 ], x1, y1, x2, y2)

                # Line 2
                do_draw, x1, y1, x2, y2 = self.check_cohen_sutherland( self.vertices[self.faces[i][1]-1][0], self.vertices[self.faces[i][1]-1][1], 
                                                                       self.vertices[self.faces[i][2]-1][0], self.vertices[self.faces[i][2]-1][1]) 
                if do_draw:
                    canvas.coords(self.objects[ i*3 + 1 ], x1, y1, x2, y2)

                # Line 3
                do_draw, x1, y1, x2, y2 = self.check_cohen_sutherland( self.vertices[self.faces[i][2]-1][0], self.vertices[self.faces[i][2]-1][1], 
                                                                       self.vertices[self.faces[i][0]-1][0], self.vertices[self.faces[i][0]-1][1])
                if do_draw:
                    canvas.coords(self.objects[ i*3 + 2 ], x1, y1, x2, y2)
                i += 1
            

#----------------------------------------------------------------------
