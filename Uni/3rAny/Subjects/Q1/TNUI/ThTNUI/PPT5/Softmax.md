Funció per passar de valoració (score) a probabilitat

$$
softmax(z) = \frac{e^z}{\sum_{j=0}^{K-1}e^{z_j}}
$$

```python
 import math
 z = [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0]
 z_exp = [math.exp(i) for i in z]
 sum_z_exp = sum(z_exp)
 softmax = [round(i / sum_z_exp, 3) for i in z_exp]
 print(softmax)
```
```
>>>[0.024, 0.064, 0.175, 0.475, 0.024, 0.064, 0.175]
```



## Preliminary: Cross-Entropy

**Example**: Binary (two-classes) Cross-Entropy Loss function.

Given a dataset \((\mathbf x_i, y_i)\) with \(n\) samples, with features \(\mathbf x \in \mathbb R^m\), and labels \(y \in \{0,1\}\), the cross-entropy loss is defined as:

$$
CE = - \frac{1}{n} \sum_{i=1}^n (y_i \log(\hat y_i) + (1-y_i) \log(1- \hat y_i))
$$

where \(\hat y\) is the predicted probability for class `1` and \(1- \hat y\) is the predicted probability for class `0`.

## Preliminary: Cross-Entropy

**Example**: Binary Cross-Entropy.

```python
import numpy as npdef b_cross_entropy_loss(yHat, y):    if y == 1:      return -np.log(yHat)    else:      return -np.log(1 - yHat) b_cross_entropy_loss(0.99, 1)>>> 0.01005033585350145b_cross_entropy_loss(0.01, 1)>>> 4.605170185988091
```

## Preliminary: Cross-Entropy



## Preliminary: Cross-Entropy

**Example**: Multiclass Cross-Entropy.

Given a dataset \((\mathbf x_i, y_i)\) with \(n\) samples, with features \(\mathbf x \in \mathbb R^m\), and labels \(y \in \{1,2,\dots, K\}\), the cross-entropy loss is defined as

\[CE = - \frac{1}{n} \sum_{i=1}^n \sum_{j=1}^K y^j_i \log(\hat y^j_i)\]

Here, \(y^j\) is \(0\) or \(1\), indicating whether \(j\) is the correct classification of \(\mathbf x\) and \(\hat y^j\) is the predicted probability of class \(j\) for \(\mathbf x\).

- Binary cross entropy corresponds to the case \(K=2\).

## Preliminary: Cross-Entropy

```python
from math import log2 def cross_entropy(p, q): return -sum([p[i]*log2(q[i]) for i in range(len(p))]) p = [0.10, 0.40, 0.50]q = [0.80, 0.15, 0.05]ce_pp = cross_entropy(p, p)ce_qq = cross_entropy(q, q) > ce_pp: 1.361 bits> ce_qq: 0.884 bits
```

## Matrix Factorization for Recommenders

The intuition behind using matrix factorization to solve the recommendation problem is that there should be some **latent features** that determine how a user rates an item. These latent features can be used for representing users **and** items.

- For example, two users would give high ratings to a certain movie if they both like the **actors/actresses** (latent factor) of the movie, or if the movie is an **action** movie (latent factor), which is a genre preferred by both users.

## Matrix Factorization for Recommenders

Hence, if we can discover these latent features, we should be able to predict a rating with respect to a certain user and a certain item, because the features associated with the user should match (are similar) with the features associated with the item.

In trying to discover the different features, we also make the assumption that the number of features would be smaller than the number of users and the number of items.

### The mathematics of matrix factorization

We have a set \(U\) of users, and a set \(D\) of items. Let \(\mathbf{R}\) of size \(|U| \times |D|\) be the matrix that contains all the ratings that the users have assigned to the items.

**Definition:** Our task, then, is to find two matrices \(\mathbf{P}\) (a \(|U| \times K\) matrix) and \(\mathbf{Q}\) (a \(|D| \times K\) matrix), \(K \ll |U|\) and \(K \ll |D|\), such that their product approximates \(\mathbf{R}\):

\[ \mathbf{P} \times \mathbf{Q}^T = \hat{\mathbf{R}} \approx \mathbf{R} \]

### Features

![](https://i.imgur.com/AcE3ceS.png)

### Features

In this way, each row of \(\mathbf{P}\) would represent the strength of the associations between a user and the features.

Similarly, each row of \(\mathbf{Q}\) would represent the strength of the associations between an item and the features.

To get the prediction of a rating of an item \(d_j\) by \(u_i\), we calculate the dot product of the two vectors corresponding to \(u_i\) and \(d_j\):

\[\hat{r}_{ij} = \mathbf p_i^T \mathbf q_j = \sum_{k=1}^k{p_{ik}q_{kj}}\]

### Optimization

Now, we have to find a way to obtain \(\mathbf{P}\) and \(\mathbf{Q}\) from a very large matrix \(\mathbf{R}\).

- One way to approach this problem is the first initialize the two matrices with some random values, calculate how _different_ their product is to the known values of \(\mathbf{R}\), and then try to minimize this difference iteratively (_gradient descend_).
    
- The difference here, usually called the **error** between the estimated rating and the real rating, can be calculated by the following equation for each known user-item pair \((i,j)\):
    

\[ e_{ij}^2 = (r_{ij} - \hat{r}_{ij})^2 = (r_{ij} - \sum_{k=1}^K{p_{ik}q_{kj}})^2 \]

## Partial derivatives

To minimize the error, we differentiate the above equation with respect to these two variables separately:

\[ \frac{\partial}{\partial p_{ik}} e_{ij}^2 = -2(r_{ij} - \hat r_{ij})(q_{kj}) = -2e_{ij}q_{kj}\]

\[ \frac{\partial}{\partial q_{ik}} e_{ij}^2 = -2(r_{ij} - \hat r_{ij})(p_{kj}) = -2e_{ij}p_{kj}\]

Code Example:

- [Notebook](https://colab.research.google.com/drive/1Qk7fIvkUqz0MDK02BiRbpWjcagE60XVB?usp=sharing)

## Factorization Machines

## Factorization Machines

The matrix factorization (MF) formulation breaks down when dealing with implicit feedback data, where you do not directly observe **any explicit** numerical ratings or positive/negative responses, but rather only **implicit** ratings that can be inferred from raw user behavior (e.g. watches, page views, purchases,clicks).

Moreover, consider how most recommendations are actually served to users: as one or more **ordered lists of items**. Intuitively, the true objective should, therefore, be to derive the correct rank-ordering of items for each user.

## Factorization Machines

To overcome MF limitations we need a more general model framework that can extend the latent factor approach to incorporate **arbitrary auxiliary features** to represent users and items, and **specialized loss functions** that directly optimize item rank-order using implicit feedback data.

This is the role of **factorization machines.**

## Factorization Machines

In FM the base features \(\mathbf x\) will be binary vectors of user and item indicators, such that each training sample has exactly two non-zero entries corresponding to the given user/item combination.

However, these user/item indicators can be augmented with arbitrary auxiliary features, for example, user or item attributes and/or contextual features relevant to the interaction itself (e.g. day-of-week, add-to-cart order, etc.).

Observed ratings can be implicit or explicit.

## Factorization Machines

![](https://i.imgur.com/c8zqf4z.png)

FM models work with categorical data represented as binary integers. Auxiliary features **must be represented by a one-hot encoding**.

## Factorization Machines

The FM model equation is comprised of \(2\)-way interactions between features that includes weights for each base feature as well as interaction terms for each pairwise feature combination.

Formally, let \(\mathbf x \in \mathbb{R}^d\) denote the feature vectors of one sample, and \(𝑦\) denote the corresponding label which can be real-valued label or class label such as binary class “click/non-click”. The model for a factorization machine of degree two is defined as:

\[\hat{y}(x) = {w}_0 + \sum_{i=1}^d \mathbf{w}_i x_i + \sum_{i=1}^d\sum_{j=i+1}^d \mathbf W_{ij} x_i x_j\]

where \({w}_0 \in \mathbb{R}\) is the global bias; \(\mathbf{w} \in \mathbb{R}^d\) denotes the feature weights, and \(\mathbf{W} \in \mathbb{R}^{d \times d}\) represents the weights of the feature pair interactions.

## Factorization Machines

Example:

\[ \begin{bmatrix} u_1 & u_2 & u_3 & i_1 & i_2 & i_3 & c_1 & c_2 & c_3 & y\\ 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & y_1 \\ 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & y_2 \\ & & & & \dots & & & & & \\ 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & y_n \\ \end{bmatrix} \]

\[ y_1 = w_0 + \mathbf w_1 + \mathbf w_6 + \mathbf w_8 +\mathbf W_{1,6} + \mathbf W_{1,8} + \mathbf W_{6,8}\]

where \(\mathbf w_1 \in \mathbb{R}\) is the weight of the first user, \(\mathbf W_{1,6} \in \mathbb{R}\) is the weight corresponding to the interaction user-item, \(\mathbf W_{1,8} \in \mathbb{R}\) is the weight corresponding to the interaction user-context, and \(\mathbf W_{6,8} \in \mathbb{R}\) is the weight corresponding to the interaction item-context.

## Factorization Machines

Compared to our previous model, this formulation has the advantages that it can capture feature interactions at least for two features at a time.

But we have now ended up with a \(𝑂(d^2)\) parameters which means that to train the model, we now require a lot more time and memory.

## Factorization Machines

To solve this problem, FMs instead use **factorized interaction** parameters: feature interaction weights are represented as the inner product of the two features’ latent factor space embeddings:

\[ \hat{y}(x) = {w}_0 + \sum_{i=1}^d \mathbf{w}_i x_i + \sum_{i=1}^d\sum_{j=i+1}^d (\mathbf{v}^T_i \mathbf{v}_j) x_i x_j \]

This greatly decreases the number of parameters to estimate. Consider a realistic recommendation data set with \(10^6\) users and \(10^5\) items. A quadratic linear model would need to estimate ~\(10^{10}\) parameters. A FM model of dimension \(10\) would need only \(10^6\) parameters.

## Optimization

However, it’s not immediately obvious how to adapt FM models for implicit feedback data. One naïve approach would be to label all observed user-item interactions as `1` and all unobserved interactions as `0` and train the model using a common classification loss function.

But with real-world recommendation data sets this would require the creation of billions of unobserved user-item training samples and result in a severe class imbalance due to interaction sparsity.

The solution is to learn **rank-order** directly instead of minimizing prediction error by using loss functions that are based on the relative ordering of items instead of their raw scores.

## Optimization

**Bayesian Personalized Ranking** (BPR) from Implicit Feedback, provides a method to implement this approach.

In BPR, instead of taking one item, item pairs will be considered as training data. Optimization would be performed based on the rank of these user-item pairs instead of scoring just on the user-item interaction.

The dataset that would be considered is formulated as follows:

\[D = \{(u,i,j)\} \]

where each triplet represents: "user \(u\) is assumed to prefer item \(i\) over item \(j\)".

## Optimization

# ![](https://hackmd.io/_uploads/HklNx_Byye.png)

In the above figure, user \(u_1\) has viewed item \(i_2\) but not item \(i_1\), so the algorithm assumes that this user prefers item \(i_2\) over \(i_1\),\(( i_2 > i_1)\), and gives a positive sign.

No inference can be made about a preference for items that were both been seen by a user and is shown as \(?\) mark.

## Optimization

# ![](https://hackmd.io/_uploads/HklNx_Byye.png)

The same is true for two items that a user has not seen yet (e.g. item \(i_1\) and \(i_4\) for user \(u_1\)).

On contrary, you can observe a negative sign for \((i_1,j_2)\) as user prefers \(i_2\) over \(i_1\).

## Optimization

The BPR loss function is:

\[\sum_{(u, i, j) \in D} - \ln \sigma(\hat{y}_{ui} - \hat{y}_{uj})\]

where \(\sigma=\frac{1}{(1-e^{-x})}\) is the sigmoid function and \(\hat{y}_{ui}\) and \(\hat{y}_{uj}\) are the (FM) predicted scores of the user \(u\) to (seen) item \(i\) and (unseen) item \(j\), respectively.

This function has a minimum when, for every user \(u\), seen items have a higher score than unseen items: \(\hat{y}_{ui} - \hat{y}_{uj} > 0\).

This is a classification loss function that can be minimized with a SGD estrategy.

## The sigmoid function

![](https://i.imgur.com/P1P41yz.png)

## Session-based Recommenders

Font: https://session-based-recommenders.fastforwardlabs.com/

At a high level, **content-based filtering** makes recommendations based on user preferences for product features, as identified through either the user’s previous actions or explicit feedback.

**Collaborative filtering**, on the other hand, utilizes user-item interactions across a population of users in order to make recommendations for one particular user, based on the preferences of other, very similar users (where similar users are identified by the items they have liked, read, bought, watched, etc.).

## Session-based Recommenders

The underlying **assumption** in both of these systems is that **all of the historical interactions are equally important to the user’s current preference**, but in reality, this may not be true.

A user’s choice of items not only depends on long-term historical preference, but also on short-term and more recent preferences.

### Sessions

For instance, “recently viewed” or “recently purchased” items may actually be more relevant than others.

In addition, a user’s preference towards certain items can tend to be dynamic rather than static; it often evolves over time.

![](https://i.imgur.com/tf6KF84.png)

### Sessions

These considerations have prompted the exploration and development of a new type of recommendation system: known as **session-based recommendation** systems.

These systems rely heavily on the user’s most recent interactions, rather than on the user’s historical preferences.

### Example

Let’s say we own a popular online shopping website for workout accessories. Rhonda, a new customer, has been browsing tops, shoes, and weights. Her browsing history looks like this:

![](https://i.imgur.com/8Yjcgpm.png)

What should we recommend to her next?

### Next event prediction

We’ll consider Rhonda’s recent browsing history as a **session**.

- Formally, a session is composed of multiple user interactions that happen together in a continuous period of time—for instance, products purchased in a single transaction. Sessions can occur on the same day, or across several days, weeks, or months.

Our goal is to predict the product within Rhonda’s session that she will like enough to click on. This task is called **next event prediction (NEP)**: given a series of events (Rhonda’s browsing history), we want to predict the next event (Rhonda clicking on a product we recommend to her).

- In reality, this means that our model might generate a handful of recommendations based on Rhonda’s browsing history; we want to maximize the likelihood that Rhonda clicks on at least one of them.

### Next event prediction

To train a model for this task, we’ll need to use historical browsing sessions from our other existing users to identify trends between products that will help us learn recommendations.

### Data

# ![](https://i.imgur.com/rW3lDsV.png)

[4](#/3)
```