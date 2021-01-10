# Evaluation of Named Entity Recognition for the Danish Language

## Project course objectives

A student who has met the objectives of the course will be able to:
- Define own learning objectives for the evaluation of NER systems project.
- Collect scientific knowledge and data related to the project topic.
- Carry out a well-founded delimitation of the project and formulate specific hypotheses and aims.
- Plan and carry out the course of the project in collaboration wit the project supervisors.
- Assess and summarize the project results in relation to aims, methods and available data.
- Carry out the project and interpret results by use of Python or other programming language.
- Structure and write a final short technical report including problem formulation, description of methods, experiments, evaluation and conclusion.
- Presentation of methods and results at meetings with project supervisors.

## Short project description

Evaluate performance (NER classification performance, computational complexity: space and time) on the dataset (1) using models (2).

**(1) Dataset**

- Name: UD-DDT (DaNE)
- Task: NER
- Words: 100,733
- Sents: 5,512
- Annotated with Named Entities for PER, ORG and LOC

Link to [dataset](https://github.com/alexandrainst/danlp/blob/master/docs/docs/datasets.md).

**(2) Models**

- BERT NER model
- flair_ner_model

Link to [models](https://github.com/alexandrainst/danlp/tree/master/danlp/models).

## Relevant links

[Alexandra Institute - danlp](https://github.com/alexandrainst/danlp)

[BERT - original paper](https://arxiv.org/pdf/1810.04805.pdf)

[Transformers - original paper](https://arxiv.org/pdf/1706.03762.pdf)

[BERT word embedding tutorial](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/)

[Classification evaluation measurement](https://towardsdatascience.com/multi-class-metrics-made-simple-part-i-precision-and-recall-9250280bddc2)

[Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix)

[IOB](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging))

[How to use Flair](https://www.analyticsvidhya.com/blog/2019/02/flair-nlp-library-python/)

[Flair paper](https://www.aclweb.org/anthology/C18-1139.pdf)

[Bidirectional LSTM-CRF Models for Sequence Tagging (paper)](https://arxiv.org/pdf/1508.01991.pdf)