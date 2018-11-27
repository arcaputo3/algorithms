import math

def clock_angles(time):
    time = time.split(':')
    hr, min = time[0],time[-1]
    if hr == '12':
        hr = 0
    else:
        hr = int(hour)
