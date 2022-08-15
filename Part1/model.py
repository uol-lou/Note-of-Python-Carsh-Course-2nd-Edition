class Model:

    def __init__(self, make, year):
        self.make = make
        self.year = year
        # 给予默认值，不一定要从外部定义
        self.odo_reading = 0

    def get(self):
        return self.make.title()

    def get_odo_reading(self):
        return self.odo_reading

    def get_nova(self):
        return "There is nova."


new_model = Model("abc", 2020)
print(new_model.get())
print(new_model.odo_reading)
print(new_model.get_nova())


# 创建一个子类
# 和JAVA不同，创建子类时，父类必须包含在当先文件中，并位于子类之前！！
class ElectricModel(Model):
    def __init__(self, make, year, abc):
        super().__init__(make, year)
        self.abc = abc

    def get_abc(self):
        return self.abc

    def get_nova(self):
        return "there is no nova"


eleModel = ElectricModel("Model", 2022, "abc")
print(eleModel.get())
print(eleModel.get_odo_reading())
print(eleModel.get_nova())

# 将实例用作属性 有点类似于java中的接口
# 属性和方法越来越长，在这种情况下，可以将一部分提取出来，作为一个独立的类
