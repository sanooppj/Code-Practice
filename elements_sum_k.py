# --- Input Section ---
# Assuming input is space-separated: e.g., 1 5 7 -1 5
arr = list(map(int, input("Enter array elements: ").split()))
K = int(input("Enter target sum K: "))

# --- Logic Section ---
seen = set()
printed_pairs = set()

for num in arr:
    target = K - num
    
    if target in seen:
        # Identify the pair components
        if num < target:
            pair = (num, target)
        else:
            pair = (target, num)
            
        # Check if we have already printed this specific pair
        if pair not in printed_pairs:
            print(pair[0], pair[1])
            printed_pairs.add(pair)
            
    # Add the current number to 'seen' for future lookups
    seen.add(num)