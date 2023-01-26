import git
import os
import sys


class Colors:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    BASE = '\033[0m'


def print_instruction(message):
    print(Colors.PURPLE + message + Colors.BASE)


def print_warning(message):
    print(Colors.YELLOW + "Oops, wrong command." +
          " Try again to " + message + "." + Colors.BASE)


def print_success_message():
    print(Colors.BLUE + "Good!" + Colors.BASE)


def read_input():
    cmd = input()
    os.system(cmd)
    if cmd in {'\x1a', "exit()"}:
        sys.exit("Process stopped")
    return " ".join(cmd.split())


def change_directory(folder, nb_inst):
    print_instruction(str(nb_inst) + ".Enter the command to cd into folder `" +
                      folder + "`. This folder contains one file.")

    cmd = read_input()
    while not (cmd in {"cd " + folder, "cd " + folder + "/"}):
        print_warning("cd into " + folder)
        cmd = read_input()

    _, folder = cmd.split(" ")
    os.chdir(folder)


def initialize_repo(nb_inst):
    print_instruction(str(nb_inst) + ".Initialize a git repository.")
    cmd = read_input()

    init_repo = False
    while not init_repo:
        try:
            a = git.Repo(os.getcwd()).git_dir
            init_repo = True
        except git.exc.InvalidGitRepositoryError:
            print_warning("initialize git repo")
            cmd = read_input()

    print_success_message()


def check_staged(cmd):
    cmd_array = cmd.split()
    staged = False
    if len(cmd_array) < 3:
        pass
    elif cmd in {"git add .", "git add teleportation.py"}:
        staged = True
    elif cmd_array[0] == "git" and cmd_array[1] == "add":
        try:
            i_file = cmd_array.index("teleportation.py")
            assert i_file > 1
            staged = True
        except (ValueError, AssertionError):
            staged = False

    return staged


def stage_file(nb_inst):
    print_instruction(str(nb_inst) + ". Add the file to the staged files.")
    cmd = read_input()
    staged = check_staged(cmd)

    while not staged:
        print_warning("stage the modified file")
        cmd = read_input()
        staged = check_staged(cmd)

    print_success_message()


def check_commits(repo, branch):
    try:
        return len(list(repo.iter_commits(branch)))
    except git.exc.GitCommandError:
        return 0


def commit_change(nb_inst):
    print_instruction(str(nb_inst) + ". Commit the file to the repository.")
    repo = git.Repo(os.getcwd())
    branch = repo.active_branch
    nb_commits = check_commits(repo, branch.name)

    read_input()
    commited = (nb_commits+1 == check_commits(repo, branch.name))

    while not commited:
        print_warning("commit the staged changes")
        read_input()
        commited = (nb_commits < check_commits(repo, branch.name))

    print_success_message()


def check_status(nb_inst):
    print_instruction(str(nb_inst) + ". Check the status of repository.")
    cmd = read_input()

    while cmd != "git status":
        print_warning("check the status")
        cmd = read_input()

    print_success_message()


def check_history(nb_inst):
    print_instruction(str(nb_inst) + ". Check the history of repository.")
    cmd = read_input()

    while cmd != "git log":
        print_warning("check the history (log)")
        cmd = read_input()

    print_success_message()


def check_diff(nb_inst):
    print_instruction(str(nb_inst) +
                      ". Check the difference with the HEAD version.")

    cmd = read_input()
    cmd_array = cmd.split()
    while cmd_array[0] != "git" or cmd_array[1] != "diff":
        print_warning("check the diff")
        cmd = read_input()
        cmd_array = cmd.split()

    print_success_message()


def create_branch(branch_name, nb_inst):
    print_instruction(str(nb_inst) + ". Create a branch named `" +
                      branch_name + "` without switching to it.")

    read_input()
    branches = git.Git().branch("--all").split()

    while not ("dev" in branches):
        print_warning("create a branch named dev.")
        read_input()
        branches = git.Git().branch("--all").split()

    print_success_message()


def list_branches(nb_inst):
    print_instruction(str(nb_inst) + ". List all branches.")

    cmd = read_input()
    cmd_array = cmd.split()
    while cmd_array[0] != "git" or cmd_array[1] != "branch":
        print_warning("list all branches")
        cmd = read_input()
        cmd_array = cmd.split()

    print_success_message()


def switch_branch(branch_name, nb_inst):
    print_instruction(str(nb_inst) + ". Switch to the " + branch_name + " branch.")
    repo = git.Repo(os.getcwd())

    read_input()
    branch = repo.active_branch

    while branch.name != branch_name:
        print_warning("switch branch")
        read_input()
        branch = repo.active_branch

    print_success_message()


def merge_branches(branch_dest, branch, nb_inst):
    print_instruction(str(nb_inst) + ". Merge branch " + branch +
                      " into branch " + branch_dest)
    cmd = read_input()
    cmd_array = cmd.split()
    while cmd_array[0] != "git" or cmd_array[1] != "merge":
        print_warning("merge branches")
        cmd = read_input()
        cmd_array = cmd.split()

    print_success_message()


def rebase_branch(branch_dest, branch, nb_inst):
    print_instruction(str(nb_inst) + ". Rebase branch " + branch +
                      " into branch " + branch_dest)
    cmd = read_input()
    cmd_array = cmd.split()
    while cmd_array[0] != "git" or cmd_array[1] != "rebase":
        print_warning("rebase branch " + branch +
                      " into branch " + branch_dest)
        cmd = read_input()
        cmd_array = cmd.split()

    print_success_message()


def exercise_1():
    # 1.  With the terminal, cd into folder `ex1`.
    # This folder contains one file.
    change_directory("ex1", 1)
    # 2.  Initialize a git repository.',
    initialize_repo(2)
    # 3.  Add the file to the staged files.',
    stage_file(3)
    # 4.  Commit the file to the repository.',
    commit_change(4)
    # 5.  Open the file with the text editor of your choice and remove the
    # line marked for deletion (9th line). Save your modification.
    print_instruction("5. Open the file with the text editor of your choice" +
                      " and remove the line marked for deletion (9th line)." +
                      " Save your modification then press ENTER here.")
    read_input()
    # 6.  Check the status of your repository and the difference with
    # the HEAD version
    check_status(6)
    check_diff(7)
    # 7.  Add the file to the staged files and create a new commit.
    stage_file(8)
    # 8.  Check your git commit history.',
    commit_change(9)


def exercise_2():
    # 0.  With the terminal, cd into folder `ex2`. This folder is a git repository.
    change_directory("ex2", 1)
    # 1.  Start by looking at the status and the history of the repo.
    check_status(2)
    check_history(3)
    # 2.  Create a branch named `dev`. List the branches in the repo.
    create_branch("dev", 4)
    list_branches(5)
    # 3.  Switch to branch `dev` and look at the commit history in this branch.
    switch_branch("dev", 6)
    check_history(7)
    # 4.  With a text editor of your choice, open the file `teleportation.py`
    #     and add the following line after the qiskit import:
    #         `import numpy as np`
    #     Save your modification.
    print_instruction("8. Open `teleportation.py` with the text editor of " +
                      "your choice and add the following line after the " +
                      "qiskit import : \n`import numpy as np`\n " +
                      " Save your modification then press ENTER here.")
    read_input()
    # 5.  Add the file to the staged files and create a new commit.
    stage_file(9)
    commit_change(10)
    # 6.  Switch to the branch `main`.
    switch_branch("main", 11)
    # 7.  Open the file `teleportation.py` and remove the line marked for deletion
    #     (notice that the `import numpy` is not present). Save your modification.
    print_instruction("12. Open `teleportation.py` with the text editor of " +
                      " your choice and remove the line marked for deletion" +
                      " (9th line). \nNotice that the `import numpy` is not" +
                      " present. \nSave your modification then press ENTER here.")
    read_input()
    # 8.  Add the file to the staged files and create a new commit.
    stage_file(13)
    commit_change(14)
    # 9.  Merge the branch `dev` into branch `main`.
    merge_branches("main", "dev", 15)
    # 10. Check your git commit history.
    check_history(16)


def exercise_3():
    # 1.  With the terminal, cd into folder `ex3`. This folder is a git repository.
    #     Start by looking at the status and the history of the repo.
    change_directory("ex3", 1)
    # 2.  Create a branch named `dev`. List the branches in this repo.
    create_branch("dev", 2)
    list_branches(3)
    # 3.  Open the file `teleportation.py` with a text editor and remove the line
    #     marked for deletion. Save your modification.
    print_instruction("4. Open the file with the text editor of your choice" +
                      " and remove the line marked for deletion (9th line)." +
                      " Save your modification then press ENTER here.")
    read_input()
    # 4.  Add the file to the staged files and create a new commit.
    stage_file(5)
    commit_change(6)
    # 5.  Switch to branch `dev` and look at the commit history in this branch.
    switch_branch("dev", 7)
    check_history(8)
    # 6.  Open the file `teleportation.py` and add the following line after
    #     the qiskit import:
    #         `import numpy as np`
    #     Save your modification.
    print_instruction("9. Open `teleportation.py` with the text editor of " +
                      "your choice and add the following line after the " +
                      "qiskit import : \n`import numpy as np`\n " +
                      " Save your modification then press ENTER here.")
    read_input()
    # 7.  Add the file to the staged files and create a new commit.
    stage_file(10)
    commit_change(11)
    # 6.  Switch to the branch `main`.
    switch_branch("main", 12)
    # 9.  Rebase the the branch `main` into the branch `dev`
    rebase_branch("dev", "main", 13)
    # 10. Check your git commit history and notice how it differs from the
    #     that you would have obtained by merging `dev` into `main`.
    check_history(14)
    print("Notice how it differs from the history" +
          " that you would have obtained by merging `dev` into `main`")


def exercise_4():
    # 1.  With the terminal, cd into folder `ex4`. This folder is a git repository.
    #     Notice that there is more than one branch. Start by looking at the status
    #     and the history of the different branches.
    change_directory("ex4", 1)
    list_branches(2)
    check_status(3)
    check_history(4)
    switch_branch("dev", 5)
    check_status(6)
    check_history(7)
    switch_branch("main", 8)
    # 2.  Checkout the `main` branch and merge the content of the `dev` branch.
    merge_branches("main", "dev", 9)
    print("Oops! Look at the status of your repo and handle the merge" +
          " conflict. At the end, you should have both imports in the" +
          " `teleportation.py` file")
    check_status(10)
    print("Handle the merge conflict. At the end, you should have both" +
          " imports in the `teleportation.py` file")
    stage_file(11)
    commit_change(12)
    check_history(13)
