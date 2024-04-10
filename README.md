# COMP90042 Project Description

This assignment can be done individually or in teams of two or three or four(max). We strongly encourage healthy collaboration. See the [University of Melbourne Working in Groups Guide](https://students.unimelb.edu.au/academic-skills/resources/communicating-in-class/communicating-with-peers/working-in-groups). 
If your team member does not collaborate, please contact the lecturer ([Dr. Caren Han](mailto:caren.han@unimelb.edu.au?subject=[COMP90042]%20Project%20Group)) with describing the contributions of each collaborator. We strongly recommend to start working early so that you will have ample time to discover stumbling blocks and ask questions.

You are free to design the architecture using any of the techniques learned from our lectures and labs. For training and evaluation, we provide you a benchmark dataset in split of training, validation and test. You will use the training and validation set for training/validation while using the test set for leaderboard submission. 

For this assignment, **instead of solely focusing on achieving higher performance, having the novel architecture design & implementation with detailed justification and empirical evaluation will be important to show you’ve fully reached our expectation in this assignment.**


**Table of Contents**
- [0. Important Dates (Very Important!!)](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#0important-dates)
- [1. DataSet](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-1-dataset)
- [2. Important Notes](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#2important-note)
- [3. Model Testing](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#3testing-and-evaluation)
- [4. Documentation](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#4documentation)
- [Project Submission Method and Grading](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#project-submission-method-and-grading)
- [Week12 Presentation and Peer Review](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#week-12-presentation-and-peer-review)
- [FAQ](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#faq)

<br/>
<br/>


## <img src="https://em-content.zobj.net/thumbs/120/microsoft/319/calendar_1f4c5.png" width="30" />0.Important Dates
The Important date for the Project can be summarised as follows:
- **Project Specification Release Date**: 12 April 2024 
- **Project Group Release Date**: 12 April 2024 
- **Project Group Revision Due**: 16 April 2024 
- **Project Group Presentation**: Week 12 (at your workshop - 20 May - 24 May 2024) 
- **Project Leaderboard**: 16 April - 24 May 2024 **(no extensions possible for the leaderboard)**
- **Project Final Submission Due**:  26 May 2024 **(no extension for the final submissions 2 days before deadline)**


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
| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing) |
|-----------------------------------------|

The impact of climate change on humanity is a significant concern. However, the increase in unverified statements regarding climate science has led to a distortion of public opinion, underscoring the importance of conducting fact-checks on claims related to climate science. Consider the following claim and related evidence:

**Claim**: The Earth’s climate sensitivity is so low that a doubling of atmospheric CO2 will result in a surface temperature change on the order of 1°C or less.

**Evidence:**

1. In his first paper on the matter, he estimated that global temperature would rise by around 5 to 6 °C (9.0 to 10.8 °F) if the quantity of CO 2 was doubled.
2. The 1990 IPCC First Assessment Report estimated that equilibrium climate sensitivity to a doubling of CO2 lay between 1.5 and 4.5 °C (2.7 and 8.1 °F), with a "best guess in the light of current knowledge" of 2.5 °C (4.5 °F).


It should not be difficult to see that the claim is not supported by the evidence passages, and assuming the source of the evidence is reliable, such a claim is misleading. The challenge of the project is to develop an automated fact-checking system where given a claim, the goal is to find related evidence passages from a knowledge source and classify whether the claim is supported by the evidence.

More concretely, you will be provided a list of claims and a corpus containing a large number evidence passages (the “knowledge source”), and your system must: (1) search for the most related evidence passages from the knowledge source given the claim; and (2) classify the status of the claim given the evidence in the following 4 classes: {SUPPORTS, REFUTES, NOT_ENOUGH_INFO, DISPUTED}. To build a successful system, it must be able to retrieve the correct set of evidence passages and classify the claim correctly.

Besides system implementation, you must also write a report that describes your fact-checking system, e.g. how the retrieval and classification components work, the reason behind the choices you made and the system’s performance. We hope that you will enjoy the project. To make it more engaging, **we will run the task as a Codalab competition (Optional)**. You will be competing with other students in the class. The following sections give more details on the data format, system evaluation, grading scheme and use of Codalab. Your assessment will be graded based on your report, your performance in the competition and your code.


You are provided with several files for the project:
* [train-claims,dev-claims].json: JSON files for the labelled training and development set; 
* [test-claims-unlabelled].json: JSON file for the unlabelled test set;
* evidence.json: JSON file containing a large number of evidence passages (i.e. the “knowledge source”); 
* dev-claims-baseline.json: JSON file containing predictions of a baseline system on the development set; eval.py: Python script to evaluate system performance (see “Evaluation” below for more details).

For the labelled claim files (train-claims.json, dev-claims.json), each instance contains the claim ID, claim text, claim label (one of the four classes: {SUPPORTS, REFUTES, NOT_ENOUGH_INFO, DISPUTED}), and a list of evi- dence IDs. The unlabelled claim file (test-claims-unlabelled.json) has a similar structure, except that it only contains the claim ID and claim text. More concretely, the labelled claim files has the following format:

```
{
  "claim-2967":
  {
    claim_text: "[South Australia] has the most expensive electricity in the world."
    claim_label: "SUPPORTS"
    evidences: ["evidence-67732", "evidence-572512"]
  },
  "claim-375":
  ...
}
```

The list of evidence IDs (e.g. evidence-67732, evidence-572512) are drawn from the evidence passages in evidence.json:

```
{
  "evidence-0": "John Bennet Lawes, English entrepreneur and agricultural scientist",
  "evidence-1": "Lindberg began his professional career at the age of 16, eventually ...",
  ...
}
```


Given a claim (e.g. claim-2967), your system needs to search and retrieve a list of the most relevant evidence passages from evidence.json, and classify the claim (1 out of the 4 classes mentioned above). You should retrieve at least one evidence passage.

The training set (train-claims.json) should be used for building your models, e.g. for use in development of features, rules and heuristics, and for supervised/unsupervised learning. You are encouraged to inspect this data closely to fully understand the task.

The development set (dev-claims.json) is formatted like the training set. This will help you make major im- plementation decisions (e.g. choosing optimal hyper-parameter configurations), and should also be used for detailed analysis of your system — both for measuring performance and for error analysis — in the report.

You will use the test set (test-claims-unlabelled.json) to participate in the Codalab competition. For this reason no labels (i.e. the evidence passages and claim labels) are provided for this partition. You are allowed (and encouraged) to train your final system on both the training and development set so as to maximise per- formance on the test set, but you should not at any time manually inspect the test dataset; any sign that you have done so will result in loss of marks. In terms of the format of the system output, we have provided dev-claims-predictions.json for this. Note: you’ll notice that it has the same format as the labelled claim files (train-claims.json or dev-claims.json), although the claim_text field is optional (i.e. we do not use this field during evaluation) and you’re free to omit it.


<br/>



## <img src="https://em-content.zobj.net/thumbs/120/whatsapp/326/desktop-computer_1f5a5-fe0f.png" width="30" />2.Important Note

| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing) |
|-----------------------------------------|

**Project Rules**

You MUST follow the rules below. If not, your project submission will NOT be marked.
1) You can use different types of sequence models, such as RNN, LSTM, Bi-LSTM, GRU, Bi-GRU, Transformer, even PLM or LLM, etc. However, you MUST NOT directly use the existing state-of-the-art (SOTA) architecture as it is but need to modify it and propose your own model. For example, you MUST NOT directly use the SOTA model (i.e. BERT) without any modification.

2) You MUST NOT use any pretrained model weights or large language model weight from any sources, and MUST NOT fine-tune it; You can use pretrained language models or word embeddings.

3) The model described in the report MUST NOT differ from the submitted code and running log in the submitted ipynb file.

4) You can use packages or code from the Courses (except pretrained models). If you use/refer to any other package or code, please put the reference at the bottom of the code. Otherwise, it will be considered as plagiarism.

5) You MUST NOT submit the prediction result (to the codalab leaderboard) that is not produced from your code

6) Your code MUST NOT use any rule(or condition)-based techniques in the model.

7) You MUST NOT use models that cannot be run on Colab (e.g. very large models that don’t fit on the GPU on Colab)

8) You MUST use the given code template.

9) You MUST train your system using only the provided data, which includes a training, a development and a test set; see the instructions in “Datasets” below for information on their format and usage. 

**Useful Notes**
1) Please refer to lecture notes, workshop materials, and resources that are covered.

2) Please proceed your way if we do not specify it in the specification.

<br/>


## <img src="https://em-content.zobj.net/source/skype/289/test-tube_1f9ea.png" width="30" />3.Testing and Evaluation
| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing) |
|-----------------------------------------|

**IMPORTANT: please make sure that you check the IMPORTANT NOTES**

**Testing and Leaderboard**
For this assignment, instead of solely focusing on achieving higher performance, having a good architecture design & implementation with detailed step-by-step justification will be important to show you’ve fully reached our expectations in this assignment.

We provide a script (eval.py) for evaluating your system. This script takes two input files, the ground truth and your predictions, and computes three metrics: (1) F-score for evidence retrieval; (2) accuracy for claim classification; and (3) harmonic mean of the evidence retrieval F-score and claim classification accuracy. Shown below is the output from running predictions of a baseline system on the development set:

```
$ python eval.py --predictions dev-claims-baseline.json --groundtruth dev-claims.json
Evidence Retrieval F-score (F)    = 0.3377705627705628
Claim Classification Accuracy (A) = 0.35064935064935066
Harmonic Mean of F and A          = 0.3440894901357093
```

The three metrics are computed as follows:

1. Evidence Retrieval F-score (F): computes how well the evidence passages retrieved by the system match the ground truth evidence passages. For each claim, our evaluation considers all the retrieved evidence passages, computes the precision, recall and F-score by comparing them against the ground truth passages, and aggregates the F-scores by averaging over all claims. E.g. given a claim if a system retrieves the following set {evidence-1, evidence-2, evidence-3, evidence-4, evidence-5}, and the ground truth set is {evidence-1, evidence-5, evidence-10}, then precision = 2/5, recall = 2/3, and F-score = 1/2. The aim of this metric is to measure how well the retrieval component of your fact checking system works.

2. Claim Classification Accuracy (A): computes standard classification accuracy for claim label predic- tion, ignoring the set of evidence passages retrieved by the system. This metric assesses solely how well the system classifies the claim, and is designed to understand how well the classification component of your fact checking system works.

3. Harmonic Mean of F and A: computes the harmonic mean of the evidence retrieval F-score and claim classification accuracy. Note that this metric is computed at the end after we have obtained the aggregate (over all claims) F-score and accuracy. This metric is designed to assess both the retrieval and classification components of your system, and as such will be used as **the main metric for ranking systems on Codalab.**


The first two metrics (F-score and accuracy) are provided to help diagnose and develop your system. While they are not used to rank your system on the leaderboard, you should document them in your report and use them to discuss the strengths/weaknesses of your system.

The example prediction file, dev-claims-baseline.json, is the output of a baseline system on the development set. This file will help you understand the required file format for creating your development output (for tuning your system using eval.py) and your test output (for submission to the Codalab competition).

Note that this is not a realistic baseline, and you might find that your system performs worse than it. The reason for this is that this baseline constructs its output in the following manner: (1) the claim labels are randomly selected; and (2) the set of evidence passages combines several randomly selected ground truth passages and several randomly selected passages from the knowledge source. We created such a ‘baseline’ because a true random baseline that selects a random set of evidence passages will most probably produce a zero F-score for evidence retrieval (and consequently zero for the harmonic mean of F-score and accuracy), and it won’t serve as a good diagnostic example to explain the metrics. To clarify, this baseline will not be used in any way for ranking submitted systems on Codalab, and is provided solely to illustrate the metrics and an example system output.


<br/>


## <img src="https://em-content.zobj.net/thumbs/120/facebook/355/page-facing-up_1f4c4.png" width="30" />4.Documentation
| :exclamation:  You MUST use the [ACL template](https://github.com/acl-org/acl-style-files) when writing your report.
|-----------------------------------------|

We prefer you to use LATEX, but you are permitted to use Word. You must include your student number under the title (using the \author field in LATEX and enabling the \aclfinalcopy option), but not your name to facilitate anonymous peer reviewing. We will not accept reports that are longer than the stated limits above, or otherwise violate the style requirements.

The report should be submitted as a PDF and contain no more than five(5)** A4 pages of content, excluding references. An appendix is not allowed. Therefore, you should consider carefully the information that you want to include in the report to build a coherent and concise narrative.

A report should be submitted with a description, analysis, and comparative assessment of the methods used. You should describe your methods in enough detail that we could replicate them without looking at your code. You should mention any choices you made in implementing your system along with empirical justification for those choices using the development set. You should also detail both your development performance and the **Final
Evaluation** performance on the Kaggle leaderboard (and in your submitted code and running log). You should use tables and the appropriate charts to report your results/findings.

The description of your method should be clear and concise. You should write it at a level that a Masters student could read and understand without difficulty. If you use any existing algorithms, you do not have to rewrite the complete description, but must provide a summary that shows your understanding and you should provide a citation to reference(s) in the relevant literature. In the report, we will be very interested in seeing evidence
of your thought processes and reasoning for choosing one approach over another (as indicated by the heavier weighting of the “soundness” criteria).

The report should include the evaluation setup, including dataset description, baseline, and implementation details. You need to describe the setup environment and hyperparameter you used (e.g., input embedding dimension, epochs, learning rate, optimiser). Please check the Evaluation (Dataset, Baselines, Implementations) section in the paper [Knowledge-aware Named Entity Recognition with Alleviating Heterogeneity](https://ojs.aaai.org/index.php/AAAI/article/view/17603/17410) Nie et al., AAAI 2020.

**The justification MUST be based on the previous literature reference (incl. international conference or journal publication) or empirical evaluation. (Check the definition of 'empirical evaluation' at the following FAQ Section). **

**Note that We DO NOT MARK the Documentation if it is NOT implemented as described in the report.**



<br/>


## <img src="https://em-content.zobj.net/thumbs/120/whatsapp/326/envelope-with-arrow_1f4e9.png" width="30" />Project Submission Method and Grading
**Submission:** LMS Assignment Submission Box (The submission box will be opened on 1 May 2024)

**You Must Submit Three Files:**
- pdf file: a report (documentation) with the given template [ACL template](https://github.com/acl-org/acl-style-files) 
(file name: COMP90042_your_groupid.pdf)
- ipynb file or python packages (.py files): An ipynb file or python package that includes all your implementation (the code should be in the following sections - dataset, model, testing). You MUST use this [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing)
(file name: COMP90042_your_groupid.ipynb or  COMP90042_your_groupid.zip)
- zip file: A zip file that contains trained models, dataset, readme - if necessary, and all other required files that you used for your program.
(file name: COMP90042_your_groupid_resource.zip)


Note that we will be running peer reviewing for the report shortly after the project has been completed. Please note that you should be uploading a single PDF document for your report and a single zip file for your code; **all other formats are not allowed, e.g. docx, 7z, rar, etc. Your submission will not be marked and will be given a score of 0 if you use these other formats.** You do not need to upload your data files to the zip (e.g., the evidence passages).



**Your submissions will be graded as follows:**
| Component  | Criteria | Description  | Marks |
| ------------- | ------------- | ------------- | ------------- |
| Writing  | Clarity  | Is the report well-written and well-structured?  | 5  |
| Writing  | Tables/Figures  | Are tables and figures interpretable and used effectively?  | 4  |
| Content  | Soundness  | Are the experiments sound? Are methods justified and used correctly?  | 7  |
| Content  | Substance  | How much work is done? Is there enough substance?  | 5  |
| Content  | Novelty  | How novel or ambitious are the techniques or methods?  | 5  |
| Content  | Results  | Are the results and findings convincing? Are they well articulated?  | 5  |
| Scholarship  | Citation  | Does the report demonstrate an outstanding ability to critically evaluate the academic validity of primary sources (trustable publication) and use this information to support, unpack or question academic findings?   | 4 |
| **Total**  |   |  | **35**  |


**Leaderboard Bonus Mark**

The leaderboard submission is optional. 
The top 10 groups in the private leaderboard will receive 3 bonus marks.
The top 11 to 30 groups in the private leaderboard will receive 1 bonus mark.
The evaluation metric for this competition is **Mean F1-Score**. The F1 metric weights recall and precision equally, and a good retrieval algorithm will maximize both precision and recall simultaneously. Thus, moderately good performance on both will be favoured over extremely good performance on one and poor performance on the other.

The Mean F1 Score in Kaggle is the same as [sklearn.metrics.f1_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html), with an average of 'micro'.

In your report, you can either use token-based or entity-based performance measures.


**Leaderboard Submission Format**

Joining the competition on Codalab is optional. The Codalab competition link will be announced on Canvas at a later date (16 April).

You must use your student.unimelb.edu.au address email to join the competition (via the “Participate” tab), and you are not permitted to join the competition with multiple email accounts. 
Any student who is found to have participated with multiple accounts will be automatically suspended from the competition and graded zero for the project.
Once you have joined the competition, please edit your account details by clicking on your login in the top right corner and selecting “Settings”. Set your group number. 
Submissions which have no group number will not be marked.

To submit your test output, select the “Participate” tab, click the “Ongoing evaluation” button, and then click “Submit”. This will allow you to select a file, which is uploaded to the Codalab server, which will evaluate your results and add an entry to the leaderboard. Your file should be a zip archive containing a single file named test-claims-predictions.json. The JSON file should produce the claim labels and evidence passages for all the claims in test-claims-unlabelled.json. The format of the JSON file should follow the format of the provided baseline system (i.e. dev-claims-baseline.json). The system will produce an error message if the filename is different, as it cannot process your file.

The results are shown on the leaderboard under the “Results” tab, under “Ongoing Evaluation”. The competition ends at on 24th May, after which submissions will no longer be accepted (extensions can not be granted to this deadline). At this point, the “Final Evaluation” results will be revealed. These two sets of results reflect evaluation on different subsets of the test data. The best score on the ongoing evaluation may not be the best on the final evaluation, and we will be using the final evaluation scores in the assessment. The final result of your best submission(s) can now be discussed in the report, which is due at 11.59PM, 26 May 2024.

Note that Codalab allows only 3 submissions per user per day, so please only upload your results when you have made a meaningful change to your system. Please do not over-tune your system based on the ongoing test set, as it is very likely to see a performance drop when it’s evaluated on the final test set, since it probably has overfitted on the ongoing test set (we see this every year in COMP90042 projects, where systems that have a large number of submissions during ongoing evaluation see a large drop in ranking once the final evaluation results are released). Note that Codalab is a little slow to respond at times, so you will need to give it a minute or so to process your file and update the result table.



<br/>




## <img src="https://em-content.zobj.net/source/whatsapp/390/clipboard_1f4cb.png" width="30" />Week 12 Presentation and Peer Review
**YOU MUST Attend Week 12 Workshop**
* The presentation allows students to communicate their project background, project aims, methods, results and importance, limitations, conclusions, and future work to a group of peers (students and Academic staff). Students are assessed on their presentation skills, visual communication skills, technical content of the presentation and their answers to questions.
* Each group presents for 8 minutes. There is then 2 minutes for questions.
* Peer Review Markers must use the attached marking sheet and write comments on each item to justify their mark and provide feedback to others.

**Marking Criteria: [Link](https://docs.google.com/document/d/1e7uZSVA4X9Accvw8I52vbcecBMEBgZfGIwseu_hzrNk/edit?usp=sharing)**

**Total 8 Marks**:
* **Presentation Skill**: 6 Marks
* **Peer Review Skill**: 2 Marks



## <img src="https://em-content.zobj.net/thumbs/120/google/350/person-raising-hand_1f64b.png" width="30" />FAQ
**Question: My Model performs really bad (Low F1). What did I do wrong?**<br/>
Answer: Please don't worry about the low performance as our training dataset is very small and your model is very basic deep learning model. Of course, there is something wrong with your code if it comes out below the baseline.

**Question: Do I need to save the word embedding model?**<br/>
Answer: We highly recommend you to save your best word embedding model (if you have), and load it when you use it in your code. Otherwise, it is sometimes removed and overwrite all your code so that you need to re-run the whole code again.

**Question: What do I need to write in the justification or explanation? How much do I need to articulate?**<br/>
Answer: We recommend conducting empirical evaluation. Empirical evaluation refers to the appraisal of a theory by observation in experiments. The key to good empirical evaluation is the proper design and execution of the experiments so that the particular factors to be tested can be easily separated from other confounding factors. Hence, visualising the comparison of different testing results is a good way to justify your decision. Explain the trends based on your understanding. You can find another way (other than comparing different models) as well - like citing the peer-reviewed publications. 
