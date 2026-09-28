def _args_adjust(self):
    if self.subplots:
        if self.orientation == 'vertical':
            self.sharex = False
        else:
            self.sharey = False