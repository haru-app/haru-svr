import copy


class Schema:
    def __init__(self, value):
        self.value = value
        self.vCast = True
        self.vIsType = None
        self.vStrict = False
        self.vStrip = False
        self.vIsDefault = False
        self.vDefault = None
        self.vNullable = False
        self.vRequired = False
        self.vOneOf = []
        self.vNotOneOf = []
        self.vWhen = None

    def clone(self):
        return copy.deepcopy(self)

    def cast(self, type):
        self.vCast = type
        return self

    def isType(self, type):
        self.vIsType = type
        return self

    def strict(self, isStrict):
        self.vStrict = None
        return self

    def strip(self, isStrip):
        self.vStrip = isStrip
        return self

    def default(self, *args):
        if len(args) == 0:
            self.vIsDefault = False
        else:
            self.vIsDefault = True
            self.vDefault = args[0]
        return self

    def nullable(self, isNullable):
        self.vNullable = isNullable
        return self

    def required(self, isRequired):
        self.vRequired = isRequired
        return self

    def oneOf(self, array):
        self.vOneOf = array
        return self

    def notOneOf(self, array):
        self.vNotOneOf = array
        return self

    def when(self, function):
        self.vWhen = function
        return self
