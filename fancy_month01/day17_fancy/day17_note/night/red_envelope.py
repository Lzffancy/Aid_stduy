def a_project():
    totall_cost = 10

    def wrapper(input_money):
        nonlocal totall_cost
        if input_money > 10:
            totall_cost += 1
        return totall_cost

    return wrapper


def b_project():
    totall_cost = 0

    def wrapper(input_money):
        nonlocal totall_cost
        if input_money > 5:
            totall_cost += 1
        return totall_cost

    return wrapper


a_p = a_project()
b_p = b_project()
sum_money = 0

while 1:

    input_money = input('输入抢到的红包:')
    if input_money == '' or input_money == "exit":
        break
    else:
        f_inputmoney = float(input_money)
        sum_money += f_inputmoney
        print('总共抢到的红包', sum_money)
        print('a方案花费', a_p(f_inputmoney))
        print('b方案花费', b_p(f_inputmoney),'\n')
