class Popups:
    def __init__(self, owner=None):
        self.active_popups = []


class NotYetImplementedWarn(Popups):
    def __init__(self, feature=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.feature = feature
        if self.feature in self.active_popups:
            raise Dupl
        self.active_popups.append('feature')
