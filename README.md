# My Journey into Computer Vision

### My Architecture Background
After being in the architecture industry for a couple years, I started feeling uneasy to continue the career trajectory I had planned for myself. I was coming to some difficult realizations: much of my work as an architect can be automized, and architecture by itself may not allow room for working on larger-scale social issues that I deeply care about. 

I also noticed that many people in the discipline had started to share similar beliefs. People within architecture started to incorporate ideas from parallel fields such as economics, law, social justice, and technology to supplement architecture and increase its impact. 

People like my professor, [Gabriel Cuellar](https://cadaster.us/) researched approaches to architecture with the socio-economic and legal environments of the region into mind. Others like [Stanislas Chaillou](http://stanislaschaillou.com/articles.html), an architect with a keen interest in the latest technologies, explored the intersection of architecture and artificial intelligence by proposing a Generative Adversarial Network (GAN) to generate architectural floor plans.

Given the challenges of the 21st century, and traditional architecture's lack of resources to address these challenges, I decided to reimagine my life. I needed a diverse, versatile skillset, and after my research, AI and Data Science seemed to provide just that. I recognized just how powerful tools like machine learning, and deep neural networks are, and I believe they are a crucial piece of the puzzle if we are to address future global issues.

### Introduction to Computer Science and Machine Learning
Since I do not come from a Computer Science (CS) background, I decided to first ease myself into this vast discipline. After gathering resources from some of my friends who were already familiar with CS, I decided to use the following online resources:

- University of Michigan's EECS 203 - Discrete Math
- Part 1: Applied Math [Deep Learning Book](https://www.deeplearningbook.org/)  by Ian Goodfellow, et. al.
-  University of Birmingham's [Data Structures and Algorithms](https://www.cs.bham.ac.uk/~jxb/DSA/dsa.pdf)
- 3Blue1Brown's playlist on [Linear Algebra and Neural Networks](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)
- [The Complete 2021 Web Development Bootcamp](https://www.udemy.com/share/1013gG2@PkdgfUtjc1QOe0ZHBXtxRhRtY1c=/)
- [Python For Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org)

These resources helped introduce me to fundamentals of computational math, web development, and coding. Simultaneously, I started familiarizing myself to Deep Learning by following these online courses:
- [Machine Learning, Data Science and Deep Learning with Python ](https://www.udemy.com/share/101W9O2@FG1jVGFgcFQOe0ZHBXtxRhRuSldhYHM=/)
- [Fast.ai: Practical Deep Learning for Coders ](https://course.fast.ai/)
- [PyTorch for Deep Learning with Python](https://www.udemy.com/share/101rrK2@PW5gV2JbSl0OdkFLBHBOfRRt/)

### Introduction to Computer Vision
I now had a essential understanding of Machine Learning, Deep Learning, and PyTorch. I then wanted to pick a specialization, and mostly due to the amount of applications I could see because of my background, I decided to dig deeper into Computer Vision (CV). To get started, I used the University of Michigan's [EECS 598 - Deep Learning for Computer Vision](https://web.eecs.umich.edu/~justincj/teaching/eecs498/FA2020/) course as my guide. This course was similarly structured to Stanford's CS231n, but used a PyTorch as the main library.

This was the most useful, yet challenging course I took, but it taught me fundamentals of CV topics like:

-   Convolutional networks
-   Recurrent networks
-   Attention and transformers
-   Object detection
-   Image segmentation
-   Video classification
-   Generative models (GANs, VAEs, autoregressive models)

After taking this course, I have come to a much better understanding of the works of Stanislas Chaillou from above. I realized Stanislas's work was built on top of a vast library of research that came before it, such as the research by [Weixin Huang and Hao Zheng](https://www.researchgate.net/publication/328280126_Architectural_Drawings_Recognition_and_Generation_through_Machine_Learning), who used the [Pix2Pix GAN](https://phillipi.github.io/pix2pix/) architecture to generate apartment floor plans. I decided I try replicating these studies, but lacked open-source datasets to experiment with. That is until I came across a paper by [Wenming Wu, et. al.](http://staff.ustc.edu.cn/~fuxm/projects/DeepLayout/index.html). They had taken the time to assemble a dataset of more than 80k apartment floor plans and made them free to use for research purposes. I reached out to them and got access to the dataset, which I am currently using for learning purposes.

### My Current Work
I am currently interested in getting my hands dirty with real-world projects within computer vision. This includes
exploring generative modeling through neural nets, working on image classification and object-detection tasks, etc.

My current projects are:
- [Image Classification]()
	- MNIST
	- Amazon Deforestation
- [Image Generation]() through various types of GANs
	- Simple GAN
	- Conditional GAN
	- Wasserstein-loss GAN
	- Deep Convolutional GAN
	- Pix2Pix
	- CycleGAN
	- StyleGAN