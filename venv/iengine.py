from KnowledgeBase import *
from algorithms.FC import *
from algorithms.BC import *
from algorithms.TT import *

def main():
    filename = 'tests/test_HornKB.txt'
    kb = KnowledgeBase()
    kb.parse_file(filename)
    print(TT_ENTAILS(kb, kb.query))

if __name__ == "__main__":
    main()