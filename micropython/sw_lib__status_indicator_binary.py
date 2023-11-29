# ----------------------------------------------------------------------------------------------------------------------
# OGC.Engineering
# sw_lib__status_indicator_binary.py - software library proving sequencing for a binary status indicator
# developer contact - dustin ( at ) ogc.engineering
# ----------------------------------------------------------------------------------------------------------------------

# states:
#     OFF - static state, indicator turned off
#     ON - static state, indicator turned on
#     PULSE - continuous dynamic state, indicator blinking OFF and ON at a 50% duty cycle, rates range TBD, until interrupted
#     HEARTBEAT - continuous dynamic state, producing the classic bump, bump, pause of a heartbeat until interrupted
#     ERROR - dynamic state, slow, fast, slow code sequence that cycles a prescribed number of times ( or infinate )
#           digits limited between 1 and 9, typically major system, minor subsystem, detail error number
#     FATAL - dynamic state, fast, slow, fast code sequence that cycles a prescribed number of times ( or infinate )
#           digits limited between 1 and 9, typically major system, minor subsystem, detail error number
