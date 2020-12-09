import os


how_many_results = 100
combinations = 736
completness_all = 0
path = os.path.dirname(os.path.abspath(__file__)) + '/results/'
functions = ['Rastrigin', 'Michalewicz', 'BukinF6', 'Easom', 'Wolfe']

for func in functions:
    completed = 0
    in_progress = 0
    completness = 0
    if os.path.isdir(path + func):
        for i in range(1, combinations + 1):
            if os.path.isfile(path + func + '/result_{}.csv'.format(i)):
                with open(path + func + '/result_{}.csv'.format(i), 'r') as f:
                    lines = len(f.readlines())
                    if lines > how_many_results:
                        completed += 1
                        completness += 1
                    else:
                        in_progress += 1
                        if lines > 0:
                            completness += (lines - 1) / 100
    completness_all += completness
    print('# {} function progress'.format(func))
    print('## Completed: {} In progress: {} Total: {} Completness: {:02.4f}%'.format(completed,
                                                                                     in_progress,
                                                                                     combinations,
                                                                                     completness/combinations * 100))
print("")
print("# Summary completness: {:02.4f}%".format(completness_all/len(functions)/combinations * 100))
