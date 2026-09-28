def validate_and_set(self, handler: 'AppendableTable', append: bool):
    self.table = handler.table
    self.validate_col()
    self.validate_attr(append)
    self.validate_metadata(handler)
    self.write_metadata(handler)
    self.set_attr()