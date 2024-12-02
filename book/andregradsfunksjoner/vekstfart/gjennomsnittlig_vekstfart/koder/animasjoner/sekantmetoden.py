from manim import *


class SecantMethod(Scene):
    def construct(self):
        # Define the function
        f = lambda x: (x**2 - 4)

        # Set up axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 8, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": False},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        quadratic = axes.plot(f, x_range=[-5, 5], color=BLUE)

        xmin = -10
        xmax = 10
        # Add axes and function to the scene
        self.add(axes, labels, quadratic)

        # Initial guesses
        x_prev = -1
        x_curr = 3

        # Create initial points and labels
        y_prev = f(x_prev)
        y_curr = f(x_curr)

        dot_prev = Dot(axes.c2p(x_prev, y_prev), color=YELLOW)
        dot_curr = Dot(axes.c2p(x_curr, y_curr), color=YELLOW)

        if f(x_prev) > 0:
            x_prev_label = MathTex(f"x_{{1}}", color=YELLOW).next_to(
                axes.c2p(x_prev, 0), DOWN
            )
        else:
            x_prev_label = MathTex(f"x_{{1}}", color=YELLOW).next_to(
                axes.c2p(x_prev, 0), UP
            )

        if f(x_curr) > 0:
            x_curr_label = MathTex(f"x_{{2}}", color=YELLOW).next_to(
                axes.c2p(x_curr, 0), DOWN
            )
        else:
            x_curr_label = MathTex(f"x_{{2}}", color=YELLOW).next_to(
                axes.c2p(x_curr, 0), UP
            )

        vline_prev = DashedLine(
            start=axes.c2p(x_prev, y_prev), end=axes.c2p(x_prev, 0), color=YELLOW
        )
        vline_curr = DashedLine(
            start=axes.c2p(x_curr, y_curr), end=axes.c2p(x_curr, 0), color=YELLOW
        )

        # Display initial points and labels
        self.play(Create(dot_prev), Create(dot_curr))
        self.play(Write(x_prev_label), Write(x_curr_label))
        self.play(Create(vline_prev), Create(vline_curr))

        # Number of iterations
        num_iterations = 4  # Change this to the desired number of iterations
        for i in range(num_iterations):
            # Draw the secant line
            slope = (y_curr - y_prev) / (x_curr - x_prev)
            ymin = f(x_curr) + slope * (xmin - x_curr)
            ymax = f(x_curr) + slope * (xmax - x_curr)
            secant = Line(axes.c2p(xmin, ymin), axes.c2p(xmax, ymax), color=YELLOW)
            self.play(
                Create(secant),
                # rate_func=linear,
                run_time=4,
            )

            self.wait(2)

            # Calculate the next approximation
            slope = (y_curr - y_prev) / (x_curr - x_prev)
            x_next = x_curr - y_curr / slope
            y_next = f(x_next)

            # Create a dot at x_next on the x-axis
            dot_next = Dot(axes.c2p(x_next, 0), color=RED)
            if f(x_next) > 0:
                x_next_label = MathTex(f"x_{{{i+3}}}", color=RED).next_to(
                    axes.c2p(x_next, 0), DOWN
                )
            else:
                x_next_label = MathTex(f"x_{{{i+3}}}", color=RED).next_to(
                    axes.c2p(x_next, 0), UP
                )
            self.play(Create(dot_next), Write(x_next_label))

            self.wait(2)

            # Draw vertical dashed line from (x_next, y_next) to x-axis
            vline_next = DashedLine(
                start=axes.c2p(x_next, y_next), end=axes.c2p(x_next, 0), color=YELLOW
            )

            # Move the dot to the graph
            self.play(dot_next.animate.set_color(YELLOW))
            self.play(
                dot_next.animate.move_to(axes.c2p(x_next, y_next)),
                Create(vline_next),
                x_next_label.animate.set_color(YELLOW),
            )

            # self.play(x_next_label.animate.next_to(axes.c2p(x_next, 0), DOWN))

            # Fade out previous elements if desired
            self.play(
                FadeOut(secant),
                FadeOut(dot_prev),
                FadeOut(x_prev_label),
                FadeOut(vline_prev),
            )

            # Update variables for the next iteration
            x_prev, y_prev = x_curr, y_curr
            x_curr, y_curr = x_next, y_next

            dot_prev = dot_curr
            x_prev_label = x_curr_label
            vline_prev = vline_curr

            dot_curr = dot_next
            x_curr_label = x_next_label
            vline_curr = vline_next

        self.wait()

        # Clean up!
        self.play(
            FadeOut(x_prev_label),
            FadeOut(dot_prev),
            FadeOut(vline_prev),
        )
