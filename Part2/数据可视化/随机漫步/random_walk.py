from random import choice


class RandomWalk:
    def __init__(self, num_point=100):
        self.num_point = num_point

        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        '''计算随机漫步所包含的点'''

        while len(self.x_value) < self.num_point:
            # 确定行走方向是向左还是向右
            # choice用法形参是一个数字列表
            x_direction = choice([-1, 1])

            x_distance = choice([1,2,3,4,5])

            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([1,2,3,4,5])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的x值和y值
            # 这个地方用【-1】，因为是上一个数值，直接x_value的话是一个数列
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)

    def get_point_value(self):
        for i in self.x_value:
            print(self.x_value[i-1],",",self.y_value[i-1])