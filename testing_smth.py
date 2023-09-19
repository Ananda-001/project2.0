from kivy.lang import Builder
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("test.kv")

    def login(self):
        # Replace with your login logic here

        pass

    def forgot_password(self):
        # Replace with your forgot password logic here
        pass

    def create_account(self):
        # Replace with your create account logic here
        pass

if __name__ == "__main__":
    MyApp().run()
