"""
I think it's better to perform a depth first search
and then use classic max finding logic of only storing
the largest route and value. Maybe some early exit logic 
such as if we have n steps left in path and
current_path - max_path < 9 * n.
"""

"""
I'm going to store the tree as a two dimensional list of 
dictionaries. The outer list represents the whole tree,
the inner list represents a row of the tree and each
dictionary represents a node with children.
"""

"""
I think I want a path to look like a sequence of L and R
this represents the choice of left and right in the path.
"""

def get_path_id(path_idx: int, path_len: int) -> str:
    """
    For a given index in our ordered set of paths this returns the 
    path_len bit binary representation of that index padded with leading zeros. 

    :param path_idx: Index of the current path, when paths are listed 
    in the Left sense.
    :type path_idx: int
    :param translation_dict: Dictionary encoding the translation from
    path notation into binary notation.
    :type translation_dict: dict
    :param path_len: Length of path
    :type path_len: int
    :return: The path id.
    :rtype: str
    """
    raw_path_id = bin(path_idx)[2:]

    return "0" * (path_len - len(raw_path_id) - 1) + raw_path_id


def get_path_from_id(path_id: str, translation_dict: dict, tree: list[list[int]]) -> list[int]:
    """
    Returns a list of values for all steps on a given path.
    
    :param path_id: ID of given path.
    :type path_id: str
    :param translation_dict: Dictionary encodeing the translation from
    path notation into binary notation.
    :type translation_dict: dict
    :param tree:
    :type tree: list[list[int]]
    :return: List of all numbers along given path.
    :rtype: list[int]
    """
    curr_pos = (0, 0)

    path = [tree[curr_pos[0]][curr_pos[1]]["value"]]

    for bin_digit in path_id:
        choice = translation_dict[bin_digit]

        nxt_pos = tree[curr_pos[0]][curr_pos[1]][choice]
        
        path.append(tree[nxt_pos[0]][nxt_pos[1]]["value"])
        
        curr_pos = nxt_pos

    return path


def main(tree: list[list[dict]]):
    """
    :param tree: Stores the tree as a two dimensional array of dictionaries.
    Each dictionary contains the value of the current position and the positional
    location of it's children.
    :type tree: list[list[dict]]
    """
    binary_to_path_dict = {
        "0": "L",
        "1": "R"
    }

    path_len = len(tree)
    total_paths = 2 ** (path_len - 1)
    max_path = {
        "path": [],
        "path_total": 0
    }
    print(total_paths)

    for path in range(total_paths): # look into some early exit logic
        path_id = get_path_id(
            path_idx=path, 
            path_len=path_len
        )

        path = get_path_from_id(
            path_id=path_id,
            translation_dict=binary_to_path_dict,
            tree=tree
        )

        path_total = sum(path)

        if path_total > max_path["path_total"]:
            max_path["path"] = path
            max_path["path_total"] = path_total

    print(f"Max path: {max_path["path"]}, Total along path: {max_path["path_total"]}")


if __name__ == "__main__":

    file_path = r"C:\Users\MilesHoar-Hewitt\Documents\python\python-fundamentals\exercise-3\input.txt"
    
    with open(file_path) as input_file:
        raw_array = [row.strip().split(" ") for row in input_file.readlines() if row != "\n"]
        
    clean_tree = []
    for row_idx in range(len(raw_array)):
        
        clean_row = []
        for col_idx in range(len(raw_array[row_idx])):
            clean_lmnt_dict = {
                "value": int(raw_array[row_idx][col_idx]),
                "L": None,
                "R": None
            }

            if row_idx < len(raw_array) - 1:
                clean_lmnt_dict["L"] = (row_idx + 1, col_idx)
                clean_lmnt_dict["R"] = (row_idx + 1, col_idx + 1)
            
            clean_row.append(clean_lmnt_dict)
        
        clean_tree.append(clean_row)

    main(tree=clean_tree)