---
title: "Papers"
permalink: /papers/
author_profile: true
mathjax: true
---

[Preprints](#preprints) · [Publications](#publications) · [Notes](#notes)

## Preprints {#preprints}

- ### <span style="color:#1E90FF; font-weight:bold;">Generalization Below the Edge of Stability: The Role of Data Geometry</span>  
  **Tongtong Liang**, Alexander Cloninger, Rahul Parhi, Yu-Xiang Wang  
  *Manuscript* · 2025  
  <details>
    <summary style="font-weight: bold; color: #0073e6; cursor: pointer;">Abstract</summary>
    <p style="margin-top: 10px; padding-left: 15px;">
      Understanding generalization in overparameterized neural networks hinges on the interplay between the data geometry, neural architecture, and training dynamics. In this paper, we theoretically explore how data geometry controls this implicit bias. This paper presents theoretical results for overparameterized two-layer ReLU networks trained *below the edge of stability*. First, for data distributions supported on a mixture of low-dimensional balls, we derive generalization bounds that provably adapt to the intrinsic dimension. Second, for a family of isotropic distributions that vary in how strongly probability mass concentrates toward the unit sphere, we derive a spectrum of bounds showing that rates deteriorate as the mass concentrates toward the sphere. These results instantiate a unifying principle: When the data is harder to "shatter" with respect to the activation thresholds of the ReLU neurons, gradient descent tends to learn representations that capture shared patterns and thus finds solutions that generalize well. On the other hand, for data that is easily shattered (e.g., data supported on the sphere) gradient descent favors memorization. Our theoretical results consolidate disparate empirical findings that have appeared in the literature.
    </p>
  </details>  
  [<span style="color:#1E90FF;">arXiv</span>](https://arxiv.org/abs/2510.18120)

## Publications {#publications}

- ### <span style="color:#1E90FF; font-weight:bold;">Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon</span>  
  **Tongtong Liang**, Dan Qiao, Yu-Xiang Wang, Rahul Parhi  
  *NeurIPS 2025 (Spotlight)* · 2025  
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
    <summary style="font-weight:bold; color:#1E90FF; cursor:pointer;">Abstract / Outline</summary>
    <p>
      This note rederives the boundary map in Levine’s localization sequence for a discrete valuation
      field \((K,v)\) with valuation ring \(\mathcal O_K\) and residue field \(k\):
      \[
      \partial:\ \mathrm{CH}^n(\mathrm{Spec}\,K,n)\longrightarrow \mathrm{CH}^{n-1}(\mathrm{Spec}\,k,n-1).
      \]
      Using the Nesterenko–Suslin/Totaro identification \(\mathrm{CH}^n(\mathrm{Spec}\,F,n)\cong K^M_n(F)\),
      it is shown that \(\partial\) coincides with the Milnor \(K\)-theory residue map
      \(\partial_v:K^M_n(K)\to K^M_{n-1}(k)\).
      The proof gives an explicit cycle-level computation: a symbol \(\{t,u_2,\dots,u_n\}\) corresponds to
      a zero-cycle \(W_u\subset \Delta^n_K\); after taking closure in \(\Delta^n_{\mathcal O_K}\), one checks
      face intersections in two cases \(v(\lambda_u)=0\) and \(v(\lambda_u)>0\), recovering
      \(\{ \overline{u}_2,\dots,\overline{u}_n\}\) or \(0\) respectively.
      As a consequence, \(\mathrm{CH}^n(\mathcal O_K,n)=\ker(\partial_v)\) and
      \(\mathrm{CH}^n(\mathcal O_K,n-1)=\mathrm{coker}(\partial_v)=0\); an application reformulates
      these results in motivic cohomology, yielding for \(p\)-adic \(K\) the comparison
      \(H^{i+1}(\mathcal O_K;\mathbb F_p(j-1))\cong H^{i+1}(K;\mathbb F_p(j))\) when \(i>j\). :contentReference[oaicite:0]{index=0}
    </p>
  </details>  
  [<span style="color:#1E90FF;">PDF</span>](/files/HigherChowGroupsOfDVR.pdf)


- ### <span style="color:#1E90FF; font-weight:bold;">Motivic Multiplicative Structures</span>  
  Tongtong Liang · 2024  
  <details>
    <summary style="font-weight:bold; color:#1E90FF; cursor:pointer;">Abstract / Outline</summary>
    <p>
      A reading-style note on multiplicative structures in motivic homotopy theory centered around
      <em>norms</em> (multiplicative transfer) \(p_\otimes\). It explains how, for an integral universally
      open morphism \(p:T\to S\), one constructs a symmetric monoidal functor
      \(p_\otimes:\mathsf{H}^\bullet(T)\to \mathsf{H}^\bullet(S)\) that preserves sifted colimits and
      extends \(p_+\), and tracks this construction across levels:
      unbased/based presheaves \(\to\) motivic spaces \(\to\) motivic spectra.
      The note then organizes the coherence data of motivic norms via span categories
      (comparing “\(E_\infty\)-operadic” structure vs. “universal normed” structure),
      and introduces the <em>category of normed motivic spectra</em> with its functorial properties.
      A final section recalls norms in equivariant homotopy theory for comparison, and an Appendix
      reviews Galois descent (vector spaces, quasi-coherent sheaves, schemes) to support base-change
      considerations in the motivic context.
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
