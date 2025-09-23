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

    res_dir = '.'
#    if not os.path.exists(res_dir):
#        print('create directory:',res_dir)
#        os.makedirs(res_dir)
    # 
    cmapcolours = ['Blues','Greens','Oranges']
    listcolours = ['b','g','o']
    
    measure_labels = ['pow','cov','corr']
    n_measures = len(measure_labels)
    
    freq_bands = ['alpha','beta','gamma']
    n_bands = len(freq_bands)
    
    #%% load data
    
    #    ts = sio.loadmat('./cleanData18092019/dataClean-25-T1.mat')['dataSorted']
    n_motiv = 3
    ts_tmp = sio.loadmat('dataClean2-'+str(i_sub)+'-T1.mat')['dataSorted2'] # [N,T,n_trials,motiv]   
    
    N = 60 # number of channels
    n_trials = 108 # number of trials per block
    T = 1200 # trial duration
    
    # discard silent channels
    invalid_ch = np.logical_or(np.abs(ts_tmp[:,:,0,0]).max(axis=1)==0, np.isnan(ts_tmp[:,0,0,0]))
    valid_ch = np.logical_not(invalid_ch)
    ts_tmp = ts_tmp[valid_ch,:,:,:]
    N = valid_ch.sum()
    
    # get time series for each block
    ts = np.zeros([n_motiv,n_trials,T,N])
    for i_motiv in range(n_motiv):
        for i_trial in range(n_trials):
            # swap axes for time and channels
            ts[i_motiv,i_trial,:,:] = ts_tmp[:,:,i_trial,i_motiv].T
    
    # for each motivation
    pp.figure(figsize=[4,3])
    
    aa = ts_tmp.shape
    sigM = np.zeros([aa[0],aa[1],aa[3]])
    for i in range(n_motiv):
        
        sigM[:,:,i] = ts_tmp[:,:,:,i].mean(axis=2)

    # plot confusion matrix for MLR

            
    #   fig, axs = pp.subplots(1, 3,figsize=(5,15))
    fig = pp.figure(figsize=(10,3))
    ax = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    
    pos=ax.imshow(sigM[:,:,0], aspect=10, vmin=-1, vmax=1, cmap=cmapcolours[0])
    ax.set_xlabel('Time, ms')
    ax.set_ylabel('#EEG Channel')
    ax.set_title('M-State 0')
    fig.colorbar(pos,ax=ax,fraction=0.02, pad=0.05)
    #  fig.colorbar(pos, ax=ax)
    
    pos2=ax2.imshow(sigM[:,:,1], aspect=10,vmin=-1, vmax=1, cmap=cmapcolours[0])        
    ax2.set_title('M-State 1')
    ax2.set_xlabel('Time, ms')
    fig.colorbar(pos2,ax=ax2,fraction=0.02, pad=0.05)
     # fig.colorbar(pos2, ax=ax2,)
    
    pos3=ax3.imshow(sigM[:,:,2], aspect=10,vmin=-1, vmax=1, cmap=cmapcolours[0])      
    ax3.set_title('M-State 2')
    ax3.set_xlabel('Time, ms')
    fig.colorbar(pos3,ax=ax3,fraction=0.02, pad=0.05)
    #fig.colorbar(pos3, ax=ax3)

    fig.show()
    
    fig.savefig('data'+str(i_sub)+'.png', format='png')
        
    