from gooey import Gooey, GooeyParser
@Gooey 
def main():
    parser = GooeyParser(description="My first GUI")
    parser.add_argument("number1", type=int, help = 'Enter first Number: ' )
    parser.add_argument("number2", type=int, help = 'Enter second Number: ')
    parser.add_argument("number3", type=int, help = 'Enter third Number: ' )
    parser.add_argument("number4", type=int, help = 'Enter forth Number: ' )
    args = parser.parse_args()
    arge_number1 = args.number1 
    arge_number2 = args.number2 
    arge_number3 = args.number3
    arge_number4 = args.number4
    
    if arge_number1 % 2 == 0:
        print('even')
    else:
        print('odd')
    if arge_number2 % 2 == 0:
        print('even')
    else:
        print('odd')
    if arge_number3 % 2 == 0:
        print('even')
    else:
        print('odd')
    if arge_number4 % 2 == 0:
        print('even')
    else:
        print('odd')
    print(args)
main()
