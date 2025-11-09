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
        if selection == 'l':
            projects = load_projects()
        elif selection == 's':
            save_projects(projects)
        elif selection == "d":
            display_projects(projects, 1)
        elif selection == "f":
            display_projects(projects)
            filter_projects(projects)
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
    if file_name == "":
        print(f"Defaulting to {DEFAULT_FILE}")
        file_name = DEFAULT_FILE
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


def display_projects(projects, order_selection=0):
    """Display specified projects. Ordering depends on selection:
    0 = Displays all projects with their index.
    1 = Separates incomplete and complete into different categories."""
    if order_selection == 1:
        incomplete_projects = [project for project in projects if not project.is_complete()]
        complete_projects = [project for project in projects if project.is_complete()]
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"\t{project}")
        print("Completed projects:")
        for project in complete_projects:
            print(f"\t{project}")
    else:
        for index, project in enumerate(projects):
            print(f"{index} {project}")


def filter_projects(projects):
    """Show only projects started on or after a specified date."""
    filter_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "),
                                             "%d/%m/%Y").date()
    for project in [project for project in projects if project.start_date >= filter_date]:
        print(project)


def add_project():
    pass  # TODO: add new project


def update_project(project):
    pass  # TODO: update selected project


def get_valid_index(projects, message):
    """Prompt user for a list index until a valid one is given."""
    index = int(input("Project choice: "))  # TODO: error checking on int
    while 0 <= index < len(projects):
        print("Invalid option!")
        index = int(input("Project choice: "))  # TODO: error checking on int
    return index


if __name__ == '__main__':
    main()
