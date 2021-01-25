from usl import StudentView

# 主模块(第一次运行的模块)不会生成pyc文件

# 快捷键: main + 回车
if __name__ == '__main__':
    # 如果当前模块是主模块,才启动项目
    # 如果当前模块被导入,不执行下列代码
    view = StudentView()
    view.main()
