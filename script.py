from manim import * 
import numpy as np

class Drake(Scene):
    def construct(self):
        heading = Tex("Do Alien's Exist?")
        drake = Tex("The Drake Equation")

        # Show heading
        self.play(Write(heading))
        self.wait(1)

        # Then fade it out
        self.play(Unwrite(heading))
        self.wait(1)
        # Then show Drake title
        self.play(Write(drake))
        self.wait()
        self.play(Unwrite(drake))

class Ozma(Scene):
    def construct(self):
        img = ImageMobject("Drake.jpg")
        img.scale(.4)
        self.play(FadeIn(img))
        self.wait(4.5)

        self.play(
            img.animate.scale(0.9).to_edge(LEFT),
            run_time=1.5
        )

        self.wait(2)
        title = Tex("SETI").scale(1.2)
        subtitle = Tex("Search for Extraterrestrial Intelligence").scale(0.7)

        text_group = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT)
        text_group.next_to(img, RIGHT, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP * 0.2))
        self.wait(3)
        self.play(FadeOut(text_group))

        wave = FunctionGraph(
            lambda x: 0.35 * np.sin(6 * x),
            x_range=[-1.5, 6, 0.01],
            color=BLUE
        )
        wave.next_to(img, RIGHT, buff=0.2)
        wave = wave.reverse_direction()

        self.play(Create(wave), run_time=2)

        question = Tex("?").scale(2)
        question.next_to(wave, UP, buff=0.5)

        self.play(Write(question))
        self.wait()
        self.play(FadeOut(question))

        full_wave = FunctionGraph(
            lambda x: 0.35 * np.sin(6 * x),
            x_range=[-7, 7, 0.01],
            color=BLUE
        )
        full_wave.move_to(ORIGIN)
        full_wave = full_wave.reverse_direction()

        self.play(
            FadeOut(img),
            Transform(wave, full_wave),
            run_time=1
        )

        bg_waves = VGroup()
        for y in [-3, -2, -1, 1, 2, 3]:
            bg_wave = FunctionGraph(
                lambda x: 0.22 * np.sin(6 * x),
                x_range=[-7, 7, 0.01],
                color=BLUE
            )
            bg_wave.move_to(ORIGIN).shift(UP * y)
            bg_waves.add(bg_wave)

        self.play(
            LaggedStart(*[Create(w) for w in bg_waves], lag_ratio=0),
            run_time=1
        )

        strong_wave = FunctionGraph(
            lambda x: 0.9 * np.sin(6 * x),
            x_range=[-7, 7, 0.01],
            color=RED
        )
        strong_wave.move_to(ORIGIN)
        strong_wave = strong_wave.reverse_direction()

        self.play(
            Transform(wave, strong_wave),
            run_time=1.5
        )
        self.wait()
        self.play(
            Transform(wave, full_wave),
            run_time=1.5
        )

        self.wait(3)
        self.play(FadeOut(wave),
                  FadeOut(bg_waves))
        self.wait()
        center_question= Tex("?").scale(2)
        self.play(
            Write(center_question),
            run_time=1
        )
        self.wait(7)
        self.play(
            FadeOut(center_question)
        )
        drake = Tex("The Drake Equation")
        self.play(Write(drake))
        self.wait(2)
        self.play(FadeOut(drake))
