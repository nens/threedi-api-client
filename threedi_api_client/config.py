import os


class Config:
    def __init__(self, env_file=None):
        self.file_values = {}
        if env_file is not None and os.path.isfile(env_file):
            self.file_values = self._read_file(env_file)

    def __call__(self, key):
        return self.get(key)

    def get(self, key):
        if key in os.environ:
            value = os.environ[key]
            return value
        if key in self.file_values:
            return self.file_values[key]
        raise KeyError(f"Config '{key}' is missing.")

    def _read_file(self, file_name):
        file_values = {}
        with open(file_name) as input_file:
            for line in input_file.readlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    file_values[key] = value
        return file_values
