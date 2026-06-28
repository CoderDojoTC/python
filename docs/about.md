---
title: "About This Book"
description: "About Beginning Python — its history, purpose, audience, design, and the team behind it."
---

# About This Book

## Welcome from Monty

!!! mascot-welcome "Welcome!"
    ![Monty waving welcome](./img/mascot/welcome.png){ class="mascot-admonition-img" }
    Hi, I'm Monty! I've been living in these pages since the very beginning, guiding
    students from their first `print("Hello!")` all the way to neural networks and
    maze-solving algorithms. This book is my home, and I'm so glad you're here.
    Whether you're brand new to Python or just looking for a place to level up,
    I'll be right alongside you every step of the way. Let's code something awesome together!

---

## A Note on Platform History

This textbook has a story, and that story matters for understanding why it is built the way it is today.

**Beginning Python** was created in 2020 by Dan McCreary as a volunteer teaching resource
for [CoderDojo Twin Cities](https://www.coderdojotc.org/), a free, community-run coding
club for kids. The earliest lessons used **Trinket.io** — a popular, browser-based Python
sandbox that made it easy for students to write and run Python programs without installing
anything on their computers. From 2020 through 2025, Trinket powered hundreds of interactive
coding examples in this book, and it served the CoderDojo community well.

In 2026, Trinket announced it would be
**[shutting down permanently in early August 2026](https://trinket.io/announcement)**:

> *"Trinket will be shutting down in early August 2026. After this date, trinket.io will no
> longer be available, and you will not be able to access your trinkets, courses, or any
> content on this site."*

This was a significant disruption. Every embedded Trinket lab in the book became a dead link.
Weeks of searching for a replacement followed. **Pickcode.io** was the most promising alternative,
but it proved inadequate: it had rendering bugs, limited support for turtle graphics, and
capped free-tier users at only five turtle programs — far too few for a course built around
visual, hands-on drawing exercises.

After evaluating the alternatives, the decision was made to rewrite the book from scratch
around **[Skulpt](https://skulpt.org/)** — a self-hosted, open-source Python implementation
that runs entirely in the browser. Skulpt has no external dependencies, no account requirements,
no free-tier caps, and full support for Python's `turtle` module. Every Skulpt lab in this
book is embedded directly in the page using a small local JavaScript file (`skulpt.js`),
which means the interactive coding environment will continue to work as long as the page itself
loads — with no third-party service that can disappear.

The book was also formally renamed at this time from its CoderDojo-specific identity to
**Beginning Python**, reflecting its broader mission as an open educational resource for
any student, classroom, or coding club that wants a free, self-contained introduction to Python.

---

## Why This Intelligent Textbook

Python is the most popular programming language in the world — and has been for years.
It powers breakthroughs in data science, artificial intelligence, scientific computing,
web development, and the Raspberry Pi / Maker community. Yet most beginner Python resources
assume either that students already know how to install software, or that they are adult
learners comfortable reading reference documentation. Beginning programmers ages 10–13
deserve better.

**In the United States (2025–2026):**

- Python is the **#1 most taught language** in U.S. K–12 schools, according to
  the Computer Science Teachers Association's most recent state-of-K12-CS survey[^1]
- The U.S. Bureau of Labor Statistics projects **25% growth** in software developer
  and quality assurance jobs through 2032 — the majority of which use Python as a
  primary language[^2]
- Only **57% of U.S. high schools** offer at least one computer science course, leaving
  millions of students with no classroom exposure to programming before college[^3]
- Stack Overflow's 2024 Developer Survey found that **Python is the most-used language**
  among developers for the fifth consecutive year, used by **51% of all respondents**[^4]

**Worldwide:**

- Python's package index (PyPI) hosts more than **550,000 packages**, making it the
  largest ecosystem of reusable code in any programming language[^5]
- The global market for Python-related developer tools and education is valued at
  over **$8 billion** and is growing at 25% per year[^6]

These numbers represent millions of young learners who need a genuinely accessible
on-ramp — one that meets them where they are (block-based programming), uses tools
that work without installation or accounts, and teaches through visual, hands-on projects
rather than dry syntax drills.

This book takes a fundamentally different approach. It is built on a **learning graph
of 450 interconnected concepts** validated across 38 chapters, with each concept introduced
only after its prerequisites are established. Every early chapter includes **Skulpt labs** —
fully interactive Python editors embedded directly in the browser, no accounts or installs
required. Students run code, modify it, and see results instantly. Monty the mascot
provides encouragement, hints, and predictions at each step. The entire textbook is
**open source and free** — no paywalls, no access codes, no annual edition upgrades.

---

## How to Use This Book

This textbook is designed for self-paced study, starting from zero and building toward
genuine Python fluency. Each chapter builds on previous material, so reading in order is
recommended, especially for chapters 1–18 where turtle graphics provide the visual foundation.

The book includes:

- **38 Chapters** covering core Python syntax, turtle graphics, control flow, functions,
  collections, object-oriented programming, algorithms, data visualization, NumPy,
  image processing, and an introduction to machine learning
- **Skulpt Labs** embedded in chapters — fully interactive Python editors that run in
  your browser, no installation or account required
- **Quizzes** at the end of each chapter to test understanding and retention
- **Annotated References** linking to Wikipedia, Python documentation, and authoritative sources
- **Glossary** with definitions for every key concept, written at an accessible reading level
- **FAQ** answering common questions from students transitioning from block-based coding
- **Learning Graph** visualizing all 450 concept dependencies across the course
- **Teacher's Guide** with pacing recommendations, discussion questions, and CSTA alignment
- **Search** available from any page using the search bar at the top

The [Learning Graph](learning-graph/index.md) is especially useful if you want to explore
non-linearly or check prerequisites for a specific concept — it shows exactly how ideas
connect and which chapters introduce them.

!!! mascot-tip "Where to Start"
    ![Monty offering a tip](./img/mascot/tip.png){ class="mascot-admonition-img" }
    If you've never written Python before, start at Chapter 1 and work forward.
    If you've done some Python but want to strengthen your foundations, check the
    [Learning Graph](learning-graph/index.md) to find exactly where to jump in.
    I'll be there to guide you either way!

---

## About the Author

![Dan McCreary headshot](./img/dan-headshot-small.png){ width="150px" align="right"}

Dan McCreary is a semi-retired AI researcher, solution architect, and educator who has
spent more than three decades helping Fortune 100 organizations reason over massive
datasets. At Optum he founded the Generative AI Center of Excellence and led the team
that built one of the world's largest healthcare knowledge graphs — spanning over
25 billion vertices — to unify member, provider, and patient insights. Dan's deep
background in knowledge representation and systems thinking underpins the precise
learning graphs and intelligent textbook workflows used throughout this course.

He is the co-author of *Making Sense of NoSQL* (Manning Publications), the founding
chair of the NoSQL Now! conference, and a frequent keynote speaker on semantic search,
ontology strategy, and AI hardware. Beyond industry, Dan has mentored students as a
STEM volunteer since 2014 through CoderDojo Twin Cities, and now applies the same
rigor he used at enterprise scale to building open educational resources for young
learners. You can visit the
[Intelligent Textbooks Case Studies](https://dmccreary.github.io/intelligent-textbooks/case-studies/)
to see over 87 textbooks that Dan has created or co-created with other authors.

**Selected Credentials**

- B.A. in Physics and Computer Science from Carleton College
- M.S.E.E. from the University of Minnesota
- MBA coursework at the University of St. Thomas
- Patent holder in semantic search and ontology management techniques
- Advocate for large-scale Enterprise Knowledge Graph adoption across healthcare and education
- Long-time promoter of accessible, low-cost AI-powered learning experiences for K–12 students

---

## How to Cite This Book

If you reference this textbook in academic work, curriculum proposals, lesson plans,
or other publications, please use one of the following citation formats.

**APA (7th edition)**

McCreary, D. (2026). *Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/

**Chicago (17th edition)**

McCreary, Dan. 2026. *Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/.

**MLA (9th edition)**

McCreary, Dan. *Beginning Python: From Blocks to Code with Monty*. 2026, dmccreary.github.io/python/.

**BibTeX**

```bibtex
@book{mccreary2026python,
  title     = {Beginning Python: From Blocks to Code with Monty},
  author    = {McCreary, Dan},
  year      = {2026},
  url       = {https://dmccreary.github.io/python/},
  note      = {Interactive intelligent textbook with Skulpt inline Python labs}
}
```

To cite a specific chapter, append the chapter number and title — for example:

McCreary, D. (2026). Chapter 1: Welcome to Python and Skulpt. In
*Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/chapters/01-welcome-to-python/

---

## License

This work is released under the
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
You are free to share and adapt the material for non-commercial purposes as long as
you give appropriate credit and share your adaptations under the same license.

---

## References

[^1]: Computer Science Teachers Association. (2023). *State of K-12 Computer Science Education*. https://advocacy.code.org/stateofcs

[^2]: U.S. Bureau of Labor Statistics. (2024). *Occupational Outlook Handbook: Software Developers, Quality Assurance Analysts, and Testers*. https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm

[^3]: Code.org. (2024). *2024 State of Computer Science Education: Laying the Groundwork*. https://advocacy.code.org/2024_state_of_cs.pdf

[^4]: Stack Overflow. (2024). *2024 Developer Survey*. https://survey.stackoverflow.co/2024/

[^5]: Python Package Index. (2026). *PyPI Statistics*. https://pypi.org/

[^6]: Grand View Research. (2024). *Python Web Frameworks Market Size, Share & Trends Analysis Report*. https://www.grandviewresearch.com/industry-analysis/python-web-framework-market-report
