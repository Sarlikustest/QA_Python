month = input("Месяц?\n")
if month=="декабрь" or month=="январь" or month=="февраль":
    print(f"{month} - это зима")
elif month=="март" or month=="апрель" or month=="май":
    print(f"{month} - это весна")
elif month=="июнь" or month=="июль" or month=="август":
    print(f"{month} - это лето")
elif month=="сентябрь" or month=="октябрь" or month=="ноябрь":
    print(f"{month} - это осень")
else:
    print("Введен не месяц")