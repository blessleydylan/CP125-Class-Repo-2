def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    # Check if one rectangle is completely to the left of the other
    if x1 + w1 <= x2 or x2 + w2 <= x1:
        return False

    # Check if one rectangle is completely above the other
    if y1 + h1 <= y2 or y2 + h2 <= y1:
        return False

    # Otherwise, rectangles overlap
    return True

    """
    Checks if two rectangles are colliding (overlapping).
    
    Parameters:
    x1, y1: Top-left coordinate of Rectangle 1
    w1, h1: Width and Height of Rectangle 1
    x2, y2: Top-left coordinate of Rectangle 2
    w2, h2: Width and Height of Rectangle 2
    
    Returns:
    True if rectangles overlap, False otherwise
    
    Hint: It's easier to check when they DON'T overlap:
    - Rect 1 is completely to the left of Rect 2
    - Rect 1 is completely to the right of Rect 2
    - Rect 1 is completely above Rect 2
    - Rect 1 is completely below Rect 2
    
    If none of these are true, they must be overlapping!
    """
    # TODO: Implement collision detection logic
    pass
