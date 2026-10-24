from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyFirstApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.message = Label(
            text="আমার প্রথম Android অ্যাপ!",
            font_size=24
        )

        button = Button(
            text="এখানে চাপ দাও",
            font_size=20
        )
        button.bind(on_press=self.clicked)

        layout.add_widget(self.message)
        layout.add_widget(button)

        return layout

    def clicked(self, instance):
        self.message.text = "অভিনন্দন! অ্যাপ কাজ করছে!"


MyFirstApp().run()
