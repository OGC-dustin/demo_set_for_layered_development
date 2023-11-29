# ----------------------------------------------------------------------------------------------------------------------
# OGC.Engineering
# fw_hal.py - redirection to actual firmware source files and definition of general haL functions needed software
# developer contact - dustin ( at ) ogc.engineering
# ----------------------------------------------------------------------------------------------------------------------

# can be used to redirect or directly define hardware abstractions
# in this example we are directly defining some basic abstractions to the binary status indicator
# import hardware descriptions
import hw_description
# import CSP resources
from machine import Pin

# ----------------------------------------------------------------------------------------------------------------------
#                                                                               User Interface - Status Indicator Binary
# ----------------------------------------------------------------------------------------------------------------------
status_indicator_binary = Pin( pin_ld2, Pin.OUT )

def init_status_indicator_binary():
    print( "fw_hal -> init_status_indicator_binary()" )
    status_indicator_binary.value( 0 )

def set_status_indicator_binary( state ):
    if ( state is False ):
        status_indicator_binary.value( 0 )
    else:
        status_indicator_binary.value( 1 )

# ----------------------------------------------------------------------------------------------------------------------
#                                                                               HAL generalize init and config functions
# ----------------------------------------------------------------------------------------------------------------------
def hal_init():
    print( "fw_hal -> hal_init()" )
    init_status_indicator_binary()

