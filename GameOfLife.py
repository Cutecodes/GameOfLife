import sys
import getopt
import GUI

def main(argv):
    filename = ''
    try:
        opts, args = getopt.getopt(argv,"hf:",["filename="])
    except getopt.GetoptError:
        print('python GameOfLife.py -f <filename>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python GameOfLife.py -f <filename>')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
    GUI.GUI(filename)


if __name__ == '__main__':
	main(sys.argv[1:])
