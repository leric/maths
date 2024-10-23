"""
面积相等的三角形 1

利用穿过三角形顶点的底边平行线，寻找等面积三角形
"""

from manimlib import *

class Example1(Scene):
  '''
  三角形顶点在底的平行线上移动例题1
  '''
  def construct(self):
    title = Text('面积相等的三角形 例题1').to_corner(UP + LEFT)
    instruction = Tex(r"\text{长方形ABCD长8cm, 宽4cm, 蓝色三角形GEC的面积是}10\text{cm}^2\text{, 求线段OF的长.}", font_size=20).next_to(title, DOWN, aligned_edge=LEFT_SIDE)
    self.play(Write(title), ShowCreation(instruction))

    # 创建一个长方形
    rect = Rectangle(width=4, height=3)
    top_right, top_left, bottom_left, bottom_right = rect.get_vertices()
    labels = [
        Text("A", font_size=20).next_to(top_left, UP + LEFT, buff=0.1),
        Text("B", font_size=20).next_to(bottom_left, DOWN + LEFT, buff=0.1),
        Text("C", font_size=20).next_to(bottom_right, DOWN + RIGHT, buff=0.1),
        Text("D", font_size=20).next_to(top_right, UP + RIGHT, buff=0.1)
    ]
    self.play(ShowCreation(rect), *[FadeIn(label) for label in labels])

    # 创建水平线段
    point_e = [top_left[0], 0.3, 0]
    point_f = [top_right[0], 0.3, 0]
    line = Line(point_e, point_f)
    e_label = Text("E", font_size=20).next_to(point_e, LEFT, buff=0.1)
    f_label = Text("F", font_size=20).next_to(point_f, RIGHT, buff=0.1)
    self.play(ShowCreation(line), FadeIn(e_label), FadeIn(f_label))

    # 从point_e, bottom_right, 和AD上任意一点画一个三角形，填充蓝色
    point_g = [0.2, top_left[1], 0]  # 上边上任意一点
    g_label = Text("G", font_size=20).next_to(point_g, UP, buff=0.1)
    g_dot = Dot(point_g)
    triangle = Polygon(point_e, bottom_right, point_g)
    triangle.set_fill(BLUE, opacity=0.5)

    o_point = line_intersection([point_e, point_f], [bottom_right, point_g])
    o_label = Text("O", font_size=20).next_to(o_point, UP, buff=0.1)
    o_dot = Dot(o_point)
    self.play(ShowCreation(triangle), FadeIn(g_label), FadeIn(g_dot), FadeIn(o_dot), FadeIn(o_label))

    # highlight OE
    line_oe = Line(o_point, point_e)
    line_oe.set_stroke(color=YELLOW)
    self.play(FlashyFadeIn(line_oe))
    self.wait(4)

    # Highlight two triangles
    tri_up = Polygon(point_e, point_g, o_point)
    tri_down = Polygon(point_e, o_point, bottom_right)
    self.play(FlashyFadeIn(tri_up))
    self.wait()
    self.play(FlashyFadeIn(tri_down))
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


class Example2(Scene):
  def construct(self):
    title = Text('面积相等的三角形 例题2').to_corner(UP + LEFT)
    instruction = Tex(r"\text{.}", font_size=20).next_to(title, DOWN, aligned_edge=LEFT_SIDE)
    self.play(Write(title), ShowCreation(instruction))

    # 画出一个正方形，一个直角梯形
    D = [0, 0, 0]
    E = [0, -2, 0]
    F = [2, -2, 0]
    H = [2, 0, 0]

    A = [0, 2.5, 0]
    B = [2.5, 2.5, 0]
    C = [3, 0, 0]
    
    defh = Polygon(D, E, F, H)
    abcd = Polygon(A, B, C, D)
    
    lables = [
       Text(p[0], font_size=20).next_to(p[1], UP, buff=0.1)
       for p in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E), ('F', F), ('H', H)]
    ]
    self.play(ShowCreation(defh), ShowCreation(abcd), *[ShowCreation(x) for x in lables])

    # 画出要求面积的三角形
    O = line_intersection([E, B], [C, D])
    lable_o = Text('O', font_size=20).next_to(O, UP, buff=0.1)
    beh = Polygon(B, E, H)
    beh.set_fill(BLUE, opacity=0.5)
    self.play(ShowCreation(beh), ShowCreation(lable_o))
    self.wait(2)

    # 画出辅助线BD，平行AC
    line_db = DashedLine(B, D)
    self.play(ShowCreation(line_db))

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
    

