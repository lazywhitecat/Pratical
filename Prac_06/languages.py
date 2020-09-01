from Prac_06.programming_language import ProgrammingLanguage
def main():


    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    programming_language = [ruby,python,visual_basic]
    print('The dynamically typed languages are:')
    for language in programming_language:
        if language.is_dynamic():
            print(language.field)
if __name__ == '__main__':
    main()