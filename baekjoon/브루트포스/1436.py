import sys
import re

def solution(movie: int) ->str:
    movie_title = 666
    result = 1
    matching = re.search(r"666", str(movie_title))
    while result != movie:
        movie_title = movie_title + 1
        if re.search(r"666", str(movie_title)):
            result += 1
    return str(movie_title)



if __name__ == "__main__":
    movie = int(sys.stdin.read().strip())
    print(solution(movie))
