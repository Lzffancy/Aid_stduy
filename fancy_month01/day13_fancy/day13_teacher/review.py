class XXView:
    def __init__(self):
        self.__controller = XXController()

    def func01(self):
        self.__controller.func02()


class XXController:
    def func02(self):
        print("func02")


view = XXView()
view.func01()
