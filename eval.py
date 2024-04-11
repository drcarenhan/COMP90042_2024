import argparse
import sys
import json
import numpy as np

######
#main#
######

def main(args):

    try:
        predictions = json.load(open(args.predictions))
    except:
        print("Error loading predictions json file:", args.predictions)
        raise SystemExit

    try:
        groundtruth = json.load(open(args.groundtruth))
    except:
        print("Error loading groundtruth json file:", args.groundtruth)
        raise SystemExit

    try:
        f, acc = [], []

        #iterate through the groundtruth instances
        for claim_id, claim in sorted(groundtruth.items()):
            if claim_id in predictions and \
                "claim_label" in predictions[claim_id] and \
                "evidences" in predictions[claim_id]:

                #check claim level label
                instance_correct = 0.0
                if predictions[claim_id]["claim_label"] == claim["claim_label"]:
                    instance_correct = 1.0
                
                #check retrieved evidences
                evidence_correct = 0
                evidence_recall = 0.0
                evidence_precision = 0.0
                evidence_fscore = 0.0
                if type(predictions[claim_id]["evidences"]) == list and (len(predictions[claim_id]["evidences"]) > 0):
                    top_six_ev = set(predictions[claim_id]["evidences"])
                    for gr_ev in claim["evidences"]:
                        if gr_ev in top_six_ev:
                            evidence_correct += 1
                    if evidence_correct > 0:
                        evidence_recall = float(evidence_correct) / len(claim["evidences"])
                        evidence_precision = \
                            float(evidence_correct) / len(predictions[claim_id]["evidences"])
                        evidence_fscore = (2*evidence_precision*evidence_recall)/(evidence_precision+evidence_recall)

                if args.verbose:
                    print("groundtruth =", claim)
                    print("predictions =", predictions[claim_id])
                    print("instance accuracy =", instance_correct)
                    print("evidence recall =", evidence_recall)
                    print("evidence precision =", evidence_precision)
                    print("evidence fscore =", evidence_fscore, "\n\n")

                #add the metric results
                acc.append(instance_correct)
                f.append(evidence_fscore)

        #compute aggregate performance
        mean_f = np.mean(f if len(f) > 0 else [0.0])
        mean_acc = np.mean(acc if len(acc) > 0 else [0.0])
        if mean_f == 0.0 and mean_acc == 0.0:
            hmean = 0.0
        else:
            hmean = (2*mean_f*mean_acc)/(mean_f+mean_acc)

        print("Evidence Retrieval F-score (F)    =", mean_f)
        print("Claim Classification Accuracy (A) =", mean_acc)
        print("Harmonic Mean of F and A          =", hmean)
                
    except Exception as error:
        print("Error:", error)
        raise SystemExit

if __name__ == "__main__":

    #parser arguments
    desc = "Evaluation script that computes evidence retrieval f-score, claim classification accuracy, and aggregate performance."
    parser = argparse.ArgumentParser(description=desc)

    #arguments
    parser.add_argument("--predictions", required=True, help="json file containing the claim label predictions and retrieved evidences produced by a system")
    parser.add_argument("--groundtruth", required=True, help="json file containing the ground truth claim labels and evidences")
    parser.add_argument("--verbose", action="store_true", help="turn on debug prints")
    args = parser.parse_args()

    main(args)
