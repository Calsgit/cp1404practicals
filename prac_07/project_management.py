"""
Time Estimate: 40 min
Time Elapsed:
"""
import datetime

from project import Project

DEFAULT_FILE = "projects.txt"
MENU_OPTIONS = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(True)
    print(MENU_OPTIONS)
    selection = input(">>> ").lower()
    while selection != 'q':
        if selection == 's':
            save_projects(projects)


def load_projects(is_on_startup=False):
    """Load projects from a specified file (or the default file on startup)"""
    projects = []
    file_name = DEFAULT_FILE if is_on_startup else input("")
    with open(file_name, 'r') as in_file:
        in_file.readline()  # read header
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(
                Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(), int(parts[2]),
                        float(parts[3]), int(parts[4])))
    return projects


def save_projects(projects, preferred_file=""):
    if preferred_file == "":
        preferred_file = input(f"Would you like to save to {DEFAULT_FILE}? ").lower()
    if preferred_file == "y" or "yes":
        pass  # TODO: saving


def display_projects(projects):
    pass  # TODO: display


def filter_projects(projects):
    pass  # TODO: filter by after input date


def add_project():
    pass  # TODO: add new project


def update_project(project):
    pass  # TODO: update selected project


if __name__ == '__main__':
    main()
