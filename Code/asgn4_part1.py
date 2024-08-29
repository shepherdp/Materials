import networkx as nx
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc
from bokeh.io import output_notebook, show
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend

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

# A function to run a typical SIR model.
def run_SIR():

    # Network topology
    g = nx.watts_strogatz_graph(1000, 4, 0.01)

    model = ep.SIRModel(g)

    config = mc.Configuration()
    # Beta is the probability of transitioning from S to I
    config.add_model_parameter('beta', .01)
    # Gamma is the probability of transitioning from I to R
    config.add_model_parameter('gamma', .01)
    config.add_model_parameter("fraction_infected", 0.05)
    model.set_initial_status(config)

    iterations = model.iteration_bunch(1000)
    trends = model.build_trends(iterations)

    viz = DiffusionTrend(model, trends)
    p = viz.plot(width=400, height=400)
    show(p)

# A function to run a typical SEIR model.
def run_SEIR():

    # Network topology
    g = nx.watts_strogatz_graph(1000, 4, 0.1)

    # Model selection
    model = ep.SEIRModel(g)

    # Model Configuration
    cfg = mc.Configuration()

    # Beta is the probability of transitioning from S to E
    cfg.add_model_parameter('beta', 0.01)
    # alpha is the probability of transitioning from E to I
    cfg.add_model_parameter('alpha', 0.01)
    # Gamma is the probability of transitioning from I to R
    cfg.add_model_parameter('gamma', 0.01)
    cfg.add_model_parameter("fraction_infected", 0.05)
    model.set_initial_status(cfg)

    # Simulation execution
    iterations = model.iteration_bunch(1000)
    trends = model.build_trends(iterations)

    viz = DiffusionTrend(model, trends)
    p = viz.plot(width=400, height=400)
    show(p)

# A function to run a typical SIS model.
def run_SIS():

    # Network topology
    g = nx.watts_strogatz_graph(1000, 4, 0.1)

    model = ep.SISModel(g)

    config = mc.Configuration()
    # Beta is the probability of transitioning from S to I
    config.add_model_parameter('beta', 0.01)
    # Lambda is the probability of transitioning from I to S
    config.add_model_parameter('lambda', 0.01)
    config.add_model_parameter("fraction_infected", 0.05)
    model.set_initial_status(config)

    iterations = model.iteration_bunch(1000)
    trends = model.build_trends(iterations)

    viz = DiffusionTrend(model, trends)
    p = viz.plot(width=400, height=400)
    show(p)

# A function to run a typical SEIS model.
def run_SEIS():

    # Network topology
    g = nx.watts_strogatz_graph(1000, 8, 0.1)

    model = ep.SEISModel(g)

    config = mc.Configuration()
    # Beta is the probability of transitioning from S to E
    config.add_model_parameter('beta', 0.02)
    # alpha is the probability of transitioning from E to I
    config.add_model_parameter('alpha', 0.01)
    # Gamma is the probability of transitioning from I to S
    config.add_model_parameter('lambda', 0.01)
    config.add_model_parameter("fraction_infected", 0.05)
    model.set_initial_status(config)

    iterations = model.iteration_bunch(1000)
    trends = model.build_trends(iterations)

    viz = DiffusionTrend(model, trends)
    p = viz.plot(width=400, height=400)
    show(p)

run_SIR()
# run_SEIR()
# run_SIS()
# run_SEIS()
