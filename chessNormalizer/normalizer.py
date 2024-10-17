
def normalize(move: str, legal_moves) -> str:
    """
    Normalize a chess move to a legal format if possible.
    
    Parameters:
        move (str): The chess move input by the user.
        legal_moves (list): A list of legal moves in SAN (Standard Algebraic Notation).
        
    Returns:
        str: The normalized move if it's valid, otherwise an error message.
    """
    move = move.strip()
    normalized_move = move.capitalize()
    if move in legal_moves:
        return move

    if move + '+' in legal_moves:
        return move + '+'
    elif move + '#' in legal_moves:
        return move + '#'
    
    if normalized_move in legal_moves:
        return normalized_move

    # Check variations with '+' or '#' for check or checkmate
    if normalized_move + '+' in legal_moves:
        return normalized_move + '+'
    elif normalized_move + '#' in legal_moves:
        return normalized_move + '#'

    # If no valid normalization found
    raise ValueError(f"Failed to normalize move: {move}.")
