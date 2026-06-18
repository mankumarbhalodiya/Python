from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        # Initialize the counter variable
        self.counter = 0

        # Main layout is a vertical BoxLayout
        main_layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Create a label to display the counter value
        self.counter_label = Label(
            text=str(self.counter),
            font_size=100,
            size_hint=(1, 0.7)  # Give it more vertical space
        )

        # Create a button to increment the counter
        increment_button = Button(
            text="Increment Counter",
            font_size=40,
            size_hint=(1, 0.3)  # Give it less vertical space
        )

        # Bind the button's 'on_press' event to the increment_counter method
        increment_button.bind(on_press=self.increment_counter)

        # Add the widgets to the main layout
        main_layout.add_widget(self.counter_label)
        main_layout.add_widget(increment_button)

        return main_layout

    # Method to increment the counter and update the label
    def increment_counter(self, instance):
        self.counter += 1
        self.counter_label.text = str(self.counter)

# Run the app
if __name__ == '__main__':
    CounterApp().run()