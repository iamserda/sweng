def calculate_age(birth_year=0):
    while True:
        if not birth_year:
            print("\nEnter your year of birth(YYYY) or -1 to Exit.\n ex: 1970.")
            birth_year = input("$ ")
            if not birth_year.isdigit():
                continue

        birth_year = int(birth_year)
        if birth_year == -1:
            return birth_year

        age = 2025 - birth_year
        if age > 120:
            birth_year = 0
        else:
            decade = int(age / 10)
            year = age % 10
            return age, year, decade


for yob in [1983, 1984, 1985, 1993, 1998, 1999, 2003, 2010, 2015, 2018, 2020, 2022]:
    age, year, decade = calculate_age(yob)
    print(
        f"""You are {decade} {'decade' if decade < 2 else 'decades'} and {year} {'year' if year < 2 else 'years'} old or {age} {'year' if age < 2 else 'years'} old."""
    )
