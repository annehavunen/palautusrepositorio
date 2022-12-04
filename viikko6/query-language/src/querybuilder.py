from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


class QueryBuilder:
    def __init__(self, matchers=[]):
        self.matchers = matchers

    def playsIn(self, team):
        self.matchers.append(PlaysIn(team))
        return QueryBuilder(self.matchers)

    def hasAtLeast(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(self.matchers)

    def hasFewerThan(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(self.matchers)

    def build(self):
        return And(*self.matchers)
