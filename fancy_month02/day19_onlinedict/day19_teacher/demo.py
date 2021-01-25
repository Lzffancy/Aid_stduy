def login():
    while True:
        print("""
    =============== Query ==============
     1. 查单词     2. 历史记录    3. 注销
    ====================================
        """)
        item = input("请输入选项:")
        if item == "1":
            pass
        elif item == "2":
            pass
        elif item == "3":
            break
        else:
            print("请输入正确选项!")


while True:
    print("""
    =========== Welcome =============
     1. 登录     2. 注册    3. 退出
    =================================
    """)
    item = input("请输入选项:")
    if item == "1":
        login()
    elif item == "2":
        pass
    elif item == "3":
        break
    else:
        print("请输入正确选项!")