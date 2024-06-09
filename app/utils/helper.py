
import logging
from typing import List

loger=logging.getLogger(__name__)
loger.setLevel(logging.DEBUG)

handler = logging.FileHandler('logfile.log')
handler.setLevel(logging.DEBUG)
loger.addHandler(handler)

def add_integers(input_list: List[int]) -> str:
    try:
        if not isinstance(input_list, list):
            loger.error(f"Unsupported input type: {type(input_list)}")
            return None

        total = sum(input_list)
        loger.info(f"Added list = {total}")
        return str(total)
    except Exception as e:
        loger.error(f"Error occurred: {e}")
        return None

def helper_toconvert_add(s: list):
    return ",".join(list(map(str, s)))


def str_int(s: str):
    str_list = s.split(',')
    int_list = []
    for x in str_list:
        try:
            int_list.append(int(x))
        except ValueError:
            int_list.append(None)
    return int_list
