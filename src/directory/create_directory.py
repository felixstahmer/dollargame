import os 

class FileManager():
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def create_level_directory(self, url):
        node_directory = '{}/nodes/'.format(url)
        os.makedirs(url, exist_ok=True)
        os.makedirs(node_directory, exist_ok=True)

    def create_directories_for_active_game(self, amount_of_level):
        level_directories = []
        for x in range(amount_of_level):
            file_index = x + 1
            
            directory_url = "{}/Level{}".format(self.base_dir, file_index)

            self.create_level_directory(directory_url)

            level_directories.append(directory_url)

        return level_directories



