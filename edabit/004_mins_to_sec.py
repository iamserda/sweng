def minutes_to_secconds(minutes: int = 0):
    if minutes > 0:
        return minutes * 60
    else:
        return 0


assert minutes_to_secconds(1) == 60
assert minutes_to_secconds(100) == 60
