import os 

class FileManager():
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def prepare_level_directory(self, url):
        node_directory = '{}/nodes/'.format(url)
        os.makedirs(url, exist_ok=True)
        os.makedirs(node_directory, exist_ok=True)

    def create_level_directories(self, start_at, amount_of_level):
        level_directories = []
        for x in range(start_at, amount_of_level):
            file_index = x + 1
            
            directory_url = "{}/Level{}".format(self.base_dir, file_index)

            self.prepare_level_directory(directory_url)

            level_directories.append(directory_url)

        return level_directories

    def create_world_directory(self, world_dir):
        os.makedirs(world_dir, exist_ok=True)



