# COMP90042 Project Description

This assignment can be done individually or in teams of two or three or four(max). We strongly encourage healthy collaboration. See the [University of Melbourne Working in Groups Guide](https://students.unimelb.edu.au/academic-skills/resources/communicating-in-class/communicating-with-peers/working-in-groups). If your team member does not engage or collaborate, please contact the lecturer ([Dr. Caren Han](mailto:caren.han@unimelb.edu.au?subject=[COMP90042]%20Project%20Group)) with describing the contributions of each collaborator. We strongly recommend to start working early so that you will have ample time to discover stumbling blocks and ask questions.

In this assignment, you will work on proposing and implementing a model/framework for Named Entity Recognition (NER) from the defence corpus. The detailed information for the implementation and submission step are specified in the following sections. Note that lecture note and workshop exercises would be a good starting point and baseline for the assignment [especially, Lecture XX/Lab XX].
Note that we specified which lectures and labs are highly related!

You are free to design the architecture using any of the techniques learned from our lectures and labs. For training and evaluation, we provide you a benchmark dataset in split of training, validation and test. You will use the training and validation set for training/validation while using the test set for leaderboard submission. 

For this assignment, **instead of solely focusing on achieving higher performance, having the good architecture design & implementation with detailed step-by-step justification will be important to show you’ve fully reached our expectation in this assignment.**


**Table of Contents**
- [0. Important Dates (Very Important!!)](https://github.com/drcarenhan/COMP90042_2024#0important-dates)
- [1. DataSet](https://github.com/drcarenhan/COMP90042_2024#-1-dataset)
- [2. Important Notes](https://github.com/drcarenhan/COMP90042_2024#2)
- [3. Model Testing](https://github.com/drcarenhan/COMP90042_2024#3model-testing)
- [4. Documentation](https://github.com/drcarenhan/COMP90042_2024#4documentation)
- [Assignment Submission Method](https://github.com/drcarenhan/COMP90042_2024#assignment-submission-method)
- [FAQ](https://github.com/drcarenhan/COMP90042_2024#faq)

<br/>
<br/>


## <img src="https://em-content.zobj.net/thumbs/120/microsoft/319/calendar_1f4c5.png" width="30" />0.Important Dates
The Important date for the Project can be summarised as follows:
- **Project Specification Release Date**: 12 April 2024 
- **Project Group Release Date**: 12 April 2024 
- **Project Group Revision Due**: 16 April 2024 
- **Project Group Presentation**: Week 12 (at your workshop - 20 May - 24 May 2024) 
- **Project Leaderboard**: 16 April - 24 May 2024 
- **Project Final Submission Due**:  26 May 2024 


All deadlines are **11:59 PM (Melbourne Time- AEST)**.

**Project Group Release**
**YOU MUST CONTACT YOUR GROUP MEMBER BY THE GROUP REVISION DUE.** Please check the reason as follows.

**Project Group Revision Due**
If you want to change your group to individual, you can revise it by the Project Group Change Due. However, in this case, you MUST get your team member's agreement.
NOTE: If you do not respond your group member by the Group Revision Due, and your group member requests for working as an individual, you must work the Project individually (or without that team member).

**Leaderboard**
The leaderboard will be opened from 16 April to 24 May, 2024, 11:59PM, which is two days before the Project submission due.




<br/>

## <img src="https://em-content.zobj.net/thumbs/120/samsung/349/card-file-box_1f5c3-fe0f.png" width="30" /> 1. DataSet
| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1flkFWGcD1S84HONhTGodsEudyPZjsJ75?usp=sharing) |
|-----------------------------------------|


**Data And Input**
For this Project, you are to use PART OF the [re3d dataset](https://github.com/juand-r/entity-recognition-datasets/tree/master/data/re3d) from Defense Science and Technology Laboratory, U.K., which focuses on named entity extraction relevant to somebody operating in the role of a defence and security intelligent analyst. You are provided with three files (train, val, test)

**Data Download and Load**
Please go to the [Data page](https://www.kaggle.com/c/2021-comp5046-a2/data) in order to download and see more detailed information about the dataset.
Make sure that you load the dataset via google drive. (If you want to use Jupyter notebook, you can submit your dataset in the zip file)

**Data Preprocessing**
There is no restriction of pre-processing the dataset. You do not have to do data pre-processing if no need. 
NOTE: There is no deduction even if you do not apply any data pre-processing technique. However, please specify the reason in the report.


<br/>



## <img src="https://em-content.zobj.net/thumbs/120/whatsapp/326/desktop-computer_1f5a5-fe0f.png" width="30" />2.Important Note

| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template]() |
|-----------------------------------------|

**Project Rules**
You MUST follow the rules below. If not, your project submission will NOT be marked.
1) You can use the NER model with different types of sequence model, such as RNN, LSTM, Bi-LSTM, GRU, Bi-GRU, Transformer, even PLM or LLM, etc. However, you MUST NOT directly use the existing state-of-the-art (SOTA) architecture as it is but need to modify it and propose your own model. For example, you MUST NOT directly use the SOTA model (i.e. BERT) without any modification.

2) You can use any pretrained model or large langauge model from any sources but MUST NOT fine-tune it

3) The model described in the report MUST NOT be different from the submitted code and running log in the submitted ipynb file.

4) You can use packages or code from the Workshops. If you use/refer any other package or code, please put the reference at the bottom of the code. Otherwise, it will be considered as plagiarism.

5) You MUST NOT submit the prediction result (to the kaggle leaderboard) that is not produced from your code

6) Your code MUST NOT use any rule(or condition)-based techniques in the model.

7) You MUST NOT use any testing data when you train your NER model. You are allowed to use only training and validation set that are provided

8) You MUST use the given code template.

9) You MUST use only given training, validate, test dataset for training and testing.

**Useful Notes
**1) Please refer to lecture notes, workshop materials, and resources that are covered.

2) Please proceed your own way if we do not specify it in the assignment specification.

<br/>


## <img src="https://em-content.zobj.net/source/skype/289/test-tube_1f9ea.png" width="30" />3.Testing and Evaluation
| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1flkFWGcD1S84HONhTGodsEudyPZjsJ75?usp=sharing) |
|-----------------------------------------|

You need to justify your decision and explain the pattern by testing the performance of your implementation. The testing result should include precision, recall and F-value -refer to [Lab4(Exercise)](https://colab.research.google.com/drive/1WvRFQX_j-cg3prcGZb7zC_85c2wG64Uc?usp=sharing).

You need to write a manual (readme) for the assessor. Your manual should guide how to test your program and also includes a list of packages (with version) that you used. If you work on Google Colab or Jupyter Notebook (.ipynb), your manual should guide the assessor on where to upload the required files (trained model, dataset, etc.). Note the assessor will use Google Colab to open your ipynb file. Unless you have a function that downloads required files from URL or Google Drive. 

The following model testings should be conducted. For each testing, you MUST include and visualise the table/graph in the ipynb file (your code) and your documentation (section 4). Note that you MUST make the final model and conduct the ablation studies with that final model as follows:
- **Input Embedding Ablation Study[3 marks]: (Explain the performance)** <br/> Test at least three types of input embedding variants (e.g. word2vec only, word2vec+POS tag embedding, word2vec+all 3 features embeddings) for your model, and visualise a table/graph with the peformance (exact value of precision, recall, and f1) of all 3 variants. 
- **Attention Ablation Study[3 marks]: (Explain the performance)** <br/> Test at least three types of attention variants (attention calculation variants or attention alignment variants) for your model, and visualise a table/graph with the peformance (exact value of precision, recall, and f1) of all 3 variants. e.g. try three different attention calculations, including dot-product, scaled dot-product, and cosine attention caluation.
- **Hyper Parameter Testing[3 marks]: (Explain the performance)** <br/> Test at least different 5 hyperparameter variants (5 different epoch values or 5 learning rates) for your model, and visualise a table/graph with the performance (exact value of precision, recall, and f1) of all 5 variants.


<br/>


## <img src="https://em-content.zobj.net/thumbs/120/facebook/355/page-facing-up_1f4c4.png" width="30" />4.Documentation [7 marks]
| :exclamation:  Please use the provided documentation template ([overleaf](https://www.overleaf.com/read/wpjzvgkcjkwp) or [word](https://github.com/drcarenhan/COMP90042_2024/blob/main/assign_report.docx))|
|-----------------------------------------|

You should submit pdf version of the assignment report (8 pages Maximum - excluding reference and appendix). The detailed documentation requirement for each section can be found above section 1. Dataset **(2 marks)**, 2. QA Model Implementation **(2 marks)**, and 3. Model Testing **(3 marks)**. **Please check the requirement items with the tag of (Justify your decision) or (Explain the performance). You MUST write those items to the report.**



**The justification MUST be based on the previous literature reference (incl. international conference or journal publication) or empirical evaluation. (Check the definition of 'empirical evaluation' at the following FAQ Section). **

**Note that We DO NOT MARK the Documentation if it is not implemented as described in the report.**



<br/>


## <img src="https://em-content.zobj.net/thumbs/120/whatsapp/326/envelope-with-arrow_1f4e9.png" width="30" />Assignment Submission Method
**Due Date:** 11:59 PM, Saturday 20 May 2023

**Submission:** LMS Assignment Submission Box (The submission box will be opened on 1 May 2023)

**You Must Submit Three Files:**
- pdf file: a report (documentation) with the given template ([overleaf](https://www.overleaf.com/read/wpjzvgkcjkwp) or [word](https://github.com/drcarenhan/COMP90042_2024/blob/main/assign_report.docx))
(file name: COMP90042_your_groupid.pdf)
- ipynb file or python packages (.py files): An ipynb file or python package that includes all your implementation (the implementation is described in the following sections - dataset, qa model, model testing). You MUST use this [ipynb template](https://colab.research.google.com/drive/1flkFWGcD1S84HONhTGodsEudyPZjsJ75?usp=sharing)
(file name: COMP90042_your_groupid.ipynb)
- zip file: A zip file that contains trained models, dataset, readme - if necessary, and all other required files that you used for your program.
(file name: COMP90042_your_groupid.zip)

<br/>

## <img src="https://em-content.zobj.net/thumbs/120/google/350/person-raising-hand_1f64b.png" width="30" />FAQ
**Question: My Model performs really bad (Low F1). What did I do wrong?**<br/>
Answer: Please don't worry about the low performance as our training dataset is very small and your model is very basic deep learning model. Of course, there is something wrong with your code if it comes out below 10% (0.1).

**Question: How can we make POS Tag or NER Tag to the embedding?**<br/>
Answer: You can either use it as a categorial embedding (e.g. putting the POS tag index- like Noun-->0, Verb -->1, etc) or applied word embeding (e.g. Extracting the Pretrained Word2Vec embedding for the term 'Noun' or 'Verb'). If you have any other approach to apply, please proceed! (Note you need to have a justification - why you apply it by using theoretial justification or empirical evaluation) 

**Question: Do I need to save the word embedding model or Recurrent models?**<br/>
Answer: We highly recommend you to save your best word embedding model, and load it when you use it in your code. Otherwise, it is sometimes removed and overwrite all your code so that you need to re-run the whole code again.

**Question: Is there any other marking scheme/marking criteria available for the assignment?**<br/>
Answer: The assignment specification is extremely detailed and the partial mark details are already given. The marking will be directly conducted based on the specification. It means you will get the full mark if you fulfill all the requirement that we mentioned in the specification.

**Question: What do I need to write in the justification or explanation? How much do I need to articulate?**<br/>
Answer: We recommend conducting empirical evaluation. Empirical evaluation refers to the appraisal of a theory by observation in experiments. The key to good empirical evaluation is the proper design and execution of the experiments so that the particular factors to be tested can be easily separated from other confounding factors. Hence, visualizing the comparison of different testing results is a good way to justify your decision. Explain the trends based on your understanding. You can find another way (other than comparing different models) as well - like citing the peer-reviewed publications. 

**Question: Can I use other Sequence Model(like Transformer)?**<br/>
Answer: Yes, you can but please make sure all requirements in other sections should be successfully followed. For example, make sure you have all required dataset settings, input embeddings and model testings.
