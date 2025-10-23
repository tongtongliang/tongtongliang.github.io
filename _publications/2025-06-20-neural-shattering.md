---
title: "Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon"
collection: publications
permalink: /publication/neural-shattering
date: 2025-06-20
venue: "NeurIPS 2025 (Spotlight)"
authors: "Tongtong Liang, Dan Qiao, Yu-Xiang Wang, Rahul Parhi"
paperurl: "https://arxiv.org/abs/2506.20779"
category: conferences
selected: true
---

<span style="color:#00629B; font-weight:600;">
Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon
</span>  
**Tongtong Liang**, Dan Qiao, Yu-Xiang Wang, Rahul Parhi  
*NeurIPS 2025* <span style="color:#C69214; font-size: 12pt;">Spotlight</span> · [arXiv](https://arxiv.org/abs/2506.20779)

We study the implicit bias of flatness / low (loss) curvature and its effects on generalization in two-layer overparameterized ReLU networks with multivariate inputs---a problem well motivated by the minima stability and edge-of-stability phenomena in gradient-descent training. Existing work either requires interpolation or focuses only on univariate inputs. This paper presents new and somewhat surprising theoretical results for multivariate inputs. On two natural settings (1) generalization gap for flat solutions, and (2) mean-squared error (MSE) in nonparametric function estimation by stable minima, we prove upper and lower bounds, which establish that while flatness does imply generalization, the resulting rates of convergence necessarily deteriorate exponentially as the input dimension grows. This gives an exponential separation between the flat solutions compared to low-norm solutions (i.e., weight decay), which are known not to suffer from the curse of dimensionality. In particular, our minimax lower bound construction, based on a novel packing argument with boundary-localized ReLU neurons, reveals how flat solutions can exploit a kind of ``neural shattering'' where neurons rarely activate, but with high weight magnitudes. This leads to poor performance in high dimensions. We corroborate these theoretical findings with extensive numerical simulations. To the best of our knowledge, our analysis provides the first systematic explanation for why flat minima may fail to generalize in high dimensions.
