from manim import *


class QuadraticFunctionAndDerivativeSideBySide(Scene):
    def construct(self):
        # Create left axes for f(x)
        axes_left = Axes(
            x_range=[-3, 4, 1],
            y_range=[0, 12, 1],
            x_length=5,
            y_length=7,
            axis_config={"include_numbers": True},
        ).to_edge(LEFT, buff=1)
        labels_left = axes_left.get_axis_labels(x_label="x", y_label="y")

        # Create right axes for f'(x)
        axes_right = Axes(
            x_range=[-4, 5, 1],
            y_range=[-8, 8, 2],
            x_length=5,
            y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(RIGHT, buff=1)
        labels_right = axes_right.get_axis_labels(x_label="x", y_label="y")

        # Plot f(x) = x^2 on left axes
        f = lambda x: x**2 + 2
        quadratic_graph = axes_left.plot(f, x_range=[-4, 4], color=BLUE)
        quadratic_label = axes_left.get_graph_label(
            quadratic_graph, label="f(x) = x^2", x_val=2, direction=UP
        )

        # Plot f'(x) = 2x on right axes
        derivative_graph = axes_right.plot(lambda x: 2 * x, x_range=[-5, 5], color=RED)
        derivative_label = axes_right.get_graph_label(
            derivative_graph, label="f'(x) = 2x", x_val=2, direction=UP
        )

        # Draw the axes and graphs
        self.add(axes_left, labels_left, axes_right, labels_right)
        self.play(Create(quadratic_graph), Create(derivative_graph))
        self.wait(1)

        # Create dots that move along f(x) and f'(x)
        moving_dot = Dot(color=YELLOW)
        derivative_dot = Dot(color=GREEN)
        self.add(moving_dot, derivative_dot)

        # Create a ValueTracker to animate x-values
        tracker = ValueTracker(-3)

        # Updater functions for the dots
        def update_moving_dot(mob):
            x = tracker.get_value()
            y = f(x)
            mob.move_to(axes_left.c2p(x, y))

        def update_derivative_dot(mob):
            x = tracker.get_value()
            y = 2 * x
            mob.move_to(axes_right.c2p(x, y))

        # Add updaters to the dots
        moving_dot.add_updater(update_moving_dot)
        derivative_dot.add_updater(update_derivative_dot)

        # Create the tangent line with always_redraw
        tangent_line = always_redraw(
            lambda: axes_left.get_secant_slope_group(
                x=tracker.get_value(),
                graph=quadratic_graph,
                dx=0.01,
                secant_line_length=5,
                secant_line_color=YELLOW,
            )
        )
        self.play(
            Create(tangent_line),
            run_time=1,
        )

        # Animate the movement from x = -5 to x = 5
        slope_texts = []
        dots = []
        derivative_coords = []
        for x_val in range(-3, 2):
            # Animate tracker from current x to x + 1
            x = x_val + 1
            y = f(x)
            slope = 2 * x
            derivative_coords.append((x, slope))

            x_next = x + 1
            y_next = y + slope

            self.play(tracker.animate.set_value(x), run_time=2, rate_func=linear)
            self.wait(0.5)  # Pause at the integer value

            # Stage 1: create horisontal and vertical lines to illustrate slope on left graph

            # Create vertical line
            if x <= 0:
                p1 = axes_left.c2p(x, y)
                p2 = axes_left.c2p(x, y_next)
            else:
                p1 = axes_left.c2p(x, y)
                p2 = axes_left.c2p(x, y_next)

            vertical_line = DashedLine(
                start=p1,
                end=p2,
                color=YELLOW,
            )

            # Create horisontal line
            if x <= 0:
                p1 = axes_left.c2p(x, y_next)
                p2 = axes_left.c2p(x_next, y_next)
            else:
                p1 = axes_left.c2p(x, y_next)
                p2 = axes_left.c2p(x_next, y_next)

            horisontal_line = DashedLine(
                start=p1,
                end=p2,
                color=YELLOW,
            )

            if x != 0:
                stage_1 = VGroup(vertical_line, horisontal_line)
                self.play(
                    Create(stage_1),
                    run_time=1,
                )
            else:
                pass
                # stage_1 = VGroup(horisontal_line, vertical_line)

            # Stage 2: map slope next to horisontal line on left graph
            if x != 0:
                slope_text = MathTex(f"{slope:.0f}", color=YELLOW).next_to(
                    vertical_line, LEFT
                )
            else:
                slope_text = MathTex(f"{slope:.0f}", color=YELLOW).next_to(
                    horisontal_line, DOWN
                )
            slope_texts.append(slope_text)

            stage_2 = slope_text

            self.play(
                Create(slope_text),
                run_time=1,
            )

            # Stage 3: Leave a point behind
            dot = Dot(color=YELLOW).move_to(axes_left.c2p(x, y))
            self.add(dot)
            dots.append(dot)

            # Stage 4: map slope and x-value onto derivative graph at fixes x-values

            # Clean up

            self.play(stage_1.animate.set_opacity(0.5))

            self.wait(2)

        self.remove(derivative_dot)
        moving_dot.remove_updater(update_moving_dot)
        derivative_dot.remove_updater(update_derivative_dot)

        for coords, dot, slope_text in zip(derivative_coords, dots, slope_texts):
            x = coords[0]
            y = coords[1]
            slope = 2 * x
            x_start_dot = Dot(color=RED).move_to(axes_left.c2p(coords[0], 0))
            x_horisontal = DashedLine(
                start=axes_left.c2p(x, f(x)), end=axes_left.c2p(x, 0), color=RED
            )
            x_start = VGroup(x_horisontal, x_start_dot)
            self.play(Create(x_start))

            start = VGroup(x_start, slope_text)

            x_target = Dot(color=RED).move_to(axes_right.c2p(coords[0], 0))
            y_target = Dot(color=YELLOW).move_to(axes_right.c2p(0, coords[-1]))
            target = VGroup(x_target, y_target)
            # target = Dot(color=YELLOW).move_to(axes_right.c2p(*coords))

            self.wait(2)
            self.play(
                Transform(start, target),
                run_time=1,
            )

            self.wait(2)

            v_line = DashedLine(
                start=axes_right.c2p(x, 0),
                end=axes_right.c2p(x, slope),
                color=YELLOW,
            )

            h_line = DashedLine(
                start=axes_right.c2p(0, slope),
                end=axes_right.c2p(x, slope),
                color=YELLOW,
            )

            lines = VGroup(v_line, h_line)

            self.play(
                Create(lines),
                run_time=1,
            )

            self.wait(2)

        # Clean up updaters
