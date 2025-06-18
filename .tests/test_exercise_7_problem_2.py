from points_decorator import points
import inspect
import pandas as pd
import os

class TestProblem2:
    @points(0.5, "Problem 2, Part 1: Variable ´data´ does not exist or has incorrect length!")
    def test_problem_2_part_1_len(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"
        variables = section_data[section]['variables']

        assert isinstance(variables['data'], pd.DataFrame)
        assert len(variables['data']) == 706

    @points(0.5, "Problem 2, Part 1: Did you set the date as index of the dataframe?")
    def test_problem_2_part_1_index(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"
        variables = section_data[section]['variables']

        assert isinstance(variables['data'].index, pd.DatetimeIndex)

    @points(1, "Problem 2, Part 2: The first value of the dataframe ``selection`` is not correct!")
    def test_problem_2_part_2_first(self, problem2):
        section_data, namespace = problem2
        section = "Part 2"
        variables = section_data[section]['variables']
        selection = variables['selection']
        # Check that the first value matches (assumes that TEMP_F column is at index 1 on axis 1)
        assert round(selection.iloc[0, 1]) == 27

    @points(1, "Problem 2, Part 2: The last value of the dataframe ``selection`` is not correct!")
    def test_problem_2_part_2_last(self, problem2):
        section_data, namespace = problem2
        section = "Part 2"
        variables = section_data[section]['variables']    
        selection = variables['selection']
        # Check that the last value matches (assumes that TEMP_F column is at index 1 on axis 1)
        assert round(selection.iloc[-1, -1]) == 1

    @points(1, "Problem 2, Part 3: Did you add a title to your plot?")
    def test_problem_2_part_3_title(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        variables = section_data[section]['variables']    

        # Check if the variable `title` exists in `variables`
        assert isinstance(variables['title'], str)

    @points(1, "Problem 2, Part 3: Did you add a x-label to your plot?")
    def test_problem_2_part_3_xlabel(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        variables = section_data[section]['variables']  

        # Check if the variable `x-label` exists in `variables`
        assert isinstance(variables['xlabel'], str)

    @points(1, "Problem 2, Part 3: Did you add a y-label to your plot?")
    def test_problem_2_part_3_ylabel(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        variables = section_data[section]['variables']  

        # Check if the variable `y-label` exists in `variables`
        assert isinstance(variables['ylabel'], str)

        
    @points(1, "Problem 2, Part 3: Did you export the plot using the variable `outputfp´ ?")
    def test_problem_2_part_3_path(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        variables = section_data[section]['variables']  

        # Check if the variable `y-label` exists in `variables`
        # Check if the path stored in the variable `outputfp` exists
        
        assert os.path.exists(variables['outputfp'])