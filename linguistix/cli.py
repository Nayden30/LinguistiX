import argparse

from .io.corpus import read_corpus
from .analysis.tokenization import tokenize
from .analysis.frequency import word_frequencies


def main(argv=None):
    parser = argparse.ArgumentParser(description="LinguistiX corpus tool")
    parser.add_argument("files", nargs="+", help="Text files to analyze")
    parser.add_argument("-n", type=int, default=10, help="Number of top items to display")
    args = parser.parse_args(argv)

    text = read_corpus(args.files)
    tokens = tokenize(text)
    freq = word_frequencies(tokens)

    for word, count in freq.most_common(args.n):
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
