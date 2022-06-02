# I love PengJing!!!

class Duck:
    def quack(self):
        print('呱呱呱！')
    def features(self):
        print('这个鸭子拥有灰白色的羽毛。')


class Person:
    def quack(self):
        print('你才是鸭子，你们全家都是鸭子！！！')
    def features(self):
        print('这个人穿着鸭绒大衣。')


def in_the_forest(duck):
    duck.quack()
    duck.features()



def game():
    donald = Duck()
    PengJing = Person()
    in_the_forest(donald)
    in_the_forest(PengJing)

game()
