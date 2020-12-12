from .loading import customLoad
from .color import textManage
import multiprocessing as mp
import time
import sys
from .cursor import hide
from .cursor import show


class loadingBar(customLoad):
    """
    Use as context manger to start a process for showing a loading bar as the interior code runs

    Attributes
    ----------
    widthbar : int
        Says how long loading bar should be

    Methods
    -------
    spin(self)
        Outputs loading bar

    spinTrack(self)
        Generator to track which symbol goes next into progress bar

    clear(self)
        Clears output from screen
    """

    def __init__(self, width=30, text_color="black"):
        self.name = 'bar'
        self.width = width
        self.text_color = text_color
        self.spin_track_i = 0
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
        spin_symbols = [" " for i in range(self.width)]
        sys.stdout.write("{}".format(self.c.colorText("[" + ''.join(spin_symbols) + "]", fg=self.text_color)) + "\r")
        while self.spin_on == True:
            time.sleep(.5)
            spin_symbols[track] = self.spinTrack()
            sys.stdout.write(
                "{}".format(self.c.colorText("[" + ''.join(spin_symbols) + "]", fg=self.text_color)) + "\r")
            sys.stdout.flush()
            track += 1
            if track == self.width:
                sys.stdout.flush()
                spin_symbols = [" " for i in range(self.width)]
                track = 0
                sys.stdout.write(self.c.text["clear"])
                sys.stdout.write("{}{}{}".format("[", ''.join(spin_symbols), "]") + "\r")
                time.sleep(.5)

    def spinTrack(self):
        """Tracks what symbol to push next"""
        if self.spin_track_i == 0:
            self.spin_track_i += 1
            return "|"
        elif self.spin_track_i == 1:
            self.spin_track_i += 1
            return "/"
        elif self.spin_track_i == 2:
            self.spin_track_i += 1
            return "-"
        elif self.spin_track_i == 3:
            self.spin_track_i += 1
            return "|"
        elif self.spin_track_i == 4:
            self.spin_track_i = 0
            return "\\"


if __name__ == "__main__":
    with loadingBar(width=6, text_color="lightgreen") as f:
        time.sleep(10)
