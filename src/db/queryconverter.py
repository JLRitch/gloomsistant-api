"""queryconverter.py is a set of utilities to convert queries from a sqlite database into a target object"""
# standard modules
from typing import List

def to_obj_array(query_resp: list, obj_keys: List[str], key_filter: List[str]=[]) -> list:
    """
    Converts a list of lists to a list of dictionaries.
    """
    out_list = []
    if query_resp == []:
        return out_list
    for in_record in query_resp:
        out_record = {}
        for i, k in enumerate(obj_keys):
            out_record[k] = in_record[i]
        # use key_filter to subset specific values for output
        if key_filter != []:
            out_record = {
                k:v for k,v in out_record.items() if k in key_filter
            }
        out_list.append(out_record)
    return out_list

def delimited_str_to_list(delimited_value: str, delimiter: str="|") -> list:
    """
    Converts a string value to a delimited list. Default delimiter is "|"
    """
    if delimited_value is not None:
        out_list = delimited_value.split(delimiter)
    else:
        out_list = []
    return out_list