from threading import Timer,Thread,Event 
from playsound import playsound

class Metronome(Thread):
	max_bpm = 260
	min_bpm = 40
	_soundfile = 'guitar/resources/click.wav'
	
	def beat(self):
		playsound(self._soundfile)
		print('Beat method invoked.')
		
	def __init__(self, tempo=80):
		self._tempo = tempo
		self._timer = Timer(_tempo/60.0, beat)
		self._stop_event = threading.Event()
		print(f'Metronome instantiated w/ tempo of {tempo} bpm.')

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		return _stop_event.is_set()
	
	def run():
		_timer.start()
