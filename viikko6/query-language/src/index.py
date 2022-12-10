from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from querybuilder import QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    # matcher = And(
    #     HasAtLeast(70, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("FLA"),
    #         PlaysIn("BOS")
    #     )
    # )
    # print(matcher)

    # matcher = (
    #     query
    #     .playsIn("NYR")
    #     .hasAtLeast(10, "goals")
    #     .hasFewerThan(20, "goals")
    #     .build()
    # )

    # matcher = And(
    #     PlaysIn("NYR"),
    #     HasAtLeast(10, "goals"),
    #     HasFewerThan(20, "goals")
    # )

    matcher = (
    query
        .oneOf(
        query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
        query.playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )
        .build()
    )

    # m1 = (
    # query
    #     .playsIn("PHI")
    #     .hasAtLeast(10, "assists")
    #     .hasFewerThan(5, "goals")
    #     .build()
    # )
    # # for player in stats.matches(m1):
    # #     print(player)

    # m2 = (
    # query
    #     .playsIn("EDM")
    #     .hasAtLeast(50, "points")
    #     .build()
    # )
    # # for player in stats.matches(m2):
    # #     print(player)
    # matcher = query.oneOf(m1, m2).build()

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()


#matcher = And(Or(And(PlaysIn("PHI"), HasAtLeast(10, "assists"), HasFewerThan(5, "goals")), And(PlaysIn("EDM"), HasAtLeast(50, "points"))))