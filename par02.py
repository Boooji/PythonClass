from gooey import Gooey, GooeyParser
existing_users = {}

@Gooey(program_name="Simple Calculator")
def main():
    parser = GooeyParser(description="A simple calculator that performs basic arithmetic operations.")
    
    parser.add_argument('First Name', help='Enter your first name')
    parser.add_argument('Last Name', help='Enter your last name')
    
    parser.add_argument('Number 1', type=int, help='Enter a two-digit number (10-99)', choices=range(10, 100))
    parser.add_argument('Number 2', type=int, help='Enter another two-digit number (10-99)', choices=range(10, 100))
    
    parser.add_argument('Operation', choices=['Add', 'Subtract', 'Multiply', 'Divide'], help='Choose an operation')

    args = parser.parse_args()

  
    full_name = f"{args.First_Name} {args.Last_Name}"

 
    if full_name not in existing_users:
        existing_users[full_name] = True
        print("Error: User does not exist. Please register first.")
        return

   
    result = None
    if args.Operation == 'Add':
        result = args.Number_1 + args.Number_2
    elif args.Operation == 'Subtract':
        result = args.Number_1 - args.Number_2
    elif args.Operation == 'Multiply':
        result = args.Number_1 * args.Number_2
    elif args.Operation == 'Divide':
        if args.Number_2 != 0:
            result = args.Number_1 / args.Number_2
        else:
            print("Error: Division by zero is not allowed.")
            return

    print(f"Result: {result}")

if __name__ == '__main__':
    main()
