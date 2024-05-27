for i in range(1, 10):  # Outer loop
    if i == 7:
        break  # Break out of the outer loop when i is 7
    for j in range(1, 10):  # Inner loop
        if j == 3:
            continue  # Skip the number 3
        print(j, end=' ')
    print()  # Newline for each iteration of the outer loop
