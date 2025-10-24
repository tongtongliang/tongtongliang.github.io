---
title: "Papers"
permalink: /papers/
layout: single
author_profile: true
---

<!-- 页内导航 -->
<div style="text-align:center; margin-bottom: 1.5rem;">
  <a href="#preprints" style="margin:0 1rem; color:#1E90FF; text-decoration:none; font-weight:600;">Preprints</a> |
  <a href="#publications" style="margin:0 1rem; color:#1E90FF; text-decoration:none; font-weight:600;">Publications</a> |
  <a href="#notes" style="margin:0 1rem; color:#1E90FF; text-decoration:none; font-weight:600;">Notes</a>
</div>

<!-- 局部样式 -->
<style>
  .papers .item { margin: 1.0rem 0 1.2rem; }
  .papers .title { font-weight: 600; font-size: 1.05rem; }
  .papers .title a { color: #1E90FF; text-decoration: none; }
  .papers .meta { color: #5f6b7a; margin-top: 0.2rem; }
  .papers .links a { margin-right: .8rem; text-decoration: none; }
  .papers details { margin-top: .35rem; }
  .papers summary { cursor: pointer; color: #1E90FF; font-weight: 600; }
  .papers img { width: 500px; max-width: 100%; display:block; margin:.3rem 0; }
</style>

<div class="papers">

## <a id="preprints"></a>Preprints

<div class="item">
  <div class="title">
    <a href="https://arxiv.org/abs/2510.18120">Generalization Below the Edge of Stability: The Role of Data Geometry</a>
  </div>
  <div class="meta">
    <strong>Tongtong Liang</strong>, Alexander Cloninger, Rahul Parhi, Yu-Xiang Wang<br>
    <em>Manuscript</em> · 2025
  </div>
  <div class="links">
    <a href="https://arxiv.org/abs/2510.18120">arXiv</a>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abs">
     Understanding generalization in overparameterized neural networks hinges on the interplay between the data geometry, neural architecture, and training dynamics. In this paper, we theoretically explore how data geometry controls this implicit bias. This paper presents theoretical results for overparameterized two-layer ReLU networks trained below the edge of stability. First, for data distributions supported on a mixture of low-dimensional balls, we derive generalization bounds that provably adapt to the intrinsic dimension. Second, for a family of isotropic distributions that vary in how strongly probability mass concentrates toward the unit sphere, we derive a spectrum of bounds showing that rates deteriorate as the mass concentrates toward the sphere. These results instantiate a unifying principle: When the data is harder to "shatter" with respect to the activation thresholds of the ReLU neurons, gradient descent tends to learn representations that capture shared patterns and thus finds solutions that generalize well. On the other hand, for data that is easily shattered (e.g., data supported on the sphere) gradient descent favors memorization. Our theoretical results consolidate disparate empirical findings that have appeared in the literature.
    </div>
  </details>
</div>

---

## <a id="publications"></a>Publications

<div class="item">
  <div class="title">
    <a href="https://arxiv.org/abs/2506.20779">Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon</a>
  </div>
  <div class="meta">
    <strong>Tongtong Liang</strong>, Dan Qiao, Yu-Xiang Wang, Rahul Parhi<br>
    <em>NeurIPS 2025 (Spotlight)</em> · 2025
  </div>
  <div class="links">
    <a href="https://arxiv.org/abs/2506.20779">arXiv</a>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abs">
  We study the implicit bias of flatness / low (loss) curvature and its effects on generalization in two-layer overparameterized ReLU networks with multivariate inputs---a problem well motivated by the minima stability and edge-of-stability phenomena in gradient-descent training. Existing work either requires interpolation or focuses only on univariate inputs. This paper presents new and somewhat surprising theoretical results for multivariate inputs. On two natural settings (1) generalization gap for flat solutions, and (2) mean-squared error (MSE) in nonparametric function estimation by stable minima, we prove upper and lower bounds, which establish that while flatness does imply generalization, the resulting rates of convergence necessarily deteriorate exponentially as the input dimension grows. This gives an exponential separation between the flat solutions compared to low-norm solutions (i.e., weight decay), which are known not to suffer from the curse of dimensionality. In particular, our minimax lower bound construction, based on a novel packing argument with boundary-localized ReLU neurons, reveals how flat solutions can exploit a kind of "neural shattering" where neurons rarely activate, but with high weight magnitudes. This leads to poor performance in high dimensions. We corroborate these theoretical findings with extensive numerical simulations. To the best of our knowledge, our analysis provides the first systematic explanation for why flat minima may fail to generalize in high dimensions.
    </div>
  </details>
</div>

---

## <a id="notes"></a>Notes

<div class="item">
  <div class="title">
    <a href="/files/QuillenSurvey.pdf" style="color:#1E90FF; text-decoration:none; font-weight:600;">
      Power Operations and Formal Group Laws in Complex Cobordism Theory
    </a>
  </div>
  <div class="meta">Tongtong Liang · 2022</div>
  <details>
    <summary>Abstract / Outline</summary>
    <div class="abs">
      A survey of Quillen’s elementary approach to complex cobordism, focusing on how power operations
      and Landweber–Novikov operations interact to control the formal group law for \(MU\).
      The note streamlines notation, clarifies arguments in Quillen’s papers, and highlights two ideas:
      a Riemann–Roch–type formula with fixed-point localization that links cobordism power operations
      to Landweber–Novikov operations, and a homotopical construction of power operations via an
      \(H^\infty\)-structure on \(MU\). It also promotes a lemma of Rudyak from mod-2 to mod-\(p\) to prove
      a technical step toward the structure theorem, showing \(U^*(X)\) is generated over the coefficient
      ring determined by the formal group law.
    </div>
  </details>
</div>

<div class="item">
  <div class="title">
    <a href="/files/ThomSurvey.pdf" style="color:#1E90FF; text-decoration:none; font-weight:600;">
      Obstructions to Realizing Homology Classes by Manifolds
    </a>
  </div>
  <div class="meta">Tongtong Liang · 2022</div>
  <details>
    <summary>Abstract / Outline</summary>
    <div class="abs">
      A survey of Thom’s solution to the Steenrod problem: translating the realization of a class
      in \(H_k(X)\) by a submanifold into a homotopy lifting problem \(X \to MO(k)\) (or \(MSO(k)\) in
      the oriented case). The note develops the cohomology of \(MO(k)\) with Steenrod algebra action,
      uses Wu’s formula and admissible Sq-bases, applies Whitehead’s theorem to identify the relevant
      Postnikov truncations, and derives the dimension bounds (e.g., realizability when \(k \le n/2\))
      and a proof of the unoriented Steenrod theorem for finite polyhedra via embeddings and retracts.
    </div>
  </details>
</div>

