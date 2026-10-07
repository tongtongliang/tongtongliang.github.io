---
title: "Papers"
permalink: /papers/
author_profile: true
mathjax: true
redirect_from:
  - /publications/
  - /publication/generalization-geometry
  - /publication/neural-shattering
---

[Preprints](#preprints) · [Publications](#publications) · [Notes](#notes)

## Preprints {#preprints}
{% for paper in site.data.papers %}
{% if paper.section == 'preprints' %}
{% include paper-entry.html paper=paper detailed=true %}
{% endif %}
{% endfor %}

## Publications {#publications}
{% for paper in site.data.papers %}
{% if paper.section == 'publications' %}
{% include paper-entry.html paper=paper detailed=true %}
{% endif %}
{% endfor %}

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
