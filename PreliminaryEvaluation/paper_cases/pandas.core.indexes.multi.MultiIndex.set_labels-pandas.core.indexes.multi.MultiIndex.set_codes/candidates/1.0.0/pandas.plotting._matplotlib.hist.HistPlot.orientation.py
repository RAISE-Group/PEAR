@property
def orientation(self):
    if self.kwds.get('orientation', None) == 'horizontal':
        return 'horizontal'
    else:
        return 'vertical'