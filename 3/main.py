import re
import itertools


def getSchematicsPart(line, position, length):
    return list(
        map(
            lambda line: line[
                position if position == 0 else position - 1 : position + length + 1
            ],
            schematics[line if line == 0 else line - 1 : line + 2],
        )
    )


def isPartValid(schematicPart):
    return any(map(lambda part: len(re.sub(r"[\d\.\n]", "", part)) > 0, schematicPart))


with open("3/input.txt") as file:
    schematics = file.readlines()

    partsWithSoundings = list(
        map(
            lambda x: list(
                map(
                    lambda match: (
                        int(match.group()),
                        getSchematicsPart(x[0], match.start(), len(match.group())),
                    ),
                    re.finditer("\d+", x[1].strip()),
                )
            ),
            enumerate(schematics),
        )
    )

    partsWithSoundings = list(itertools.chain(*partsWithSoundings))

    partsNotFiltered = map(
        lambda part: (part[0], isPartValid(part[1])), partsWithSoundings
    )

    partsFiltered = map(
        lambda part: part[0], filter(lambda part: part[1], partsNotFiltered)
    )

    print(sum(partsFiltered))
