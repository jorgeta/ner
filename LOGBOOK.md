# Project logbook

## Log

### Monday 04.01

Start-up meeting.
List of expectations and what I want to do with the project.
Start running code with data using the models.
Read BERT paper.

### Tuesday 05.01

Company work. 
Read Attention is All You Need paper. 
Watch videos explaining BERT and transformers. 
Start looking at how Alexandra Institute has fine-tuned the model. 
Start github repository.

### Wednesday 06.01

Start evaluating performance of the danlp Flair and Bert based NER models on the dataset.
Focus on where the model fails.

### Thursday 07.01

Continue evaluation notebook on the models.
Look at what a flair_ner model is.
Set up a report outline.

### Friday 08.01

Research space complexity and how to calculate that.
Calculate time complexity.

### Monday 11.01

Master thesis meeting.
Questions related to complexity and pre-training.
Read paper related to the flair model and paper relatied to the BiLSTM-CRF.

### Tuesday 12.01

Output the mistakes that the models make.
Look at and discuss the mistakes that the models make.

Read paper related to the danlp repository.

Time complexity: compare timings of all test set data on a CPU and on a GPU for both models.

Space complexity:
- find the number of parameters used by each model
- figure out how much space each of the models use on disk 
    - flair: 474 955 814 bytes (481,5 MB on disk)
    - bert: 442 545 317 bytes (443,1 MB on disk)

### Wednesday 13.01

Status meeting.
Questions:
- Problems related to using the models on the GPU.
- BERT and Flair has 9 and 10 classes respectively, haven't figured out why.
- None of the models does ever predict MISC.
- WHat does inference mean when talking about memory usage during inference?

### Thursday 14.01

Calibration.

Confusion matrices.

Analysis of sentences where the predictions are wrong.

Look at probabilities that the softmax outputs.

## Plan

### Friday 15.01

Look at the same as on Thursday for flair.

Status meeting.

### For later maybe

Continue work on time and space complexity.

Describe the fine-tuning done by danlp.
Set up paper, describe models.

Look at the outputted mistakes that the models make, and discuss potential pitfalls and drawbacks of their model.

