"""
Estimated time: 15 min
Elapsed time:
"""

from programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    programming_languages = [python, ruby, visual_basic]
    names_of_dynamic_languages = get_dynamic_languages(programming_languages)
    print("The dynamically typed languages are:")
    print('\n'.join(names_of_dynamic_languages))


def get_dynamic_languages(languages):
    return [language.name for language in languages if language.is_dynamic() == True]

main()