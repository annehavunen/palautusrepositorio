from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from querybuilder import QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(5, "assists"),
    #     PlaysIn("PHI")
    # )

    # matcher = And(
    #     Not(HasAtLeast(1, "goals")),
    #     PlaysIn("NYR")
    # )

    # matcher = And(
    #     HasFewerThan(1, "goals"),
    #     PlaysIn("NYR")
    # )

    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all))

    # matcher = Or(
    # HasAtLeast(45, "goals"),
    # HasAtLeast(70, "assists")
    # )

    # matcher = And(
    #     HasAtLeast(70, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("FLA"),
    #         PlaysIn("BOS")
    #     )
    # )
    # print(matcher)
    
    query = QueryBuilder()
    
    #matcher = query.playsIn("NYR").build()

    # matcher = And(
    #     PlaysIn("NYR"),
    #     HasAtLeast(10, "goals"),
    #     HasFewerThan(20, "goals")
    # )

    # matcher = query.build() #kaikki, 1123

    matcher = (
        query
        .playsIn("NYR")
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals")
        .build()
    )

    print("matcher",matcher)

    for player in stats.matches(matcher):
        print(player)
    print(len(stats.matches(matcher)))

if __name__ == "__main__":
    main()
