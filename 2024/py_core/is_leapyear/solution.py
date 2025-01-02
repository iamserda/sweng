def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Error: not an integer...")
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return True


# TEST ARENA
# years = [year for year in range(2000, 2025)]
# leap = []
# for year in years:
#     try:
#         assert is_leap_year(year) == True
#         leap.append(year)
#     except AssertionError:
#         pass
# print(f"Leap years [2000-2024]: {leap}")
