class Developer:
    skill = "python"
    rate = 1100


developer1 = Developer()
developer2 = Developer()
developer3 = Developer()
# Поднимите первому программисту (developer1) зарплату до уровня 1300 долларов и переменной
# total_rate присвойте значение фонда оплаты труда трех программистов.
developer1.rate = 1300
total_rate = developer1.rate + developer2.rate + developer3.rate