# ----------------------------------------------------------------------------------------------------------------------
# OGC.Engineering
# sw_app.py - redirection to actual app source file and definition of general app functions needed by main.py
# developer contact - dustin ( at ) ogc.engineering
# ----------------------------------------------------------------------------------------------------------------------

# import actual app source ( a demo in this case )
import sw_app__demo

# ----------------------------------------------------------------------------------------------------------------------
#                                                                               APP generalize init and config functions
# ----------------------------------------------------------------------------------------------------------------------
def app_init():
    print( "sw_app -> app_init()" )
    sw_app__init()

def app_start():
    print( "sw_app -> app_start()" )
    sw_app__start()