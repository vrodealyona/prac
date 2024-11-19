class Sender:
	_count = True
	@classmethod
	def report(*args):
		if Sender._count:
			print("Greeting!")
			Sender._count = False
		else:
			print("Get away!")
class Asker:
	@staticmethod
	def askall(lst):
		for i in lst:
			i.report()
			
check = [Sender(), Sender(), Sender()]
a = Asker()
a.askall(check)
