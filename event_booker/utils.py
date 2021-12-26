def list_divider(lst, n):
    """Divides list into n long chunks
    lst: list with elements
    n: length of chunk required"""
    return [lst[i:i + n] for i in range(0, len(lst), n)]


if __name__ == '__main__':
    print(list_divider([x for x in range(18)], 3))
