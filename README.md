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

Besides system implementation, you must also write a report that describes your fact-checking system, e.g. how the retrieval and classification components work, the reason behind the choices you made and the system’s performance. We hope that you will enjoy the project. To make it more engaging, **we will run the task as a Codalab competition**. You will be competing with other students in the class. The following sections give more details on the data format, system evaluation, grading scheme and use of Codalab. Your assessment will be graded based on your report, your performance in the competition and your code.

<br/>



## <img src="https://em-content.zobj.net/thumbs/120/whatsapp/326/desktop-computer_1f5a5-fe0f.png" width="30" />2.Important Note

| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing) |
|-----------------------------------------|

**Project Rules**

You MUST follow the rules below. If not, your project submission will NOT be marked.
1) You can must modify the Transformer model with different types of sequence models, such as RNN, LSTM, Bi-LSTM, GRU, Bi-GRU, Transformer, even PLM or LLM, etc. However, you MUST NOT directly use the existing state-of-the-art (SOTA) architecture as it is but need to modify it and propose your own model. For example, you MUST NOT directly use the SOTA model (i.e. BERT) without any modification.

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

**Testing and Evaluation**
You are to implement a testing program with the trained model. When the testing program is executed, the program should show the testing result by using your proposed model. The testing result should include accuracy, same as [**Workshop XX**](https://colab.research.google.com/drive/1yVy7T9DNB9lJo3NgFdsHAuEsI0msAuPz). Moreover, your testing result should be compared with the baseline. The Bi-LSTM CRF section (the original code can be found on the [pytorch official website](https://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html)

You need to justify your decision and explain the pattern by testing the performance of your implementation. The testing result should include precision, recall and F-value -refer to **Workshop XX**.

You need to write a manual (readme) for the assessor. Your manual should guide you on how to test your program and also include a list of packages (with versions) that you used. If you work on Google Colab or Jupyter Notebook (.ipynb), your manual should guide the assessor on where to upload the required files (trained model, dataset, etc.). Note the assessor will use Google Colab to open your ipynb file unless you have a function that downloads required files from URL or Google Drive. 

Please check the following sample Evaluation setup section. 
- [Hierarchical Contextualized Representation for Named Entity Recognition](https://arxiv.org/pdf/1911.02257v2.pdf) Luo et al., AAAI 2020

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

For every token in the dataset, submission files should contain two columns: Id and Predicted.
The file should contain a header and have the following format:

```ID,Predicted
1,O
2,O
3,O
4,I-LOC
...
```



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
