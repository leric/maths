"""
面积相等的三角形 1

利用穿过三角形顶点的底边平行线，寻找等面积三角形
"""
from manim import *

config['tex_template'] = TexTemplateLibrary.ctex

class Example1(Scene):
  '''
  三角形顶点在底的平行线上移动例题1
  '''
  def construct(self):
    title = MathTex(r"\text{长方形ABCD长8cm, 宽4cm, 蓝色三角形GEC的面积是}10\text{cm}^2\text{, 求线段EO的长.}",
                      font_size=22).to_corner(UP + LEFT)
    self.add(title)

    # 创建一个长方形
    rect = Rectangle(width=4, height=3)
    top_right, top_left, bottom_left, bottom_right = rect.get_vertices()
    labels = [
        Text("A", font_size=20).next_to(top_left, UP + LEFT, buff=0.1),
        Text("B", font_size=20).next_to(bottom_left, DOWN + LEFT, buff=0.1),
        Text("C", font_size=20).next_to(bottom_right, DOWN + RIGHT, buff=0.1),
        Text("D", font_size=20).next_to(top_right, UP + RIGHT, buff=0.1)
    ]
    self.play(Create(rect), *[FadeIn(label) for label in labels])

    # 创建水平线段
    point_e = (top_left[0], 0.3, 0.0)
    point_f = (top_right[0], 0.3, 0.0)
    line = Line(point_e, point_f)
    e_label = Text("E", font_size=20).next_to(point_e, LEFT, buff=0.1)
    f_label = Text("F", font_size=20).next_to(point_f, RIGHT, buff=0.1)
    self.play(Create(line), FadeIn(e_label), FadeIn(f_label))

    # 从point_e, bottom_right, 和AD上任意一点画一个三角形，填充蓝色
    point_g = (0.2, top_left[1], 0.0)  # 上边上任意一点
    g_label = Text("G", font_size=20).next_to(point_g, UP, buff=0.1)
    g_dot = Dot(point_g)
    triangle = Polygon(point_e, bottom_right, point_g)
    triangle.set_fill(BLUE, opacity=0.5)

    o_point = intersect_point(point_e, point_f, bottom_right, point_g)
    o_label = Text("O", font_size=20).next_to(o_point, UP, buff=0.1)
    o_dot = Dot(o_point)
    self.play(Create(triangle), FadeIn(g_label), FadeIn(g_dot), FadeIn(o_dot), FadeIn(o_label))

    # highlight OE
    line_oe = Line(o_point, point_e)
    line_oe.set_stroke(color=YELLOW)
    self.play(FadeIn(line_oe))
    self.wait(4)

    # Highlight two triangles
    tri_up = Polygon(point_e, point_g, o_point)
    tri_down = Polygon(point_e, o_point, bottom_right)
    self.play(FadeIn(tri_up))
    self.wait()
    self.play(FadeIn(tri_down))
    self.wait()

    # 将三角形ECG转换为四边形ECOG，并创建移动顶点G和C的动画
    polygon = Polygon(point_e, bottom_right, o_point, point_g)

    # 更新G点的位置，同时更新三角形的形状
    def move_g_point(polygon):
      new_g_point = g_dot.get_center()  # 获取G点的当前位置
      new_shape = Polygon(point_e, bottom_right, o_point, new_g_point)
      new_shape.set_fill(BLUE, opacity=0.5)
      polygon.become(new_shape)  # 更新三角形

    self.play(
      MoveAlongPath(g_dot, Line(point_g, top_left)),
      UpdateFromFunc(polygon, move_g_point),
      run_time=2
    )

    self.wait(2)

    # 更新C点的位置，同时更新三角形的形状
    c_dot = Dot(bottom_right)
    def move_c_point(polygon):
      new_c_point = c_dot.get_center()  # 获取C点的当前位置
      new_shape = Polygon(point_e, new_c_point, o_point, g_dot.get_center())
      new_shape.set_fill(BLUE, opacity=0.5)
      polygon.become(new_shape)  # 更新三角形

    self.play(
      MoveAlongPath(c_dot, Line(bottom_right, bottom_left)),
      UpdateFromFunc(polygon, move_c_point),
      run_time=2
    )

    self.wait(2)

    # 列出算式
    result = Text(r"10 × 2 ÷ 4 = 5cm", font_size=24).to_edge(RIGHT)
    self.play(Write(result))
    self.wait(2)


class Example2(Scene):
  def construct(self):
    title = Text("直角梯形ABCD的上底与高相等，正方形DEFH的边长为6cm，涂色部分的面积是多少？",
              font_size=20).to_corner(UP + LEFT)
    self.add(title)
  
    # 画出一个正方形，一个直角梯形
    D = (0, 0, 0)
    E = (0, -2, 0)
    F = (2, -2, 0)
    H = (2, 0, 0)

    A = (0.0, 2.5, 0.0)
    B = (2.5, 2.5, 0.0)
    C = (3, 0, 0)

    defh = Polygon(D, E, F, H)
    abcd = Polygon(A, B, C, D)

    lables = [
       Text(p[0], font_size=20).next_to(p[1], UP, buff=0.1)
       for p in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E), ('F', F), ('H', H)]
    ]
    self.play(Create(defh), Create(abcd), *[Create(x) for x in lables])

    # 画出要求面积的三角形
    O = intersect_point(E, B, C, D)
    lable_o = Text('O', font_size=20).next_to(O, UP, buff=0.1)
    beh = Polygon(B, E, H)
    beh.set_fill(BLUE, opacity=0.5)
    self.play(Create(beh), Create(lable_o))
    self.wait(4)

    # 画出辅助线BD，平行AC
    line_db = DashedLine(B, D)
    self.play(Create(line_db))
    self.wait(2)

    # 移动三角形顶点
    b_dot = Dot(B)
    beh2 = Polygon(B, E, H)
    def move_b_point(polygon):
      new_b_point = b_dot.get_center()
      new_shape = Polygon(E, H, new_b_point)
      new_shape.set_fill(YELLOW, opacity=0.5)
      polygon.become(new_shape)  # 更新三角形

    self.play(
      MoveAlongPath(b_dot, Line(B, D)),
      UpdateFromFunc(beh2, move_b_point),
      run_time=2
    )
    self.wait(2)


def intersect_point(p1, p2, p3, p4):
    """
    计算直线p1p2和直线p3p4的交点
    """
    x1, y1 = p1[:2]
    x2, y2 = p2[:2]
    x3, y3 = p3[:2]
    x4, y4 = p4[:2]

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if denominator == 0:
        # Lines are parallel
        return None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator

    return (px, py, 0.0)
  
