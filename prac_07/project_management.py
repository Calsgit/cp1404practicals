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
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    print(MENU_OPTIONS)
    selection = input(">>> ").lower()
    while selection != 'q':
        if selection == 's':
            save_projects(projects)
        else:
            print("Invalid selection.")
        print(MENU_OPTIONS)
        selection = input(">>> ").lower()
    selection = input(f"Would you like to save to {DEFAULT_FILE}? ").lower()
    if selection == "y" or selection == "yes":
        save_projects(projects, DEFAULT_FILE)


def load_projects(is_on_startup=False):
    """Load projects from a specified file (or the default file on startup)."""
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
    """Save projects to a specified file (or the default file if unspecified)."""
    if preferred_file == "":
        preferred_file = input("What file would you like to save to? (Must end with .txt)\n>").lower()
        while preferred_file[-4:] != ".txt":
            print("File must end with .txt!")
            preferred_file = input("What file would you like to save to? (Must end with .txt)\n>").lower()
    with open(preferred_file, 'w') as out_file:
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            end_of_file_string = "" if project == projects[-1] else "\n"
            save_string = f"{project.name}\t{project.start_date.day:02}/{project.start_date.month:02}/{project.start_date.year:04}\t{project.priority}\t{project.cost_estimate:.1f}\t{project.completion_percentage}{end_of_file_string}"
            out_file.write(save_string)


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
