from .loading import customLoad
from .color import textManage
import multiprocessing as mp
import time
import sys
from .cursor import hide
from .cursor import show


class loadingDots(customLoad):
    """
    Use as context manger to start a process for showing a loading dots as the interior code runs

    Attributes
    ----------
    n_dots : int
        Says how many dots to print in a line

    Methods
    -------
    spin(self)
        Outputs loading bar

    spinTrack(self)
        Generator to track which symbol goes next into progress bar

    clear(self)
        Clears output from screen
    """

    def __init__(self, width=30, text_color="black", text_bg=None):
        self.name = 'dots'
        self.width = width
        self.text_color = text_color
        self.text_bg = text_bg
        self.track_i = 0
        self.spin_on = True
        self.c = textManage()

    def __enter__(self):
        hide()
        self.p = mp.Process(target=self.showBar)
        self.p.start()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.p.terminate()
        self.p.join()
        self.clear()
        show()

    def showBar(self):
        """Manage output of progress bar"""
        track = 0
        dot_symbols = [" " for i in range(self.width)]
        sys.stdout.write("{}".format(''.join(dot_symbols)) + "\r")
        while self.spin_on == True:
            dot_symbols[track] = "."
            sys.stdout.write("{}".format(self.c.colorText(''.join(dot_symbols), fg=self.text_color)) + "\r")
            time.sleep(.5)
            track += 1
            if track == self.width:
                dot_symbols = [" " for i in range(self.width)]
                track = 0
                sys.stdout.flush()
                sys.stdout.write(self.c.text["clear"])
                sys.stdout.write("" + "\r")
                time.sleep(.5)


if __name__ == "__main__":
    with loadingDots(width=3, text_color="purple") as f:
        print("Testing loadingDots")
        time.sleep(10)
