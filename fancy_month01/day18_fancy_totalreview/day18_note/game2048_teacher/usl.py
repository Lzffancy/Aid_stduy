from bll import GameController


class GameView:
    def __init__(self):
        self.__controller = GameController()

    def __draw_map(self):
        for line in self.__controller.map:
            for item in line:
                print(item,end = " ")
            print() # 换行

    def __start(self):
        self.__draw_map()
        # 产生2个随机数

    def __update(self):
        while True:
            # 获取输入
            self.__move_map()
            self.__draw_map()
            # 产生一个随机数
            # 如果游戏结束,退出循环

    def __move_map(self):
        dir = input("请输入:")
        if dir == "w":
            self.__controller.move_up()
        elif dir == "s":
            self.__controller.move_down()
        elif dir == "a":
            self.__controller.move_left()
        elif dir == "d":
            self.__controller.move_right()

    def main(self):
        self.__start()
        self.__update()