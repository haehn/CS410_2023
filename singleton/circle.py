class Circle:

  instance = None

  def __init__(self):
    '''
    Creates a new circle.
    '''
    self.__radius = 7
    self.__radius2 = 5

    print('created new circle')

  def getRadius(self):
    '''
    '''
    return self.__radius

  def setRadius(self, radius):
    '''
    Update radius 1 to either 7 or 8.

    @param radius the new radius
    ''' 
    if radius == 7 or radius == 8:
    	self.__radius = radius
    else:
    	raise Exception('invalid value')

  def draw(self):

   return 'O'*self.__radius

  @staticmethod
  def getInstance():

  	# lazy loading
    if not Circle.instance:
      Circle.instance = Circle()

    return Circle.instance





