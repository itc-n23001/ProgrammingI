class Cylinder:
    """円柱"""

    pi = 3.14

    def __init__(self, radius=1, height=1):
        """円柱を特徴づける属性"""
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        """底面積を計算"""
        pi = Cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        """即面積を計算"""
        pi = Cylinder.pi
        r = self.radius
        h = self.radius
        return 2 * pi * r * h

    def calc_surface_area(self):
        """表面積を計算"""
        c = self.calc_base_area()
        s = self.calc_side_area()
        return 2 * c + s

    def calc_volume(self):
        """体積を求める"""
        c = self.calc_base_area()
        h = self.height
        return c * h

    def show_results(self):
        """属性を見せる"""
        r = self.radius
        h = self.height
        S = self.calc_surface_area()
        V = self.calc_volume()
        print("半径: {}, 高さ: {}, 表面積: {}, 体積: {}".format(r, h, S, V))


c1 = Cylinder()
print(c1.show_results())
c2 = Cylinder(1.0, 3.0)
print(c2.show_results())
c3 = Cylinder(2.0, 1.0)
print(c3.show_results())
c4 = Cylinder(2.0, 3.0)
print(c4.show_results())
