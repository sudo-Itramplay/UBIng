#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:34:37 2018


"""

import os
import numpy as np
import scipy.signal as spsg
import scipy.stats as stt
import scipy.io as sio
import sklearn.linear_model as skllm
import sklearn.neighbors as sklnn
import sklearn.preprocessing as skprp
import sklearn.pipeline as skppl
import sklearn.feature_selection as skfs
import sklearn.model_selection as skms
import sklearn.metrics as skm
import matplotlib.pyplot as pp
import networkx as nx

#%% general info

subjects = [25] 
#range(25,30)

for i_sub in (subjects):

    res_dir = 'sub'+str(i_sub)+'/'
    if not os.path.exists(res_dir):
        print('create directory:',res_dir)
        os.makedirs(res_dir)
    
    # 
    cmapcolours = ['Blues','Greens','Oranges']
    listcolours = ['b','g','o']
    
    measure_labels = ['pow','cov','corr']
    n_measures = len(measure_labels)
    
    freq_bands = ['alpha','beta','gamma']
    n_bands = len(freq_bands)
    
    #%% load data
    
    n_motiv = 3
    ts_tmp = sio.loadmat('dataClean2-'+str(i_sub)+'-T1.mat')['dataSorted2'] 
    
    N = 60 # number of channels
    n_trials = 108 # number of trials per block
    T = 1200 # trial duration
    
        
    # save results       
    perf = np.load(res_dir+'perf.npy')
    perf_shuf = np.load(res_dir+'perf_shuf.npy')
    conf_matrix = np.load(res_dir+'conf_matrix.npy')
    rk_pow = np.load(res_dir+'rk_pow.npy')
    rk_FC = np.load(res_dir+'rk_FC.npy')
    pearson_corr_rk = np.load(res_dir+'pearson_corr_rk.npy')
    
    #%% plots
    fmt_grph = 'png'
    
    
    for i_band in range(n_bands):
        freq_band = freq_bands[i_band]
        for i_measure in range(n_measures):
            measure_label = measure_labels[i_measure]
    
            # the chance level is defined as the trivial classifier that predicts the label with more occurrences 
            chance_level = np.max(np.unique(labels, return_counts=True)[1]) / labels.size
        
            # plot performance and surrogate
            pp.figure(figsize=[4,3])
            pp.axes([0.2,0.2,0.7,0.7])
            pp.violinplot(perf[i_band,i_measure,:,0],positions=[-0.2],widths=[0.3])
            pp.violinplot(perf[i_band,i_measure,:,1],positions=[0.2],widths=[0.3])
            pp.violinplot(perf_shuf[i_band,i_measure,:,0],positions=[0.8],widths=[0.3])
            pp.violinplot(perf_shuf[i_band,i_measure,:,1],positions=[1.2],widths=[0.3])
            pp.plot([-1,2],[chance_level]*2,'--k')
            pp.axis(xmin=-0.6,xmax=1.6,ymin=0,ymax=1.05)
            pp.xticks([0,1],['Pearson Correlation','surrogate'],fontsize=8)
            pp.ylabel('accuracy_'+freq_band+'_'+measure_label,fontsize=8)
            pp.title(freq_band+', '+measure_label)
            pp.savefig(res_dir+'accuracy_'+freq_band+'_'+measure_label, format=fmt_grph)
            pp.close()
    
            # plot confusion matrix for MLR
            pp.figure(figsize=[4,3])
            pp.axes([0.2,0.2,0.7,0.7])
            pp.imshow(conf_matrix[i_band,i_measure,:,0,:,:].mean(0), vmin=0, cmap=cmapcolours[i_band])
            pp.colorbar()
            pp.xlabel('true label',fontsize=8)
            pp.ylabel('predicted label',fontsize=8)
            pp.title(freq_band+', '+measure_label)
            pp.savefig(res_dir+'conf_mat_MLR_'+freq_band+'_'+measure_label, format=fmt_grph)
            pp.close()
    
    
            # plot RFE support network
            pp.figure(figsize=[10,10])
            pp.axes([0.05,0.05,0.95,0.95])
            pp.axis('off')
            if i_measure == 0: # power
                list_best_feat = np.argsort(rk_pow[i_band,:,:].mean(0))[:10] # select 10 best features
                node_color_aff = []
                g = nx.Graph()
                for i in range(N):
                    g.add_node(i)
                    if i in list_best_feat:
                        node_color_aff += ['red']
                    else:
                        node_color_aff += ['orange']
                nx.draw_networkx_nodes(g,pos=pos_circ,node_color=node_color_aff)
                nx.draw_networkx_labels(g,pos=pos_circ,labels=ch_labels)
            else: # covariance or correlation
                list_best_feat = np.argsort(rk_FC[i_band,i_measure-1,:,:].mean(0))[:20] # select 20 best features
                g = nx.Graph()
                for i in range(N):
                    g.add_node(i)
                node_color_aff = ['orange']*N
                list_ROI_from_to = [] # list of input/output ROIs involved in connections of support network
                for ij in list_best_feat:
                    g.add_edge(col_ind[ij],row_ind[ij])
                nx.draw_networkx_nodes(g,pos=pos_circ,node_color=node_color_aff)
                nx.draw_networkx_labels(g,pos=pos_circ,labels=ch_labels)
                nx.draw_networkx_edges(g,pos=pos_circ,edges=g.edges(),edge_color=listcolours[i_band])
            pp.title(freq_band)
            pp.savefig(res_dir+'support_net_RFE_'+freq_band+'_'+measure_label, format=fmt_grph)
            pp.close()
    
        # plot stability of RFE rankings
        pp.figure(figsize=[4,3])
        pp.axes([0.2,0.2,0.7,0.7])
        pp.violinplot(pearson_corr_rk[i_band,:,:].T,positions=range(n_measures),widths=[0.4]*3)
        pp.axis(ymin=0,ymax=1)
        pp.xticks(range(n_measures),measure_labels,fontsize=8)
        pp.ylabel('Pearson between rankings',fontsize=8)
        pp.title(freq_band)
        pp.savefig(res_dir+'stab_RFE_rankings_'+freq_band, format=fmt_grph)
        pp.close()
            
    
            
            
