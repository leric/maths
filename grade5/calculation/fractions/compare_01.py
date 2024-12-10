"""
分数比大小

1. 转化成同分子或同分母的分数
2. 同时加减乘除，大小关系不变

"""
from manim import *

config['tex_template'] = TexTemplateLibrary.ctex


class Example1(Scene):
  def construct(self):
    # 展示题目
    title = Text('分数比大小 例题1', font_size=32).to_corner(UP + LEFT)
    instruction = Tex((r"比较下列分数的大小："
                        r"$\frac{22222}{9999}$与$\frac{2222}{999}$, "
                        r"$\frac{222}{9999}$与$\frac{22}{999}$"),
                        font_size=36)

    self.add(title, instruction)
    self.wait(2)

    self.play(instruction.animate().scale(0.6).next_to(title, DOWN, aligned_edge=LEFT))

    self.quiz2()

    #self.quiz3()
    

  def quiz1(self):
    ### 列出第一组分数
    frac_line1 = Line(LEFT, RIGHT).scale(1.2)
    numerator1 = MathTex("{{22222}}").set_color(GREEN)
    denominator1 = MathTex("{{99999}}").set_color(ORANGE)
    fraction1 = VGroup(numerator1, frac_line1, denominator1).arrange(DOWN, buff=0.1)
    fraction1.shift(LEFT * 3).shift(UP * 1.8)

    frac_line2 = Line(LEFT, RIGHT).scale(0.9)
    numerator2 = MathTex("{{222}}").set_color(GREEN)
    denominator2 = MathTex("{{999}}").set_color(ORANGE)
    fraction2 = VGroup(numerator2, frac_line2, denominator2).arrange(DOWN, buff=0.1)
    fraction2.shift(RIGHT * 3).shift(UP * 1.8)

    self.play(Write(fraction1), Write(fraction2))
    self.wait()

    # 因式分解
    numerator1_1 = MathTex(r"{{2}}", r"\times", r"{{11111}}").set_color(GREEN).move_to(numerator1)
    denominator1_1 = MathTex(r"{{9}}", r"\times", r"{{11111}}").set_color(ORANGE).move_to(denominator1)
    numerator2_1 = MathTex(r"{{2}}", r"\times", r"{{111}}").set_color(GREEN).move_to(numerator2)
    denominator2_1 = MathTex(r"{{9}}", r"\times", r"{{111}}").set_color(ORANGE).move_to(denominator2)

    self.play(
      TransformMatchingShapes(numerator1, numerator1_1), 
      TransformMatchingShapes(denominator1, denominator1_1),
      TransformMatchingShapes(numerator2, numerator2_1), 
      TransformMatchingShapes(denominator2, denominator2_1),
    )
    self.wait()

    # 约分
    numerator1_2 = MathTex(r"{{2}}").set_color(GREEN).move_to(numerator1)
    denominator1_2 = MathTex(r"{{9}}").set_color(ORANGE).move_to(denominator1)
    numerator2_2 = MathTex(r"{{2}}").set_color(GREEN).move_to(numerator2)
    denominator2_2 = MathTex(r"{{9}}").set_color(ORANGE).move_to(denominator2)

    self.play(
      TransformMatchingShapes(VGroup(numerator1_1, denominator1_1), VGroup(numerator1_2, denominator1_2)), 
    )
    self.play(
      TransformMatchingShapes(VGroup(numerator2_1, denominator2_1), VGroup(numerator2_2, denominator2_2)),
    )
    self.wait()

    # 相等
    answer = MathTex(r"\frac{22222}{99999} = \frac{222}{999}")
    self.play(Create(answer))
    self.wait(3)
    self.remove(fraction1, fraction2, answer, numerator1_2, denominator1_2, numerator2_2, denominator2_2, frac_line1, frac_line2)
    self.wait()

  def quiz2(self):
    ### 显示题目
    frac_line1 = Line(LEFT, RIGHT).scale(1)
    numerator1 = MathTex("{{22222}}").set_color(GREEN)
    denominator1 = MathTex("{{9999}}").set_color(ORANGE)
    fraction1 = VGroup(numerator1, frac_line1, denominator1).arrange(DOWN, buff=0.1)
    fraction1.shift(LEFT * 3).shift(UP * 1.8)

    frac_line2 = Line(LEFT, RIGHT).scale(0.8)
    numerator2 = MathTex("{{2222}}").set_color(GREEN)
    denominator2 = MathTex("{{999}}").set_color(ORANGE)
    fraction2 = VGroup(numerator2, frac_line2, denominator2).arrange(DOWN, buff=0.1)
    fraction2.shift(RIGHT * 3).shift(UP * 1.8)

    self.play(Write(fraction1), Write(fraction2))
    self.wait()

    # 因式分解
    numerator1_1 = MathTex(r"11111 \times 2").set_color(GREEN).move_to(numerator1)
    denominator1_1 = MathTex(r"1111 \times 9").set_color(ORANGE).move_to(denominator1)
    numerator2_1 = MathTex(r"1111 \times 2").set_color(GREEN).move_to(numerator2)
    denominator2_1 = MathTex(r"111 \times 9").set_color(ORANGE).move_to(denominator2)
    self.play(
      TransformMatchingShapes(VGroup(numerator1, denominator1), VGroup(numerator1_1, denominator1_1)), 
      TransformMatchingShapes(VGroup(numerator2, denominator2), VGroup(numerator2_1, denominator2_1)),
    )
    self.wait()

    # 两边同时除以 2/9
    frac_left = Tex(r"÷ $\frac{2}{9}$").next_to(fraction1, RIGHT)
    frac_right = Tex(r"÷ $\frac{2}{9}$").next_to(fraction2, RIGHT)
    self.play(Write(frac_left), Write(frac_right), run_time=1.5)
    self.wait()

    # 抵消 2/9
    numerator1_2 = MathTex(r"11111").set_color(GREEN).move_to(numerator1)
    denominator1_2 = MathTex(r"1111").set_color(ORANGE).move_to(denominator1)
    numerator2_2 = MathTex(r"1111").set_color(GREEN).move_to(numerator2)
    denominator2_2 = MathTex(r"111").set_color(ORANGE).move_to(denominator2)
    self.play(
      ReplacementTransform(VGroup(numerator1_1, denominator1_1, frac_left), VGroup(numerator1_2, denominator1_2)), 
      FadeTransform(VGroup(numerator2_1, denominator2_1, frac_right), VGroup(numerator2_2, denominator2_2)),
    )
    self.wait()
  
    # 改为带分数的形式
    numerator1_3 = MathTex(r"{{11110 + 1}}").set_color(GREEN).move_to(numerator1)
    numerator2_3 = MathTex(r"{{1110 + 1}}").set_color(GREEN).move_to(numerator2)
    self.play(
      TransformMatchingShapes(numerator1_2, numerator1_3), 
      TransformMatchingShapes(numerator2_2, numerator2_3), 
    )
    self.wait()

    numerator1_4 = MathTex(r"1").set_color(GREEN).move_to(numerator1)
    numerator2_4 = MathTex(r"1").set_color(GREEN).move_to(numerator2)
    integer1 = MathTex(r"10 + ").next_to(fraction1, LEFT)
    integer2 = MathTex(r"10 + ").next_to(fraction2, LEFT)
    self.play(
      TransformMatchingShapes(numerator1_3, VGroup(numerator1_4, integer1)), 
      TransformMatchingShapes(numerator2_3, VGroup(numerator2_4, integer2)), 
    )
    self.wait()

    # 两边减去10
    self.play(
      Transform(VGroup(numerator1_4, integer1), numerator1_4), 
      Transform(VGroup(numerator2_4, integer2), numerator2_4), 
    )
    self.wait()

    # 小于
    answer = MathTex(r"\frac{22222}{9999} < \frac{2222}{999}")
    self.play(Create(answer))
    self.wait(3)
    self.remove(fraction1, fraction2, answer, numerator1_4, denominator1_2, numerator2_4, denominator2_2, frac_line1, frac_line2)
    self.wait()

  def quiz3(self):
    # ### 第三组分数
    frac_line1 = Line(LEFT, RIGHT).scale(1)
    numerator1 = MathTex("{{2222}}").set_color(GREEN)
    denominator1 = MathTex("{{99999}}").set_color(ORANGE)
    fraction1 = VGroup(numerator1, frac_line1, denominator1).arrange(DOWN, buff=0.1)
    fraction1.shift(LEFT * 3).shift(UP * 1.8)

    frac_line2 = Line(LEFT, RIGHT).scale(0.8)
    numerator2 = MathTex("{{222}}").set_color(GREEN)
    denominator2 = MathTex("{{9999}}").set_color(ORANGE)
    fraction2 = VGroup(numerator2, frac_line2, denominator2).arrange(DOWN, buff=0.1)
    fraction2.shift(RIGHT * 3).shift(UP * 1.8)

    self.play(Write(fraction1), Write(fraction2))
    self.wait()

    # 同时除以2/9
    frac_left = Tex(r"÷ $\frac{2}{9}$").next_to(fraction1, RIGHT)
    frac_right = Tex(r"÷ $\frac{2}{9}$").next_to(fraction2, RIGHT)
    self.play(Write(frac_left), Write(frac_right))
    self.wait()
    numerator1_1 = MathTex(r"1111").set_color(GREEN).move_to(numerator1)
    denominator1_1 = MathTex(r"11111").set_color(ORANGE).move_to(denominator1)
    numerator2_1 = MathTex(r"111").set_color(GREEN).move_to(numerator2)
    denominator2_1 = MathTex(r"1111").set_color(ORANGE).move_to(denominator2)
    self.play(
      TransformMatchingShapes(numerator1, numerator1_1), 
      TransformMatchingShapes(denominator1, denominator1_1),
      TransformMatchingShapes(numerator2, numerator2_1), 
      TransformMatchingShapes(denominator2, denominator2_1),
      FadeOut(frac_left), FadeOut(frac_right),
    )
    self.wait()

    # 右边变形
    numerator2_2 = MathTex(r"1110").set_color(GREEN).move_to(numerator2)
    denominator2_2 = MathTex(r"11110").set_color(ORANGE).move_to(denominator2)
    self.play(
      TransformMatchingShapes(numerator2_1, numerator2_2), 
      TransformMatchingShapes(denominator2_1, denominator2_2),
    )
    self.wait()

    # 左边变形
    numerator1_2 = MathTex(r"1110 + 1").set_color(GREEN).move_to(numerator1)
    denominator1_2 = MathTex(r"11110 + 1").set_color(ORANGE).move_to(denominator1)
    self.play(
      TransformMatchingShapes(numerator1_1, numerator1_2), 
      TransformMatchingShapes(denominator1_1, denominator1_2),
    )
    self.wait()

    # ???
    answer = MathTex(r"\frac{a + 1}{b + 1} \,?\, \frac{a}{b}")
    self.play(Create(answer))
    self.wait()

    answer2 = MathTex(r"\frac{a + 1}{b + 1}  >  \frac{a}{b} \quad \text{if a < b}")
    self.play(TransformMatchingShapes(answer, answer2))
    self.wait()

    answer3 = MathTex(r"\frac{2222}{99999} > \frac{222}{9999}")
    answer3.next_to(answer2, DOWN)
    self.play(Create(answer3))
    self.wait()

  def theorem(self):
    # 证明 a/b 与 a+1/b+1 的大小关系
    title = Text('定理', font_size=32).to_corner(UP + LEFT)
    instruction = Tex((
        r"对于任意正整数a和b，"
        r"当a < b时，$\frac{a}{b} < \frac{a + 1}{b + 1}$"
        r"，当a > b时，$\frac{a}{b} > \frac{a + 1}{b + 1}$"
      )).next_to(title, DOWN, aligned_edge=LEFT)
    
    self.add(title, instruction)