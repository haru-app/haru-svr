from .schema import Schema


class StringSchema(Schema):
    def __init__(self, value):
        super.__init__(value)
        self.min = None
        self.max = None
        self.required = False
        self.match = None
        self.sub = None
        self.ensure = False
        self.case = None

    def min(self, value):
        self.min = value
        return self

    def max(self, value):
        self.max = value
        return self

    def length(self, value):
        self.min = value
        self.max = value
        return self

    def required(self, value):
        self.required = value
        return self

    def match(self, value, **kwargs):
        self.match = {'value': value, 'options': kwargs}
        return self

    def sub(self, value, **kwargs):
        self.sub = {'value': value, 'options': kwargs}
        return self

    def ensure(self, value):
        self.ensure = value
        return self

    def trim(self, value):
        self.ensure = value
        return self

    def lowercase(self, value):
        if value is None:
            self.case = None
        self.case = 'lower'
        return self

    def uppercase(self, value):
        if value is None:
            self.case = None
        self.case = 'upper'
        return self
