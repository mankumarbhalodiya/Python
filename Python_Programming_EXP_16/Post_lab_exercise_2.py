from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Label to display the typed text
        self.output_label = Label(
            text="Type something and press the button!",
            font_size=24,
            size_hint=(1, 0.4)
        )

        # TextInput widget for user input
        self.input_text = TextInput(
            multiline=False,
            font_size=32,
            size_hint=(1, 0.2)
        )

        # Button to trigger the display
        display_button = Button(
            text="Display Text",
            font_size=28,
            size_hint=(1, 0.2)
        )
        display_button.bind(on_press=self.update_label)

        # Add widgets to layout
        main_layout.add_widget(self.output_label)
        main_layout.add_widget(self.input_text)
        main_layout.add_widget(display_button)

        return main_layout

    # Method to update label with input text
    def update_label(self, instance):
        typed_text = self.input_text.text
        self.output_label.text = f"You typed: {typed_text}"


# Run the app
if __name__ == '__main__':
    TextInputApp().run()
