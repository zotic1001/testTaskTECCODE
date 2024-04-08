from typing import List


def str_list_sort_asc(list_string: List[str]) -> List[str]:
    return sorted(list_string, key=lambda x: len(x))


def str_list_sort_desc(list_string: List[str]) -> List[str]:
    return sorted(list_string, key=lambda x: len(x), reverse=True)
