@property
def shape(self):
    try:
        return (len(self.group.values),)
    except (TypeError, AttributeError):
        return None