# Beginning Python — Concept List v1

This concept list was derived from the existing manually created course content in the `docs/` directory
and supplemented with additional concepts appropriate for a beginning Python course.
The original textbook was created by hand by humans starting around May of 2020 when Trinket was
the best practice for teaching introduction to Python with Turtle graphics.  This
course was used in the CoderDojo Twin Cities coding clubs and the Code Savvy clubs for many years.
It serves as the foundation for the learning graph used to regenerate the course in June of 2026
using Claude Code Opus 2.6 in High effort mode.

---

## 1. Development Environments & Setup

1. Python interpreter overview
2. Python 2 vs Python 3 differences
3. Trinket.io — web-based Python environment
4. repl.it — online Python IDE
5. Thonny — beginner-friendly Python IDE
6. Spyder IDE — scientific Python IDE
7. VS Code — general-purpose code editor
8. Jupyter Notebooks — interactive computational environment
9. JupyterLab — enhanced Jupyter environment
10. Conda — environment and package manager
11. pip — Python package installer
12. Virtual environments
13. Installing Python locally
14. Running Python scripts from the terminal
15. The Python REPL (interactive shell)
16. Raspberry Pi as a Python platform

---

## 2. Basic Syntax & Output

17. print() function
18. Comments (single-line with `#`)
19. Multi-line strings (triple quotes)
20. Indentation as syntax (whitespace rules)
21. Case sensitivity in Python
22. Python keywords (reserved words)
23. Blank lines and code readability

---

## 3. Variables & Assignment

24. Variable definition and assignment (`=`)
25. Variable naming rules (letters, digits, underscores)
26. Snake_case naming convention
27. Meaningful variable names
28. Multiple assignment (`a, b = 1, 2`)
29. Augmented assignment operators (`+=`, `-=`, `*=`, `/=`)
30. Constants (by convention, ALL_CAPS)

---

## 4. Data Types

### Numeric
31. Integers (`int`) — whole numbers, positive and negative
32. Floats (`float`) — decimal numbers
33. Division always returns float in Python 3
34. Integer division (`//`)
35. Modulo operator (`%`) — remainder after division
36. Exponentiation (`**`)
37. Arithmetic operators: `+`, `-`, `*`, `/`

### Boolean
38. Boolean type (`bool`) — `True` and `False`
39. Comparison operators: `>`, `<`, `>=`, `<=`, `==`, `!=`
40. Logical operators: `and`, `or`, `not`
41. Truthiness and falsiness of values

### Strings
42. String type (`str`) — text enclosed in quotes
43. Single vs double quotes
44. String concatenation with `+`
45. String repetition with `*`
46. String indexing (0-based)
47. String slicing (`s[start:end:step]`)
48. Escape characters (`\n`, `\t`, `\\`, `\"`)
49. String length with `len()`
50. String methods: `.lower()`, `.upper()`, `.strip()`, `.lstrip()`, `.rstrip()`
51. String methods: `.split()`, `.join()`, `.replace()`
52. String methods: `.startswith()`, `.endswith()`, `.find()`, `.count()`
53. String methods: `.isdigit()`, `.isalpha()`, `.isalnum()`
54. String formatting with `.format()`
55. f-strings (formatted string literals)
56. String immutability

### None
57. `None` — null/empty value, `NoneType`
58. Functions without `return` return `None`
59. Checking for `None` with `is None`

---

## 5. Type Conversion (Casting)

60. `int()` — convert to integer
61. `float()` — convert to float
62. `str()` — convert to string
63. `bool()` — convert to boolean
64. `type()` — inspect a variable's type
65. `isinstance()` — check if object is an instance of a type

---

## 6. User Input

66. `input()` function — read text from user
67. Prompting the user (passing a string to `input()`)
68. Converting input strings to numbers with `int()` / `float()`
69. Input validation basics

---

## 7. Control Flow — Conditionals

70. `if` statement
71. `if...else` block
72. `elif` (else-if) chains
73. Nested `if` statements
74. Conditional expressions (ternary): `x if condition else y`
75. `match`/`case` statement (Python 3.10+, structural pattern matching)

---

## 8. Control Flow — Loops

76. `for` loop — iterating over a sequence
77. `for` loop with `range()`
78. `range(start, stop, step)`
79. `while` loop — condition-based repetition
80. `break` — exit a loop early
81. `continue` — skip to next iteration
82. `else` clause on loops
83. Nested loops
84. Loop counter variable (`i`, `j`)
85. Infinite loops and how to avoid them
86. `enumerate()` — iterate with index and value
87. `zip()` — iterate over multiple sequences simultaneously

---

## 9. Functions

88. Defining a function with `def`
89. Calling a function
90. Function parameters (positional)
91. Default parameter values
92. Keyword arguments
93. `return` statement
94. Functions that return `None` implicitly
95. Local scope — variables inside functions
96. Global scope — variables at module level
97. `global` keyword — access global variable inside function
98. `nonlocal` keyword — access enclosing scope variable
99. Docstrings — documenting functions
100. Pure functions vs functions with side effects
101. Recursion — a function calling itself
102. Recursion base case and recursive case
103. Recursion depth and stack overflow
104. Lambda functions (anonymous functions)

---

## 10. Collections — Lists

105. List type (`list`) — ordered, mutable collection
106. Creating a list with `[]`
107. List indexing (0-based, negative indexing)
108. List slicing
109. `len()` — number of items in a list
110. List methods: `.append()`, `.insert()`, `.extend()`
111. List methods: `.remove()`, `.pop()`, `.clear()`
112. List methods: `.sort()`, `.reverse()`, `.copy()`
113. List methods: `.index()`, `.count()`
114. Checking membership with `in`
115. List concatenation and repetition
116. Iterating over a list with `for`
117. Nested lists (lists of lists)
118. List comprehensions

---

## 11. Collections — Tuples

119. Tuple type (`tuple`) — ordered, immutable collection
120. Creating a tuple with `()`
121. Tuple indexing and slicing
122. Tuple unpacking
123. When to use tuples vs lists
124. Single-element tuple syntax (`(x,)`)

---

## 12. Collections — Dictionaries

125. Dictionary type (`dict`) — key-value pairs
126. Creating a dictionary with `{}`
127. Accessing values by key (`d[key]`)
128. `.get()` method — safe key access with default
129. Adding and updating key-value pairs
130. Removing entries: `.pop()`, `del`
131. Dictionary methods: `.keys()`, `.values()`, `.items()`
132. Iterating over a dictionary
133. Checking key membership with `in`
134. Nested dictionaries
135. Dictionary comprehensions

---

## 13. Collections — Sets

136. Set type (`set`) — unordered collection of unique items
137. Creating a set with `{}` or `set()`
138. Set operations: union (`|`), intersection (`&`), difference (`-`)
139. `.add()`, `.remove()`, `.discard()` methods
140. Checking membership with `in`
141. Frozensets (immutable sets)

---

## 14. Built-in Functions

142. `print()` — output to console
143. `input()` — read user input
144. `len()` — length of a sequence
145. `range()` — generate a sequence of numbers
146. `type()` — get type of an object
147. `int()`, `float()`, `str()`, `bool()` — type conversions
148. `list()`, `tuple()`, `set()`, `dict()` — collection constructors
149. `max()`, `min()` — find maximum/minimum
150. `sum()` — sum values in an iterable
151. `abs()` — absolute value
152. `round()` — round a number
153. `sorted()` — return sorted list
154. `reversed()` — return reverse iterator
155. `enumerate()` — iterate with index
156. `zip()` — combine iterables
157. `map()` — apply function to each item
158. `filter()` — filter items by condition
159. `dir()` — list attributes/methods of an object
160. `help()` — display documentation

---

## 15. Modules & Imports

161. `import` statement
162. `from ... import ...` — import specific names
163. `import ... as ...` — alias a module
164. `from ... import *` — import all (use sparingly)
165. Creating custom modules (`.py` files)
166. `__name__ == "__main__"` guard
167. The Python standard library overview

### Standard Library Modules
168. `random` — random number generation
169. `random.randint(min, max)`
170. `random.choice(sequence)`
171. `random.shuffle(list)`
172. `random.seed()` — reproducibility
173. `math` — mathematical functions
174. `math.sqrt()`, `math.floor()`, `math.ceil()`
175. `math.sin()`, `math.cos()`, `math.pi`
176. `math.radians()` — degrees to radians
177. `string` — string constants (punctuation, digits, etc.)
178. `time` — time operations
179. `time.sleep()` — pause execution
180. `sys` — system-level operations
181. `sys.path` — Python module search path
182. `os` — operating system interface
183. `os.path` — file path operations
184. `re` — regular expressions

---

## 16. Regular Expressions

185. Importing `re` module
186. `re.search(pattern, string)` — find first match
187. `re.findall(pattern, string)` — find all matches
188. `re.split(pattern, string)` — split by pattern
189. `re.sub(pattern, replacement, string)` — substitute matches
190. Common patterns: `\d` (digit), `\w` (word char), `\s` (whitespace)
191. Anchors: `^` (start), `$` (end)
192. Character classes: `[a-z]`, `[A-Z]`, `[0-9]`
193. Quantifiers: `+` (one or more), `*` (zero or more), `?` (optional)
194. Alternation with `|`
195. Escaping special characters with `\`
196. Raw strings for regex patterns (`r"..."`)

---

## 17. File Input/Output

197. `open()` function
198. File modes: `'r'` (read), `'w'` (write), `'a'` (append), `'b'` (binary)
199. `file.read()` — read entire file as string
200. `file.readlines()` — read all lines into a list
201. `file.readline()` — read one line at a time
202. `file.write()` — write string to file
203. `file.close()` — close file handle
204. `with` statement (context manager) for safe file handling
205. Iterating over file lines with `for`
206. String methods for text processing: `.strip()`, `.lower()`, `.replace()`
207. CSV file reading basics

---

## 18. Error Handling

208. Types of errors: syntax errors vs runtime errors vs logic errors
209. Common exceptions: `ValueError`, `TypeError`, `IndexError`, `KeyError`, `NameError`, `ZeroDivisionError`
210. Reading a traceback (stack trace)
211. `try...except` block
212. `except ExceptionType as e` — catching specific exceptions
213. `else` clause in try/except
214. `finally` clause — always executes
215. `raise` — raising exceptions manually
216. `assert` statement with error messages
217. Debugging with `print()` statements
218. Using Google and Stack Overflow to debug errors

---

## 19. Object-Oriented Programming (Intro)

219. Objects and classes — conceptual overview
220. Attributes — properties of an object
221. Methods — functions belonging to an object
222. `class` keyword — defining a class
223. `__init__()` — constructor method
224. `self` parameter
225. Creating instances of a class
226. Accessing attributes and calling methods (`obj.attr`, `obj.method()`)
227. String methods as examples of OOP
228. List methods as examples of OOP
229. Inheritance — basics
230. `__str__()` — string representation of an object

---

## 20. Turtle Graphics

231. `import turtle`
232. Creating a `turtle.Turtle()` object
233. Creating a `turtle.Screen()` object
234. Screen setup: `setup(width, height)`, `bgcolor(color)`, `title(text)`
235. Movement: `forward()`, `backward()`, `left()`, `right()`
236. Absolute positioning: `goto(x, y)`, `setx()`, `sety()`
237. Pen control: `penup()`, `pendown()`, `pensize()`
238. Color: `color()`, `pencolor()`, `fillcolor()`
239. Fill: `begin_fill()`, `end_fill()`
240. Drawing shapes: `circle(radius)`, drawing squares/polygons with loops
241. Turtle appearance: `shape()` (turtle, arrow, circle, square, triangle, classic)
242. Hiding/showing turtle: `hideturtle()`, `showturtle()`
243. Writing text: `write(text, font=...)`
244. Clearing: `clear()`, `reset()`
245. Position query: `xcor()`, `ycor()`, `heading()`
246. Speed control: `speed(value)`
247. Direction: `setheading(angle)`
248. Event handling: `onscreenclick(function)`
249. Animation with turtle (frame-based loops)
250. Building a color picker with turtle
251. Drawing fractals with recursion and turtle
252. Drawing a sine wave with turtle and math

---

## 21. Data Visualization

253. `matplotlib` library overview
254. `import matplotlib.pyplot as plt`
255. `plt.plot(x, y)` — line plot
256. `plt.show()` — display plot
257. `plt.title()`, `plt.xlabel()`, `plt.ylabel()` — labels
258. `plt.grid()` — show grid lines
259. Plotting a sine wave
260. Working with lists as x/y data

---

## 22. Numerical Computing (NumPy Intro)

261. `numpy` library overview
262. `import numpy as np`
263. `np.array()` — creating arrays
264. `np.argmax()` — index of maximum value
265. Array operations and broadcasting basics
266. Reshaping arrays (`array.reshape()`)

---

## 23. Image Processing (Intro)

267. PIL (Python Imaging Library) / Pillow overview
268. `Image.open(path)` — open an image
269. `image.show()` — display an image
270. Pixel data and image arrays

---

## 24. Data Structures & Algorithms

271. Abstract data types overview
272. Stack — LIFO (Last In, First Out)
273. Queue — FIFO (First In, First Out)
274. Queue operations: enqueue (`append()`), dequeue (`pop(0)`)
275. Graph — nodes and edges
276. Adjacency list representation
277. Breadth-First Search (BFS) algorithm
278. BFS color tracking (white, gray, black)
279. BFS for path finding
280. Depth-First Search (DFS) algorithm
281. DFS with recursion and backtracking
282. DFS and BFS for maze solving
283. Sorting algorithms overview (bubble, selection, insertion)
284. Binary search concept

---

## 25. Machine Learning & Neural Networks (Advanced)

285. Machine learning overview — supervised vs unsupervised
286. `keras` library overview
287. Sequential model
288. Dense layers — fully connected layers
289. Activation functions: `relu`, `softmax`
290. Conv2D — convolutional layers
291. MaxPooling2D — pooling layers
292. Dropout — regularization to prevent overfitting
293. Flatten layer — reshape for dense layers
294. `model.compile()` — loss function, optimizer, metrics
295. `model.fit()` — training the model
296. `model.evaluate()` — testing accuracy
297. `model.predict()` — making predictions
298. Loss functions: `categorical_crossentropy`
299. Optimizer: Adam
300. Metrics: accuracy
301. Batch size and epochs
302. MNIST dataset — handwritten digit recognition
303. Data normalization/preprocessing
304. Convolutional Neural Networks (CNN)
305. Feedforward networks
306. Recurrent networks (RNN) — overview
307. LSTM networks — overview
308. Autoencoders — overview

---

## 26. Graphics in Jupyter

309. `ipycanvas` — canvas drawing in Jupyter
310. `mobilechelonian` — turtle graphics in Jupyter
311. Drawing shapes on a canvas
312. Color bars and data visualization in Jupyter

---

## 27. Event-Driven & Interactive Programming

313. Event-driven programming model
314. Mouse click event handlers (`onscreenclick`)
315. Keyboard event handlers (turtle `onkey`)
316. Callback functions
317. Animation loops

---

## 28. Programming Practices & Patterns

318. Modularity — breaking code into functions
319. Code reusability
320. DRY principle (Don't Repeat Yourself)
321. Meaningful variable and function names
322. Code comments — when and why
323. Literate programming with Jupyter
324. Reading documentation with `help()` and `dir()`
325. Version control basics (git overview)
326. Searching Stack Overflow and documentation

---

## 29. Color & Graphics Concepts

327. Named colors (red, green, blue, orange, etc.)
328. Hex color values (`#FA057F`)
329. RGB color model
330. Color in turtle graphics
331. Background and pen colors

---

## Concepts Added Beyond Existing Content

The following concepts are recommended additions to make the course more complete
for a modern beginning Python curriculum:

332. f-strings (formatted string literals) — more readable than `.format()`
333. List comprehensions — concise way to build lists
334. Dictionary comprehensions
335. `with` statement / context managers — safe resource handling
336. `match`/`case` statement (Python 3.10+) — modern pattern matching
337. Lambda functions — anonymous single-expression functions
338. `map()` and `filter()` — functional programming basics
339. Sorting with a key function (`sorted(list, key=...)`)
340. String f-string formatting with format specifiers (e.g., `{x:.2f}`)
341. `os` and `os.path` — file path and directory operations
342. CSV files — reading/writing structured data
343. Exception hierarchy — understanding `Exception` base class
344. `raise` — throwing custom errors
345. Class `__str__()` and `__repr__()` methods
346. Inheritance — subclasses and method overriding
347. DRY principle and code reuse patterns
348. `__name__ == "__main__"` guard for runnable modules
349. Virtual environments — keeping projects isolated
350. Reading and writing JSON files (`json` module)
