from app import calculator

def main():
    result = calculator.Calculator(1, 3)
    return result.arithmetic()


if __name__ == '__main__':
    print(main())