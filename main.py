#! /bin/python3

import sys
from PyQt5.QtWidgets import QApplication

## ==> SPLASH SCREEN
from splashScreen import SplashScreen

## ==> APP Functions
from app_soring_functions import SortingAppFunctions
#from app_tree_functions import TreeAppFunctions

class MainWindowS(SortingAppFunctions):
    def __init__(self):
        super(MainWindowS, self).__init__()

class SplashScreenS(SplashScreen):
    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindowS()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

counter = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreenS()
    sys.exit(app.exec_())
