def is_valid_triangle(a ,b ,c):
    if ((a + b) > c) or ((a + c) > b) or ((b + c) > a):
        return True
    else:
        return False
    
