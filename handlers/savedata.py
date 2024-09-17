import pickle


class Data:
    def __init__(self):
        self.data = self.load_data()
    
    def load_data(self) -> dict:
        try:
            with open("data.pkl", "rb") as file:
                data = pickle.load(file)
        except (FileNotFoundError, EOFError) as e:
            data = {}
            print(f'Error: {e} - No save data found.')
        return data

    def save_data(self):
        with open("data.pkl", "wb") as file:
            pickle.dump(self.data, file)
    
    def modify_data(self, key, value):
        self.data[key] = value
        self.save_data()
