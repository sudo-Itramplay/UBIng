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
    ts2 = np.zeros([n_motiv,n_bands,T,N])
    for i_motiv in range(n_motiv):
        for i_trial in range(n_trials):
            # swap axes for time and channels
            ts[i_motiv,i_trial,:,:] = ts_tmp[:,:,i_trial,i_motiv].T
    
    del ts_tmp # clean memory
        
    
    #%% loop over the measures and frequency bands
    #fig = pp.figure(figsize=(10,3))
#    ax = fig.axes
#    axis = fig.add_subplot(131)
#    ax[1] = fig.add_subplot(132)
#    ax[2] = fig.add_subplot(133)

#    for i, ax in enumerate(fig.axes):
#        ax.set_ylabel(str(i))

    for i_band in range(n_bands):

        # figure def        
        nrow = 1
        ncol = 3
        fig, axs = pp.subplots(nrow, ncol,figsize=(10,3))    

        # select band
        freq_band = freq_bands[i_band]
        
        # band-pass filtering (alpha, beta, gamma)
        n_order = 3
        sampling_freq = 500. # sampling rate
        
        if freq_band=='alpha':
            low_f = 8./sampling_freq
            high_f = 12./sampling_freq
        elif freq_band=='beta':    
            # beta
            low_f = 15./sampling_freq
            high_f = 30./sampling_freq
        elif freq_band=='gamma':
            # gamma
            low_f = 40./sampling_freq
            high_f = 80./sampling_freq
        else:
            raise NameError('unknown filter')
        
        # apply filter ts[n_motiv,n_trials,T,N]
        b,a = spsg.iirfilter(n_order, [low_f,high_f], btype='bandpass', ftype='butter')
        filtered_ts = spsg.filtfilt(b, a, ts, axis=2)
        
        for i_motiv in range(n_motiv):
            
            # plot signal separated by frequency band
            ts2[i_motiv,i_band,:,:] = filtered_ts.mean(axis=1)[i_motiv,:,:]
            
            pos=axs[i_motiv].imshow(ts2[i_motiv,i_band,:,:].T, aspect=10, vmin=-.5, vmax=.5, cmap=cmapcolours[i_band])
            axs[i_motiv].set_xlabel('Time, ms')
            axs[i_motiv].set_ylabel('#EEG Channel')
            axs[i_motiv].set_title('Freq: '+str(i_band)+' Motiv: '+str(i_motiv))
            fig.colorbar(pos,ax=axs[i_motiv],fraction=0.02, pad=0.05)
        
    #  fig.colorbar(pos, ax=ax)
        fig.show()
    
        fig.savefig('dataEEG-band-'+str(i_band)+'-sub-'+str(i_sub)+'.png', format='png')
    