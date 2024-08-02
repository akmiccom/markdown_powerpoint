---
# Title for pptx
title: Pandoc Template for Powerpoint
subtitle: Sub Title
# date: 21 April 2024
paginate: true

# For pandoc
# reference-doc: "powerpoint/YPP_Ver1.0.pptx"
# css:
#   - style\YPP_ver1.0.css
  # - styles/special.css

# For marp
theme: YPP_ver01
math: mathjax
marp: true
---

<!-- _class: title -->

<!-- Tilte for Marp -->
<!-- # Title
Makoto.Yaguchi@motherson.com_
2024/04/22 -->


<!-- _class: chapter -->
## Section Title

---

<!-- _class: slide -->
### How to do a slide(Title and Content)

I like to use:

* H1 for section titles
- H2 for slide titles
+ H3 for additional headings in slides
  + Level3
    + Level3

---

<!-- _class: slide -->
### Two-column slide with image(Two content)


:::::::::::::: {.columns}
::: {.column width="50%"}
Left column:

- Bullet
- Bullet
- Bullet

:::
::: {.column width="50%"}
<!-- ![logo](img\Logo_01.png) -->
- Bullet
- Bullet
- Bullet
:::
::::::::::::::


---

<!-- _class: slide -->
### Table(Title and Content)

| Heading | Heading | Heading | Heading | Heading |
| ------- | ------- | ------- | ------- | ------- |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |
| Cell    | Cell    | Cell    | Cell    | Cell    |


---

<!-- _class: slide -->
### An image(Title and Content)

<!-- ![Alt text looks like this](img/Logo_01.png) -->

---

<!-- _class: slide -->
### Bullet lists(Title and Content)

- Bullets work
  -  Indenting works

---

<!-- _class: slide -->
### Ordered lists(Title and Content)

1. Ordered lists work
   1. Sub-lists in ordered lists 
1. Next item


---

<!-- _class: slide -->
### Code(Title and Content)

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

Something else:
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```

---

<!-- _class: slide -->
### Blockquotes(Title and Content)

Blockquotes look like this.

> Here is a blockquote


::: notes

Speaker notes go here

:::

---

<!-- _class: slide -->
### mathjax

$$
\begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix}
$$

---
<!-- _class: end -->
© Motherson  All rights reserved by Motherson and/or its affiliated companies. Any commercial use hereof, especially any transfer and/or copying hereof, is prohibited without the prior written consent of Motherson and/or its affiliated companies. In case of transfer of information containing know-how for which copyright or any other intellectual property right protection may be afforded, Motherson and/or its affiliated companies reserve all rights to any such grant of copyright protection and/or grant of intellectual property right protection. www.motherson.com
