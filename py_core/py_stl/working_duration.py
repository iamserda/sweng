from datetime import datetime, timedelta

jan1 = datetime(year=2025, month=1, day=1)
current_datetime = datetime.now()
days_since_jan1 = current_datetime - jan1
print(f"There has been {days_since_jan1} since {jan1.strftime("%d/%m/%Y")}")
xmas = datetime(2025, 12, 25)
until_xmas = xmas - current_datetime
print(f"There is {until_xmas} days until Christmas({xmas.strftime("%d/%m/%Y")})")
