# Suggestions - Changes

## Handling script arguments

Using the argparse module is easier and scalable to deal with extra arguments in a script.

## Wiki

- Arriving at the repository anyone can get an idea what the repository can do, but they don't now the HOW. To be more specific how to test it and try out by itself.

Examples like this would be nice to have:

```python
python main.py data/corpus/universal-dependencies/moore.conllu
```

## Paths troubles

for that the file [common_paths.py](src/common_paths.py) is one thing that I like to use when there is a complex code structure. One file where all the references are noted and where you could minimize the time for refactoring.

## File openning

It is a good to have, every time openning a file using the `try` and `except` feature. See the example below how the error are more clear. It's recommended to check the existence of the file before trying to access. The try catch would protect the code flow from an unexpected break.

```
with open(args.infile) as f:
            lines = f.readlines()
        nh.tagText(lines)
$ pyhton main.py data/corpus/universal-dependencies/moorae.conllu

Traceback (most recent call last):
  File "/Users/pablofreitas/Documents/git_ws/nheengatu/main.py", line 36, in <module>
    main()
  File "/Users/pablofreitas/Documents/git_ws/nheengatu/main.py", line 30, in main
    with open(args.infile) as f:
         ^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data/corpus/universal-dependencies/moorae.conllu'
```

```
try:
with open(args.infile) as f:
lines = f.readlines()
nh.tagText(lines)
except FileNotFoundError as e:
print(e)
$ pyhton main.py data/corpus/universal-dependencies/moorae.conllu

FileNotFoundError: [Errno 2] No such file or directory: 'data/corpus/universal-dependencies/moorae.conllu'

```
