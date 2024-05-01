def BC(KB, ask):
    result, inferred_str = BC_recursive(KB, ask, {}, '')
    if result:
        return "YES: " + inferred_str[0:-2]
    return "NO: " + inferred_str[0:-2]


def BC_recursive(KB, ask, inferred, inferred_str):
    if ask in inferred:
        return inferred[ask], inferred_str

    for sentence in KB.sentences:
        if sentence.head == ask:
            if not sentence.conjuncts:
                inferred[ask] = True
                inferred_str += ask + ', '
                return True, inferred_str
            else:
                all_true = True
                for conjuncts in sentence.conjuncts:
                    result, inferred_str = BC_recursive(KB, conjuncts, inferred, inferred_str)
                    if not result:
                        all_true = False
                        break
                if all_true:
                    inferred[ask] = True
                    inferred_str += ask + ', '
                    return True, inferred_str
    return False, inferred_str
