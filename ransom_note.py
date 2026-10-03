def can_construct(ransomNote: str, magazine: str) -> bool:
    
    if len(ransomNote) > len(magazine):
        return False
    
    letter_counts = {}
  
    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    for char in ransomNote:
        if letter_counts.get(char, 0) == 0:
            return False
        letter_counts[char] -= 1

    return True
