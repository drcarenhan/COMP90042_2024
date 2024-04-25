# COMP90042 Project Description

This assignment can be done individually or in teams of two or three or four. We strongly encourage healthy collaboration. See the [University of Melbourne Working in Groups Guide](https://students.unimelb.edu.au/academic-skills/resources/communicating-in-class/communicating-with-peers/working-in-groups). 
If your team member does not contribute, please contact the lecturer ([Dr. Caren Han](mailto:caren.han@unimelb.edu.au?subject=[COMP90042]%20Project%20Group)) and explain the situation (e.g. by describing the contributions of each collaborator in your team). We strongly recommend to start working early so that you will have ample time to discover stumbling blocks and ask questions.

You are free to design the architecture using any of the techniques learned from our lectures and labs (as long as they don't conflict with the project rules (see below). For training and evaluation, we provide you a benchmark dataset in split of training, validation and test. You will use the training and validation set for training/validation while using the test set for leaderboard submission. 

For this assignment, **instead of solely focusing on achieving higher performance, you should consider exploring novel architecture design and justify your decision processes**, as grading is by-and-large based on your research process rather than system performance (see grading details below).


**Table of Contents**
- [0. Important Dates (Very Important!!)](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-0-important-dates)
- [1. DataSet](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-1-dataset)
- [2. Important Notes](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-2-important-notes)
- [3. Model Testing](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-3-testing-and-evaluation)
- [4. Report Writing](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-4-report-writing)
- [5. Project Submission Method and Grading](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-5-project-submission-method-and-grading)
- [6. Week12 Presentation and Peer Review](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-6-week-12-presentation-and-peer-review)
- [7. Codalab](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#7-codalab)
- [8. FAQ](https://github.com/drcarenhan/COMP90042_2024?tab=readme-ov-file#-8-faq)

<br/>
<br/>


## <img src="https://em-content.zobj.net/thumbs/120/microsoft/319/calendar_1f4c5.png" width="30" /> 0. Important Dates
The Important date for the Project can be summarised as follows:
- **Project Specification Release Date**: 12 April 2024 
- **Project Group Release Date**: 12 April 2024 
- **Project Group Revision Due**: 16 April 2024 
- **Project Group Presentation**: Week 12 (at your workshop - 20 May - 24 May 2024) 
- **Project Leaderboard Competition Period**: 26 April - 24 May 2024 **(no extensions possible for the leaderboard)**
- **Project Final Submission Due**:  26 May 2024 **(no extension will be given less than 2 days before deadline)**


All deadlines are **11:59 PM (Melbourne Time AEST)**.


**Project Group Announcement**
PLEASE ENSURE COMMUNICATION WITH YOUR GROUP MEMBER BY THE GROUP REVISION DEADLINE. Please take a look at the details below.

**Project Group Revision Due**
If you wish to switch from a group to an individual status, adjustments can be made by the Project Group Change Deadline. However, in that case, you SHOULD receive agreements from your team members before the group revision due.
NOTE: If you do not communicate with your group member by the Group Revision Deadline at all, and if your group member(s) contact the lecturer (Dr. Caren Han) and requests you to proceed individually, you will be assigned to work on the project individually (or without that team member).


**Leaderboard**
The leaderboard competition will run from 26 April to 24 May 2024, 11:59PM. The closing date is two days before the Final Submission due date.




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

Besides system implementation, you must also write a report that describes your fact-checking system, e.g. how the retrieval and classification components work, the reason behind the choices you made and the system’s performance. We hope that you will enjoy the project. To make it more engaging, **we will run the task as a Codalab competition (participation is optional; more details below)**. You will be competing with other students in the class. The following sections give more details on the data format, system evaluation, grading scheme and use of Codalab. Your assessment will be graded based on your report, your performance in the competition (in the form of bonus marks) and your code.


You are provided with several files for the project:
* [train-claims,dev-claims].json: JSON files for the labelled training and development set; 
* [test-claims-unlabelled].json: JSON file for the unlabelled test set;
* evidence.json: JSON file containing a large number of evidence passages (i.e. the “knowledge source”); 
* dev-claims-baseline.json: JSON file containing predictions of a baseline system on the development set;
* eval.py: Python script to evaluate system performance (see “Evaluation” below for more details).

For the labelled claim files (train-claims.json, dev-claims.json), each instance contains the claim ID, claim text, claim label (one of the four classes: {SUPPORTS, REFUTES, NOT_ENOUGH_INFO, DISPUTED}), and a list of evidence IDs. The unlabelled claim file (test-claims-unlabelled.json) has a similar structure, except that it only contains the claim ID and claim text. More concretely, the labelled claim files has the following format:

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

The development set (dev-claims.json) is formatted like the training set. This will help you make major implementation decisions (e.g. choosing optimal hyper-parameter configurations), and should also be used for detailed analysis of your system — both for measuring performance and for error analysis — in the report.

You will use the test set (test-claims-unlabelled.json) to participate in the Codalab competition. For this reason no labels (i.e. the evidence passages and claim labels) are provided for this partition. You are allowed (and encouraged) to train your final system on both the training and development set so as to maximise performance on the test set, but you should not at any time manually inspect the test dataset; any sign that you have done so will result in loss of marks. In terms of the format of the system output, we have provided dev-claims-predictions.json for this. Note: you’ll notice that it has the same format as the labelled claim files (train-claims.json or dev-claims.json), although the claim_text field is optional (i.e. we do not use this field during evaluation) and you’re free to omit it.


<br/>



## <img src="https://em-content.zobj.net/thumbs/120/whatsapp/326/desktop-computer_1f5a5-fe0f.png" width="30" /> 2. Important Notes

| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing) |
|-----------------------------------------|

**Project Rules**

You MUST follow the rules below. Any team found to break any of these rules will receive zero mark to their project.

1) You're encouraged to explore different models for the task, but in terms of sequence processing components you MUST use one of the following architectures: RNN, LSTM, GRU, and Transformer. You are allowed to use deep-learning libraries (e.g. pytorch) to import these sequence processing components (i.e. you do not have to code RNN from scratch). You should read relevant publications to come up with a sensible design for your fact-checking system, but you MUST NOT copy any open-source code from any publications (in other words, you MUST implement the fact-checking system yourself).

2) You MUST NOT use any pretrained word embeddings (e.g. Word2Vec), pretrained language model weights or checkpoints (e.g. BERT checkpoints), or any closed-source models (OpenAI GPT-3). In other words, you MUST train your system from scratch, using the data provided in the project.

3) The following deep-learning libraries are allowed: pytorch, keras, and tensorflow. Huggingface is not allowed. Standard python libraries (e.g. numpy and matplotlib) and NLP preprocessing toolkits (e.g. NLTK and Spacy) are allowed.

4) The model described in the report MUST be faithful to the submitted code and running log that you submit. You MUST include the running log (with the reported result/performance) in the submitted ipynb file (more details about submission below). 

5) You are allowed to use code from the workshop (provided that they don't conflict with any project rules), but you MUST NOT use any open source project code from GitHub or other platforms.

6) You MUST NOT submit the prediction result (to the codalab leaderboard) that is not produced from your code.

7) You MUST NOT use any rule-based techniques.

8) You MUST NOT use models that cannot be run on Colab (e.g. very large models that don’t fit on the GPU on Colab).

9) You MUST use the given [code template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing) for development.

10) You MUST train your system using only the provided data, which includes a training and a development. 

<br/>


## <img src="https://em-content.zobj.net/source/skype/289/test-tube_1f9ea.png" width="30" /> 3. Testing and Evaluation
| :exclamation:  You need to put the code that you conduct all actions for this section to the [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing) |
|-----------------------------------------|

**IMPORTANT: please make sure that you check the IMPORTANT NOTES**

**Testing and Leaderboard**

We provide a script (eval.py) for evaluating your system. This script takes two input files, the ground truth and your predictions, and computes three metrics: (1) F-score for evidence retrieval; (2) accuracy for claim classification; and (3) harmonic mean of the evidence retrieval F-score and claim classification accuracy. Shown below is the output from running predictions of a baseline system on the development set:

```
$ python eval.py --predictions dev-claims-baseline.json --groundtruth dev-claims.json
Evidence Retrieval F-score (F)    = 0.3377705627705628
Claim Classification Accuracy (A) = 0.35064935064935066
Harmonic Mean of F and A          = 0.3440894901357093
```

The **three metrics** are computed as follows:

1. **Evidence Retrieval F-score (F)**: computes how well the evidence passages retrieved by the system match the ground truth evidence passages. For each claim, our evaluation considers all the retrieved evidence passages, computes the precision, recall and F-score by comparing them against the ground truth passages, and aggregates the F-scores by averaging over all claims. E.g. given a claim if a system retrieves the following set {evidence-1, evidence-2, evidence-3, evidence-4, evidence-5}, and the ground truth set is {evidence-1, evidence-5, evidence-10}, then precision = 2/5, recall = 2/3, and F-score = 1/2. The aim of this metric is to measure how well the retrieval component of your fact checking system works.

2. **Claim Classification Accuracy (A)**: computes standard classification accuracy for claim label prediction, ignoring the set of evidence passages retrieved by the system. This metric assesses solely how well the system classifies the claim, and is designed to understand how well the classification component of your fact checking system works.

3. **Harmonic Mean of F and A**: computes the harmonic mean of the evidence retrieval F-score and claim classification accuracy. Note that this metric is computed at the end after we have obtained the aggregate (over all claims) F-score and accuracy. This metric is designed to assess both the retrieval and classification components of your system, and as such will be used as **the main metric for ranking systems on Codalab.**


The first two metrics (F-score and accuracy) are provided to help diagnose and develop your system. While they are not used to rank your system on the leaderboard, you should document them in your report and use them to discuss the strengths/weaknesses of your system.

The example prediction file, dev-claims-baseline.json, is the output of a baseline system on the development set. This file will help you understand the required file format for creating your development output (for tuning your system using eval.py) and your test output (for submission to the Codalab competition).

Note that this is not a realistic baseline, and you might find that your system performs worse than it. The reason for this is that this baseline constructs its output in the following manner: (1) the claim labels are randomly selected; and (2) the set of evidence passages combines several randomly selected ground truth passages and several randomly selected passages from the knowledge source. We created such a ‘baseline’ because a true random baseline that selects a random set of evidence passages will most probably produce a zero F-score for evidence retrieval (and consequently zero for the harmonic mean of F-score and accuracy), and it won’t serve as a good diagnostic example to explain the metrics. To clarify, this baseline will not be used in any way for ranking submitted systems on Codalab, and is provided solely to illustrate the metrics and an example system output.


<br/>


## <img src="https://em-content.zobj.net/thumbs/120/facebook/355/page-facing-up_1f4c4.png" width="30" /> 4. Report Writing
| :exclamation:  You MUST use the [ACL template](https://github.com/acl-org/acl-style-files) when writing your report.
|-----------------------------------------|

You must use LATEX for writing your report. You must include your group number under the title (using the \author field in LATEX and enabling the \aclfinalcopy option), but not your name. We will not accept reports that are longer than the stated limits below, or otherwise violate the style requirements.

The report should be submitted as a PDF and contain **no more than five(5)** A4 pages of content, excluding  team contribution and references. An appendix is NOT allowed. Therefore, you should consider carefully the information that you want to include in the report to build a coherent and concise narrative.

Below is a suggested report structure:

**Title** The title of your project and Group Number

**Abstract**. An abstract should concisely (less than 300 words) motivate the problem, describe your aims, describe your contribution, and highlight your main finding(s).

**Introduction** The introduction explains the problem, why it’s difficult, interesting, or important, how and why current methods succeed/fail at the problem, and explains the key ideas of your approach and results. Though an introduction covers similar material as an abstract, the introduction gives more space for motivation, detail, and references to existing work and captures the reader’s interest.

**Approach** This section details your approach(es) to the problem. For example, this is where you describe the architecture of your neural network(s), and any other key methods or algorithms.
* You should be specific when describing your main approaches – you probably want to include equations and figures.
* You should also describe your baseline(s). Depending on space constraints, and how standard your baseline is, you might do this in detail, or simply refer the reader to some other paper for the details.
* If any part of your approach is original, make it clear (so we can give you credit!). For models and techniques that aren’t yours, provide references.
* As you’re setting up equations, notation, and the like, be sure to agree on a fixed technical vocabulary (that you’ve defined, or is well-defined in the literature) before writing and use it consistently throughout the report! This will make it easier for the teaching team to follow and is nice practice for research writing in general.

**Experiments**. This section contains the following. 
* **Evaluation method**: If you’re defining your own metrics (for diagnostic purposes), be clear as to what you’re hoping to measure with each evaluation method (whether quantitative or qualitative, automatic or human-defined!), and how it’s defined.
* **Experimental details**: Report how you ran your experiments (e.g., model configurations, learning rate, training time, etc.)

**Results**: Report the quantitative results that you have found so far. Use a table or plot to compare results and compare against baselines. You must report dev results, and also test results if you participate in the Codalab competition.
When you write results, please be aware of the following questions: Are they what you expected?; Better than you expected?; Is It worse than you expected?; Why do you think that is?; What does that tell you about your approach?

**Conclusion**. Summarise the main findings of your project, and what you have learnt. Highlight your achievements, and note the primary limitations of your work. If you like, you can describe avenues for future work.

**Team contributions** (doesn't count towards the page limit) If you are a multi-person team, briefly describe the contributions of each member of the team.

**References** (doesn't count towards the page limit) Your references section should be produced using BibTeX.

**Note that We DO NOT MARK the report if it's not a faithful description of the implemented system (i.e. the submitted system is different to what is described in the report).**



<br/>


## <img src="https://em-content.zobj.net/thumbs/120/whatsapp/326/envelope-with-arrow_1f4e9.png" width="30" /> 5. Project Submission Method and Grading
**Submission:** LMS Assignment Submission Box (The submission box will be opened on 1 May 2024)

**You Must Submit Two Files:**
- **pdf file** (filename format: COMP90042_groupid.pdf): a report using the [ACL template](https://github.com/acl-org/acl-style-files).

- **zip file** (filename format: COMP90042_groupid_resource.zip): A zip file that contains: **1)** ipynb file(s) (You MUST use this [ipynb template](https://colab.research.google.com/drive/1CjlVXdEsioH_iGOHUbmrhimTLRXGJIt0?usp=sharing)), and **2)** a README file to describe how to run the code if it's not apparent from the documentation in the ipynb files (optional), and **3)** any shell scripts that you use to run your code, e.g. to pre-install packages (optional). Note: you MUST NOT upload any data files or trained model checkpoints.


**Your submissions will be graded as follows:**
| Component  | Criteria | Description  | Marks |
| ------------- | ------------- | ------------- | ------------- |
| Writing  | Clarity  | Is the report well-written and well-structured?  | 5  |
| Writing  | Tables/Figures  | Are tables and figures interpretable and used effectively?  | 4  |
| Content  | Soundness  | Are the experiments sound? Are methods justified and used correctly?  | 7  |
| Content  | Substance  | How much work is done? Is there enough substance?  | 5  |
| Content  | Novelty  | How novel or ambitious are the techniques or methods?  | 5  |
| Content  | Results  | Are the results and findings convincing? Are they well articulated?  | 5  |
| Scholarship  | Citation  | Does the report cite relevant publications to drive decision making (e.g. to motivate design choices or to support findings)?   | 4 |
| **Total**  |   |  | **35**  |


**Leaderboard Bonus Mark**

The leaderboard submission is optional. 
The top 10 groups in the private leaderboard will receive 3 bonus marks.
The top 11 to 30 groups in the private leaderboard will receive 1 bonus mark.
Project mark can not exceed 35 marks, including these bonus marks.


**Leaderboard Submission Instructions**

Joining the competition on Codalab is optional. The Codalab competition link will be announced on Canvas later (26 April).
Regardless of whether you join the competition or not, you need to include the output log in the ipynb files for the development set.

Should you decide to participate, your team must nominate one member to join join the competition (via the “Participate” tab) using their student.unimelb.edu.au address email. Each team can only have 1 member joining the competition. Any team that is found to have participated with multiple accounts will be automatically suspended from the competition and graded zero for the project.
Once you have joined the competition, please edit your account details by clicking on your login in the top right corner and selecting “Settings”. Set your group number. 
Submissions which have no group number will not be marked.

To submit your test output, select the “Participate” tab, click the “Ongoing evaluation” button, and then click “Submit”. This will allow you to select a file, which is uploaded to the Codalab server, which will evaluate your results and add an entry to the leaderboard. Your file should be a zip archive containing a single file named test-claims-baseline.json. The JSON file should produce the claim labels and evidence passages for all the claims in test-claims-unlabelled.json. The format of the JSON file should follow the format of the provided baseline system (i.e. dev-claims-baseline.json). The system will produce an error message if the filename is different, as it cannot process your file.

The results are shown on the leaderboard under the “Results” tab, under “Ongoing Evaluation”. The competition ends at on 24th May, after which submissions will no longer be accepted (extensions can not be granted to this deadline). At this point, the “Final Evaluation” results will be revealed. These two sets of results reflect evaluation on different subsets of the test data. The best score on the ongoing evaluation may not be the best on the final evaluation, and we will be using the final evaluation scores in the assessment. The final result of your best submission(s) can now be discussed in the report, which is due at 11.59PM, 26 May 2024. Note: if your team did not participate, then you won't have any test results to report, so focus on reporting the development results.

Note that Codalab allows only 3 submissions per team per day, so please only upload your results when you have made a meaningful change to your system. Please do not over-tune your system based on the ongoing test set, as you are very likely to see a performance drop when it’s evaluated on the final test set, since it probably has overfitted on the ongoing test set (we see this every year in COMP90042 projects, where systems that have a large number of submissions during ongoing evaluation see a large drop in ranking once the final evaluation results are released). Note that Codalab is a little slow to respond at times, so you will need to give it a minute or so to process your file and update the result table.



<br/>




## <img src="https://em-content.zobj.net/source/whatsapp/390/clipboard_1f4cb.png" width="30" /> 6. Week 12 Presentation and Peer Review
**YOU MUST Attend Week 12 Workshop**
* The presentation allows students to communicate their project background, project aims, methods, results and importance, limitations, conclusions, and future work to a group of peers (students and Academic staff). Students are assessed on their presentation skills, visual communication skills, technical content of the presentation and their answers to questions.
* Each group presents for 8 minutes. There is then 2 minutes for questions.
* Peer Review Markers must use the attached marking sheet and write comments on each item to justify their mark and provide feedback to others.
* **More information on the presentation procedure and peer review process will be released in Week 8.**

**Marking Criteria: [Link](https://docs.google.com/document/d/1e7uZSVA4X9Accvw8I52vbcecBMEBgZfGIwseu_hzrNk/edit?usp=sharing)**

**Total 8 Marks**:
* **Presentation Skill**: 6 Marks
* **Peer Review Skill**: 2 Marks

## 7. Codalab

Codalab competition website: [Link](https://codalab.lisn.upsaclay.fr/competitions/18719?secret_key=dbe1f3f8-4f05-4dcd-9e56-4b02708fd3be)

You should elect one member in your team to participate in the competition (i.e. we do not want everyone in the team to sign up for the competition). The elected member will be responsible for uploading your team's system results and they should sign up for a Codalab account **using their {student.unimelb.edu.au} address** and request to join the 
competition via the "Participate" tab. Only 
students enrolled in the subject will be permitted to join.

After joining the competition, please edit your account details by clicking on your login in the top 
right corner and selecting "Settings".  **Remember to set your team name.**  **Submissions which have no 
team name or incorrect team name format will not be marked.**

-----
**The team name MUST be formatted by following these steps:**
1) Please check your *Workshop DayTime* and *Group Number* from the following [Project Group Sheet](https://docs.google.com/spreadsheets/d/1AUReGexXTE7FiOyLcKYPzoS1mLznyrQq/edit?usp=sharing&ouid=102389134173271487528&rtpof=true&sd=true)
2) The *Workshop DayTime* is given by the sheet names (e.g. Mon1PM); *Group Number* is in column E within a sheet.
3) Your team name should be formatted as **WorkshopDayTime_GroupID** (e.g. **Tue9AM_Group1** or **Wed2PM_Group3**). Note: If your workshop starts on the quarter (e.g. Wed 2:15 PM), you should still follow sheet name (e.g. Wed2PM_GroupX).

----

You can use this system to submit your test output, by selecting the 
"Participate" tab and then clicking the "Ongoing evaluation" button, 
and then "Submit". This will allow you to select a file, which is 
uploaded to the Codalab server, which will evaluate your results and add 
an entry to the leaderboard. Your file should be a **zip archive** 
containing a single file named **test-claims-predictions.json**.
The JSON file should produce the claim labels and evidence passages for all the claims in **test-claims-unlabelled.json**. The format of the JSON file should follow the format of the provided baseline system (i.e. **dev-claims-baseline.json**).
**The system  will produce an error message if the filename is different, as it cannot 
process your file.**

The results are shown on the leaderboard under the "Results" tab, 
under "Ongoing Evaluation".  The 
competition ends at 11:59pm on 24th May 2024, after which submissions will no 
longer be accepted (extensions can not be granted to this 
deadline). At this point the "Final Evaluation" results will be 
revealed.  These two sets of results reflect evaluation on different 
subsets of the test data. The best score on the ongoing evaluation may 
not be the best on the final evaluation, and we will be using the final 
evaluation scores for ranking systems on the leaderboard. **The final result of your best 
submission(s) can now be discussed in the report**, which is due at 11:59pm 
on 26th May.

Note that Codalab allows only 3 submissions per user per day, so please 
only upload your results when you have made a meaningful change to your 
system. Note that the system is a little slow to respond at times, so 
you will need to give it a minute or so to process your file and update 
the result table. 


## <img src="https://em-content.zobj.net/thumbs/120/google/350/person-raising-hand_1f64b.png" width="30" /> 8. FAQ
**The FAQ will be updated based on the student's questions.

For a better and more supportive learning environment, our team summarised the FAQs based on the topic and would like to share the following posts (with our teaching team’s answer).  Please check the FAQ summary.

**[FAQ Discussion Board Summary](https://docs.google.com/document/d/15WcU-V-dIvyWrFticHr2iX8QQCc61REH2WmbwdSFfNs/edit?usp=drivesdk)**

