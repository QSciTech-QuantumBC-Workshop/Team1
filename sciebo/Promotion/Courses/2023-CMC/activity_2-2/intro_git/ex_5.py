import argparse
import os
import shutil

from git import Repo
from pathlib import Path

CWD = Path(os.getcwd())
EXP_NAME = 'ex5'
EXP_DIR = CWD / EXP_NAME
FILENAME = 'teleportation.py'
LINE_WIDTH = 80


def print_instructions():
    inst = ['#' * LINE_WIDTH,
            '# 1.  With the terminal, cd into folder `ex5`. This folder is a git repository.',
            '#     Start by looking at the status, the history and the branches of the repo.',
            '# 2.  With your browser, create a new **PUBLIC** repository in the GitHub of the',
            '#     organization (https://github.com/QSciTech-QuantumBC-Workshop).',
            '# 3.  Copy the URL that points to your new repo. Use the https URL unless you',
            '#     know what you are doing! It should look like',
            '#         https://github.com/QSciTech-QuantumBC-Workshop/<your_repo>.git',
            '# 4.  Back into your terminal add a remote to your git repo. This remote should',
            '#     be named `origin` and point toward the URL that you copied at step 2.',
            '# 5.  Push your local `main` branch to a remote `main` branch hosted on GitHub.',
            '#     Go back to your browser and check that the code is now hosted on GitHub.',
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
    # Initialization
    repo = Repo.init(EXP_DIR)
    repo.git.add(EXP_DIR / FILENAME)
    repo.git.commit('-m', "Teleportation circuit")


def parse_args():
    parser = argparse.ArgumentParser(description='Git exercise.')
    parser.add_argument('--inst', action='store_true', help='Print the instructions for this exercise.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if not args.inst:
        setup_filesystem()
        setup_git_repo()
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
