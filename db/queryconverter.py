"""queryconverter.py is a utility to convert queries from a sqlite database into a """

def to_obj_array(query_resp: list, obj_keys: list) -> list:
    """
    Converts a list of lists to a list of dictionaries.
    """
    out_list = []
    for in_record in query_resp:
        out_record = {}
        for i, k in enumerate(obj_keys):
            out_record[k] = in_record[i]
        out_list.append(out_record)
    return out_list
