from translator import Translator

def main():

    t = Translator()
    # t.translate(1000000)
    first = 0
    second= 1
    t.get_segment(which_segment=first, number=123456)
    x = t.get_segment(which_segment=0, number=20000000)
    t.translate_segment(x)


if __name__ == "__main__":
    main()
