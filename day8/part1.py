def countDigitsWithUniqueSegments(outputs):
    unique_amounts = {2, 3, 4, 7}
    return len([i for i in outputs if len(i) in unique_amounts])


def parseOutputValues(filename):
    outputs = []

    with open(filename) as f:
        for line in f:
            output = line.split("|")[1].split()
            outputs.extend(output)

    return outputs


def main():
    outputs = parseOutputValues("input.txt")
    digits_with_unique = countDigitsWithUniqueSegments(outputs)
    print(digits_with_unique)


if __name__ == "__main__":
    main()
