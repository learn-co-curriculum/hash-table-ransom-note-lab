def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Dictionary to count how many times each character appears in the magazine
    counts = {}

    # Count characters in magazine
    for char in magazine:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1

    # build ransomNote using the counted characters
    for char in ransomNote:
        if char not in counts:
            return False

        if counts[char] == 0:
            return False

        counts[char] -= 1

    return True
