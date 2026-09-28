@cache_readonly
def colorconverter(self):
    import matplotlib.colors as colors
    return colors.colorConverter