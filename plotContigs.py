#!/usr/bin/env python
###############################################################################
#
# plotContigs.py - Make a kms vs coverage plot for my contigs
#
###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

__author__ = "Michael Imelfort"
__copyright__ = "Copyright 2012"
__credits__ = ["Michael Imelfort"]
__license__ = "GPL3"
__version__ = "0.0.1"
__maintainer__ = "Michael Imelfort"
__email__ = "mike@mikeimelfort.com"
__status__ = "Development"

###############################################################################

import argparse
import sys

#import os
#import errno

#import numpy as np
#np.seterr(all='raise')     

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from pylab import plot,subplot,axis,stem,show,figure


###############################################################################
###############################################################################
###############################################################################
###############################################################################

  # classes here

###############################################################################
###############################################################################
###############################################################################
###############################################################################

def parseFile(filename):
    """parse a csv file and returna an array"""
    return_array = []
    # parse a file    
    try:
        with open(filename, "r") as fh:
            for line in fh:
                value = float(line.rstrip().split("\t")[-1])
                return_array.append(value)
        
    except: 
        print "Error opening file:", filename, exc_info()[0]
        raise    
    return return_array

def doWork( args ):
    """ Main wrapper"""
    coverages = parseFile(args.coverage)
    kms = parseFile(args.kms)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(coverages,
            kms,
            '*g')

    ax.plot(kms,
            coverages,
            '*r')
    
    plt.savefig('fred.png',dpi=300,format='png')

    plt.close(fig)
    del fig

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(coverages, 
               coverages,
               kms,
               #edgecolors='none',
               #c=colors,
               s=2,
               marker='.'
               )
    plt.show()
    plt.close(fig)
    del fig


    """
    fig = plt.figure()

    #-----
    # make a 3d plot
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], 
               points[:,1],
               points[:,2],
               #edgecolors='none',
               #c=colors,
               #s=2,
               #marker='.'
               )
    
    #-----
    # make a 2d plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(points[:,0],
            points[:,1],
            '*g')

    #-----
    # show figure
    plt.show()  
    # or save figure
    plt.savefig(filename,dpi=300,format='png')
    
    #-----
    # clean up!
    plt.close(fig)
    del fig
    """

###############################################################################
###############################################################################
###############################################################################
###############################################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('coverage', help="csv of coverages")
    parser.add_argument('kms', help="csv of kmer sigs")
    #parser.add_argument('positional_arg', help="Required")
    #parser.add_argument('positional_arg2', type=int, help="Integer argument")
    #parser.add_argument('positional_arg3', nargs='+', help="Multiple values")
    #parser.add_argument('-X', '--optional_X', action="store_true", default=False, help="flag")
    
    # parse the arguments
    args = parser.parse_args()        

    # do what we came here to do
    doWork(args)

###############################################################################
###############################################################################
###############################################################################
###############################################################################