---
title: "Papers"
permalink: /papers/
author_profile: true
mathjax: true
---

[Preprints](#preprints) · [Publications](#publications) · [Notes](#notes)

## Preprints {#preprints}

- ### <span style="color:#1E90FF; font-weight:bold;">The Inductive Bias of Convolutional Neural Networks: Locality and Weight Sharing Reshape Implicit Regularization
</span>  
  **Tongtong Liang**, Esha Singh, Rahul Parhi, Alexander Cloninger, Yu-Xiang Wang  
  *Manuscript* · 2026  
  <details>
    <summary style="font-weight: bold; color: #0073e6; cursor: pointer;">Abstract</summary>
    <p style="margin-top: 10px; padding-left: 15px;">
      We study how architectural inductive bias reshapes the implicit regularization induced by the edge-of-stability phenomenon in gradient descent. Prior work has established that for fully connected networks, the strength of this regularization is governed solely by the global input geometry; consequently, it is insufficient to prevent overfitting on difficult distributions such as the high-dimensional sphere. In this paper, we show that locality and weight sharing fundamentally change this picture. Specifically, we prove that provided the receptive field size \(m\) remains small relative to the ambient dimension \(d\), these networks generalize on spherical data with a rate of \(n^{-\frac{1}{6} +O(m/d)}\), a regime where fully connected networks provably fail. This theoretical result confirms that weight sharing couples the learned filters to the low-dimensional patch manifold, thereby bypassing the high dimensionality of the ambient space. We further corroborate our theory by analyzing the patch geometry of natural images, showing that standard convolutional designs induce patch distributions that are highly amenable to this stability mechanism, thus providing a systematic explanation for the superior generalization of convolutional networks over fully connected baselines.
    </p>
  </details>  
  [<span style="color:#1E90FF;">arXiv</span>](https://arxiv.org/abs/2603.04807)
  
 - ### <span style="color:#1E90FF; font-weight:bold;">IsoCompute Playbook: Optimally Scaling Sampling Compute for LLM RL
</span>  
  Zhoujun Cheng, Yutao Xie, Yuxiao Qu, Amrith Setlur, Shibo Hao, Varad Pimpalkhute, **Tongtong Liang**, Feng Yao, Zhengzhong Liu, Eric Xing, Virginia Smith, Ruslan Salakhutdinov, Zhiting Hu, Taylor Killian, Aviral Kumar  
  *Manuscript* · 2026  
  <details>
    <summary style="font-weight: bold; color: #0073e6; cursor: pointer;">Abstract</summary>
    <p style="margin-top: 10px; padding-left: 15px;">
      While scaling laws guide compute allocation for LLM pre-training, analogous prescriptions for reinforcement learning (RL) post-training of large language models (LLMs) remain poorly understood. We study the compute-optimal allocation of sampling compute for on-policy RL methods in LLMs, framing scaling as a compute-constrained optimization over three resources: parallel rollouts per problem, number of problems per batch, and number of update steps. We find that the compute-optimal number of parallel rollouts per problem increases predictably with compute budget and then saturates. This trend holds across both easy and hard problems, though driven by different mechanisms: solution sharpening on easy problems and coverage expansion on hard problems. We further show that increasing the number of parallel rollouts mitigates interference across problems, while the number of problems per batch primarily affects training stability and can be chosen within a broad range. Validated across base models and data distributions, our results recast RL scaling laws as prescriptive allocation rules and provide practical guidance for compute-efficient LLM RL post-training.
    </p>
  </details>  
  [<span style="color:#1E90FF;">arXiv</span>](https://arxiv.org/abs/2603.12151)

## Publications {#publications}

- ### <span style="color:#1E90FF; font-weight:bold;">Generalization Below the Edge of Stability: The Role of Data Geometry</span>  
  **Tongtong Liang**, Alexander Cloninger, Rahul Parhi, Yu-Xiang Wang  
  *ICLR 2026* · 2025  
  <details>
    <summary style="font-weight: bold; color: #0073e6; cursor: pointer;">Abstract</summary>
    <p style="margin-top: 10px; padding-left: 15px;">
      Understanding generalization in overparameterized neural networks hinges on the interplay between the data geometry, neural architecture, and training dynamics. In this paper, we theoretically explore how data geometry controls this implicit bias. This paper presents theoretical results for overparameterized two-layer ReLU networks trained *below the edge of stability*. First, for data distributions supported on a mixture of low-dimensional balls, we derive generalization bounds that provably adapt to the intrinsic dimension. Second, for a family of isotropic distributions that vary in how strongly probability mass concentrates toward the unit sphere, we derive a spectrum of bounds showing that rates deteriorate as the mass concentrates toward the sphere. These results instantiate a unifying principle: When the data is harder to "shatter" with respect to the activation thresholds of the ReLU neurons, gradient descent tends to learn representations that capture shared patterns and thus finds solutions that generalize well. On the other hand, for data that is easily shattered (e.g., data supported on the sphere) gradient descent favors memorization. Our theoretical results consolidate disparate empirical findings that have appeared in the literature.
    </p>
  </details>  
  [<span style="color:#1E90FF;">arXiv</span>](https://arxiv.org/abs/2510.18120)

- ### <span style="color:#1E90FF; font-weight:bold;">Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon</span>  
  **Tongtong Liang**, Dan Qiao, Yu-Xiang Wang, Rahul Parhi  
  <em>NeurIPS 2025 (<span style="color:#FF4500; font-weight:bold;">Spotlight</span>)</em> · 2025  
  <details>
   <summary style="font-weight: bold; color: #0073e6; cursor: pointer;">Abstract</summary>
    <p style="margin-top: 10px; padding-left: 15px;">
     We study the implicit bias of flatness / low (loss) curvature and its effects on generalization in two-layer overparameterized ReLU networks with multivariate inputs---a problem well motivated by the minima stability and edge-of-stability phenomena in gradient-descent training. Existing work either requires interpolation or focuses only on univariate inputs. This paper presents new and somewhat surprising theoretical results for multivariate inputs. On two natural settings (1) generalization gap for flat solutions, and (2) mean-squared error (MSE) in nonparametric function estimation by stable minima, we prove upper and lower bounds, which establish that while flatness does imply generalization, the resulting rates of convergence necessarily deteriorate exponentially as the input dimension grows. This gives an exponential separation between the flat solutions compared to low-norm solutions (i.e., weight decay), which are known not to suffer from the curse of dimensionality. In particular, our minimax lower bound construction, based on a novel packing argument with boundary-localized ReLU neurons, reveals how flat solutions can exploit a kind of "neural shattering" where neurons rarely activate, but with high weight magnitudes. This leads to poor performance in high dimensions. We corroborate these theoretical findings with extensive numerical simulations. To the best of our knowledge, our analysis provides the first systematic explanation for why flat minima may fail to generalize in high dimensions.
    </p>
  </details>  
  [<span style="color:#1E90FF;">arXiv</span>](https://arxiv.org/abs/2506.20779)

## Notes {#notes}
- ### <span style="color:#1E90FF; font-weight:bold;">Localization Sequences of Higher Chow Groups of a DVR</span>  
  Tongtong Liang · 2024  
  <details>
    <summary style="font-weight:bold; color:#1E90FF; cursor:pointer;">Abstract</summary>
    <p>
     Levine gave an extension of Bloch's localization theorem for the higher Chow groups to schemes of finite type over a Dedekind domain.In particular, given a discrete valuation field  \((K,v)\) with the valuation ring \(\mathcal{O}_K\) and the residue field \(k\), Levine's localization sequence induces a boundary map \(\mathrm{CH}^n(\mathrm{Spec} K, n)\xrightarrow{\partial}\mathrm{CH}^{n-1}(\mathrm{Spec} k,n-1)\). Using Nesterenko-Suslin's identification \(\mathrm{CH}^n(\mathrm{Spec} F; n)\cong K^M_n(F)\) for any field \(F\), we will show that this boundary map coincides with the residue boundary map \(\partial_v\) in the Milnor K-theories.
    </p>
  </details>  
  [<span style="color:#1E90FF;">PDF</span>](/files/HigherChowGroupsOfDVR.pdf)


- ### <span style="color:#1E90FF; font-weight:bold;">Motivic Multiplicative Structures</span>  
  Tongtong Liang · 2024  
  <details>
    <summary style="font-weight:bold; color:#1E90FF; cursor:pointer;">Abstract</summary>
    <p>
      A reading-style note on multiplicative structures in motivic homotopy theory centered around
      <em>norms</em> (multiplicative transfer) \(p_\otimes\). 
    </p>
  </details>  
  [<span style="color:#1E90FF;">PDF</span>](/files/MotivicMultiplicaitveStructures.pdf)

- ### <span style="color:#1E90FF; font-weight:bold;">Power Operations and Formal Group Laws in Complex Cobordism Theory</span>  
  Tongtong Liang · 2023  
  <details>
   <summary style="font-weight: bold; color: #0073e6; cursor: pointer;">Abstract</summary>
    <p style="margin-top: 10px; padding-left: 15px;">
       This is a survey on Quillen's elementary proofs of some results of cobordism theory using power operations. We optimize the system of notations and clarify some vague arguments in Quillen's paper. Furthermore, we emphasize the relations among cobordism power operations, Landweber-Novikov operations and the formal group law associated to the complex cobordism theory. Particularly, we present a stable-homotopy-theoric construction of cobordism power operations in order to demonstrate the relations. Based on this, we give a different proof of Quillen's technical lemma by promoting a lemma in Rudyak's book from mod-2 case to mod-\(p\) cases for all primes \(p\).

    </p>
  </details>  
  [<span style="color:#1E90FF;">PDF</span>](/files/QuillenSurvey.pdf)

- ### <span style="color:#1E90FF; font-weight:bold;">Obstructions to Realizing Homology Classes by Manifolds</span>  
  Tongtong Liang · 2022  
  <details>
    <summary style="font-weight: bold; color: #0073e6; cursor: pointer;">Abstract</summary>
    <p style="margin-top: 10px; padding-left: 15px;">
      This is a survey on Thom's solution to the Steenrod problem that is asking whether each homology class of a finite complex can be realized as a manifold. In particular, we clarify some vague arguments and calculations in Thom's paper. Following Thom's method, We first show how the problem is translated into a homotopy lifting problem by Thom's construction, then we calculate the obstructions of the corresponding lifting problems in terms of Steenrod operations. This survey aims to understand this method essentially, which is expected to enlighten us to think about how to generalize it to algebraic-geometric setting.
    </p>
  </details>  
  [<span style="color:#1E90FF;">PDF</span>](/files/ThomSurvey.pdf)
