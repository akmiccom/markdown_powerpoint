---
# Title for pptx
title: Pandoc Template for Powerpoint
subtitle: Sub Title
# date: 21 April 2024
paginate: true

# For pandoc
reference-doc: "powerpoint/YPP_Ver1.0.pptx"
css:
  - style\YPP_ver1.0.css
  - styles/special.css

# For marp
theme: YPP_ver01
math: mathjax
marp: true
---

<!-- _class: title -->

# Title Slide

Makoto.Yaguchi@motherson.com_
2024/04/22

---

<!-- Tilte for Marp -->
<!-- # Title
Makoto.Yaguchi@motherson.com_
2024/04/22 -->

<!-- _class: chapter -->
## Section Title

---

<!-- _class: OneContent -->
### Title and Content

I like to use:

* H1 for section titles

* H2 for slide titles

* H3 for additional headings in slides
  * Level3
    * Level3

---

<!-- _class: TwoContent -->
### Two-column slide with image(Two content)

<div class="columns">

<div class="column">

**左カラム**  

* 項目1
* 項目2  

</div>

<div class="column">

**右カラム**  

* 内容Aafjaklsdjfkljasdklfjasdkl;fjals;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;ls;l
* 内容B  

</div>

</div>

---

<!-- _class: OneContent -->
### Table(Title and Content)

| Heading | Heading | Heading | Heading | Heading |
| ------- | ------- | ------- | ------- | ------- |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |

---

<!-- _class: OneContent -->
### An image(Title and Content)

<!-- ![Alt text looks like this](img/Logo_01.png) -->

---

<!-- _class: OneContent -->
### Bullet lists(Title and Content)

* Bullets work
  * Indenting works

---

<!-- _class: OneContent -->
### Ordered lists(Title and Content)

1. Ordered lists work
   1. Sub-lists in ordered lists
1. Next item

---

<!-- _class: OneContent -->
### Code(One Content)

JavaScript:

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

---

<!-- _class: TwoContent -->
### Code(Two Content)

<div class="columns">

<div class="column">

JavaScript:

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

Python:

```python
s = "Python syntax highlighting"
print s
```

</div>
<div class="column">

Something else:

``` cmd
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```

</div>
</div>

---

<!-- _class: OneContent -->
### Blockquotes(Title and Content)

Blockquotes look like this.

> Here is a blockquote

::: notes

Speaker notes go here

:::

---

<!-- _class: OneContent -->
### mathjax

$$
\begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix}
$$

---
<!-- _class: end -->
© Motherson  All rights reserved by Motherson and/or its affiliated companies. Any commercial use hereof, especially any transfer and/or copying hereof, is prohibited without the prior written consent of Motherson and/or its affiliated companies. In case of transfer of information containing know-how for which copyright or any other intellectual property right protection may be afforded, Motherson and/or its affiliated companies reserve all rights to any such grant of copyright protection and/or grant of intellectual property right protection. <www.motherson.com>
