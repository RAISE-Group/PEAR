@cache_readonly
def groups(self):
    """ dict {group name -> group labels} """
    result = {key: value for key, value in zip(self.binlabels, self.bins) if key is not NaT}
    return result