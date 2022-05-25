class FileHandler:
    def __init__(self, file_path: str) -> None:
        self.tool = None
        self.file_path = file_path

    def create_file(self) -> None:
        self.tool = open(self.file_path, 'w')

    def write_to_file(self, entry: str) -> None:
        self.tool.write(entry + '\n')

    def __del__(self):
        if self.tool is not None:
            self.tool.close()


