# Dalio, Brian A.
# dalioba
# 2018-03-28, v1.0
#----------------------------------------------------------------------
# https://en.wikipedia.org/wiki/Cohen-Sutherland_algorithm

INSIDE = 0
LEFT   = 1
RIGHT  = 2
BELOW  = 4
ABOVE  = 8

#------------------------------------------------------------
# clipLine( p1x, p1y, p2x, p2y, portal )
#   p1x, p1y -- the coordinates of point 1.
#   p2x, p2y -- the coordinates of point 2.
#   portal   -- a list of the viewport region limits
#               in this order:
#                 [ xmin, ymin, xmax, ymax ]
#
# returns ( doDraw, p1x, p1y, p2x, p2y )
#   doDraw   -- True if the line should be drawn, False if not.
#   p1x, p1y -- the new coordinates of point 1.
#   p2x, p2y -- the new coordinates of point 2.
#
def clipLine( p1x, p1y, p2x, p2y, portal ) :
  ( xMin, yMin, xMax, yMax ) = portal

  # In which region is each of the endpoints?
  p1Code = _regionCode( p1x, p1y, xMin, yMin, xMax, yMax )
  p2Code = _regionCode( p2x, p2y, xMin, yMin, xMax, yMax )

  # Loop until we have a definite accept or reject.
  while ( True ) :
    if ( ( p1Code | p2Code ) == 0 ) :
      # Both points have code 0000 and are therefore inside
      # the clipping region.  Trivial accept.
      doDraw = True
      break

    if ( ( p1Code & p2Code ) != 0 ) :
      # Both points outside on same side, either above, below,
      # left, or right of the region.  Trivial reject.
      doDraw = False
      break

    # Neither both out in a convenient way nor both in.  We have
    # to clip the line so that it's 'closer' to being out of the
    # region conveniently or entirely in the region.

    # Get the code of a point that is outside.  Both points
    # cannot be INSIDE (as we would have accepted above), so
    # if p1 in INSIDE, we use p2, otherwise p1.
    aRegionCode = p2Code if p1Code == INSIDE else p1Code

    # For that point, compute another point that is on the same
    # line, but at the corresponding edge of the region.

    if ( aRegionCode & ABOVE ) :
      # Point was ABOVE.  Move it along the line down to Y max.
      x = p1x + ( p2x - p1x )*( yMax - p1y )/( p2y - p1y )
      y = yMax

    elif ( aRegionCode & BELOW ) :
      # Point was BELOW.  Move it along the line up to Y min.
      x = p1x + ( p2x - p1x )*( yMin - p1y )/( p2y - p1y )
      y = yMin

    elif ( aRegionCode & RIGHT ) :
      # Point was to the RIGHT.  Move it along the line over to X max.
      x = xMax
      y = p1y + ( p2y - p1y )*( xMax - p1x )/( p2x - p1x )

    elif ( aRegionCode & LEFT ) :
      # Point was to the LEFT.  Move it along the line over to X min.
      x = xMin
      y = p1y + ( p2y - p1y )*( xMin - p1x )/( p2x - p1x )

    else :
      # Huh?  We didn't match _any_ region?  How did that happen?
      raise ValueError( 'code %s did not match any region?' % aRegionCode )

    # Replace whatever point we chose with the newly computed point.
    # We also have to recompute its region code.
    if ( aRegionCode == p1Code ) :
      # We were looking at p1.  Update its location and its code.
      p1x = x
      p1y = y
      p1Code = _regionCode( p1x, p1y, xMin, yMin, xMax, yMax )

    else :
      # We were looking at p2.  Update its location and its code.
      p2x = x
      p2y = y
      p2Code = _regionCode( p2x, p2y, xMin, yMin, xMax, yMax )

    # and now we do the loop again.

  # At this point, we have exited the loop and doDraw is True if
  # there's something to draw;  that is, if (eventually) there are
  # two points inside the draw region.
  # Either or both of p1 and p2 may have had their elements changed
  # so we have to return both to the caller.

  return ( doDraw, p1x, p1y, p2x, p2y )

#----------------------------------------------------------------------
# Computes the region code for the point x, y against the
# clipping region bounded by xMin, yMin, xMax, yMax.
def _regionCode( x, y, xMin, yMin, xMax, yMax ) :
  code = INSIDE

  # We use different bits for each 'side': LEFT, RIGHT, BELOW,
  # and ABOVE.  That way we can bitwise OR each bit in and still
  # keep them distinct.

  if ( x < xMin ) :
    code = code | LEFT
  elif ( x > xMax ) :
    code = code | RIGHT

  if ( y < yMin ) :
    code = code | BELOW
  elif ( y > yMax ) :
    code = code | ABOVE

  return code

#----------------------------------------------------------------------
# Some testing of Cohen-Sutherland.  For a known clipping region, it
# constructs lines both inside, outside, and across.  Each test checks
# doDraw and (where appropriate) the updated values of p1 and p2.
def _testCohenSutherland() :
  import itertools
  import time

  #----------------------------------------
  # The clipping region, otherwise known as INSIDE:  a
  # rectangle going from 1 to 3 in the X dimension and
  # 2 to 4 in the Y dimension.
  limits = ( 1, 2, 3, 4 )
  xMin, yMin, xMax, yMax = limits

  #----------------------------------------
  # Some categories of coordinates.
  # 21 points across the INSIDE region for x and y.
  xOK   = [ xMin ] + [ xMin + d/10.0 for d in range( 1, (xMax - xMin )*10 ) ] + [ xMax ]
  yOK   = [ yMin ] + [ yMin + d/10.0 for d in range( 1, (yMax - yMin )*10 ) ] + [ yMax ]

  # 4 points outside of INSIDE for each of the sides.
  xLOW  = [ xMin-1 ] + [ xMin-1 + d/4.0 for d in range( 1, 4 ) ]
  xHIGH = [ xMax + d/4.0 for d in range( 1, 5 ) ]
  yLOW  = [ yMin-1 ] + [ yMin-1 + d/4.0 for d in range( 1, 4 ) ]
  yHIGH = [ yMax + d/4.0 for d in range( 1, 5 ) ]

  # 29 points along each of x and y.
  xANY  = xLOW + xOK + xHIGH
  yANY  = yLOW + yOK + yHIGH

  #----------------------------------------
  # Some sets of points to be used in constructing test lines.
  # Points in the INSIDE region.
  OKPoints    = list( itertools.product( xOK, yOK ) )

  # Points to the LEFT (xLOWPoints) or RIGHT (xHIGHPoints)
  # of the INSIDE region.  Could be ABOVE, OK, or BELOW
  # along the y dimension.
  xLOWPoints  = list( itertools.product( xLOW, yANY ) )
  xHIGHPoints = list( itertools.product( xHIGH, yANY ) )

  # Points ABOVE (yHIGHPoints) or BELOW (yLOWPoints) the
  # INSIDE region.  Could be LEFT, OK, or RIGHT along
  # the x dimension.
  yLOWPoints  = list( itertools.product( xANY, yLOW ) )
  yHIGHPoints = list( itertools.product( xANY, yHIGH ) )

  # Points OK in the y dimension but anywhere along the
  # x dimension (horMiddle).  Points OK in the x
  # dimension but anywhere along the y dimension (verMiddle).
  horMiddle   = list( itertools.product( xANY, yOK ) )
  verMiddle   = list( itertools.product( xOK, yANY ) )

  # As long as the LOW and HIGH sets are 'close enough' to
  # the clipping region edges, points in the diagonally-
  # across regions will define a line that crosses the
  # INSIDE.
  lowerLeft   = list( itertools.product( xLOW, yLOW ) )
  lowerRight  = list( itertools.product( xHIGH, yLOW ) )
  upperLeft   = list( itertools.product( xLOW, yHIGH ) )
  upperRight  = list( itertools.product( xHIGH, yHIGH ) )

  #----------------------------------------
  # Trivial accept tests: Both points inside region.  Should get
  # doDraw True and unchanged points.
  numTests  = 0
  numErrors = 0
  startTime = time.time()

  for p1 in OKPoints :
    for p2 in OKPoints :
      numTests += 1

      ( doDraw, p1x, p1y, p2x, p2y ) = clipLine( p1[0], p1[1], p2[0], p2[1], limits )
      if ( not doDraw ) :
        print( 'For OK points %s, %s, doDraw was False.' % ( p1, p2 ) )
        numErrors += 1

      if ( p1 != ( p1x, p1y ) ) :
        print( 'For OK points %s, %s, p1 came back ( %s, %s ).' % ( p1, p2, p1x, p1y ) )
        numErrors += 1

      if ( p2 != ( p2x, p2y ) ) :
        print( 'For OK points %s, %s, p2 came back ( %s, %s ).' % ( p1, p2, p2x, p2y ) )
        numErrors += 1

  elapsedTime = time.time() - startTime
  perTest     = 1000000 * elapsedTime / numTests
  print( '%d error%s detected in %s trivial accept tests. %.2fS, %.2fμS/test.' % (
    numErrors, '' if numErrors == 1 else 's', numTests, elapsedTime, perTest ) )

  #----------------------------------------
  # Both points on same side.  Should be trivial reject.  Doesn't
  # matter what point values are returned as the line isn't drawn.
  numTests  = 0
  numErrors = 0
  startTime = time.time()

  for ( testName, points ) in [
    ( 'X Low', xLOWPoints ), ('X High', xHIGHPoints ),
    ( 'Y Low', yLOWPoints ), ( 'Y High', yHIGHPoints ) ] :

    for p1 in points :
      for p2 in points :
        numTests += 1

        ( doDraw, p1x, p1y, p2x, p2y ) = clipLine( p1[0], p1[1], p2[0], p2[1], limits )
        if ( doDraw ) :
          print( 'For Same Side test %s points %s, %s, doDraw was True ( %s, %s ), ( %s, %s ).' % (
            testName, p1, p2, p1x, p1y, p2x, p2y ) )
          numErrors += 1

  elapsedTime = time.time() - startTime
  perTest     = 1000000 * elapsedTime / numTests
  print( '%d error%s detected in %s trivial reject tests. %.2fS, %.2fμS/test.' % (
    numErrors, '' if numErrors == 1 else 's', numTests, elapsedTime, perTest ) )

  #----------------------------------------
  # Points are on opposite sides of the clipping region in such a
  # way that the line intersects INSIDE.  Therefore, a line should
  # be drawn and the points will be moved.
  numTests  = 0
  numErrors = 0
  startTime = time.time()

  for ( testName, points1, points2 ) in [
    ( 'Horizontal Middle', horMiddle, horMiddle ), ('Vertical Middle', verMiddle, verMiddle ),
    ( 'Diag UR-LL', upperRight, lowerLeft ), ( 'Diag LR-UL', lowerRight, upperLeft ),
    ( 'Diag LL-UR', lowerLeft, upperRight ), ( 'Diag UL-LR', upperLeft, lowerRight ) ] :

    for p1 in points1 :
      for p2 in points2 :
        p1Code = _regionCode( p1[0], p1[1], xMin, yMin, xMax, yMax )
        p2Code = _regionCode( p2[0], p2[1], xMin, yMin, xMax, yMax )

        if ( (p1Code | p2Code) == 0 or (p1Code & p2Code != 0 ) ) :
          # Don't bother with any the trivial accept / rejects.
          continue

        numTests += 1

        ( doDraw, p1x, p1y, p2x, p2y ) = clipLine( p1[0], p1[1], p2[0], p2[1], limits )
        if ( doDraw ) :
          # Correct!  The line is to be drawn.  Now see if the points are OK.
          ( shouldBeP1, shouldBeP2 ) = _directClipLine( p1, p2, xMin, yMin, xMax, yMax )

          if ( _pointsMatch( shouldBeP1, ( p1x, p1y ) ) ) :
            # Cohen's p1 matches what we expect for p1.
            # Cohen's p2 should match what we expect for p2.
            if ( not _pointsMatch( shouldBeP2, ( p2x, p2y ) ) ) :
              # Hmm, one point matched, but the other didn't.  Error.
              print( '(%s) ① For Opposite Side test %s points %s, %s,'
                '\npoints do not match expected ( %s, %s ), ( %s, %s ) ≠ ( %s, %s ), ( %s, %s ).' % (
                numTests, testName, p1, p2, p1x, p1y, p2x, p2y, shouldBeP1[0], shouldBeP1[1], shouldBeP2[0], shouldBeP2[1] ) )
              numErrors += 1

          elif ( _pointsMatch( shouldBeP1, ( p2x, p2y ) ) ) :
            # Cohen's p2 matches what we expect for p1.
            # Cohen's p1 should match what we expect for p2.
            if ( not _pointsMatch( shouldBeP2, ( p1x, p1y ) ) ) :
              # Hmm, one point matched, but the other didn't.  Error.
              print( '(%s) ② For Opposite Side test %s points %s, %s,'
                '\npoints do not match expected ( %s, %s ), ( %s, %s ) ≠ ( %s, %s ), ( %s, %s ).' % (
                numTests, testName, p1, p2, p1x, p1y, p2x, p2y, shouldBeP1[0], shouldBeP1[1], shouldBeP2[0], shouldBeP2[1] ) )
              numErrors += 1

          else :
            # Neither of Cohen's points match what we expect for p1.
            print( '(%s) ③ For Opposite Side test %s points %s, %s,'
              '\npoints do not match expected ( %s, %s ), ( %s, %s ) ≠ ( %s, %s ), ( %s, %s ).' % (
              numTests, testName, p1, p2, p1x, p1y, p2x, p2y, shouldBeP1[0], shouldBeP1[1], shouldBeP2[0], shouldBeP2[1] ) )
            numErrors += 1

        else :
          # Error!
          print( '(%s) For Opposite Side test %s points %s, %s,\ndoDraw was False ( %s, %s ), ( %s, %s ).' % (
            numTests, testName, p1, p2, p1x, p1y, p2x, p2y ) )
          numErrors += 1

  elapsedTime = time.time() - startTime
  perTest     = 1000000 * elapsedTime / numTests
  print( '%d error%s detected in %s opposite side tests. %.2fS, %.2fμS/test.' % (
    numErrors, '' if numErrors == 1 else 's', numTests, elapsedTime, perTest ) )

#----------------------------------------------------------------------
# Given two points that are guaranteed to have at least a portion
# of the line segment they define displayed, this routine calculates
# the end points of what should be drawn.
# We make use of the fact that at least some portion of the line is
# drawn, so ensure that is true when when using this routine.
# This routine calculates the drawn portion of the line using a
# different algorithm than Cohen-Sutherland so it can be used as a
# check against it.  Since the floating-point math is different, the
# final calculated values for p1 and p2 might differ by some small
# value, so don't compare the points directly for equality.
def _directClipLine( p1, p2, xMin, yMin, xMax, yMax ) :
  if ( p1[0] == p2[0] ) :
    # Vertical line.  The points have the same x coordinate
    # and the y coordinates should be whatever's inside the
    # clipping region or snap to the edges.
    shouldBeP1 = ( p1[0], max( min( p1[1], p2[1] ), yMin ) )
    shouldBeP2 = ( p1[0], min( max( p1[1], p2[1] ), yMax ) )

  elif ( p1[1] == p2[1] ) :
    # Horizontal line.  The points have the same y coordinate
    # and the x coordinates should be whatever's inside th
    # clipping region or snap to the edges.
    shouldBeP1 = ( max( min( p1[0], p2[0] ), xMin ), p1[1] )
    shouldBeP2 = ( min( max( p1[0], p2[0] ), xMax ), p1[1] )

  else :
    # Not vertical or horizontal line.  Have to 'do math' to get
    # the points.  We know the slope and the intercept exist
    # because the line is not vertical.
    slope = ( p1[1] - p2[1] )/( p1[0] - p2[0] )
    intercept = p1[1] - slope*p1[0]

    # Helper functions to get y from x and x from y
    # given the just-computed slope and intercept.
    def yFromX( x ) :
      return slope * x + intercept

    def xFromY( y ) :
      return ( y - intercept )/slope

    # Determine the left-most x value in the clipping
    # region for the given line and its corresponding
    # y value.  (This x value might be the same as the
    # right-most one we will find below.)
    leastX    = max( min( p1[0], p2[0] ), xMin )
    leastXY   = yFromX( leastX )

    # Snap the corresponding y value to an edge of the
    # clipping region if it's out of bounds and get the
    # x value that corresponds to it.  (We know this works
    # because the two points are guaranteed to have at
    # least some portion of their line visible.)
    if ( leastXY > yMax ) :
      leastX  = xFromY( yMax )
      leastXY = yMax

    if ( leastXY < yMin ) :
      leastX  = xFromY( yMin )
      leastXY = yMin

    # Determine the right-most x value in the clipping
    # region for the given line and its corresponding
    # y value.  (This x value might be the same as the
    # left-most one we just found above.)
    greatestX = min( max( p1[0], p2[0] ), xMax )
    greatestXY   = yFromX( greatestX )

    # Snap the corresponding y value to an edge of the
    # clipping region if it's out of bounds and get the
    # x value that corresponds to it.  (We know this works
    # because the two points are guaranteed to have at
    # least some portion of their line visible.)
    if ( greatestXY > yMax ) :
      greatestX  = xFromY( yMax )
      greatestXY = yMax

    if ( greatestXY < yMin ) :
      greatestX  = xFromY( yMin )
      greatestXY = yMin

    # These two points might be the same, but that's OK.
    shouldBeP1 = ( leastX, leastXY )
    shouldBeP2 = ( greatestX, greatestXY )

  return ( shouldBeP1, shouldBeP2 )

#----------------------------------------------------------------------
# Since we do a bunch of floating-point math in different patterns,
# we can't expect the coordinates to come out identically.  We have to
# test 'equality' as meaning 'within a certain epsilon'.
def _pointsMatch( p1, p2 ) :
  EPSILON = 1e-13

  xMatch = abs( p1[0] - p2[0] ) < EPSILON
  yMatch = abs( p1[1] - p2[1] ) < EPSILON

  return xMatch and yMatch

#----------------------------------------------------------------------
# If we get run as a standalone file, just do the unit testing.
if ( __name__ == '__main__' ) :
  _testCohenSutherland()

#----------------------------------------------------------------------
