import time
from ProgressBar.loadingBar import loadingBar
from ProgressBar.loadingDots import loadingDots

if __name__ == "__main__":
    with loadingBar(width=6, text_color="lightgreen") as f:
        print("Testing loadingBar")
        time.sleep(10)

    with loadingDots(width=3, text_color="purple") as f:
        print("Testing loadingDots")
        time.sleep(10)