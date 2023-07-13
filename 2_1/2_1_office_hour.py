
"""

    Vehicle Types:
        private ( cars, trucks )
        public ( busses )
        emergency ( ambulance, fire )
        human ( bicycle )

    Lights:
        green
        yellow
        red
        white

    Rules:
        Only public and emergency vehicles can go through white lights
        Emergency vehicles must slow down to 20 when coming to a red light and 30 for yellow and white lights. 
            Otherwise, they do not need to slow down.
        Public vehicles must stop at green and yellow lights
        Private vehicles must slow down to 20 at yellow lights. Except for emergency vehicles, all others must stop

"""

speed = 5
vehicle_type = "human"
light_color = "yellow"

if speed > 0:
    pass

print(f"The speed is: {speed}")