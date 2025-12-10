\# IMDB Sentiment Classification – Hard Mode Fundamentals



Goal:

\- Build a solid, well-structured sentiment classifier on the IMDB dataset.

\- Use this project as a "fundamentals gym" for NLP:

  - clean project structure

  - clear baselines

  - evaluation + error analysis

  - comparison: classic ML vs. a small transformer



Planned steps:

1\. Exploratory data analysis (EDA) of IMDB reviews.

2\. Baseline model: TF-IDF + Logistic Regression.

3\. Error analysis: where does the baseline fail?

4\. Improved models and tuning.

5\. Small transformer fine-tuning (e.g. DistilBERT).

6\. Report and conclusions.



Tech stack:

\- Python 3.11

\- NumPy, pandas, scikit-learn

\- Jupyter

\- (Later) PyTorch + Transformers



\## Model \& Interpretability



The baseline model is a TF-IDF + Logistic Regression pipeline.



\- Vocabulary size: 50,000

\- N-grams: unigrams and bigrams (1, 2)

\- Regularization: C = 2.0



On the validation set, the model achieves:



\- Accuracy: ~0.9112

\- F1-score: ~0.9119



\### What the model learned



Inspecting the learned weights for each word/bigram gives some nice insights:



\- Strongly \*\*positive\*\* words include:  

&nbsp; `great`, `excellent`, `perfect`, `wonderful`, `hilarious`, `the best`, `gem`, etc.

\- Strongly \*\*negative\*\* words include:  

&nbsp; `worst`, `awful`, `boring`, `waste`, `nothing`, `disappointing`, `ridiculous`, etc.



There are also some interesting “meta” words:



\- Words like \*\*"still"\*\* and \*\*"today"\*\* appear often in positive reviews,  

&nbsp; e.g. \*"it still holds up today"\*, so they get positive weights.

\- Words like \*\*"minutes"\*\* are heavily negative because they appear in complaints such as  

&nbsp; \*"I wasted 90 minutes of my life"\* or \*"after 10 minutes I wanted to turn it off."\*



These patterns show that the model is not just memorizing obvious sentiment words,  

but also picking up on how people talk about their experience with a movie.



