def _get_row(self):
    return self.filepath_or_buffer.read(80).decode()