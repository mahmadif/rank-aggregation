# Bradley-Terry-Luce (BTL)

The Bradley-Terry-Luce (BTL) model is well-known in the literature on discrete choice (Bradley & Terry, 1952). It starts from the parametric model of pairwise comparisons:

<img src="https://latex.codecogs.com/gif.latex?\mathbb{P}(&space;\textbf{x}_i&space;\succ&space;\textbf{x}_j&space;)&space;=&space;\dfrac{&space;\theta_i&space;}{&space;\theta_i&space;&plus;&space;\theta_j&space;}&space;\,&space;." title="\mathbb{P}( \textbf{x}_i \succ \textbf{x}_j ) = \dfrac{ \theta_i }{ \theta_i + \theta_j } \, ." />

Given `n x n` matrix `C` of pairwise comparisons, where `C[i,j]` informs about how often the item `x_i` wins over `x_j`, the parameters can be estimated by likelihood maximization:

<img src="https://latex.codecogs.com/gif.latex?\hat{\theta}&space;\in&space;\arg&space;\max_{\theta&space;\in&space;\mathbb{R}^{n}&space;}&space;\prod_{1&space;\leq&space;i&space;\neq&space;j&space;\leq&space;n}&space;\left(&space;\dfrac{\theta_{i}}{\theta_{i}&space;&plus;&space;\theta_{j}}&space;\right)^{c_{i,j}}&space;\,&space;." title="\hat{\theta} \in \arg \max_{\theta \in \mathbb{R}^{n} } \prod_{1 \leq i \neq j \leq n} \left( \dfrac{\theta_{i}}{\theta_{i} + \theta_{j}} \right)^{c_{i,j}} \, ." />

Check out [this work](http://proceedings.mlr.press/v70/fahandar17a/fahandar17a.pdf) for more information.
