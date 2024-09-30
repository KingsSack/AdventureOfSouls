import pickle


class Data:
    def __init__(self):
        self.data = self.load()
    
    def load(self) -> dict:
        try:
            with open("data.pkl", "rb") as file:
                data = pickle.load(file)
        except (FileNotFoundError, EOFError) as e:
            data = {}
            print(f'Error: {e} - No save data found.')
        return data

    def save(self):
        try:
            with open("data.pkl", "wb") as file:
                pickle.dump(self.data, file)
        except (FileNotFoundError, EOFError) as e:
            print(f'Error: {e} - Could not save data.')
    
    def get_or_set_default(self, key, default_value):
        if key not in self.data:
            self.data[key] = default_value
            self.save()
        return self.data[key]

    def modify(self, key, value):
        self.data[key] = value
        self.save()
        return self.data[key]
