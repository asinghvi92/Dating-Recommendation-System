### PROJECT: Dating/Friendship Recommender
    CS670: Information Storage and Retrieval
	Spring 2017
	Texas A&M University
	
### Name of all Team Members:
	Richa Surbhi
	Saket Ati
	Kelly Luk Bounsawat
	Akshit Singhvi

### Special Directions
Jupyter Notebook is located in code/report.ipynb
Within the notebook, we call our code from our report which allows a cleaner and faster run time. 
There are three seperate modules that can be run:

- run_training(num_samples): 
Training on our model takes a long time for sample sizes above 100. For this reason
we have a precomputed training output located in code/myClassifier.log. So you can skip the training part.
However, git is known to cause issue in reading files using cPickle.load() module in python. 
If this occurs, be sure to run the training in the report before running calculate_compatibility().

- calculate_compatibility(num_samples): Run the compatibility algorithm and writes the outputs to
compatibility.json and compatibility_ml.json.

- verify_compatibility(): Uses the above two files to calculate the precision. Also outputs 
compatibility_with_proxyLabel.txt and compatibility_with_proxyLabel_ML.txt. Refer to the report for more info.


Our parsed and cleaned dataset is located in dataset/users.csv.
Our training dataset is dataset/users_training.json.
Our evaluation dataset is dataset/users_evaluation.json.



### Reference:
Link to paper ‘RECON: a reciprocal recommender for online dating’:
http://www.cs.usyd.edu.au/~judy/Homec/Pubs/2010_RecSysUSYD.pdf

Link to dataset OKCupid: 
https://github.com/rudeboybert/JSE_OkCupid

Link to our repository:
https://github.tamu.edu/kelly-12azn/datingRecommender

Link to our youtube video:
https://www.youtube.com/watch?v=byOjiZ26LZQ&feature=youtu.be 
