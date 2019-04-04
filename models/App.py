import pandas


class App:
    def __init__(self):
        self.phone_numbers = {}
        self.input_file = None
        self.output_file = None

    def set_input_file(self, filename):
        self.input_file = filename

    def set_output_file(self, filename):
        self.output_file = filename

    @staticmethod
    def read_csv(file_name, **kwargs):
        return pandas.read_csv(file_name, **kwargs)

    def processing_data(self):
        csv_data = self.read_csv(self.input_file, parse_dates=['ACTIVATION_DATE', 'DEACTIVATION_DATE'],
                                 converters={'PHONE_NUMBER': lambda x: str(x)})
        csv_data.sort_values(by=['PHONE_NUMBER', 'ACTIVATION_DATE'], kind="heapsort", inplace=True)

        for index, row in csv_data.iterrows():
            if row['PHONE_NUMBER'] in self.phone_numbers:
                if row['ACTIVATION_DATE'] == self.phone_numbers[row['PHONE_NUMBER']]['deactivation_date']:
                    self.phone_numbers[row['PHONE_NUMBER']]['deactivation_date'] = row['DEACTIVATION_DATE']

                elif row['ACTIVATION_DATE'] > self.phone_numbers[row['PHONE_NUMBER']]['deactivation_date']:
                    self.phone_numbers.update({row['PHONE_NUMBER']: {
                        "REAL_ACTIVATION_DATE": row['ACTIVATION_DATE'],
                        "deactivation_date": row['DEACTIVATION_DATE']
                    }})
            else:
                self.phone_numbers[row['PHONE_NUMBER']] = {
                    "REAL_ACTIVATION_DATE": row['ACTIVATION_DATE'],
                    "deactivation_date": row['DEACTIVATION_DATE']
                }

    def write_result(self):
        result = pandas.DataFrame.from_dict(self.phone_numbers, orient="index")
        result.drop(columns="deactivation_date", inplace=True)
        result.reset_index(level=0, inplace=True)
        result.rename(columns={'index': 'PHONE_NUMBER'}, inplace=True)
        result.to_csv(self.output_file, encoding='utf8', index=False)

    def run(self):
        self.processing_data()
        self.write_result()
