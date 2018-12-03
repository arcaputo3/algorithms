def time_angle(time):
    """ Returns the angle between the minute hand and hour hand.
    Args:
        time:   str represented as 'HH:MM:SS'
    Returns:
        Angle between minute hand and hour hand.
    """
    # Get each time measurement
    time = time.split(':')
    hr, min, sec = time[0], int(time[1]), int(time[2])
    # Correct for 12 indexed
    if hr == '12':
        hr = 0
    else:
        hr = int(hr)
    # Get each angle
    hr_hand_angle = (hr + min/60 + sec/3600)*30
    min_hand_angle = (min + sec/60)*6
    # Get angle between
    angle = abs(hr_hand_angle - min_hand_angle)
    # Correct if over 180 degrees
    return angle if angle <= 180 else 360 - angle

print(time_angle("05:24:00"))
