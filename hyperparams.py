# -*- coding: utf-8 -*-
# /usr/bin/python2


class Hyperparams:
    '''Hyperparameters'''
    # data
    static_random_seed = 3
    tf_random_seed = 3
    neg_pos_ratio = 1
    train_val_ratio = 0.9
    batch_size = 32
    epoch_num = 200  # 200 # 5
    cv_fold_num = 5

    learning_rate = 0.001
    threshold = 0.5

    # model
    col_num = 272  # XL
    L_layer1_num = 48
    L_layer2_num = 32

    row_num = 577  # XR
    R_layer1_num = 48
    R_layer2_num = 32

    pca_dim = 64
    pca_maxiter = 200

    keep_prob = 0.95
    reg = 0.001
