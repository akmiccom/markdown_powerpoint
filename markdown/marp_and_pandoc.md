---
# Title 
title: Pandoc Template for Powerpoint
subtitle: (Title Slide)
date: 21 April 2024

# for pandoc
# reference-doc: "powerpoint/YPP_Ver1.0.pptx"
# css:
#   - style\YPP_ver1.0.css
  # - styles/special.css

# for marp
theme: YPP_ver1.0
math: mathjax
marp: true
---



<!-- _class: title -->
# Section Title(Section Header)

---

## How to do a slide(Title and Content)

I like to use:

* H1 for section titles
- H2 for slide titles
+ H3 for additional headings in slides

::: notes

Speaker notes go here

:::

---

## Two-column slide with image(Two content)


:::::::::::::: {.columns}
::: {.column width="50%"}
Left column:

- Bullet
- Bullet
- Bullet
- 
:::
::: {.column width="50%"}
![](img\Logo_01.png)
:::
::::::::::::::

::: notes

Speaker notes go here

:::

---

## Table(Title and Content)

| Heading | Heading | Heading | Heading | Heading |
| --- | --- | --- | --- | --- |
| Cell | Cell | Cell | Cell | Cell |
| Cell | Cell | Cell | Cell | Cell |
| Cell | Cell | Cell | Cell | Cell |
| Cell | Cell | Cell | Cell | Cell |
| Cell | Cell | Cell | Cell | Cell |

::: notes

Speaker notes go here

:::

---

## An image(Title and Content)

![Alt text looks like this](./img/Logo_01.png){width=25%}

::: notes

Speaker notes go here

:::

---

## Bullet lists(Title and Content)

- Bullets work
  -  Indenting works

---

## Ordered lists(Title and Content)

1. Ordered lists work
   1. Sub-lists in ordered lists 
1. Next item

::: notes

Speaker notes go here

:::

---

## Code(Title and Content)

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
::: notes

Speaker notes go here

:::

---

## Blockquotes(Title and Content)

Blockquotes look like this.

> Here is a blockquote


::: notes

Speaker notes go here

:::

---

## mathjax

$$
\begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix}
$$

---

# Thank you(Section Header)