#!/usr/bin/env python3

'''
TODO: Description Needed

'''

def test_build_NEB():

    from software.build.neb import switch_indices, switch_all_indices, check_interpolation
    from software.analyse.bonds import compare_structures
    from software.examples.data.model_gen import get_example_adsorbate as co2

    initial = co2()
    final = co2()

    #check_interpolation('initial.traj','final.traj',10)
    #### Assertion tests ####
    assert(check_interpolation(initial, final, 10, verbose=False, save=False))
    ########

    atom_to_swap = 1
    other_atom_to_swap = 2

    #updated_final = switch_indices('final.traj', atom_to_swap, other_atom_to_swap):
    updated_final = switch_indices(final, atom_to_swap, other_atom_to_swap)

    #### Assertion tests ####
    assert(not check_interpolation(initial, updated_final, 10, verbose=False, save=False))
    ########

    #### Functionality to identify indices that would need swapping automatically
    indices_to_swap, distances = compare_structures(initial, updated_final)
    reupdated_final = switch_all_indices(updated_final, indices_to_swap)

    #### Assertion tests ####
    assert(check_interpolation(initial, reupdated_final, 10, verbose=True, save=False))

# Run the example
test_build_NEB()