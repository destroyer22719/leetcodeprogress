def solution(S):
    answer = 0
    leading_zero_index = 0
    for i in range(len(S)):
        if S[i] != "0":
            break
        else:
            leading_zero_index += 1

    S = S[leading_zero_index:]
    S = S[::-1]

    S = S[::-1]
    for i in range(len(S)):
        if i != len(S) - 1:
            if S[i] == "1":
                answer += 2
            else:
                answer += 1
        else:
            if S[i] == "0":
                break
            else:
                answer += 1
    return answer

a = solution("011100")
print(a)