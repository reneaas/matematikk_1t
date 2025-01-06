from manim import *


class SecantTangentEquality(Scene):

    def construct(self):
        # Set up the axes and the quadratic function

        f = lambda x: 0.5 * (x**2 - 4)

        def df(x):
            return (f(x + 1) - f(x - 1)) / 2

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        quadratic = axes.plot(f, x_range=[-5, 5], color=BLUE)

        # prerender graph and coordinate system
        self.add(labels)
        self.add(axes)
        self.add(quadratic)
        # self.play(Create(axes), Write(labels))
        # self.play(Create(quadratic))

        x_values = [-2, -1, 0, 1, 2]
        xmin = -5
        xmax = 5

        positions = {
            "point1": [
                (-3 - 1, f(-3) - 1),
                (-2 - 1, f(-2) - 1),
                (-1 - 1, f(-1) - 1),
                (0 + 1, f(0) - 1),
                (1 + 1, f(1) - 1),
            ],
            "point2": [
                (-1 - 1, f(-1) - 1),
                (0 - 1, f(0) - 1),
                (1 + 1, f(1) - 1),
                (2 + 1, f(2) - 1),
                (3 + 1, f(3) - 1),
            ],
            "point": [
                (-2 - 1, f(-2) - 1),
                (-1 - 1, f(-1) - 0.5),
                (0, f(0) - 1.5),
                (1 + 1, f(1) - 0.5),
                (2 + 1, f(2) - 1),
            ],
        }
        for i, x in enumerate(x_values):
            x1 = x - 1
            x2 = x + 1
            # p1 = axes.coords_to_point(x1, f(x1))
            # p2 = axes.coords_to_point(x2, f(x2))
            slope = (f(x2) - f(x1)) / (x2 - x1)

            ymax = f(x1) + slope * (xmax - x1)
            ymin = f(x1) + slope * (xmin - x1)

            p1 = axes.coords_to_point(xmin, ymin)
            p2 = axes.coords_to_point(xmax, ymax)

            secant_line = Line(p1, p2, color=RED)

            # Calculate the derivative (slope) at point x
            tangent_slope = df(x)  # Derivative of f(x) = x^2

            # Define the tangent line using the point-slope form
            y_min = (tangent_slope) * (xmin - x) + f(x)
            y_max = (tangent_slope) * (xmax - x) + f(x)

            p_min = axes.coords_to_point(xmin, y_min)
            p_max = axes.coords_to_point(xmax, y_max)
            tangent_line = Line(p_min, p_max, color=YELLOW)

            dot = Dot(axes.coords_to_point(x, f(x)), color=YELLOW, radius=0.1)
            dot1 = Dot(axes.coords_to_point(x1, f(x1)), color=RED, radius=0.1)
            dot2 = Dot(axes.coords_to_point(x2, f(x2)), color=RED, radius=0.1)

            tangent_text = MathTex(f"({x}, f({x}))", color=YELLOW).move_to(
                axes.coords_to_point(*positions.get("point")[i])
            )
            background = BackgroundRectangle(
                tangent_text,
                color=BLACK,
                fill_opacity=1,
            )

            tangent_specs = VGroup(background, tangent_text)

            point1_text = MathTex(f"({x1}, f({x1}))", color=RED).move_to(
                axes.coords_to_point(*positions.get("point1")[i])
            )
            background1 = BackgroundRectangle(
                point1_text,
                color=BLACK,
                fill_opacity=1,
            )

            point1 = VGroup(background1, point1_text)

            point2_text = MathTex(f"({x2}, f({x2}))", color=RED).move_to(
                axes.coords_to_point(*positions.get("point2")[i])
            )
            background2 = BackgroundRectangle(
                point2_text,
                color=BLACK,
                fill_opacity=1,
            )

            point2 = VGroup(background2, point2_text)

            self.play(
                Create(dot1),
                Create(dot2),
                Create(secant_line),
                Create(point1),
                Create(point2),
                run_time=1,
            )
            self.wait(4)

            self.play(
                Create(dot),
                Create(tangent_line),
                Create(tangent_specs),
                runtime=1,
            )
            self.wait(4)

            if x1 >= 0:
                gjennomsnittlig_vekstfart = MathTex(
                    f"\\dfrac{{f({x2}) - f({x1})}}{{{x2} - {x1}}}", color=RED
                )
            else:
                gjennomsnittlig_vekstfart = MathTex(
                    f"\\dfrac{{f({x2}) - f({x1})}}{{{x2} - ({x1})}}", color=RED
                )
            momentan_vekstfart = MathTex(f"f'({x}) = ", color=YELLOW).next_to(
                gjennomsnittlig_vekstfart,
                LEFT,
            )

            vekstfart = VGroup(momentan_vekstfart, gjennomsnittlig_vekstfart)
            background_new = BackgroundRectangle(
                vekstfart,
                color=BLACK,
                fill_opacity=1,
            )

            vekstfart = VGroup(background_new, vekstfart).move_to(
                axes.coords_to_point(0, 4)
            )

            self.play(Transform(VGroup(tangent_specs, point1, point2), vekstfart))

            self.wait(5)
            self.play(
                FadeOut(vekstfart),
                FadeOut(dot),
                FadeOut(dot1),
                FadeOut(dot2),
                FadeOut(tangent_line),
                FadeOut(secant_line),
                FadeOut(momentan_vekstfart),
                FadeOut(gjennomsnittlig_vekstfart),
                FadeOut(point1),
                FadeOut(point2),
                FadeOut(background),
                FadeOut(background1),
                FadeOut(background2),
            )
