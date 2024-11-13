from manim import *


class CompletingTheSquare(Scene):
    def construct(self):
        # Step 1: Introduce the quadratic function
        title = Text("Fullstendige kvadraters metode").to_edge(UP)
        equation = MathTex("f(x) = x^2 + bx + c").scale(1.2).move_to(ORIGIN)

        # Display title and equation
        self.play(Write(title))
        self.play(Write(equation))

        # Step 2: Break down the quadratic function
        self.wait(3)
        step1 = MathTex(
            "f(x) = x^2 + bx",
            " + \\left(\\frac{b}{2}\\right)^2 - \\left(\\frac{b}{2}\\right)^2",
            " + c",
        ).move_to(ORIGIN)
        step1[1].set_color(RED)
        # step1.next_to(equation, DOWN, buff=0.5)
        self.play(Transform(equation, step1))

        # Step 3: Add and subtract the square to complete
        self.wait(3)
        step2 = MathTex(
            "f(x) =",
            "\\left(x + \\frac{b}{2}\\right)^2",
            "- \\left(\\frac{b}{2}\\right)^2 + c",
        ).move_to(ORIGIN)
        step2[1].set_color(RED)
        forklaring = MathTex("\\text{Bruker 1. eller 2.kvadratsetning}").to_edge(DOWN)
        self.play(Write(forklaring))
        # step2.next_to(step1, DOWN, buff=0.5)
        self.play(Transform(equation, step2))

        self.play(FadeOut(forklaring))

        self.wait(5)
        # Clear the screen at the end
        self.play(
            FadeOut(equation),
        )
