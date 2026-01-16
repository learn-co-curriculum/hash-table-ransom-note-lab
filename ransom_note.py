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
    # Build a frequency table (hash table / dictionary) for available characters.
    counts = {}
    for ch in magazine:
        counts[ch] = counts.get(ch, 0) + 1

    # Try to "spend" characters to build the ransom note.
    for ch in ransomNote:
        # If the character is missing or we already used them all -> impossible.
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1

    return True
