# CSC 486 Assignment 8

import networkx as nx
import matplotlib.pyplot as plt
from random import choice, random, shuffle


def get_binary_opinions(n):
    """
    Gets n random binary opinions
    :param n: number of opinions
    :return: a list containing randomly assigned elements of 0 and 1
    """
    ret = [0 for i in range(n // 2)] + [1 for i in range(n // 2, n)]
    shuffle(ret)
    return ret

def get_continuous_opinions(n):
    """
    Gets n random continuous opinions
    :param n: number of opinions
    :return: a list containing randomly assigned elements from [0, 1]
    """
    return [random() for i in range(n)]

class DiffusionModel:

    def __init__(self, g, method='voter'):
        """
        The diffusion model class
        :param g: a networkx graph
        :param method: a string representing the type of model to use
        """
        self.g = g
        self.method = method
        if self.method in ['voter', 'qvoter', 'majority', 'snazjd']:
            self.opinions = get_binary_opinions(self.g.number_of_nodes())
        else:
            self.opinions = get_continuous_opinions(self.g.number_of_nodes())

    def update(self):
        """
        Update the opinions of all agents.  This function should only call
        one of the methods defined below.
        :return: None
        """
        if self.method == 'voter':
            self.update_voter()

        # TODO: Task 7 Fill in the remaining cases here with elif statements

    def update_voter(self):
        """
        Update opinions based on the Voter model
        :return: None
        """
        node = choice(list(range(self.g.number_of_nodes())))
        nbr = choice(list(self.g.neighbors(node)))
        self.opinions[node] = self.opinions[nbr]

    def update_qvoter(self, q=3):
        """
        Update opinions based on the Q-Voter model
        :param q: the number of neighbors to base opinion update on
        :return: None
        """

        # TODO: Task 1
        pass

    def update_majority(self, q=5):
        """
        Update opinions based on the Majority Rule model
        :param q: the number of nodes to calculate the majority opinion of
        :return: None
        """

        # TODO: Task 2
        pass

    def update_snazjd(self):
        """
        Update opinions based on the Snazjd model
        :return: None
        """

        # TODO: Task 3
        pass

    def update_hk(self, epsilon=.3):
        """
        Update opinions based on the Hegelsmann-Krause model
        :param epsilon: maximum distance of a neighbor's opinion before it is ignored
        :return: None
        """

        # TODO: Task 4
        pass

    def update_dw(self, epsilon=.3, mu=.5):
        """
        Update opinions based on the Deffuant-Weisbuch model
        :param epsilon: maximum distance of a neighbor's opinion before it is ignored
        :param mu: a float telling how strongly to move towards a neighbor's opinion
        :return: None
        """

        # TODO: Task 5
        pass

    def update_mymodel(self):
        """
        Update opinions based on the *your name here* model
        :return: None
        """

        # TODO: Task 6
        pass

    def run_test_discrete(self):
        """
        Run a simulation using one of the binary opinion models and plot the results
        :return: None
        """
        if self.method not in ['voter', 'qvoter', 'majority', 'snazjd']:
            print(f'Call run_test_continuous when using model {self.method}')
            return

        x, y = [], [[], []]
        for i in range(100):
            x.append(i)
            y[0].append(self.opinions.count(1))
            y[1].append(self.opinions.count(0))
            self.update()
        plt.plot(x, y[0], label='Opinion=0')
        plt.plot(x, y[1], label='Opinion=1')
        plt.legend()
        plt.show()

    def run_test_continuous(self):
        """
        Run a simulation using one of the continuous opinion models and plot the results
        :return: None
        """
        if self.method not in ['hk', 'dw']:
            print(f'Call run_test_discrete when using model {self.method}')
            return

        x, ys = [], []
        for i in range(self.g.number_of_nodes()):
            ys.append([])

        for i in range(100):
            x.append(i)
            for j in range(self.g.number_of_nodes()):
                ys[j].append(self.opinions[j])

        for line in ys:
            plt.plot(x, line, alpha=0.5)
        plt.show()

    def run(self):
        """
        Driver function to run an experiment
        :return: None
        """
        if self.method in ['voter', 'qvoter', 'majority', 'snazjd']:
            self.run_test_discrete()
        else:
            self.run_test_continuous()


def main():
    g = nx.watts_strogatz_graph(100, 10, .1)
    method = 'voter'
    d = DiffusionModel(g, method=method)
    d.run()


if __name__ == '__main__':
    main()
