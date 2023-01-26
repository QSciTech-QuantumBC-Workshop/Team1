import argparse
import os
import shutil

from git import Repo
from pathlib import Path

CWD = Path(os.getcwd())
EXP_NAME = 'ex6'
EXP_DIR = CWD / EXP_NAME
FILENAME = 'teleportation.py'
LINE_WIDTH = 80


def print_instructions():
    inst = ['#' * LINE_WIDTH,
            '# 1.  You will use the repository that you created in exercise 5. With the',
            '#     terminal, clone this repository in the current folder.',
            '# 2.  cd into folder containing the code that you just cloned and look at the',
            '#     the status, the history and the branches of the repo.',
            '# 3.  Create a branch named `dev` and checkout the `dev` branch.',
            '# 4.  Open the file `teleportation.py` with a text editor and remove the line',
            '#     marked for deletion. Save your modification.',
            '# 5.  Add the file to the staged files and create a new commit.',
            '# 6.  Push your local `dev` branch to a remote `dev` branch.',
            '#     Go back to your browser and check that the code is now hosted on GitHub.',
            '# 7.  In GitHub, switch to the `dev` branch and create a pull request in order',
            '#     to merge your commit into the `main` branch.',
            '# 8.  Merge your own pull request (in principle it is the role of your',
            '#     colleagues!).',
            '# 9.  Go back to your terminal, checkout the `main` branch and pull the changes.',
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


def parse_args():
    parser = argparse.ArgumentParser(description='Git exercise.')
    parser.add_argument('--inst', action='store_true', help='Print the instructions for this exercise.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print_instructions()


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
