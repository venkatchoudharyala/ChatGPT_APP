import openai
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class MyApp(App):
        def build(self):
                layout = BoxLayout(orientation='vertical')
                self.input = TextInput(multiline=False)
                self.output0 = Label(text="YOU"+self.input.text)
                self.output = Label(text='ANSWER')
                layout.add_widget(self.input)
                layout.add_widget(self.output0)
                layout.add_widget(self.output)
                self.input.bind(on_text_validate=self.on_enter)
                scrollview = ScrollView()
                layout.add_widget(scrollview)
                self.app = App.get_running_app()
                self.app.root = scrollview
                return layout

        def on_enter(self, *args):
                self.output0.text=self.input.text
                openai.api_key="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"
                model_engine="text-davinci-002"
                prompt=str(self.input.text)
                completion=openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.9)
                response=completion.choices[0].text
                # Do something with the input and update the output
                self.output.text = "ChatGPT : " + response

if __name__ == '__main__':
        MyApp().run()
