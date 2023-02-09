"""
mapping.py - Map a Hamiltonian to a LinearCombinaisonPauliString

Copyright 2020-2021 Maxime Dion <maxime.dion@usherbrooke.ca>
This file has been modified by <Your,Name> during the
QSciTech-QuantumBC virtual workshop on gate-based quantum computing.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pauli_string import PauliString, LinearCombinaisonPauliString
import numpy as np


class Mapping:

    def fermionic_creation_annihilation_operators(self, n_qubits: int) -> tuple[list[LinearCombinaisonPauliString],
                                                                                list[LinearCombinaisonPauliString]]:
        raise NotImplementedError("abstract base class implementation")
        
    def fermionic_hamiltonian_to_qubit_hamiltonian(self, fermionic_hamiltonian)->LinearCombinaisonPauliString:
        """
        Do the mapping of a FermionicHamiltonian. First generates the LCPS representation of the creation/annihilation
        operators for the specific mapping. Uses the 'to_pauli_string_linear_combinaison' of the FermionicHamiltonian
        to generate the complete LCPS.

        Args:
            fermionic_hamiltonian (FermionicHamiltonian): A FermionicHamiltonian that provided a 
                'to_pauli_string_linear_combinaison' method.

        Returns:
            LinearCombinaisonPauliString: The LCPS representing the FermionicHamiltonian
        """

        creation_operators, annihilation_operators = self.fermionic_creation_annihilation_operators(fermionic_hamiltonian.number_of_orbitals())
        qubit_hamiltonian = fermionic_hamiltonian.to_linear_combinaison_pauli_string(creation_operators, annihilation_operators)
        return qubit_hamiltonian


class JordanWigner(Mapping):
    def __init__(self):
        """
        The Jordan-Wigner mapping
        """

        self.name = 'jordan-wigner'

    def fermionic_creation_annihilation_operators(self, n_qubits: int) -> tuple[list[LinearCombinaisonPauliString],
                                                                                list[LinearCombinaisonPauliString]]:
        """
        Build the LCPS reprensetations for the creation/annihilation operator for each qubit following 
        Jordan-Wigner mapping.

        Args:
            n_qubits (int): The number of orbitals to be mapped to the same number of qubits.

        Returns:
            list<LinearCombinaisonPauliString>, list<LinearCombinaisonPauliString>: Lists of the creation/annihilation
                operators for each orbital in the form of LinearCombinaisonPauliString.
        """

        creation_operators = list()
        annihilation_operators = list()
        
        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        # This is a large piece of the puzzle
        for i in range(n_qubits):
            x_bits = np.zeros((n_qubits), dtype=bool)
            x_bits[i] = True
            
            z_bits1 = np.zeros((n_qubits), dtype=bool)
            z_bits1[0:i] = np.ones((i), dtype=bool)
            z_bits1[i] = False
            z_bits2 = np.zeros((n_qubits), dtype=bool)
            z_bits2[0:i] = np.ones((i), dtype=bool)
            z_bits2[i] = True
            
            new_pauli_strings = np.array([PauliString(z_bits1,x_bits), PauliString(z_bits2,x_bits)])
            new_coefs = np.array([0.5, -0.5j], dtype=np.complex128)
            
            creation_operators.append(LinearCombinaisonPauliString(new_coefs,new_pauli_strings))
            annihilation_operators.append(LinearCombinaisonPauliString(np.conj(new_coefs),new_pauli_strings))
        
        
        ################################################################################################################

        #raise NotImplementedError()

        return creation_operators, annihilation_operators


class Parity(Mapping):
    def __init__(self):
        """
        The Parity mapping
        """

        self.name = 'parity'

    def fermionic_creation_annihilation_operators(self, n_qubits: int) -> tuple[list[LinearCombinaisonPauliString],
                                                                                list[LinearCombinaisonPauliString]]:
        """
        Build the LCPS reprensetations for the creation/annihilation operator for each qubit following 
        Parity mapping.

        Args:
            n_qubits (int): The number of orbtials to be mapped to the same number of qubits.

        Returns:
            list<LinearCombinaisonPauliString>, list<LinearCombinaisonPauliString>: Lists of the creation/annihilation
                operators for each orbital in the form of LinearCombinaisonPauliString
        """

        creation_operators = list()
        annihilation_operators = list()
        
        ################################################################################################################
        # YOUR CODE HERE
        # OPTIONAL
        ################################################################################################################

        raise NotImplementedError()

        return creation_operators, annihilation_operators
