from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0, z=0):
        """初始化方法
        
        :param x: 橫座標
        :param y: 縱座標
        :param Z: 高度座標
        """
        self.x = x
        self.y = y
        self.z = z

    def move_to(self, x, y, z):
        """移動到指定位置
        
        :param x: 新的橫座標
        :param y: 新的縱座標
        :param z: 新的高度座標
        """
        self.x = x
        self.y = y
        self.z = z

    def move_by(self, dx, dy, dz):
        """移動指定的增量
        
        :param dx: 橫座標的增量
        :param dy: 縱座標的增量
        :param dz: 高度座標的增量
        """
        self.x += dx
        self.y += dy
        self.z += dz

    def distance_to(self, other):
        """計算與另一個點的距離
        
        :param other: 另一個點
        """
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    def __str__(self):
        return '(%s, %s, %s)' % (str(self.x), str(self.y), str(self.z))


def main(x1=0, y1=0, z1=0, x2=0, y2=0, z2=0):
    p1 = Point(x1, y1, z1)
    p2 = Point(x2, y2, z2)
    print('Point 1: {}' .format (p1))
    print('Point 2: {}' .format (p2))
    # p2.move_by(-1, 2)
    # print(p2)
    print('Distance between P1 and P2: %.3f' % (p1.distance_to(p2)))


if __name__ == '__main__':
    main()