from usl_user_show_laye import StudentView
if __name__ == "__main__":
    #该模块如果被导入，不执行下列代码
    view = StudentView()
    view.main()

'''　
　　<编译机制>
   因为入口会一次完整编译（到机器码），所以做入口应该尽量简洁
　　使用ｍａｉｎ作为入口
　　编译后会生成除了本文件（ｍａｉｎ)以外的　ｐｙｃ字节码文件(导入的模块）
　　方便下次调用提高效率

'''

