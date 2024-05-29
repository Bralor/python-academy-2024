from pprint import pprint
from typing import Optional, Dict, Union, Any

NestedDICT = Union[str, Dict[str, Any]]


def get_flat_dictionary(nested: Dict[str, NestedDICT],
                        sep: str = '.',
                        parent: str = '',) -> Optional[Dict[str, str]]:
    """
    Return the flattened dict object with concatenated keynames.

    :param nested: The given nested dictionary,
    :type nested: Dict[str, NestedDICT]
    :param sep: the separator character,
    :param sep: str
    :param parent: the name of the parent key,
    :type parent: str
    :return: the flattened dict object.
    :rtype: Optional[Dict[str, str]]
    """
    if not nested:
        return None
    flat_dict = dict()

    for key, value in nested.items():
        formatted_key = f'{parent}{sep}{key}' if parent else key

        if not isinstance(value, dict):
            flat_dict[formatted_key] = value
        else:
            flat_dict.update(get_flat_dictionary(nested=value,
                                                 parent=formatted_key))

    return flat_dict


if __name__ == '__main__':
    nested_dictionary = {
        "first_name": "Matouš",
        "last_name": "Holinka",
        "contacts": {
            "email": "matous@holinka.com",
            "phone": {
                "personal": "111-222-333",
                "business": {
                    "office_1": "222-333-444",
                    "office_2": "444-333-222",
                }
            }
        }
    }
    result = get_flat_dictionary(nested_dictionary)
    pprint(result)
