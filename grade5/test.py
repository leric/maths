from manim import *

class MatchingEquationParts(Scene):
    def construct(self):
        # 创建分子和分母
        numerator = MathTex("a")
        denominator = MathTex("b")

        # 创建分数线
        fraction_line = Line(LEFT, RIGHT).scale(0.5)

        # 将分子、分数线和分母放在一起
        fraction = VGroup(numerator, fraction_line, denominator).arrange(DOWN, buff=0.1)
        fraction.set_color(BLUE)

        # 显示分数
        self.play(Write(fraction), run_time=1)

        # 其他动画，比如分母变色
        self.play(denominator.animate.set_color(RED))
        self.wait()


