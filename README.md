# Game_recommender
A game recommender system using collaborative filtering from scratch using pandas and numpy. The model is trained on users' playtime on games based on the dataset provided from https://cseweb.ucsd.edu/~jmcauley/datasets.html. 

The raw dataset is processed and transformed into a usable format to be used to train the model.

User can input their user ID and key to obtain their actual top 20 games and the top 20 games predicted by the model.

Problems: Since the playtime of certain games such as Counter Strike: Golbal Offensive have much higher playtimes among users than other games, so the model will identify those games have higher playtime than other games, which gives an unaccurate prediction.

Solution: Using a dataset which consist of users' rating of the games in stead of their playtime can prevent the model skewed towards high average playtime games having high playtimes on everyone. 

Lesson: The quality of the dataset determines the quality of the model.