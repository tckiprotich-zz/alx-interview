def canUnlockAll(boxes):
    # Keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True  # Mark the first box as visited

    # Stack to store the boxes to be visited
    stack = [0]

    while stack:
        box = stack.pop()  # Get the topmost box from the stack
        for key in boxes[box]:
            if key >= 0 and key < len(boxes) and not visited[key]:
                visited[key] = True  # Mark the box as visited
                stack.append(key)  # Add the box to the stack

    # Check if all boxes have been visited
    return all(visited)
