def FC(KB, ask):
    count = {}
    inferred = {}
    agenda = []
    answer = "NO: "
    inferred_str = ''

    # Initialize count and inferred tables
    for i, sentence in enumerate(KB.sentences):
        count[i] = len(sentence.conjuncts)
        if count[i] == 0:
            agenda.append(i)
        inferred[i] = False

    # Main loop
    while agenda:
        i = agenda.pop(0)
        sentence = KB.sentences[i]
        head = sentence.head
        if head == ask:
            answer = "YES: "
            inferred_str += head
            return answer + inferred_str
        if not inferred[i]:
            inferred[i] = True
            inferred_str += head + ', '
            for j, sub_sentence in enumerate(KB.sentences):
                if head in sub_sentence.conjuncts:
                    count[j] -= 1
                    if count[j] == 0:
                        agenda.append(j)

    return answer + inferred_str
