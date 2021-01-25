import random

class GameControler:
    def __init__(self):
        self.__map = []
        self.__list_merge = []

    @property
    def map(self):
        return self.__map

    def zero_to_end(self):
        """
          零元素向后移动
          思想：从后向前判断，如果是0则删除,在末尾追加.
      """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def merge(self):
        """
          合并数据
            核心思想：零元素后移，判断是否相邻相同。如果是则合并.
      """
        self.zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)
                # 加分

    def move_left(self):
        """
          向左移动map
          思想：获取每行，交给list_merge，在通知merge()进行合并
      :return:
      """
        # global list_merge
        for line in self.__map:
            self.__list_merge = line
            self.merge()

    def move_right(self):
        """
          向左移动map
          思想：获取每行，交给list_merge，在通知merge()进行合并
      :return:
      """
        # global list_merge
        for line in self.__map:
            # 从右向左获取数据形成新列表
            self.__list_merge = line[::-1]
            # 处理数据
            self.merge()
            # 将处理后的数据再从右向左还给map
            line[::-1] = self.__list_merge

    def square_matrix_transposition(self):
        """
          方阵转置（列转换为行）
      :param map: 需要转置的方阵
      :return:
      """
        for c in range(1, len(self.__map)):  # 1 2 3
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def move_up(self):
        """
          向上移动
          思想：  转置  move_left　转置　
      """
        self.square_matrix_transposition()
        self.move_left()
        self.square_matrix_transposition()

    def move_down(self):
        """
          向下移动
          思想: 转置  move_right　转置
      :return:
      """
        self.square_matrix_transposition()
        self.move_right()
        self.square_matrix_transposition()

    def new_map(self):
        list_number = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        for i in range(4):
            number = random.sample(list_number, 4)
            self.__map.append(number)                            #????????为什么设置私有，以及私有设为了已读为何还能　修改其
        #print(self.map)
    def end_game(self):                                         #待拓展的功能１．结束游戏判断　２．　在每一次移动后生成新的随机数
        pass
    def newnumber_in_map(self):
        pass
# ---------------------test
# if __name__ == '__main__':
#     map01 = [[2, 0, 0, 2],
#              [2, 0, 0, 2],
#              [2, 0, 0, 2],
#              [2, 0, 0, 2]]
#     c01 = GameControler(map01)
#
#
#     c01.move_left()
#     print(c01.map)
#     c01.move_right()
#     print(c01.map)
#     c01.move_up()
#     print(c01.map)

if __name__ == '__main__':
    c01 = GameControler()
    c01.new_map()
#   print(c01.__map)
    c01.new_map()
    print(c01.map)