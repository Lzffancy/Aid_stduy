from bll import GameControler


class GameView:
    def __init__(self):
        self.__controler = GameControler()

    def start_game(self):
        self.__controler.new_map()
        self.__show_map()

    def player_input(self):
        direction = input("请输入wsad")
        if direction == 'w':
            self.__controler.move_up()
            self.__show_map()
        elif direction == 's':
            self.__controler.move_down()
            self.__show_map()
        elif direction == 'a':
            self.__controler.move_left()
            self.__show_map()
        elif direction == 'd':
            self.__controler.move_right()
            self.__show_map()
        else:
            print("输入有误")
            self.__show_map()

    def __show_map(self):
        for item in self.__controler.map:
            print(item)

    def main(self):
        self.start_game()
        while 1:
            self.player_input()


if __name__ == '__main__':
    v01 = GameView()
    v01.start_game()
    while 1:
        v01.player_input()

# #------------test
# if __name__ == '__main__':
#     map01 =[[2, 0, 0, 2],
#             [2, 0, 0, 2],
#             [2, 0, 0, 2],
#             [2, 0, 0, 2]]
#     v01 =GameView(map01)
#     while 1:
#       v01.player_input()
#     #c01 = GameControler(map01)
