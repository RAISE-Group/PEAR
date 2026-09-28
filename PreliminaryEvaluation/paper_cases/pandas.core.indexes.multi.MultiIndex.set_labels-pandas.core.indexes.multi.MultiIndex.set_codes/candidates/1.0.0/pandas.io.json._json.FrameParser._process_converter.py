def _process_converter(self, f, filt=None):
    """
        Take a conversion function and possibly recreate the frame.
        """
    if filt is None:
        filt = lambda col, c: True
    needs_new_obj = False
    new_obj = dict()
    for i, (col, c) in enumerate(self.obj.items()):
        if filt(col, c):
            new_data, result = f(col, c)
            if result:
                c = new_data
                needs_new_obj = True
        new_obj[i] = c
    if needs_new_obj:
        new_obj = DataFrame(new_obj, index=self.obj.index)
        new_obj.columns = self.obj.columns
        self.obj = new_obj