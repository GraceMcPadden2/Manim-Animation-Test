from manim import *

class Drake(Scene):
    def construct(self):
        equation = MathTex(
            "N", "=", "R^*", "\\cdot", "f_p", "\\cdot", "n_e",
            "\\cdot", "f_l", "\\cdot", "f_i", "\\cdot", "f_c",
            "\\cdot", "L"
        ).scale(1.5)

        self.play(Write(equation))
        self.wait()

        # Empty placeholders
        description = Tex("").scale(0.7).next_to(equation, DOWN, buff=1)

        low_text = MathTex("").scale(0.7)
        high_text = MathTex("").scale(0.7)
        top_group = VGroup(low_text, high_text).arrange(RIGHT, buff=2)
        top_group.move_to(UP * 3)

        self.add(description, top_group)

        # ----- N FIRST -----
        self.play(equation[0].animate.set_color(BLUE), run_time=0.5)

        n_desc = Tex("Number of detectable civilizations").scale(0.7)
        n_desc.next_to(equation, DOWN, buff=1)


        self.play(
            Transform(description, n_desc),
            run_time=0.5
        )

        self.wait(7)

        # ----- FACTORS -----
        factors = [2, 4, 6, 8, 10, 12, 14]

        descs = [
            "Rate of star formation",
            "Fraction of stars with planets",
            "Habitable planets per system",
            "Fraction where life appears",
            "Fraction with intelligent life",
            "Fraction with detectable technology",
            "Length of signal lifetime"
        ]

        low_vals = [
            "\\text{Low: } R^* \\approx 1",
            "\\text{Low: } f_p \\approx 1",
            "\\text{Low: } n_e \\approx 0.2",
            "\\text{Low: } f_l \\approx 10^{-3}",
            "\\text{Low: } f_i \\approx 10^{-9}",
            "\\text{Low: } f_c \\approx 0.1",
            "\\text{Low: } L \\approx 100"
        ]

        high_vals = [
            "\\text{High: } R^* \\approx 3",
            "\\text{High: } f_p \\approx 1",
            "\\text{High: } n_e \\approx 0.4",
            "\\text{High: } f_l \\approx 1",
            "\\text{High: } f_i \\approx 1",
            "\\text{High: } f_c \\approx 0.2",
            "\\text{High: } L \\approx 10^9"
        ]

        for i, desc, low, high in zip(factors, descs, low_vals, high_vals):
            self.play(equation[i].animate.set_color(RED), run_time=0.3)

            new_desc = Tex(desc).scale(0.7)
            new_desc.next_to(equation, DOWN, buff=1)

            new_low = MathTex(low).scale(0.7)
            new_high = MathTex(high).scale(0.7)

            new_top = VGroup(new_low, new_high).arrange(RIGHT, buff=2)
            new_top.move_to(UP * 3)

            self.play(
                Transform(description, new_desc),
                Transform(top_group, new_top),
                run_time=0.5
            )

            self.wait(7)

            self.play(equation[i].animate.set_color(WHITE), run_time=0.3)

        self.wait()


class Range(Scene):
    def construct(self):
        low_text = Tex("Low end: less than 1").scale(1.4)
        high_text = Tex("High end: over 10 million").scale(1.4)

        low_text.move_to(UP * 2.5)
        high_text.move_to(DOWN * 2.5)

        # staggered entrance
        self.play(FadeIn(low_text, shift=DOWN), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(high_text, shift=UP), run_time=1)

        self.wait(2)

        # dramatic exit
        self.play(
            low_text.animate.shift(UP).set_opacity(0),
            high_text.animate.shift(DOWN).set_opacity(0),
            run_time=1
        )