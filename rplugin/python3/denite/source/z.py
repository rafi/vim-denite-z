import os
import time

from .base import Base


class Source(Base):
    """ Z (jump around) source for Denite """

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'z'
        self.kind = 'directory'
        self.vars = {
            'order': 'frecent',
            'data': os.environ.get('_Z_DATA') or os.path.expanduser('~/.z')
        }

    def on_init(self, context):
        self.filters = []
        if len(context['args']) > 0:
            self.filters = context['args'][0]

        if len(context['args']) > 1:
            self.vars['order'] = context['args'][1]

    def gather_candidates(self, context):
        j = J(self.vars['data'])

        # Prefer case-sensitive matches first
        if not j.matches(self.filters):
            j.matches(self.filters, True)

        directories = j.pretty(self.vars['order'])

        return [
            {
                'word': '{:<15} {}'.format(*path),
                'action__path': path[1],
                'filter__order': path[0],
            }
            for path in directories]


class J(object):
    """ Python version of z, by Rupa
        Original source: https://github.com/rupa/j2 """

    def __init__(self, datafile):
        self.datafile = datafile
        self.common = None
        self.args = []
        self.m = []
        self.ordered = {'rank': self.rank,
                        'recent': self.recent,
                        'frecent': self.frecent}
        # Get list, datafile format: path|rank|atime
        try:
            with open(self.datafile, 'r') as f:
                self.d = [l.strip().split('|') for l in f.readlines()]
            self.d = [d for d in self.d if os.path.exists(d[0])]
        except:
            self.d = []

    def pretty(self, order):
        """ return a listing by order """
        if order not in self.ordered:
            return ''
        return self.ordered[order]()

    def go(self, order):
        """ go by order """
        if order == 'common':
            return self.common
        if self.m and order in self.ordered:
            return self.ordered[order]()[-1][1]

    def rank(self):
        """ time spent/aging, taken care of in .sh """
        r = ([(i[0], i[2]) for i in self.m])
        return sorted(r, reverse=True)

    def recent(self):
        """ by recently accessed """
        r = ([(i[1], i[2]) for i in self.m])
        return sorted(r, reverse=False)

    def frecent(self):
        """ rank weighted by recently accessed """
        r = []
        for i in self.m:
            if i[1] <= 3600:
                r.append((i[0]*4, i[2]))
            elif i[1] <= 86400:
                r.append((i[0]*2, i[2]))
            elif i[1] <= 604800:
                r.append((i[0]/2, i[2]))
            else:
                r.append((i[0]/4, i[2]))
        return sorted(r, reverse=True)

    def matches(self, args, nocase=False):
        """
        set self.m to a list of possibly case sensitive path matches
        m format: (rank, atime, path)
        """

        def common(r, l, nocase):
            """
            return prefix if there's a common prefix to all matches,
            the prefix is in the list,
            and all the args match in it
            """
            pref = os.path.commonprefix([i[2] for i in r])
            if not pref or pref == '/':
                return None
            r = [i for i in r if i[2] == pref]
            if not r:
                return None
            if nocase:
                pref = pref.lower()
            for i in l:
                if i not in pref:
                    return None
            return r[0][2]

        def cmpare(str, l, nocase):
            """ every item in list l must match in string str """
            match = True
            if nocase:
                str = str.lower()
            for i in l:
                if i not in str:
                    match = False
            return match

        self.args, self.m = args, []
        if nocase:
            args = [i.lower() for i in args]
        for d in self.d:
            if not cmpare(d[0], args, nocase):
                continue
            self.m.append((float(d[1]),
                           int(time.time())-int(d[2]),
                           d[0]))
        self.common = common(self.m, args, nocase)
        return self.m
