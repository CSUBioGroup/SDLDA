# SDLDA
Predicting lncRNA–disease associations based on singular value decomposition and deep learning techniques

# Requirements

tensorflow==1.3.0

numpy==1.11.2

scikit-learn==0.18

scipy==0.18.1

# Usage

  In this GitHub project, we give a demo to show how SDLDA works. In data_processing folder, we give following datasets we used in our study.
  
  1. lda_interMatrix.mat is the raw lncRNA-disease interaction matrix with matlab format. Its shape is 577 lncRNAs x 272 diseases.
  
  2. matrix.npy is the lncRNA-disease interaction matrix with numpy format.
  
  3. data.pkl is used to store the sampled positive and negative samples.
  
  4. u_feature.npy is the U matrix of SVD technique used in our study, its shape is 577x64.
  
  5. v_feature.npy is the V matrix of SVD technique used in our study, its shape is 272x64.
  
  In our demo, we provide a leave-one-out cross validation to evaluate our model. You can use cross_validation.py to see experimental results and predict lncRNA related diseases. If you want to tune some hyper-parameters, you can change some values of hyper-parameters in hyperparams.py. 

  The other details can see the paper and the codes.
  

# Citation

# License
This project is licensed under the MIT License - see the LICENSE.txt file for details
