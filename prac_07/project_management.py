"""
Time Estimate: 40 min
Time Elapsed:
"""
import datetime

from project import Project

DEFAULT_FILE = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(True)
    print(projects)


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


if __name__ == '__main__':
    main()
