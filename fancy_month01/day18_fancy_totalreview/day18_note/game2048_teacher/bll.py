class GameController:
    def __init__(self):
        self.__list_merge = []
        self.__map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动map
            思想：获取每行，交给list_merge，在通知merge()进行合并
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向左移动map
            思想：获取每行，交给list_merge，在通知merge()进行合并
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __square_matrix_transposition(self):
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def move_up(self):
        """
            向上移动
            思想：  转置  move_left　转置　
        """
        self.__square_matrix_transposition()
        self.move_left()
        self.__square_matrix_transposition()

    def move_down(self):
        """
            向下移动
            思想: 转置  move_right　转置
        :return:
        """
        self.__square_matrix_transposition()
        self.move_right()
        self.__square_matrix_transposition()

# 测试代码
if __name__ == '__main__':
    controller = GameController()
    print(controller.map)
    controller.move_down()
    print(controller.map)
