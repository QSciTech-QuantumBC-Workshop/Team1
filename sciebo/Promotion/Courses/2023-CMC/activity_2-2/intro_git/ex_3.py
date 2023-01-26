import argparse
import os
import shutil

from git import Repo
from pathlib import Path
from interactive_utils import exercise_3

CWD = Path(os.getcwd())
EXP_NAME = 'ex3'
EXP_DIR = CWD / EXP_NAME
FILENAME = 'teleportation.py'
LINE_WIDTH = 80


def print_instructions():
    inst = ['#' * LINE_WIDTH,
            '# 1.  With the terminal, cd into folder `ex3`. This folder is a git repository.',
            '#     Start by looking at the status and the history of the repo.',
            '# 2.  Create a branch named `dev`. List the branches in this repo.',
            '# 3.  Open the file `teleportation.py` with a text editor and remove the line',
            '#     marked for deletion. Save your modification.',
            '# 4.  Add the file to the staged files and create a new commit.',
            '# 5.  Switch to branch `dev` and look at the commit history in this branch.',
            '# 6.  Open the file `teleportation.py` and add the following line after',
            '#     the qiskit import:',
            '#         `import numpy as np`',
            '#     Save your modification.',
            '# 7.  Add the file to the staged files and create a new commit.',
            '# 6.  Switch to the branch `main`.',
            '# 9.  Rebase the branch `main` onto the branch `dev`',
            '# 10. Check your git commit history and notice how it differs from the',
            '#     one that you would have obtained by merging `dev` into `main`.',
            '#' * LINE_WIDTH,
            '']

    print('\n'.join(inst))


def prompt_user():
    valid_answer = False
    while not valid_answer:
        answer = input(f'Folder {EXP_NAME} already exists. Do you want to overwrite (y/n)? ')
        a = answer.lower()
        if a in ['y', 'n']:
            return a


def setup_filesystem():
    if EXP_DIR.exists():
        answer = prompt_user()
        if answer == 'n':
            print('Leaving...')
            exit()
        else:
            shutil.rmtree(EXP_DIR)

    EXP_DIR.mkdir(exist_ok=True)
    with open(EXP_DIR / FILENAME, 'w') as f:
        f.write(teleportation)


def setup_git_repo():
    commit_msg = "Teleportation circuit"
    repo = Repo.init(EXP_DIR)
    repo.git.add(EXP_DIR / FILENAME)
    repo.git.commit('-m', commit_msg)


def parse_args():
    parser = argparse.ArgumentParser(description='Git exercise.')
    parser.add_argument('--inst', action='store_true', help='Print the instructions for this exercise.')
    parser.add_argument('--interactive', action='store_true', help='Run interactive helper for this exercise.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if not args.inst:
        setup_filesystem()
        setup_git_repo()

    if not args.interactive:
        print_instructions()
    else:
        exercise_3()


teleportation = \
"""from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


# How to use this protocole:
#   1. Prepare a quantum circuit with 3 qubits. Let's name this circuit "init_qc"
#   2. Place qubit 0 in "init_qc" in a quantum state of your choice
#   3. Combine your circuit with the `teleportation` circuit defined below
#   4. After execution, qubit 3 is now in the state of your choice!
# --> REMOVE THIS LINE!!!
qr = QuantumRegister(3, name="q")
crz, crx = ClassicalRegister(1, name="crz"), ClassicalRegister(1, name="crx")
crb = ClassicalRegister(1, name="crb")
teleportation = QuantumCircuit(qr, crz, crx, crb)

teleportation.h(1)
teleportation.cx(1, 2)
teleportation.cx(0, 1)
teleportation.h(0)

teleportation.measure(0, 0)
teleportation.measure(1, 1)

with teleportation.if_test((crx, 1)):
        teleportation.x(2)
with teleportation.if_test((crz, 1)):
    teleportation.z(2)
"""


if __name__ == '__main__':
    main()
