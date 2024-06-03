min_salary = int(input())
rating = int(input())
if min_salary >= 5000:
    print("Ваш доход выше 5000$")
    if rating >= 7:
        print("Ваш кредитный рейтинг хороший")
        print("Вам одобрен кредит")
    else:
        print("Ваш кредитный рейтинг ниже 7")
        print("Вам не одобрен кредит")
else:
    print("Ваш доход ниже 5000$")
