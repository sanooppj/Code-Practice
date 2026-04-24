n1 = input()
n2 = input()

if len(n1) != len(n2):
    print("NO")
else:
    freq = {}

    # Count characters from first string
    for ch in n1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Decrease count using second string
    for ch in n2:
        if ch in freq:
            freq[ch] -= 1
        else:
            print("NO")
            break
    else:
        # Check if all frequencies became zero
        for value in freq.values():
            if value != 0:
                print("NO")
                break
        else:
            print("YES")