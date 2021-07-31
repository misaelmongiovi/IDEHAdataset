# IDEHADataset 
## A Large Dataset for Visual Question Answering for Cultural Heritage

### Table of contents
* [General Information](#general-information)
* [Data](#data)
* [License](#license)

### General Information
Visual Question Answering (VQA) is gaining momentum for its ability of bridging Computer Vision and Natural Language Process ing. However, VQA approaches rely on Machine Learning (ML) algo rithms, need to be trained on large annotated datasets for achieving good performances, and, once trained, a ML model is barely portable on a different domain. This calls for agile methodologies for building large annotated datasets from existing resources. The cultural heritage domain represents both a natural application of this task and an exten sive source of data for training and validating VQA models. To this end, by using data and models from ArCo (Architecture of Knowledge), the knowledge graph of the Italian cultural heritage, we generated a large dataset for VQA in Italian and English. 

### Data
The dataset contains 6.49M question-answer pairs covering cultural assets, 43 question templates and 282 verbal forms. The number of pairs per template ranges from 35 to 576K.
Together with the complete dataset, we provide a small sample of question-answer pairs from different question templates and cultural asset types and a grid with the distribution of question-answer pairs over question templates and cultural asset types. 
We also provide statistics on how many times questions from every question template were formulated by the surveyed users and how many time a question template was evoked by a user.

### Details
- The [Dataset-Statistics](https://github.com/misael77/IDEHAdataset/blob/master/Dataset-statistics.xlsx) file contains the accuracy by question template obtained from the manual validation of the samples in Italian (Column F) and English (Column G) together with the total amount of occurrences of the question-answer pairs on the question models (Column B), how many different forms of question model the reports on the questions were asked by the interviewed users (Column C) and how many times a question pattern was evoked by a user (Column D).
- The [stats_occurrences_cultural-property-types](https://github.com/misael77/IDEHAdataset/blob/master/stats_occurrences_cultural-property-types.xlsx) file contains the breakdown of question-answer pair counters by cultural asset type together with the total amount of occurrences of the question-answer pairs on the question models (Column J) and the total amount of occurrences of the cultural asset type (Row 45).
- The [Italian-sample](https://github.com/misael77/IDEHAdataset/blob/master/Italian-sample.xlsx) file contains an italian language sample of 50 elements by question template together with the results obtained from the manual validation.
- The [English-sample](https://github.com/misael77/IDEHAdataset/blob/master/English-sample.xlsx) file contains an english language sample of 50 elements by question template together with the results obtained from the manual validation.
- The [IDEHAdataset - Transformation Rules](https://github.com/misael77/IDEHAdataset/blob/master/IDEHAdataset%20-%20Transformation%20Rules.xlsx) file contains a list of transformation rules used to cleaning and normalize data.
- The [QATemplate-ITA_definitivo](https://github.com/misael77/IDEHAdataset/blob/master/QATemplate-ITA_definitivo%20.xlsx) file contains a template composed by question-answer pairs in natural language (Columns D and E) and a short answer (Column F). Each pair is associated to an ID (Column A) and to a SPARQL query to extract data from ArCo KG (Column G); which is also labeled as "user" or "expert" or "both" depending on the aforementioned perspectives (Column B) and as "visual" (eg, What is the shape?) or "contextual" (eg, Who is the author?) or "mixed" (eg, What is the material?) depending on the type of information needed to answer the question (Column C).

### License
This dataset is licensed under the [Creative Commons by-sa 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The data of ArCo, the knowledge graph of the Italian cultural heritage, were extracted through SPARQL Endpoint. 

