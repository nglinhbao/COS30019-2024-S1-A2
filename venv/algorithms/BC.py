def BC(KB, q):
    return BC_recursive(KB, q, {})

def BC_recursive(KB, q, inferred):
    print(inferred)
    if q in inferred:
        return inferred[q]

    for clause in KB.clauses:
        if clause["CONCLUSION"] == q:
            if not clause["PREMISE"]:
                return True
            else:
                all_true = True
                for p in clause["PREMISE"]:
                    result = BC_recursive(KB, p, inferred)
                    if not result:
                        all_true = False
                        break
                if all_true:
                    inferred[q] = True
                    return True
    return False