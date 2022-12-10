from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, matchers=[], all_matchers=[]):
        self.matchers = matchers
        self.all_matchers = all_matchers

    def playsIn(self, team):
        self.matchers.append(PlaysIn(team))
        return QueryBuilder(self.matchers)

    def hasAtLeast(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(self.matchers)

    def oneOf(self, *matchers):
        #self.matchers = self.all_matchers
        return QueryBuilder([Or(*matchers)])

    def build(self):
        built = And(*self.matchers)
        self.all_matchers.append(built)
        self.matchers.clear()
        return built

    def hasFewerThan(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(self.matchers)
