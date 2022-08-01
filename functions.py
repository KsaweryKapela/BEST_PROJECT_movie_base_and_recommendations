def check_for_arrow(movie_list):
    try:
        movie_list[7]
        return True
    except IndexError:
        return False
