
Question: Largest Possible Square For Cut Sticks: -Want To Cut Sticks So That We Achieve 4 Sticks Of The Same Length. (There Can Be Leftover Pieces).
What Is The Longest Square Side That We Can Achieve? -Use This Function Def Square(A, B) Input: Two Integers A, B Output: Return The Side Length Of The 
Largest Square That We Can Have, If Not Possible Function Should return 0
def solution(A, B):
    total_sticks = A + B
    max_length_together = total_sticks // 4

    while max_length_together > 0:
        count_A = A // max_length_together
        count_B = B // max_length_together

        if count_A + count_B >= 4:
            return max_length_together

        max_length_together -= 1

    return 0

# Example usage:
result = solution(0,8)
print(result)
