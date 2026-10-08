---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html

---
I am a PhD student in the Department of Mathematics at [UC San Diego](https://ucsd.edu/) (since 2023), working with Prof. [Alex Cloninger](https://sites.google.com/ucsd.edu/alexandercloninger/home), Prof. [Rahul Parhi](https://sparsity.ucsd.edu/rahul/), and Prof. [Yu-Xiang Wang](https://cseweb.ucsd.edu/~yuxiangw/) on deep learning research. I received both my B.S. and M.S. degrees in Mathematics from [Southern University of Science and Technology](https://www.sustech.edu.cn/en/), where I was advised by Prof. [Yifei Zhu](https://yifeizhu.github.io/).

My research focuses on understanding **how training organizes information from data into parameterized computational structures**. My goal is to use this understanding to develop better neural architectures and training methods for foundation models.

My work on [neural shattering](https://arxiv.org/abs/2506.20779), [data geometry](https://arxiv.org/abs/2510.18120), and [sparse connectivity](https://arxiv.org/abs/2603.04807) examines how data geometry and network structure shape the implicit bias of gradient descent. Extending this perspective to the design of generative models, my recent work on [residual-stream burden](https://tongtongliang.github.io/residual-stream-burden/) investigates how prediction objectives and architecture jointly shape the representations learned by diffusion Transformers, and turns these findings into concrete architectural improvements.

Papers
======
{% for paper in site.data.papers %}
{% include paper-entry.html paper=paper %}
{% endfor %}
