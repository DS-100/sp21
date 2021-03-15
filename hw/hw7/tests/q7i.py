test = {   'name': 'q7i',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> train.shape == (135144, 72) # train should contain 80% of the data\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> test.shape == (33787, 72) # test should contain 20% of the data\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.isclose(sum(train['Log Sale Price']), 1644821.2169556788, atol=0.1) # If this doesn't match, you might have still answered the question, but "
                                               'please adjust your code so that your split matches ours by following the implementation instructions about using shuffled_indices to split the data.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(sum(test['Log Sale Price']), 410769.5181548676, atol=0.1) # If this doesn't match, you might have still answered the question, but "
                                               'please adjust your code so that your split matches ours by following the implementation instructions about using shuffled_indices to split the data.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
