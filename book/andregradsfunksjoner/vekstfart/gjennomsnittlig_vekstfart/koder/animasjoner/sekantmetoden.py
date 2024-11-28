from manim import *


class SekantMetoden(Scene):

    def construct(self):
        # Set up the axes and the quadratic function

        f = lambda x: 0.5 * (x**2 - 4)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 8, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": False},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        quadratic = axes.plot(f, x_range=[-5, 5], color=BLUE)

        # prerender graph and coordinate system
        self.add(labels)
        self.add(axes)
        self.add(quadratic)
        dy_pos = 1
        dy_neg = -1
        # self.play(Create(axes), Write(labels))
        # self.play(Create(quadratic))

        # Stage 1: make an initial guess and draw the first secant

        # Initial guesses
        x1 = -1
        y1 = f(x1)
        p1 = axes.c2p(x1, y1)
        dot1 = Dot(color=YELLOW).move_to(p1)
        x1_text = MathTex("x_1", color=YELLOW).move_to(axes.c2p(x1, dy_pos))

        x2 = 3
        y2 = f(x2)
        p2 = axes.c2p(x2, y2)
        dot2 = Dot(color=YELLOW).move_to(p2)
        x2_text = MathTex("x_2", color=YELLOW).move_to(axes.c2p(x2, dy_neg))

        vline_1 = DashedLine(
            start=axes.c2p(x1, y1),
            end=axes.c2p(x1, 0),
            color=YELLOW,
        )

        vline_2 = DashedLine(
            start=axes.c2p(x2, y2),
            end=axes.c2p(x2, 0),
            color=YELLOW,
        )

        stage1_part1 = VGroup(dot1, dot2)
        stage1_part2 = VGroup(vline_1, x1_text)
        stage1_part3 = VGroup(vline_2, x2_text)
        self.play(Create(stage1_part1), run_time=1)

        self.wait(2)

        self.play(Create(stage1_part2), run_time=1)
        self.wait(1)
        self.play(Create(stage1_part3), run_time=1)

        # Stage 2: draw secant

        slope = (y2 - y1) / (x2 - x1)
        xmin = -10
        xmax = 10

        ymin = y1 + slope * (xmin - x1)
        ymax = y1 + slope * (xmax - x1)

        p1 = axes.c2p(xmin, ymin)
        p2 = axes.c2p(xmax, ymax)
        secant = Line(
            start=p1,
            end=p2,
            color=YELLOW,
        )

        self.play(
            Create(secant),
            run_time=2,
        )

        # Stage 3: find zero of secant

        x_zero = x1 - y1 / slope

        p_zero = axes.c2p(x_zero, 0)
        dot_zero = Dot(color=RED).move_to(p_zero)
        zero_text = MathTex("x_3", color=RED).move_to(axes.c2p(x_zero, dy_pos))

        zero = VGroup(dot_zero, zero_text)
        self.play(
            Create(zero),
            run_time=1,
        )

        # Stage 4: move point to graph
