"""
    函数式编程
        适用性:多个函数,主体逻辑相同,核心算法不同.
            def 功能1():
                通用代码
                变化点1

            def 功能2():
                通用代码
                变化点2
        步骤:1. 分
            def 变化点1():
                ...
            def 变化点2():
                ...
            2. 隔
            def 通用代码(参数):
                ...
                # 变化点1()
                参数()
            3. 做
             def 变化点3():
                ...
             通用代码(变化点3)
        成果:
            将通用代码定义到IterableHelper类
"""


