# NER - Named Entity Recognition

Universidade de Brasília  
Departamento de Ciência da Computação  
CIC0269 - Processamento de Linguagem Natural - 2022/1

Professor: [Vinícius R. P. Borges](https://github.com/viniciusrpb)

## Objective

This repository contains Deep Learning and NLP models for Named Entity Recognition (NER) task, whose main purpose is to extract usefull information from a corpus, that can be texts or images.

## Datasets

- [ICDAR](https://rrc.cvc.uab.es/?ch=13&com=tasks): image tagged invoice corpus.
- [MITMovie](https://groups.csail.mit.edu/sls/downloads/movie/): semantically tagged movie corpus in BIO format.
- [MITRestaurant](https://groups.csail.mit.edu/sls/downloads/restaurant/): semantically tagged tabular restaurant corpus in BIO format.

## Project structure

```
├── 📁 ICDAR
|   ├── 📁 data
|   └── 📁 src
|       ├── experiment_one_receipt   # Experiment with one receipt
|       └── experiments/regex        # Regex model
├── 📁 MITMovie
|   ├── 📁 data
|   └── 📁 src/models
|       ├── BiLSTM_CRF               # Bidirectional LSTM + CRF model
|       ├── LSTM                     # LSTM model
|       └── LSTM_CRF                 # LSTM + CRF model
├── 📁 MITRestaurant
|   ├── 📁 data
|   └── 📁 src/models
|       ├── BiLSTM_CRF               # Bidirectional LSTM + CRF model
|       ├── LSTM                     # LSTM model
|       └── LSTM_CRF                 # LSTM + CRF model
```

## F1-score results

To accomplish this task, some NLP models were created based on Deep Learning concepts: BiLSTM CRF, LSTM CRF and LSTM; and applied on tagged text corpus in BIO format. For image corpus, an experiment were performed using OCR and Regex to extract important fields, for future work I would like to implement LayoutML model and use BERT to identify and correct misleaded words.

|            | MITMovie | MITRestaurant |
| ---------- | -------- | ------------- |
| BiLSTM CRF | 0.52     | 0.67          |
| LSTM CRF   | 0.54     | 0.66          |
| BiLSTM     | 0.57     | 0.68          |
| LSTM       | 0.55     | 0.65          |

|       | ICDAR |
| ----- | ----- |
| Regex | 0.26  |

## Requirements

- Install Python 3.8+
- Create a virtual environment and install dependencies: `python3 -m venv .venv`
- Activate the virtual environment: `source .venv/bin/activate`
- Install Requirements: `pip install -r requirements.txt`
- You are ready! :partying_face:

## References

Papers:

- [A Survey on Deep Learning for Named Entity Recognition](https://arxiv.org/abs/1812.09449)
- [LSTM-CRF for Drug-Named Entity Recognition](https://www.mdpi.com/1099-4300/19/6/283)
- [Information Extraction from Text Intensive and Visually Rich Banking Documents](https://www.sciencedirect.com/science/article/abs/pii/S0306457320308566)
- [CUTIE: Learning to Understand Documents with Convolutional Universal Text Information Extractor](https://arxiv.org/abs/1903.12363)
- [Bidirectional long short-term memory with CRF for detecting biomedical event trigger in FastText semantic space](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2543-1)
- [LayoutLM: Pre-training of Text and Layout for Document Image Understanding](https://arxiv.org/abs/1912.13318)

Codes:

- https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
- https://stackoverflow.com/questions/57858944/opencv-python-border-removal-preprocessing-for-ocr
- https://pyimagesearch.com/topics/
- https://www.dominodatalab.com/blog/named-entity-recognition-ner-challenges-and-model
- https://www.kaggle.com/code/aiswaryaramachandran/ner-using-lstm-s-and-keras/notebook
- https://github.com/viniciusrpb/cic0269_natural_language_processing/blob/main/tutorials/ner_aula.ipynb
