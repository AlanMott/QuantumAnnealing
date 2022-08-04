# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler


def get_token():
    '''Returns personal access token. Only required if submitting to autograder.'''

    # TODO: Enter your token here
    # MyToken = "Z209-62c77afc35238c74df619f5c1bd78edf1c70a956"
    MyToken = "DEV-27c9da4043a245ca615dc8dadfcdbbb8b20379d2"
    return MyToken


# Set the solver we're going to use
def set_sampler():
    '''Returns a dimod sampler'''

    sampler = LeapHybridDQMSampler()

    return sampler


# Set employees and preferences
def employee_preferences():
    '''Returns a dictionary of employees with their preferences'''

    preferences = {"Anna": [1, 2, 3, 100],
                   "Bill": [3, 2, 1, 4],
                   "Chris": [4, 2, 3, 1],
                   "Diane": [4, 1, 2, 3],
                   "Erica": [1, 2, 3, 4],
                   "Frank": [3, 2, 1, 4],
                   "George": [4, 2, 3, 1],
                   "Harriet": [4, 1, 2, 3]}

    return preferences


# Create DQM object
def build_dqm():
    '''Builds the DQM for our problem'''

    preferences = employee_preferences()
    num_shifts = 4

    # Initialize the DQM object
    dqm = DiscreteQuadraticModel()

    # Build the DQM starting by adding variables
    for name in preferences:
        dqm.add_variable(num_shifts, label=name)

    # Use linear weights to assign employee preferences
    for name in preferences:
        dqm.set_linear(name, preferences[name])

    # TODO: Restrict Anna from working shift 4

    # TODO: Set some quadratic biases to reflect the restrictions in the README.
    # Constraint: Bill & Frank can't work together
    # Iterating through the number of shifts, set a large penalty bias (e.g. 100) for Bill and Frank on any shift i
    for i in range(num_shifts):
        dqm.set_quadratic_case("Bill", i, "Frank", i, 100)

    # Constraint: Erica & Harriet are BFFs
    # Iterating through the number of shifts, set a ver, very low penalty bias (e.g. -100) for Erica and Harriet on any shift i
    for i in range(num_shifts):
        dqm.set_quadratic_case("Erica", i, "Harriet", i, -100)

    """
    Constraint: Exactly two people per shift
    Anna=A, Bill=B, Chris=C etc.
    So, for shift 1, A1+B1+C1+D1+E1+F1+G1+H1=2. QBO it by subtracting and squaring to give (A1+B1+C1+D1+E1+F1+G1+H1 -2)^2
    We need to repeat for all shifts, so its a sigma summation that expands to;
    A1^2+B1^2+...H1^2+4-4A1-4B1-...4H1+2A1B1+2A1C1+...2G1H1
    Remember with binary, A1^2=A1, so this gives us;
    -3A1-3B1-..3H1+4+2A1B1+2A1C1+...2G1H1
    This gives us linear values of -3A1-3B1-...3H1
    quadratic is the sum from i=1 thru to i=n of the sum from j=i+1 thru j=n function 2*(firstworker+secondworker), or:
    sum(sum(2*firstworker+secondworker))
    Summations tend to suggest for loops in python
    We'll also need to make a list of the workers, so we can do that using the keys in the preferences dict, as the keys happen to be the workers names
    """
    workers = list(preferences.keys())
    for i in range(num_shifts):
        for j in range(len(workers)):
            dqm.set_linear_case(workers[j], i, dqm.get_linear_case(workers[j], i) - 3)
            for k in range(j + 1, len(workers)):
                dqm.set_quadratic_case(workers[j], i, workers[k], i,
                                       dqm.get_quadratic_case(workers[j], i, workers[k], i) + 2)

    return dqm


# Solve the problem
def solve_problem(dqm, sampler):
    '''Runs the provided dqm object on the designated sampler'''

    # Initialize the DQM solver
    sampler = set_sampler()

    # Solve the problem using the DQM solver
    sampleset = sampler.sample_dqm(dqm, label='Training - Employee Scheduling')

    return sampleset


# Process solution
def process_sampleset(sampleset):
    '''Processes the best solution found for displaying'''

    # Get the first solution
    sample = sampleset.first.sample

    shift_schedule = [[] for i in range(4)]

    # Interpret according to shifts
    for key, val in sample.items():
        shift_schedule[val].append(key)

    return shift_schedule


## ------- Main program -------
if __name__ == "__main__":

    # Problem information
    shifts = [1, 2, 3, 4]
    num_shifts = len(shifts)

    dqm = build_dqm()

    sampler = set_sampler()

    sampleset = solve_problem(dqm, sampler)

    shift_schedule = process_sampleset(sampleset)

    for i in range(num_shifts):
        print("Shift:", shifts[i], "\tEmployee(s): ", shift_schedule[i])
