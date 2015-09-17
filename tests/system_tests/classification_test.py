import unittest
from pSBB.SBB.config import Config
from pSBB.SBB.sbb import SBB

TEST_CONFIG = {
    'task': 'classification',
    'classification_parameters': { # only used if 'task' is 'classification'
        'dataset': 'iris', # must have a .train and a .test file in the pSBB/datasets folder
    },
    'training_parameters': {
        'runs_total': 1,
        'generations_total': 30,
        'validate_after_each_generation': 30,
        'populations': {
            'teams': 20,
            'points': 40,
        },
        'replacement_rate': {
            'teams': 0.5,
            'points': 0.2,
        },
        'mutation': {
            'team': {
                'remove_program': 0.7,
                'add_program': 0.8,
                'mutate_program': 0.2,
            },
            'program': {
                'remove_instruction': 0.7,
                'add_instruction': 0.8,
                'change_instruction': 0.8,
                'swap_instructions': 0.8,
                'change_action': 0.1,
            },
        },
        'team_size': { # the min size is the total number of actions
            'min': 2,
            'max': 5,
        },
        'program_size': {
            'min': 2,
            'max': 20,
        },
    },

    'advanced_training_parameters': {
        'seed': 1, # default = None
        'use_pareto_for_point_population_selection': False, # if False, will select points using uniform probability
        'use_operations': ['+', '-', '*', '/', 'ln', 'exp', 'cos', 'if_lesser_than', 'if_equal_or_higher_than'],
        'extra_registers': 1,
        'diversity': {
            'use_and_show': [], # will be applied to fitness and show in the outputs
            'only_show': [], # will be only show in the outputs
            'k': 8,
        },
        'run_initialization_step2': False,
    },
}

class ClassificationTests(unittest.TestCase):
    def setUp(self):
        Config.RESTRICTIONS['write_output_files'] = False

    def test_classification_for_iris_without_pareto_and_without_diversity_maintenance_for_three_runs(self):
        """ Checking if everything for classification is still working and producing the same result. """
        config = dict(TEST_CONFIG)
        config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
        config['advanced_training_parameters']['diversity']['use_and_show'] = []
        config['advanced_training_parameters']['diversity']['only_show'] = []
        config['classification_parameters']['dataset'] = 'iris'
        config['training_parameters']['runs_total'] = 3
        config['advanced_training_parameters']['run_initialization_step2'] = False
        Config.USER = config
        sbb = SBB()
        sbb.run()
        result = len(sbb.best_scores_per_runs_)
        expected = 3
        self.assertEqual(expected, result)

    def test_classification_for_iris_without_pareto_and_without_diversity_maintenance(self):
        """ Checking if everything for classification is still working and producing the same result. """
        config = dict(TEST_CONFIG)
        config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
        config['advanced_training_parameters']['diversity']['use_and_show'] = []
        config['advanced_training_parameters']['diversity']['only_show'] = []
        config['classification_parameters']['dataset'] = 'iris'
        config['training_parameters']['runs_total'] = 1
        config['advanced_training_parameters']['run_initialization_step2'] = False
        Config.USER = config
        sbb = SBB()
        sbb.run()
        result = len(sbb.best_scores_per_runs_)
        expected = 1
        self.assertEqual(expected, result)

    def test_classification_for_iris_without_pareto_and_without_diversity_maintenance_with_step2(self):
        """ Checking if everything for classification is still working and producing the same result. """
        config = dict(TEST_CONFIG)
        config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
        config['advanced_training_parameters']['diversity']['use_and_show'] = []
        config['advanced_training_parameters']['diversity']['only_show'] = []
        config['classification_parameters']['dataset'] = 'iris'
        config['training_parameters']['runs_total'] = 1
        config['advanced_training_parameters']['run_initialization_step2'] = True
        Config.USER = config
        sbb = SBB()
        sbb.run()
        result = len(sbb.best_scores_per_runs_)
        expected = 1
        self.assertEqual(expected, result)

    def test_classification_for_iris_without_pareto_and_with_diversity_maintenance(self):
        """ Checking if everything for classification is still working and producing the same result. """
        config = dict(TEST_CONFIG)
        config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
        config['advanced_training_parameters']['diversity']['use_and_show'] = ['genotype', 'fitness_sharing']
        config['advanced_training_parameters']['diversity']['only_show'] = []
        config['classification_parameters']['dataset'] = 'iris'
        config['training_parameters']['runs_total'] = 1
        config['advanced_training_parameters']['run_initialization_step2'] = False
        Config.USER = config
        sbb = SBB()
        sbb.run()
        result = len(sbb.best_scores_per_runs_)
        expected = 1
        self.assertEqual(expected, result)

    def test_classification_for_iris_with_pareto_for_teams_without_pareto_for_points(self):
        """ Checking if everything for classification is still working and producing the same result. """
        config = dict(TEST_CONFIG)
        config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = True
        config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
        config['advanced_training_parameters']['diversity']['use_and_show'] = []
        config['advanced_training_parameters']['diversity']['only_show'] = []
        config['classification_parameters']['dataset'] = 'iris'
        config['training_parameters']['runs_total'] = 1
        config['advanced_training_parameters']['run_initialization_step2'] = False
        Config.USER = config
        sbb = SBB()
        sbb.run()
        result = len(sbb.best_scores_per_runs_)
        expected = 1
        self.assertEqual(expected, result)

    def test_classification_for_thyroid(self):
        """ Checking if everything for classification is still working and producing the same result. """
        config = dict(TEST_CONFIG)
        config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
        config['advanced_training_parameters']['diversity']['use_and_show'] = []
        config['advanced_training_parameters']['diversity']['only_show'] = []
        config['classification_parameters']['dataset'] = 'thyroid'
        config['training_parameters']['runs_total'] = 1
        config['advanced_training_parameters']['run_initialization_step2'] = False
        Config.USER = config
        sbb = SBB()
        sbb.run()
        result = len(sbb.best_scores_per_runs_)
        expected = 1
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()