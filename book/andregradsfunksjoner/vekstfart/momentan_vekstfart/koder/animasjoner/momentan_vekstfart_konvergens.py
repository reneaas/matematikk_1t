from manim import *

config.frame_width = 16
config.frame_height = 10


class ConvergingSecants(Scene):

    def construct(self):
        # Set up the axes and the quadratic function

        f = lambda x: 0.5 * (x**2 - 4)

        def df(x):
            return (f(x + 1) - f(x - 1)) / 2

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 8, 1],
            x_length=10,
            y_length=8,
            axis_config={"include_numbers": True},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        quadratic = axes.plot(f, x_range=[-5, 5], color=BLUE)
        self.add(axes)
        self.add(labels)
        self.add(quadratic)

        # Point for the derivative
        x = 1
        y = f(x)
        dot = Dot(axes.coords_to_point(x, y), color=YELLOW)
        slope = df(x)
        xmin = -7
        xmax = 7

        tangent_point_text = MathTex(f"({x}, f({x}))", color=YELLOW).move_to(
            axes.coords_to_point(x + 1, f(x) - 1)
        )
        background_tangent_point = BackgroundRectangle(
            tangent_point_text,
            color=BLACK,
            fill_opacity=1,
        )

        tangent_point = VGroup(background_tangent_point, tangent_point_text)

        ymin = f(x) + slope * (xmin - x)
        ymax = f(x) + slope * (xmax - x)
        p1 = axes.coords_to_point(xmin, ymin)
        p2 = axes.coords_to_point(xmax, ymax)
        tangent_line = Line(
            p1,
            p2,
            color=YELLOW,
        )

        self.play(
            Create(tangent_line),
            Create(tangent_point),
            Create(dot),
            run_time=2,
        )

        self.wait(4)

        dx_values = [1, 2, 3]
        for dx in dx_values:
            x1 = x - dx
            x2 = x + dx
            slope = (f(x2) - f(x1)) / (x2 - x1)

            ymax = f(x1) + slope * (xmax - x1)
            ymin = f(x1) + slope * (xmin - x1)

            p1 = axes.coords_to_point(xmin, ymin)
            p2 = axes.coords_to_point(xmax, ymax)

            secant_line = Line(p1, p2, color=RED)

            dot1 = Dot(axes.coords_to_point(x1, f(x1)), color=RED, radius=0.1)
            dot2 = Dot(axes.coords_to_point(x2, f(x2)), color=RED, radius=0.1)

            # Animate the creation of the dot, secant line, and tangent line

            point1_text = MathTex(f"({x1}, f({x1}))", color=RED).move_to(
                axes.coords_to_point(x1 - 1.5, f(x1))
            )

            background_point1 = BackgroundRectangle(
                point1_text, color=BLACK, fill_opacity=1
            )
            point1 = VGroup(background_point1, point1_text)

            point2_text = MathTex(f"({x2}, f({x2}))", color=RED).move_to(
                axes.coords_to_point(x2 + 1.1, f(x2))
            )

            background_point2 = BackgroundRectangle(
                point2_text, color=BLACK, fill_opacity=1
            )

            point2 = VGroup(background_point2, point2_text)

            self.play(
                Create(dot1),
                Create(dot2),
                Create(point1),
                Create(point2),
            )

            self.wait(2)
            self.play(
                Create(secant_line),
                run_time=2,
            )
            self.wait(4)

            if x1 >= 0:
                average_rate_text = MathTex(
                    f"\\dfrac{{f({x2}) - f({x1})}}{{{x2} - {x1}}}",
                    color=RED,
                ).move_to(axes.coords_to_point(-3, 5))
            else:
                average_rate_text = MathTex(
                    f"\\dfrac{{f({x2}) - f({x1})}}{{{x2} - ({x1})}}",
                    color=RED,
                ).move_to(axes.coords_to_point(-3, 5))

            background_average_rate = BackgroundRectangle(
                average_rate_text,
                color=BLACK,
                fill_opacity=1,
            )
            average_rate_formula = VGroup(background_average_rate, average_rate_text)

            derivative_text = MathTex(f"f'({x}) = ", color=YELLOW).next_to(
                average_rate_formula, LEFT
            )

            background_derivative = BackgroundRectangle(
                derivative_text,
                color=BLACK,
                fill_opacity=1,
            )
            derivative = VGroup(background_derivative, derivative_text)

            self.play(
                Transform(
                    VGroup(point1, point2),
                    average_rate_formula,
                ),
                Create(derivative),
                run_time=1,
            )

            # self.play(Write(slope_text))
            self.wait(5)
            self.play(
                # FadeOut(dot1),
                # FadeOut(dot2),
                # FadeOut(secant_line),
                FadeOut(point1),
                FadeOut(point2),
                FadeOut(derivative),
                FadeOut(average_rate_formula),
                # FadeOut(background_average_rate),
                # FadeOut(background_derivative),
                # FadeOut(background_point1),
                # FadeOut(background_point2),
                # FadeOut(average_rate_formula),
            )
            self.play(
                secant_line.animate.set_opacity(0.3),
                dot1.animate.set_opacity(0.3),
                dot2.animate.set_opacity(0.3),
            )

        self.wait(3)
