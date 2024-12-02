from manim import *


class GjennomsnittligVekstfart(Scene):
    def construct(self):
        # Set up the axes and the quadratic function
        f = lambda x: 0.5 * (x**2 - 4)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 10, 1],
            x_length=10,
            y_length=8,
            axis_config={"include_numbers": False},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        quadratic = axes.plot(f, x_range=[-5, 5], color=BLUE)

        # Prerender the first image into the animation
        self.add(axes, quadratic, labels)

        # Define points and secant line
        x1, x2 = -3, 4
        dot1 = Dot(axes.coords_to_point(x1, f(x1)), color=YELLOW, radius=0.1)
        dot2 = Dot(axes.coords_to_point(x2, f(x2)), color=YELLOW, radius=0.1)

        slope = (f(x2) - f(x1)) / (x2 - x1)

        xmin, xmax = -10, 10
        ymin = f(x1) + slope * (xmin - x1)
        ymax = f(x1) + slope * (xmax - x1)
        p1 = axes.coords_to_point(xmin, ymin)
        p2 = axes.coords_to_point(xmax, ymax)
        secant_line = Line(p1, p2, color=RED)

        # Add dots statically to the image
        self.add(dot1, dot2)
        self.add(secant_line)

        horisontal_line_fn = DashedLine(
            start=axes.coords_to_point(x1, f(x1)),
            end=axes.coords_to_point(x2, f(x1)),
            color=TEAL_A,
        )
        horisontal_line_text = MathTex(
            "b - a",
            color=TEAL_A,
        ).move_to(axes.coords_to_point(1, f(x1) - 0.5))

        background_horisontal_line = BackgroundRectangle(
            horisontal_line_text,
            color=BLACK,
            fill_opacity=1,
        )

        horisontal_line_data = VGroup(
            background_horisontal_line,
            horisontal_line_text,
        )

        self.add(horisontal_line_fn)
        self.add(horisontal_line_data)

        vertical_line_fn = DashedLine(
            start=axes.coords_to_point(x2, f(x1)),
            end=axes.coords_to_point(x2, f(x2)),
            color=TEAL_A,
        )

        self.add(vertical_line_fn)

        vertical_line_text = MathTex("f(b) - f(a)", color=TEAL_A).next_to(
            vertical_line_fn, RIGHT
        )

        vertical_line_data = VGroup(
            vertical_line_text,
        )

        self.add(vertical_line_data)

        # Add labeled points with background rectangles
        punkt1 = MathTex(
            "(a, f(a))",
            color=YELLOW,
        ).move_to(axes.coords_to_point(x1 - 0.7, f(x1) - 1))
        background1 = BackgroundRectangle(
            punkt1, color=BLACK, fill_opacity=1, stroke_color=YELLOW, stroke_width=10
        )
        punkt1_group = VGroup(background1, punkt1)  # Group text and background together

        punkt2 = MathTex(
            "(b, f(b))",
            color=YELLOW,
        ).move_to(axes.coords_to_point(x2 + 1.1, f(x2)))
        background2 = BackgroundRectangle(
            punkt2, color=BLACK, fill_opacity=1, stroke_color=YELLOW, stroke_width=10
        )
        punkt2_group = VGroup(background2, punkt2)

        self.add(punkt1_group, punkt2_group)

        # Add the average growth rate text with background
        gjennomsnittlig_vekstfart = MathTex(
            "\\dfrac{\\Delta f(x)}{\\Delta x} = \\dfrac{f(b) - f(a)}{b - a}",
            color=TEAL_A,
        ).move_to(axes.coords_to_point(-3, 6))
        background3 = BackgroundRectangle(
            gjennomsnittlig_vekstfart,
            color=BLACK,
            fill_opacity=1,
            stroke_color=TEAL_A,
            stroke_width=20,
        )
        vekstfart_group = VGroup(background3, gjennomsnittlig_vekstfart)

        # Animate the transformation
        punkter = VGroup(horisontal_line_data, vertical_line_data)
        punkter_copy = punkter.copy()

        self.wait(2)
        self.play(Transform(punkter, vekstfart_group))

        self.wait(5)

        self.play(
            Transform(vekstfart_group, punkter_copy),
            FadeOut(punkter),
        )
        self.wait(3)
