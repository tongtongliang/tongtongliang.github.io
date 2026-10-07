---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html

---
I am a PhD student in the Department of Mathematics at [UC San Diego](https://ucsd.edu/) (since 2023), working with Prof. [Alex Cloninger](https://sites.google.com/ucsd.edu/alexandercloninger/home), Prof. [Rahul Parhi](https://sparsity.ucsd.edu/rahul/), and Prof. [Yu-Xiang Wang](https://cseweb.ucsd.edu/~yuxiangw/) on deep learning research. I received both my B.S. and M.S. degrees in Mathematics from [Southern University of Science and Technology](https://www.sustech.edu.cn/en/), where I was advised by Prof. [Yifei Zhu](https://yifeizhu.github.io/).

I aim to develop general design principles for generative AI by understanding how data, architecture, and optimization jointly shape what neural networks learn.

Papers
======
{% for paper in site.data.papers %}
{% include paper-entry.html paper=paper %}
{% endfor %}
