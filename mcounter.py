class MCounter(object):
    '''
    multi-dimensional counter
    '''

    def __init__(self, m):
        if m < 0:
            raise Exception("dimension is negative")
        self.dimension = m
        if m == 0:
            self.count = 0
        else:
            self.count = {}

    def inc(self, *args):
        if len(args) != self.dimension:
            raise Exception("dimension not matched")
        if self.dimension == 0:
            self.count += 1
            return

        tmp = self.count
        for k in args[:-1]:
            if tmp.has_key(k):
                tmp = tmp[k]
            else:
                tmp[k] = {}
                tmp = tmp[k]
        if tmp.has_key(args[-1]):
            tmp[args[-1]] += 1
        else:
             tmp[args[-1]] = 1

    def get(self):
        return self.count

    def reset(self):
        if m == 0:
            self.count = 0
        else:
            self.count = {}
