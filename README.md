Project Goal

This project uses the IMDB movie reviews dataset to build and analyze sentiment classification models, with an emphasis on fundamentals rather than leaderboard optimization.

The focus is on:

- establishing clear baselines

- comparing classic ML methods with a small transformer

- performing structured error analysis

- understanding model behavior and dataset limitations



Project Outline

- Exploratory data analysis (EDA) of IMDB reviews

- Baseline model: TF-IDF + Logistic Regression

- Error analysis of baseline failures

- Hyperparameter tuning and refinements

- Transformer fine-tuning (DistilBERT)

- Comparative analysis and conclusions


Tech Stack

Python 3.11

NumPy, pandas, scikit-learn

Jupyter Notebook
PyTorch + Hugging Face Transformers

Baseline Model and Interpretability

The baseline model is a TF-IDF + Logistic Regression pipeline.


Configuration:

Vocabulary size: 50,000

N-grams: unigrams and bigrams (1, 2)

Regularization strength: C = 2.0

Validation performance:

Accuracy: ~0.911

F1-score: ~0.912


What the Baseline Model Learned

Inspecting learned coefficients reveals several intuitive and non-obvious patterns.

Strong positive indicators:

great, excellent, perfect, wonderful, hilarious, the best, gem

Strong negative indicators:

worst, awful, boring, waste, nothing, disappointing, ridiculous

Beyond obvious sentiment words, the model also learns meta-language patterns:

Words like “still” and “today” appear frequently in positive reviews
(e.g., “it still holds up today”).

Words like “minutes” receive strong negative weights due to phrases such as
“I wasted 90 minutes of my life” or “after 10 minutes I turned it off.”

These patterns indicate that the model captures not only sentiment vocabulary, but also how reviewers describe their viewing experience.

Report and Conclusions
Baseline Wrong / DistilBERT Correct

In the subset where the baseline model misclassified but DistilBERT was correct, reviews were typically long, discursive, and argument-driven. These texts often contained negative language early on but resolved positively after contextual justification. Bag-of-words models fail to capture such long-range discourse structure, while transformer-based models are better suited to handling contextual shifts and contrastive reasoning.

DistilBERT Wrong / Baseline Correct

In the subset where DistilBERT misclassified but the baseline model was correct, reviews were often long but lacked a coherent argumentative structure. These texts frequently resembled stream-of-consciousness rants with dense lexical sentiment and significant topic drift. In such cases, sentiment polarity was conveyed primarily through the frequency of strongly polarized words rather than through structured reasoning. Frequency-based bag-of-words models benefited from this lexical density, while the transformer model appeared vulnerable to semantic dilution and input truncation effects.

Both Models Incorrect

In the subset where both the baseline and transformer models agree yet are incorrect, reviews are often genuinely mixed or neutral in tone. In many such cases, even human evaluation does not clearly map the text to a binary positive or negative category. This suggests that these errors arise primarily from label definition constraints—specifically, the use of rating-based binary labels that exclude neutral sentiment—rather than from insufficient model capacity.

Final Takeaway

This project demonstrates that performance on IMDB sentiment classification is limited not only by model choice, but also by dataset design and label definition. Many remaining errors reflect genuine ambiguity in human language rather than modeling deficiencies. Further improvements would likely require task reformulation (e.g., multi-class or ordinal sentiment) rather than deeper or more complex models.