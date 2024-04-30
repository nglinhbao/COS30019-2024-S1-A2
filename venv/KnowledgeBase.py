class KnowledgeBase:
    def __init__(self):
        self.clauses = []
        self.query = None

    def parse_file(self, filename):
        with open(filename, 'r') as file:
            mode = None
            for line in file:
                line = line.strip()
                if line == "TELL":
                    mode = "TELL"
                elif line == "ASK":
                    mode = "ASK"
                else:
                    if mode == "TELL":
                        clauses = line.split(";")
                        for clause_str in clauses:
                            if "=>" in clause_str:
                                premise, conclusion = clause_str.split("=>")
                                premise_symbols = premise.strip().split("&")
                                clause = {"PREMISE": premise_symbols, "CONCLUSION": conclusion.strip()}
                                self.clauses.append(clause)
                            else:
                                conclusion = clause_str.strip()
                                if conclusion != '':
                                    clause = {"PREMISE": [], "CONCLUSION": conclusion}
                                    self.clauses.append(clause)

                    elif mode == "ASK":
                        clause = {"PREMISE": [], "CONCLUSION": conclusion}
                        self.query = line.strip()
