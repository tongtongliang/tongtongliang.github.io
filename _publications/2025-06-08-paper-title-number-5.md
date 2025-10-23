---
title: "Generalization Below the Edge of Stability: The Role of Data Geometry"
collection: publications
permalink: /publication/generalization-geometry
date: 2025-10-18
venue: "Manuscript"
authors: "Tongtong Liang, Alexander Cloninger, Rahul Parhi, Yu-Xiang Wang"
paperurl: "https://arxiv.org/abs/2510.18120"
category: manuscripts
selected: true
---

<span style="color:#00629B; font-weight:600;">
Generalization Below the Edge of Stability: The Role of Data Geometry
</span>  
**Tongtong Liang**, Alexander Cloninger, Rahul Parhi, Yu-Xiang Wang  
*Manuscript* · [arXiv](https://arxiv.org/abs/2510.18120)

Understanding generalization in overparameterized neural networks hinges on the interplay between the data geometry, neural architecture, and training dynamics. In this paper, we theoretically explore how data geometry controls this implicit bias. This paper presents theoretical results for overparameterized two-layer ReLU networks trained \emph{below the edge of stability}. First, for data distributions supported on a mixture of low-dimensional balls, we derive generalization bounds that provably adapt to the intrinsic dimension. Second, for a family of isotropic distributions that vary in how strongly probability mass concentrates toward the unit sphere, we derive a spectrum of bounds showing that rates deteriorate as the mass concentrates toward the sphere. These results instantiate a unifying principle: When the data is harder to ``shatter'' with respect to the activation thresholds of the ReLU neurons, gradient descent tends to learn representations that capture shared patterns and thus finds solutions that generalize well. On the other hand, for data that is easily shattered (e.g., data supported on the sphere) gradient descent favors memorization. Our theoretical results consolidate disparate empirical findings that have appeared in the literature.
