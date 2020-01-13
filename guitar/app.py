from guitar.common.metronome import Metronome

def run():
	metronome = MetronomeT()
	metronome.start()
	input('Press ENTER to cancel:')
	metronome.cancel()
	print('Program complete.')
