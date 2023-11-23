# Recipe recommendation

**Overview**
RECIPES RECOMENDATION - project aims to enhance the culinary experience by providing users with personalized suggestions for recipes similar to those they have shown interest in. Leveraging advanced natural language processing techniques and machine learning, this system recommends recipes that share textual similarities with the user's preferred recipes. 

During the development of the project, 4 models were created to compare and select the best 
*(models.py)*

*WordsComparison Model:*

Uses NLTK for lemmatization and stop words removal.
Computes the number of matching unique words between a query object and each row in the dataset.
Returns indices of rows with the highest number of matching words.

*TfidfSimilarity Model:*

Combines word-level and character-level TF-IDF representations.
Utilizes cosine similarity to measure the likeness between a query object and the entire dataset.
Returns indices of rows with the highest similarity scores.

*ObjectsTextSimilarity Model:*

Employs Sentence Transformer for text embedding.
Concatenates embeddings of different text features to create a representation for each object.
Utilizes cosine similarity to find the most similar objects to a query.

*ObjectsSimilarityFiltered Model:*

Similar to ObjectsTextSimilarity but with an additional filtering step.
Filters similar objects based on specific features and their values.
