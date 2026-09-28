def write(self, data):
    archive_name = self.filename
    if self.archive_name is not None:
        archive_name = self.archive_name
    super().writestr(archive_name, data)