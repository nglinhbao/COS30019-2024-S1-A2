def FC(KB, q):
    count = {}
    inferred = {}
    queue = []

    # Initialize count and inferred tables
    for i, clause in enumerate(KB.clauses):
        count[i] = len(clause["PREMISE"])
        inferred[i] = False

    # Initialize queue with symbols known to be true in KB
    for i, clause in enumerate(KB.clauses):
        if count[i] == 0:
            queue.append(i)

    # Main loop
    while queue:
        i = queue.pop(0)
        clause = KB.clauses[i]
        p = clause["CONCLUSION"]
        if p == q:
            return True
        if not inferred[i]:
            inferred[i] = True
            for j, c in enumerate(KB.clauses):
                if p in c["PREMISE"]:
                    count[j] -= 1
                    if count[j] == 0:
                        queue.append(j)

    return False
