from models.App import App

app = App()

if __name__ == "__main__":
    app.set_input_file("data/PhoneNumber.csv")
    app.set_output_file("data/PhoneNumberResult.csv")
    app.run()
