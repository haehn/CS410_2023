
  class Logger:

  	instance = None

  	def __init__(self):

  		self.file = None
  		self.file = open('log.txt', 'w')

    def close(self):
    	self.file.close()

  @staticmethod
  def print(event):

  	if not Logger.instance:
  		Logger.instance = Logger()

  	Logger.instance.file.write(event)

  	# with open('log.txt', 'w') as f:
  	# 	f.write(event+'\n')
