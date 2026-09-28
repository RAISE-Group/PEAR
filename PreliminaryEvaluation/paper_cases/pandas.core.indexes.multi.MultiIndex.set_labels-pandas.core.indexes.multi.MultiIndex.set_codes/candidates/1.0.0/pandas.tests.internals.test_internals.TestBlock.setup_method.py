def setup_method(self, method):
    self.fblock = create_block('float', [0, 2, 4])
    self.cblock = create_block('complex', [7])
    self.oblock = create_block('object', [1, 3])
    self.bool_block = create_block('bool', [5])
    self.int_block = create_block('int', [6])