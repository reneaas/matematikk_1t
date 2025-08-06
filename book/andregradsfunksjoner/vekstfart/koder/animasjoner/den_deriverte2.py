from manim import *


class QuadraticFunctionWithTangentAndDerivative(Scene):
    def construct(self):
        # Create left axes for f(x)
        self.axes_left = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 17, 2],
            x_length=5,
            y_length=6,
            tips=False,
            axis_config={"include_numbers": True},
        ).to_edge(LEFT, buff=0.4)
        labels_left = self.axes_left.get_axis_labels(x_label="x", y_label="y")

        # Create right axes for f'(x)
        self.axes_right = Axes(
            x_range=[-4, 4, 1],
            y_range=[-6, 6, 1],
            x_length=5,
            y_length=6,
            tips=False,
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": False},
        ).to_edge(RIGHT, buff=0.4)
        labels_right = self.axes_right.get_axis_labels(x_label="x", y_label="y")

        self.f = lambda x: x**2 + 2
        # Plot f(x) = x^2 on left axes
        quadratic_graph = self.axes_left.plot(
            lambda x: self.f(x), x_range=[-4, 4], color=BLUE
        )
        quadratic_label = self.axes_left.get_graph_label(
            quadratic_graph, label="f(x) = x^2", x_val=2, direction=UP
        )

        self.add(self.axes_left, labels_left, quadratic_graph)
        self.add(self.axes_right, labels_right)

        # Create a dot that moves along f(x)
        x_start = -3
        moving_dot = Dot(color=YELLOW).move_to(
            self.axes_left.c2p(x_start, self.f(x_start))
        )
        self.play(FadeIn(moving_dot))

        # Create a ValueTracker to animate x-values
        self.x_tracker = ValueTracker(x_start)

        # Updater for moving dot
        def update_moving_dot(dot):
            x = self.x_tracker.get_value()
            y = self.f(x)
            dot.move_to(self.axes_left.c2p(x, y))

        moving_dot.add_updater(update_moving_dot)

        # Create the tangent line using always_redraw with a local function
        tangent_line = always_redraw(
            lambda: self.axes_left.get_secant_slope_group(
                x=self.x_tracker.get_value(),
                graph=quadratic_graph,
                dx=0.01,
                secant_line_length=6,
                secant_line_color=YELLOW,
            )
        )
        self.play(Create(tangent_line))
        self.wait(1)

        # Draw the triangle representing the slope using a local function
        def get_slope_triangle():
            x = self.x_tracker.get_value()
            slope = 2 * x
            y = self.f(x)
            x0 = x
            x1 = x + 1
            y0 = y
            y1 = y + slope * (x1 - x0)

            height = DashedLine(
                start=self.axes_left.c2p(x0, y0),
                end=self.axes_left.c2p(x0, y1),
                color=TEAL_A,
            )
            base = DashedLine(
                start=self.axes_left.c2p(x0, y1),
                end=self.axes_left.c2p(x1, y1),
                color=WHITE,
            )
            base_label = MathTex("1").next_to(base, DOWN, buff=0.1)
            height_label = MathTex(f"{slope:.2f}", color=TEAL_A).next_to(
                height, LEFT, buff=0.1
            )
            triangle_group = VGroup(base, height, base_label, height_label)
            return triangle_group

        triangle = always_redraw(get_slope_triangle)
        self.play(Create(triangle))
        self.wait(1)

        # Animate moving dot from x = -3 to x = 3 and back
        self.play(
            self.x_tracker.animate.set_value(-x_start), run_time=8, rate_func=linear
        )
        self.wait(1)

        self.play(
            self.x_tracker.animate.set_value(x_start), run_time=8, rate_func=linear
        )
        self.wait(1)

        # Add the derivative dot and its updater
        derivative_dot = Dot(color=WHITE).move_to(
            self.axes_right.c2p(x_start, 2 * x_start)
        )

        def update_derivative_dot(dot):
            x = self.x_tracker.get_value()
            y = 2 * x
            dot.move_to(self.axes_right.c2p(x, y))

        derivative_dot.add_updater(update_derivative_dot)

        # Create derivative_hline using a local function
        def create_derivative_hline():
            x = self.x_tracker.get_value()
            y = 2 * x
            return DashedLine(
                start=self.axes_right.c2p(x, y),
                end=self.axes_right.c2p(0, y),
                color=WHITE,
            )

        derivative_hline = always_redraw(create_derivative_hline)

        # Create derivative_text using a local function
        def create_derivative_text():
            y = 2 * self.x_tracker.get_value()
            hline = derivative_hline
            return MathTex(f"{y:.2f}", color=TEAL_A).next_to(hline, LEFT, buff=0.1)

        derivative_text = always_redraw(create_derivative_text)

        # Add derivative dot, line, and label to the scene
        self.play(
            FadeIn(derivative_dot),
            Create(derivative_hline),
            Write(derivative_text),
        )
        self.wait(1)

        # Animate moving dot again and trace derivative
        derivative_path = TracedPath(
            derivative_dot.get_center,
            stroke_color=TEAL_A,
            stroke_width=5,
        )
        self.add(derivative_path)

        # Animate from x = -3 to x = 3 (first half of the second roundtrip)
        self.play(
            self.x_tracker.animate.set_value(-x_start), run_time=8, rate_func=linear
        )
        self.wait(1)

        # Stop updating the derivative path so it remains fully drawn
        # derivative_path.clear_updaters()

        # Optionally, you can add the derivative graph (f'(x) = 2x) to the scene
        derivative_graph = self.axes_right.plot(
            lambda x: 2 * x, x_range=[-4, 4], color=RED
        )
        # self.play(Create(derivative_graph), run_time=2)
        self.wait(1)

        # Animate from x = 3 back to x = -3 (second half of the second roundtrip)
        self.play(
            self.x_tracker.animate.set_value(x_start), run_time=8, rate_func=linear
        )
        self.wait(1)

        # Clean up updaters
        moving_dot.remove_updater(update_moving_dot)
        derivative_path.clear_updaters()
        derivative_dot.clear_updaters()
