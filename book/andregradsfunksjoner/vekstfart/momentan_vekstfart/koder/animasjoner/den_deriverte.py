from manim import *


class TheDerivative(Scene):
    def construct(self):
        # Step 1: Set up axes and the function
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3, 10, 2],
            axis_config={"include_numbers": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))

        # Define the function f(x) = x^2 and plot it
        func = lambda x: x**2
        func_graph = axes.plot(func, color=BLUE)
        self.play(Create(func_graph))

        # Step 2: Define the initial point and range for Δx
        x_val = 1  # Starting x-value for point A
        dx_values = [2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]  # Δx values approaching 0

        # Step 3: Animate secant lines with larger domain from x = -3 to x = 3
        x_min = -5
        x_max = 5
        secant_lines = []
        for dx in dx_values:
            # Calculate points A and B for the secant line
            x_val_dx = x_val + dx
            y_a = func(x_val)  # y-coordinate of point A
            y_b = func(x_val_dx)  # y-coordinate of point B

            # Create dots for points A and B
            point_a = axes.c2p(x_val, y_a)
            point_b = axes.c2p(x_val_dx, y_b)
            dot_a = Dot(point_a, color=RED)
            dot_b = Dot(point_b, color=GREEN)

            # Calculate the slope of the secant line
            secant_slope = (y_b - y_a) / dx

            # Calculate the start and end points of the secant line for x in [-3, 3]
            x_start, x_end = -3, 3
            y_start = y_a + secant_slope * (x_min - x_val)
            y_end = y_a + secant_slope * (x_max - x_val)
            secant_start = axes.c2p(x_min, y_start)
            secant_end = axes.c2p(x_max, y_end)

            # Create the secant line across the larger domain
            secant_line = Line(secant_start, secant_end, color=RED)

            # Display the slope of the secant line
            slope_text = MathTex(f"a = {secant_slope:.2f}").move_to(axes.c2p(1, 6))
            # Draw the secant line, dots, and slope text
            self.play(
                Create(secant_line),
                Write(slope_text),
                FadeIn(dot_a),
                FadeIn(dot_b),
                run_time=1.5,
            )
            secant_lines.append(secant_line)  # Keep secant line for fade out later

            # Remove the slope text and dots for the next iteration
            self.play(
                FadeOut(slope_text), FadeOut(dot_b), FadeOut(secant_line), run_time=0.5
            )

        # Step 4: Draw the tangent line as Δx approaches 0
        tangent_slope = 2 * x_val  # Derivative of x^2 at x_val is 2*x
        y_start = y_a + tangent_slope * (x_min - x_val)
        y_end = y_a + tangent_slope * (x_max - x_val)
        tangent_line = Line(
            axes.c2p(x_min, y_start), axes.c2p(x_max, y_end), color=ORANGE
        )
        # tangent_slope_text = MathTex(
        #     f"\\text{{Tangent slope }} m = {tangent_slope:.2f}"
        # ).next_to(axes, UP)
        slope_text = MathTex(f"a = {tangent_slope:.2f}").move_to(axes.c2p(1, 6))

        # Display the tangent line and final slope text
        # self.play(*[FadeOut(secant) for secant in secant_lines])
        self.play(Create(tangent_line), Write(slope_text), run_time=2)

        # Clean up the scene
        self.wait(4)
        # self.play(
        #     FadeOut(tangent_line),
        #     FadeOut(func_graph),
        #     FadeOut(dot_a),
        #     FadeOut(axes),
        #     FadeOut(labels),
        # )
