# Language Dictionary #

This is a hopefully multi-language dictionary that you can run with python installed.

Please keep in mind that the translations are mostly made and updated by the community/contributors.

## Setup ##
First you need [python](https://www.python.org/downloads/) installed as well as the packages: pygame and rapidfuzz.
```
pip install pygame, rapidfuzz
```
Then you go to main.py and run that script. If everything is setup correctly it should run.
If you have any problems please feel free to open an issue and we will try to sort it as fast as possible.

## Word rules ##

If you want to help with the words just open a pull request in the language JSON file you want to change.
However, the JSON file must follow some rules.

You __must__ follow this format:
```
"hello": {
    "translation": "hallo",
    "gender": "na",
},
"street": {
    "translation": "StraU+1E9Ee",
    "gender": "fe"
}
```

Any NSFW words must have this in the object: ```"adult": True```. If this is not present the code will assume the word id SFW\
Any special characters must be in Unicode form. Please go to the [UNICODE](UNICODE.md) file for the unicode values\
The english word must be the key.\
There has to be a translation into whichever language you are changing.\
You must put a word gender if the language has them.\
```
Masculine: ma
Feminine: fa
Neuter/Neutral: ne
None: na
```
