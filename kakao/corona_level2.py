#아직 못품
def solution(places):
    answer = []
    for i in rnage(len(places)):
        place = places[i]
        for j in range(len(place)):
            for k in range(5):
                if place[j][k] == "P":
                    pass


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    solution(places)