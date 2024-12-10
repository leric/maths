"""
面积相等的三角形 3

综合题
"""
from manim import *

config['tex_template'] = TexTemplateLibrary.ctex


class Example1(Scene):
  def construct(self):
    title = Text('在边长为10cm的正方形内，有一个四边形ABCD，求这个四边形的面积。', font_size=20).to_corner(UP + LEFT)
    self.add(title)

    # 创建一个正方形
    square = Square(side_length=5)
    self.play(Create(square))
    # 获取正方形的顶点坐标
    top_right, _, bottom_left, _ = square.get_vertices()

    # 从顶边靠左任意一点A，画垂直线到底边
    point_a = (top_right[0] - 3.5, top_right[1], 0.0)
    a_label = Text("A", font_size=20).next_to(point_a, UP, buff=0.1)
    point_a2 = (point_a[0], bottom_left[1], 0.0)
    line_a = Line(point_a, point_a2)

    # 左边靠下任意一点B, 画水平线到右边
    point_b = (bottom_left[0], bottom_left[1] + 1.8, 0.0)
    b_label = Text("B", font_size=20).next_to(point_b, LEFT, buff=0.1)
    point_b2 = (top_right[0], point_b[1], 0.0)
    line_b = Line(point_b, point_b2)

    point_c = (point_a[0] + 0.5, bottom_left[1], 0.0)
    c_label = Text("C", font_size=20).next_to(point_c, DOWN, buff=0.1)
    point_d = (top_right[0], point_b[1] + 1, 0.0)
    d_label = Text("D", font_size=20).next_to(point_d, RIGHT, buff=0.1)
    rect = Polygon(point_a, point_b, point_c, point_d)

    self.play(Create(line_a), Create(line_b), FadeIn(a_label), FadeIn(b_label), FadeIn(c_label), FadeIn(d_label))
    self.play(Create(rect))

    # 长度标识
    a2c = Line(point_a2, point_c)
    a2c_label = Text('1cm', font_size=18)
    brace_a2c = Brace(a2c, direction=DOWN).put_at_tip(a2c_label)
    brace_a2c.set_stroke(width=1)
    b2d = Line(point_b2, point_d)
    b2d_label = Text('2cm', font_size=18)
    brace_b2d = Brace(b2d, direction=RIGHT).put_at_tip(b2d_label)
    brace_b2d.set_stroke(width=1)
    self.play(Create(a2c_label), Create(brace_a2c), Create(b2d_label), Create(brace_b2d))
    self.wait(5)

    # 画四条辅助线
    point_o = [point_a[0], point_b[1], 0]
    line_ba2 = DashedLine(point_a2, point_b)
    line_oc = DashedLine(point_o, point_c)
    line_od = DashedLine(point_o, point_d)
    line_b2c = DashedLine(point_b2, point_c)
    self.play(Create(line_ba2), Create(line_oc), Create(line_od), Create(line_b2c))

    self.wait(2)

    # 标示出占总面积一半的区域
    t_abo = Polygon(point_a, point_b, point_o)
    t_abo.set_stroke(width=0)
    t_abo.set_fill(BLUE, opacity=0.2)

    t_ado = Polygon(point_o, point_a, point_d)
    t_ado.set_stroke(width=0)
    t_ado.set_fill(BLUE, opacity=0.2)

    t_ba2o = Polygon(point_o, point_b, point_a2)
    t_ba2o.set_stroke(width=0)
    t_ba2o.set_fill(BLUE, opacity=0.2)

    t_cob2 = Polygon(point_b2, point_c, point_o)
    t_cob2.set_stroke(width=0)
    t_cob2.set_fill(BLUE, opacity=0.2)

    self.play(Create(t_abo), Create(t_ado), Create(t_ba2o), Create(t_cob2))
    self.wait(2)

    # 标记处于ABCD区域的差异面积
    point_o1 = line_intersection([point_a, point_a2], [point_b, point_c])
    t_oco1 = Polygon(point_o, point_c, point_o1)
    t_oco1.set_stroke(width=0)
    t_oco1.set_fill(RED, opacity=0.5)

    point_o2 = line_intersection([point_b, point_b2], [point_c, point_d])
    t_odo2 = Polygon(point_o, point_d, point_o2)
    t_odo2.set_stroke(width=0)
    t_odo2.set_fill(RED, opacity=0.5)

    self.play(Create(t_oco1), Create(t_odo2))
    self.wait(2)

    t_bo1a2 = Polygon(point_b, point_o1, point_a2)
    t_bo1a2.set_stroke(width=0)
    t_bo1a2.set_fill(GREEN, opacity=0.5)

    t_co2b2 = Polygon(point_c, point_o2, point_b2)
    t_co2b2.set_stroke(width=0)
    t_co2b2.set_fill(GREEN, opacity=0.5)

    self.play(Create(t_bo1a2), Create(t_co2b2))
    self.wait(2)
