class UI:

  def __init__(self):
  	pass

  def run(self, controller):

    print('Please enter 2 numbers')

    n1 = float(input('Number 1 ?'))

    n2 = float(input('Number 2 ?'))
    
    return controller.add(n1, n2)
     
