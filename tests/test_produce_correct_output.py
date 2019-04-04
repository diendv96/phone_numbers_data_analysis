import models.App as App
import os

app = App.App()

os.chdir("..")


def run_sample():
    app.set_input_file("data/PhoneNumber.csv")
    app.set_output_file("data/PhoneNumberResult.csv")
    app.run()


def test_output_csv_file():
    run_sample()
    actual_result = app.read_csv("data/PhoneNumberResult.csv")
    expect_result = app.read_csv("tests/PhoneNumberResult_Test.csv")
    assert actual_result.equals(expect_result)
