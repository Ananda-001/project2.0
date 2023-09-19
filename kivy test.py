from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import mysql.connector

# Connect to your MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test"
)

cursor = db.cursor()

# Function to fetch data from the database
def fetch_data():
    cursor.execute("SELECT * FROM employee")
    return cursor.fetchall()

# Define the ScreenManager
class MyScreenManager(ScreenManager):
    pass

# Define the Screen that displays the tables
class TableScreen(Screen):
    def __init__(self, table_data, **kwargs):
        super(TableScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        for row in table_data:
            row_label = Label(text=str(row))
            layout.add_widget(row_label)

        button = Button(text="Next Page")
        button.bind(on_release=self.next_page)
        layout.add_widget(button)

        self.add_widget(layout)

    def next_page(self, instance):
        self.manager.current = "second_page"

# Define the App
class MyApp(App):
    def build(self):
        manager = MyScreenManager()

        # Fetch data for the first six tables
        for i in range(6):
            table_data = fetch_data()
            screen = TableScreen(name=f"table_screen_{i}", table_data=table_data)
            manager.add_widget(screen)

        # Create a button on the first screen to navigate to the second screen
        button = Button(text="Next Page")
        button.bind(on_release=lambda x: manager.switch_to(manager.screens[6]))
        manager.screens[5].children[0].add_widget(button)  # Add the button to the last table screen

        # Add a second screen (empty for now)
        second_screen = Screen(name="second_page")
        manager.add_widget(second_screen)

        return manager

if __name__ == '__main__':
    MyApp().run()
