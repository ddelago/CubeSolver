# Dalio, Brian A.
# dalioba
# 2018-04-05
#------------------------------------------------------------
import numpy as np

#------------------------------------------------------------
# A simple script to help you test your implementation of the
# Euler angle rotation.
# Change the lines in this section to reflect the Euler angles
# you want to use, the center of the object, and the points
# that should be transformed.
# Then run this script with the command,
#    python3 EulerRotation.py
# It will print the r00 through r22 and ax, ay, az values
# and then the transformations of the points.
# All displayed values are _rounded to three places_.

# With the default values, you should see this output,
#
# For ϕ   0.785 (  45.000°), θ   0.524 (  30.000°), ψ   0.000 (   0.000°),
#   r00   0.866, r01  -0.000, r02   0.500
#   r10   0.354, r11   0.707, r12  -0.612
#   r20  -0.354, r21   0.707, r22   0.612
#
# For t = (   4.000,   8.000,  12.000 ),
#   ax   -5.464, ay    8.277, az    0.409
#
# Some point transformations,
# (   1.000,   2.000,   3.000 ) -> (  -3.098,   8.208,   3.307 )
# (   4.000,   5.000,   6.000 ) -> (   1.000,   9.553,   6.204 )
# (   7.000,   8.000,   9.000 ) -> (   5.098,  10.898,   9.102 )

#-----
# The Euler angles, in radians.
phi, theta, psi = ( np.pi/4, np.pi/6, 0 )

#-----
# The object center.
tx, ty, tz  = ( 4, 8, 12 )

#-----
# The points to transform.
points = [
  ( 1, 2, 3 ),
  ( 4, 5, 6 ),
  ( 7, 8, 9 )
]

#------------------------------------------------------------
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
print( 'For ϕ %7.3f (%8.3f°), θ %7.3f (%8.3f°), ψ %7.3f (%8.3f°),' % (
  phi, np.rad2deg( phi ), theta, np.rad2deg( theta ), psi, np.rad2deg( psi ) ) )
print( '  r00 %7.3f, r01 %7.3f, r02 %7.3f' % ( r00, r01, r02 ) )
print( '  r10 %7.3f, r11 %7.3f, r12 %7.3f' % ( r10, r11, r12 ) )
print( '  r20 %7.3f, r21 %7.3f, r22 %7.3f' % ( r20, r21, r22 ) )

#------------------------------------------------------------
# Step Two -- Compute the ax, ay, and az values.
ax  = -r00*tx - r01*ty - r02*tz + tx
ay  = -r10*tx - r11*ty - r12*tz + ty
az  = -r20*tx - r21*ty - r22*tz + tz

# Display the ax, ay, and az values _rounded to three places_.
print()
print( 'For t = ( %7.3f, %7.3f, %7.3f ),' % ( tx, ty, tz) )
print( '  ax  %7.3f, ay  %7.3f, az  %7.3f' % ( ax, ay, az ) )

#------------------------------------------------------------
# Step Three -- Transform the points.
print()
print( 'Some point transformations,' )

for x, y, z in points :
  xp  = r00*x + r01*y + r02*z + ax
  yp  = r10*x + r11*y + r12*z + ay
  zp  = r20*x + r21*y + r22*z + az

  print( '( %7.3f, %7.3f, %7.3f ) -> ( %7.3f, %7.3f, %7.3f )' % ( x, y, z, xp, yp, zp ) )
#------------------------------------------------------------
