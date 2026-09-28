def close(self):
    """ close the handle if its open """
    try:
        self.path_or_buf.close()
    except IOError:
        pass