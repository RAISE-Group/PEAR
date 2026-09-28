def write_metadata(self, handler: 'AppendableTable'):
    """ set the meta data """
    if self.metadata is not None:
        handler.write_metadata(self.cname, self.metadata)