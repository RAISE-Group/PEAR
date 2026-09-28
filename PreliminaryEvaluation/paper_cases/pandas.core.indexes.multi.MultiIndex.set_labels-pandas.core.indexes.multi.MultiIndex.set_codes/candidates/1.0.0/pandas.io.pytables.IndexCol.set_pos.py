def set_pos(self, pos: int):
    """ set the position of this column in the Table """
    self.pos = pos
    if pos is not None and self.typ is not None:
        self.typ._v_pos = pos