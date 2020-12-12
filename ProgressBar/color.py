
class textManage:
    def __init__(self):

        # ANSI escape codes for text settings
        self.text = {
        "clear": "\033[K",
        "reset" : '\033[0m',
        "bold" : '\033[01m',
        "disable" : '\033[02m',
        "underline" : '\033[04m',
        "reverse" : '\033[07m',
        "strikethrough" : '\033[09m',
        "invisible" : '\033[08m',
        }

        # ANSI escape codes for text colors
        self.fgColors = {
        "black": '\033[30m',
        "red": '\033[31m',
        "green": '\033[32m',
        "orange": '\033[33m',
        "blue": '\033[34m',
        "purple": '\033[35m',
        "cyan": '\033[36m',
        "lightgrey": '\033[37m',
        "darkgrey": '\033[90m',
        "lightred": '\033[91m',
        "lightgreen": '\033[92m',
        "yellow": '\033[93m',
        "lightblue": '\033[94m',
        "pink": '\033[95m',
        "lightcyan": '\033[96m',
        }

        # ANSI escape codes for background colors
        self.bgColors = {
        "black": '\033[40m',
        "red": '\033[41m',
        "green": '\033[42m',
        "orange": '\033[43m',
        "blue": '\033[44m',
        "purple": '\033[45m',
        "cyan": '\033[46m',
        "lightgrey": '\033[47m',
        }

    def colorText(self,text,fg="black",bg=None):
        if bg != None:
            return self.fgColors[fg]+text+self.bgColors[bg]
        else:
            return self.fgColors[fg]+text+self.text["reset"]