![header](img/001.png)

# Vector Space Indexing Engine in Python

### Here is an example indexer using Python.

- First we need to convert our documents into an concordance. A concordance is a count of every word that occurs in a document.
  
- The only other thing we need is a vector space. A vector space is a way of calculating the distances between two points. Essentially it works the same way calculating the 3rd side of a triangle. Except that instead of *2 planes (x and y)* or even *3 planes (x,y,z)* you can have as many planes as you want.
  
- To use it you just supply two concordances (one the document and the other the query) and it returns a number from 0 to 1 of how related they are. The higher the number the more relevant the search terms are to the document.

## Project structure

```
$PROJECT_ROOT
├── main-search.py        # Entry point
└── docsx.py              # The Document
```

## Executing

```sh
python3 main-search.py
```

> Update the document ```docsx.py``` for personalized results.
