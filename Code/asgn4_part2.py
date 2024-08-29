import networkx as nx
import matplotlib.pyplot as plt
import random

# A convenient function to create an undirected scale free graph.
def undirected_scale_free_graph(n):
    """
    Create an undirected scale free networkx graph.
    :param n: Number of nodes
    :return: A networkx graph
    """
    H = nx.scale_free_graph(n)
    G = nx.Graph()
    for (u, v) in H.edges():
        G.add_edge(u, v)
    del H
    return G

def set_parameters(G, beta, gamma):
    """

    :param G: A networkx graph
    :param beta: Probability of transitioning from S -> I
    :param gamma: Probability of transitioning from I -> R
    :return: None
    """

    # Give the graph properties 'gamma' and 'beta' here
    # Set a graph property by using
    #    graphName.graph['propertyName'] = someValue
    # TODO: Task 1
    pass

def set_initial_states(G, perc_inf=0.1):
    """
    Choose perc_inf * number_of_nodes nodes to be initial spreaders
    Set the initial states of all nodes
    :param G: A networkx graph
    :param perc_inf: The percentage of the network to infect initially
    :return: None
    """
    # TODO: Task 2
    pass

# Returns the number of nodes in state S
def get_num_s(G):
    return len([G.nodes[i]['state'] for i in range(G.number_of_nodes()) if
                G.nodes[i]['state'] == 'S'])

# Returns the number of nodes in state I
def get_num_i(G):
    return len([G.nodes[i]['state'] for i in range(G.number_of_nodes()) if
                G.nodes[i]['state'] == 'I'])

# Returns the number of nodes in state R
def get_num_r(G):
    return len([G.nodes[i]['state'] for i in range(G.number_of_nodes()) if
                G.nodes[i]['state'] == 'R'])

def set_resistance(G, nodelist=[]):
    """
    Sets the resistance value of each node in nodelist to True, and all others to False.
    :param G: A networkx graph
    :param nodelist: A list of nodes to give resistance to
    :return: None
    """
    # TODO: Task 5
    pass

def get_influential_nodes(G):
    """
    A function to determine the 10 most 'influential' nodes in the network
    The number of nodes can be changed for the last task
    :param G: A networkx graph
    :return: A list of nodes
    """
    # TODO: Task 6
    pass

def update(G):
    """
    Update the conditions (S/I/R) of all nodes
    :param G: A networkx graph
    :return: None
    """
    # TODO: Task 3
    # TODO: Task 7
    pass

def run_sim(G, numsteps=250):
    """
    Run a simulation for numsteps steps, then plot the SIR curves
    :param G: A networkx graph
    :param numsteps: The number of steps to run the simulation for
    :return: None
    """
    num_s = []
    num_i = []
    num_r = []

    for i in range(numsteps):
        update(G)
        num_s.append(get_num_s(G))
        num_i.append(get_num_i(G))
        num_r.append(get_num_r(G))

    x = list(range(numsteps))
    plt.plot(x, num_s, label='Susceptible')
    plt.plot(x, num_i, label='Infected')
    plt.plot(x, num_r, label='Recovered')
    plt.legend()
    plt.show()

def main():
    # Create your graph called G
    # Set your parameters to their desired values
    # Set your nodes' initial states
    # Run the simulation
    # TODO: Task 4

if __name__ == '__main__':
    main()
