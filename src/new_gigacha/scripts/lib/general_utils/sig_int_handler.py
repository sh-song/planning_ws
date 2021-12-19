import sys
import signal

class Activate_Signal_Interrupt_Handler:
    def __init__(self):
        
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, sig, frame):
        print('\nYou pressed Ctrl+C! Never use Ctrl+Z!')
        sys.exit(0)


