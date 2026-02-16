from manim import *

class BaselProblemDetailed(Scene):
    def construct(self):
        # ------------------- 标题与引言 -------------------
        title = Text("巴塞尔问题的欧拉证明", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP).scale(0.8))
        self.wait(0.5)

        intro = Text(
            "求自然数平方的倒数和：",
            font_size=36,
            color=WHITE
        ).next_to(title, DOWN, buff=0.5)
        series = MathTex(
            r"\sum_{n=1}^{\infty} \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots = ?",
            font_size=40
        ).next_to(intro, DOWN)
        self.play(Write(intro), Write(series))
        self.wait(2)

        basel = Text(
            "这个问题被称为巴塞尔问题，困扰数学家近百年。",
            font_size=30,
            color=YELLOW
        ).next_to(series, DOWN, buff=0.8)
        self.play(Write(basel))
        self.wait(2)

        euler = Text(
            "1735年，28岁的欧拉给出了惊人的答案：",
            font_size=30,
            color=GREEN
        ).next_to(basel, DOWN, buff=0.5)
        answer = MathTex(r"\frac{\pi^2}{6}", font_size=48, color=ORANGE).next_to(euler, DOWN)
        self.play(Write(euler), Write(answer))
        self.wait(2)

        # 清屏，只保留标题
        self.play(*[FadeOut(mob) for mob in [intro, series, basel, euler, answer]])
        self.wait(0.5)

        # ------------------- 欧拉的核心思想 -------------------
        idea = Text("欧拉的核心思想：", font_size=36, color=BLUE).next_to(title, DOWN, buff=0.8)
        self.play(Write(idea))
        self.wait(0.5)

        analogy = Text(
            "将 sin x 视为一个“无穷次多项式”，",
            font_size=30,
            color=WHITE
        ).next_to(idea, DOWN, buff=0.5)
        self.play(Write(analogy))
        self.wait(1)

        poly_analogy = Text(
            "利用它的根写出因式分解形式。",
            font_size=30,
            color=WHITE
        ).next_to(analogy, DOWN, buff=0.3)
        self.play(Write(poly_analogy))
        self.wait(2)

        # 清屏，保留标题和idea
        self.play(*[FadeOut(mob) for mob in [analogy, poly_analogy]])
        self.wait(0.5)

        # ------------------- 1. 泰勒展开 -------------------
        taylor_title = Text("1. sin x 的泰勒展开", font_size=32, color=PURPLE).next_to(idea, DOWN, buff=1)
        self.play(Write(taylor_title))
        self.wait(0.5)

        taylor_eq = MathTex(
            r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots",
            font_size=38
        ).next_to(taylor_title, DOWN, buff=0.5)
        self.play(Write(taylor_eq))
        self.wait(2)

        # 坐标轴调整位置：使用 shift 上移，并缩小一点
        axes = Axes(
            x_range=[-3*PI, 3*PI, PI],
            y_range=[-2, 2, 1],
            x_length=9,
            y_length=3.5,
            axis_config={"color": BLUE}
        ).next_to(taylor_eq, DOWN, buff=0.5)  # 减小 buff 使其更靠近上方公式
        axes.shift(UP*0.3)  # 再微调上移

        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-3*PI, 3*PI])
        sin_label = axes.get_graph_label(sin_graph, label="\\sin x")

        taylor_1 = axes.plot(lambda x: x, color=RED, x_range=[-3*PI, 3*PI])
        taylor_3 = axes.plot(lambda x: x - x**3/6, color=GREEN, x_range=[-3*PI, 3*PI])
        taylor_5 = axes.plot(lambda x: x - x**3/6 + x**5/120, color=BLUE, x_range=[-3*PI, 3*PI])

        self.play(Create(axes), Create(sin_graph), Write(sin_label))
        self.wait(1)
        self.play(Create(taylor_1), Create(taylor_3), Create(taylor_5))
        self.wait(2)

        # 清除图形，只保留 taylor_eq
        self.play(FadeOut(axes), FadeOut(sin_graph), FadeOut(sin_label),
                  FadeOut(taylor_1), FadeOut(taylor_3), FadeOut(taylor_5))

        sin_over_x = MathTex(
            r"\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \frac{x^6}{7!} + \cdots",
            font_size=38
        ).next_to(taylor_eq, DOWN, buff=0.5)
        self.play(Transform(taylor_eq.copy(), sin_over_x))
        self.wait(2)

        # 强调 x^2 项系数
        x2_coef_text = Text("x² 项的系数：", font_size=36, color=ORANGE)
        x2_coef_formula = MathTex(r"-\frac{1}{3!} = -\frac{1}{6}", font_size=36, color=ORANGE)
        x2_coef_group = VGroup(x2_coef_text, x2_coef_formula).arrange(RIGHT, buff=0.2).next_to(sin_over_x, DOWN, buff=0.5)
        self.play(Write(x2_coef_group))
        self.wait(2)

        # 清屏，保留标题和idea
        self.play(*[FadeOut(mob) for mob in [taylor_title, taylor_eq, sin_over_x, x2_coef_group]])
        self.wait(0.5)

        # ------------------- 2. 无穷乘积 -------------------
        product_title = Text("2. sin x 的无穷乘积表示", font_size=32, color=PURPLE).next_to(idea, DOWN, buff=1)
        self.play(Write(product_title))
        self.wait(0.5)

        roots_text = Text("sin x 的根：", font_size=30, color=GREEN).next_to(product_title, DOWN, buff=0.5)
        roots = MathTex(r"0,\ \pm\pi,\ \pm2\pi,\ \pm3\pi,\ \dots", font_size=36).next_to(roots_text, RIGHT)
        self.play(Write(roots_text), Write(roots))
        self.wait(1)

        roots2_text = Text("因此 sin x / x 的根：", font_size=30, color=GREEN).next_to(roots_text, DOWN, buff=0.5, aligned_edge=LEFT)
        roots2 = MathTex(r"\pm\pi,\ \pm2\pi,\ \pm3\pi,\ \dots", font_size=36).next_to(roots2_text, RIGHT)
        self.play(Write(roots2_text), Write(roots2))
        self.wait(1)

        product = MathTex(
            r"\frac{\sin x}{x} = \left(1 - \frac{x}{\pi}\right)\left(1 + \frac{x}{\pi}\right)"
            r"\left(1 - \frac{x}{2\pi}\right)\left(1 + \frac{x}{2\pi}\right)\cdots",
            font_size=30
        ).next_to(roots2_text, DOWN, buff=1)
        self.play(Write(product))
        self.wait(2)

        product_sq = MathTex(
            r"\frac{\sin x}{x} = \prod_{n=1}^{\infty} \left(1 - \frac{x^2}{n^2\pi^2}\right)",
            font_size=36
        ).next_to(product, DOWN, buff=0.5)
        self.play(Transform(product.copy(), product_sq))
        self.wait(2)

        expand_text = Text("展开乘积，x² 项的系数来源于每个因子中的", font_size=30, color=ORANGE).next_to(product_sq, DOWN, buff=1)
        term = MathTex(r"-\frac{x^2}{n^2\pi^2}", font_size=36).next_to(expand_text, DOWN)
        self.play(Write(expand_text), Write(term))
        self.wait(1)

        coef_product = MathTex(
            r"-\left( \frac{1}{\pi^2} + \frac{1}{4\pi^2} + \frac{1}{9\pi^2} + \cdots \right)",
            font_size=36
        ).next_to(term, DOWN, buff=0.5)
        self.play(Write(coef_product))
        self.wait(1)

        coef_simple = MathTex(
            r"= -\frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2}",
            font_size=36
        ).next_to(coef_product, DOWN, buff=0.3)
        self.play(Write(coef_simple))
        self.wait(2)

        # 清屏，保留标题和idea
        self.play(*[FadeOut(mob) for mob in [product_title, roots_text, roots, roots2_text, roots2,
                                             product, product_sq, expand_text, term, coef_product, coef_simple]])
        self.wait(0.5)

        # ------------------- 3. 比较系数 -------------------
        compare_title = Text("3. 比较两种展开的 x² 系数", font_size=32, color=PURPLE).next_to(idea, DOWN, buff=1)
        self.play(Write(compare_title))
        self.wait(0.5)

        compare_eq = MathTex(
            r"-\frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2} = -\frac{1}{6}",
            font_size=44
        ).next_to(compare_title, DOWN, buff=0.8)
        self.play(Write(compare_eq))
        self.wait(2)

        result = MathTex(
            r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}",
            font_size=48,
            color=YELLOW
        ).next_to(compare_eq, DOWN, buff=1)
        self.play(Write(result))
        self.wait(2)

        # 清屏，保留标题和idea
        self.play(*[FadeOut(mob) for mob in [compare_title, compare_eq, result]])
        self.wait(0.5)

        # ------------------- 4. 讨论与扩展 -------------------
        discussion_title = Text("欧拉证明的意义与后续发展", font_size=32, color=PURPLE).next_to(idea, DOWN, buff=1)
        self.play(Write(discussion_title))
        self.wait(0.5)

        # 使用 Text 对象创建带项目符号的列表
        point1 = Text("• 欧拉的证明基于大胆的类比，当时缺乏严格性。", font_size=28)
        point2 = Text("• 但结果正确，后来被魏尔斯特拉斯等数学家严格化。", font_size=28)
        point3 = Text("• 这个等式揭示了三角级数与数论的深刻联系。", font_size=28)
        point4_text = Text("• 更一般地，ζ(2n) 与伯努利数有关：", font_size=28)
        point4_formula = MathTex(r"\zeta(2n) = (-1)^{n+1} \frac{(2\pi)^{2n} B_{2n}}{2(2n)!}", font_size=28)
        point4 = VGroup(point4_text, point4_formula).arrange(RIGHT, buff=0.2)
        points = VGroup(point1, point2, point3, point4).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        points.next_to(discussion_title, DOWN, buff=0.5)

        self.play(Write(points))
        self.wait(4)

        final_text = Text(
            "欧拉的洞察力令人惊叹！",
            font_size=36,
            color=BLUE
        ).next_to(points, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(3)

        # 最终清屏
        self.play(*[FadeOut(mob) for mob in self.mobjects])
