from random import  randint

def get_temp(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_preassure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 780)

def get_wind_speed(sensor):
    if sensor == 1:
        return  randint(0, 30)
    else:
        return  randint(30, 60)

