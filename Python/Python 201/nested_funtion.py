def func1(name):
    print(f"I am {name} from Function 1..")

    def func2():
        print(f"I am {name} from Function 2..")  # here func2 inherit the variable(name) from func1

    func2()

func1("Nischal")
