import os
import data_handling
from anytree import Node, RenderTree
import labelling
import argparse

if __name__ == "__main__":
    # accept commandline arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--mv3d_file', help = 'Path to the mv3d file output from Avizo', required=True)
    parser.add_argument('--flow_file', help = 'The flow file containging the construction fo the centreline tree', required=True)
    parser.add_argument('--title', help = 'Title of the run (to appear in the output file', default=None)

    args = parser.parse_args()


    # Obtaining endpoints dictionary, take files as inputs preferrably
    path_to_mv3d = args.mv3d_file
    path_to_flow_file = args.flow_file
    run_name  = args.title

    
    coords = data_handling.construct_dict_from_mv3d(path_to_mv3d)
    endpoints = data_handling.get_endpoints_dictionary(coords)

    tree = data_handling.tree_from_flow_file(path_to_flow_file)

    labelled_tree = labelling.label_tree(tree, endpoints)

    if run_name is None:
        # following labelling convention of flow files
        temp = path_to_flow_file.split('/')[-1]
        temp = temp.split('.')[0]
        run_name = temp.split('_')[0]

    labelling.write_to_excel(labelled_tree, run_name)
