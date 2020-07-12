# Bradley-Terry-Luce (BTL)

The Bradley-Terry-Luce (BTL) model is well-known in the literature on discrete choice (Bradley & Terry, 1952). It starts from the parametric model of pairwise comparisons:

<img src="https://latex.codecogs.com/png.latex?\mathbb{P}(&space;\boldsymbol{x}_i&space;\succ&space;\boldsymbol{x}_j&space;)&space;=&space;\dfrac{&space;\theta_i&space;}{&space;\theta_i&space;&plus;&space;\theta_j&space;}&space;\,&space;." title="\mathbb{P}( \boldsymbol{x}_i \succ \boldsymbol{x}_j ) = \dfrac{ \theta_i }{ \theta_i + \theta_j } \, ." />

Given `n x n` matrix `C` of pairwise comparisons, where `C[i,j]` informs about how often the item `x_i` wins over `x_j`, the parameters 

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{100}&space;\bg_white&space;\large&space;\boldsymbol{\theta}&space;=&space;(&space;\theta_1,&space;\theta_2,&space;\dots,&space;\theta_n&space;)&space;\in&space;\mathbb{R}^n_&plus;&space;\,&space;," title="\large \boldsymbol{\theta} = ( \theta_1, \theta_2, \dots, \theta_n ) \in \mathbb{R}^n_+ \, ," />

can be estimated by likelihood maximization:

<img src="https://latex.codecogs.com/pdf.latex?\dpi{100}&space;\large&space;\hat{&space;\boldsymbol{\theta}&space;}&space;\in&space;\underset{{&space;\boldsymbol{\theta}&space;\in&space;\mathbb{R}^{n}&space;}}{\arg&space;\max}&space;\prod_{1&space;\leq&space;i&space;\neq&space;j&space;\leq&space;n}&space;\left(&space;\dfrac{\theta_{i}}{\theta_{i}&space;&plus;&space;\theta_{j}}&space;\right)^{c_{i,j}}&space;\,&space;," title="\large \hat{ \boldsymbol{\theta} } \in \underset{{ \boldsymbol{\theta} \in \mathbb{R}^{n} }}{\arg \max} \prod_{1 \leq i \neq j \leq n} \left( \dfrac{\theta_{i}}{\theta_{i} + \theta_{j}} \right)^{c_{i,j}} \, ," />

the implementation of which is placed in `BTL.py`. Check out [this work](http://proceedings.mlr.press/v70/fahandar17a/fahandar17a.pdf) for more details.
