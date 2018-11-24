# Data Set Information:
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult: [Web Link] or the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are many more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.

The UCI Machine Learning Repository's Wine data set measures eleven physicochemical attributes, including the pH and alcohol content, of 1,599 different red wines. Each wine's quality has been scored by human judges. The scores range from zero to ten; zero is the worst quality and ten is the best quality. The data set can be downloaded from https://archive.ics.uci.edu/ml/datasets/Wine

We will approach this problem as a regression task and regress the wine's quality onto one or more physicochemical attributes. 

# Features
The following features are included

1. fixed acidity 
2. volatile acidity 
3. citric acid 
4. residual sugar 
5. chlorides 
6. free sulfur dioxide 
7. total sulfur dioxide 
8. density 
9. pH 
10. sulphates 
11. alcohol 
Output variable (based on sensory data): 
12. quality (score between 0 and 10)

## Aim of Assignment
1. Building a Classification Model
   - Select a method for performing the analytic task.
   - Carry out descriptive summarization of data and make observations.
   - Identify relevant, irrelevant attributes for building model.
2. Evaluate the model.
3. Refine the model, as appropriate
