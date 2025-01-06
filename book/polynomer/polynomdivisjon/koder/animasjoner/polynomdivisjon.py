from manim import *


class PolynomialDivision(Scene):
    def construct(self):

        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{xcolor}")
        # Define the polynomials
        dividend = "(x^3 - 2x^2 - 5x + 6)"
        divisor = "(x - 3)"

        # Stage 1: write the expression
        stage1 = MathTex(f"{dividend} \\div {divisor} = ").move_to(LEFT * 3 + UP * 2.5)
        self.add(stage1)
        # self.play(Write(stage1))

        self.wait(2)

        self.play(
            stage1[0][1:3].animate.set_color(RED),
            stage1[0][-5].animate.set_color(RED),
        )

        self.wait(1)

        dividend = MathTex("x^3").set_color(RED).move_to(stage1[0][1:4])
        divisor = MathTex("x").set_color(RED).move_to(stage1[0][-5])

        self.add(dividend)
        self.add(divisor)

        self.play(
            dividend.animate.next_to(stage1[0][1:4], DOWN),
            divisor.animate.next_to(stage1[0][-5], DOWN),
        )

        self.wait(2)

        division = MathTex("\\dfrac{x^3}{x}", color=RED).next_to(stage1[0][-1])
        result = MathTex("x^2", color=RED).next_to(stage1[0][-1])
        self.play(Transform(VGroup(divisor, dividend), division))

        self.wait(2)

        self.play(
            Transform(VGroup(divisor, dividend), result),
        )

        self.wait(2)
        self.play(
            stage1[0][1:4].animate.set_color(WHITE),
            stage1[0][-6:-1].animate.set_color(RED),
        )

        # Draw horisontal line
        p1 = stage1.get_left()
        p1 += 0.5 * DOWN

        p2 = stage1[0][:-1].get_right()
        p2 += 0.5 * DOWN
        hline = Line(
            start=p1,
            end=p2,
            color=WHITE,
        )

        self.play(
            Create(hline),
        )

        self.wait(2)

        # Multiply result back
        stage2_part1 = MathTex("-x^2(x - 3)", color=RED).move_to(
            stage1[0][1:7].get_center() + DOWN
        )
        self.play(Create(stage2_part1))

        self.wait(2)

        stage2_part2 = MathTex("-x^3 + 3x^2", color=RED).move_to(stage2_part1)
        self.play(
            Transform(stage2_part1, stage2_part2),
        )

        stage2_part3 = Line(
            start=stage2_part2.get_left() + 0.5 * DOWN,
            end=stage2_part2.get_right() + 0.5 * DOWN,
            color=WHITE,
        )

        self.play(Create(stage2_part3))

        self.wait(2)

        self.play(
            stage1[0][:].animate.set_color(WHITE),
            result.animate.set_color(WHITE),
            stage1[0][1:7].animate.set_color(RED),
        )
        self.wait(2)

        term1 = MathTex("x^3 - 2x^2", color=RED).move_to(stage1[0][1:7])
        term2 = MathTex("-x^3 + 3x^2", color=RED).move_to(stage2_part2)

        self.add(term1, term2)

        # Substract the two

        self.play(
            term1.animate.move_to(2 * RIGHT),
        )

        self.play(
            term2.animate.next_to(term1, DOWN),
        )

        self.wait(2)

        hline = Line(
            start=term2.get_left() + 0.5 * DOWN,
            end=term2.get_right() + 0.5 * DOWN,
            color=WHITE,
        )

        self.play(
            Create(hline),
        )

        result = MathTex("x^2", color=RED).move_to(term2[0][6])
        result.move_to(result.get_center() + DOWN + 0.5 * LEFT)
        self.play(
            Create(result),
        )

        self.wait(2)
        self.play(
            FadeOut(term1),
            FadeOut(term2),
            FadeOut(hline),
            result.animate.move_to(stage2_part2[0][5].get_center() + 0.8 * DOWN),
        )

        self.wait(2)
