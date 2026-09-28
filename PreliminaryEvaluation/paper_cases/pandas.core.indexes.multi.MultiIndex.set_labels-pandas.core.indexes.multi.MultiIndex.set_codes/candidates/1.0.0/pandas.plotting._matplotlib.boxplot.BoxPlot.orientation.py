@property
def orientation(self):
    if self.kwds.get('vert', True):
        return 'vertical'
    else:
        return 'horizontal'