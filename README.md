# Uyghur_number_speller
python script to spell numbers and dates in Uyghur. This project is is forked from Turkish_number_speller.

# TODO
- spell decimal number.
- spell fraction number.
- other from your feedback.

# Noting
I use common Turkish Alphabet as Uyghur script. It is quite similar to ULY. Here is the mapping:

| ULY | CTA |
|---|---|
|sh|ş|
|ch|ç|
|gh|ğ|
|ng|ñ|
|j|c|

## Usage
Usage is quite simple, for numbers:
```
$ python speller.py -n 92
doksan iki
```
for dates:
```
$ python speller.py -d 4.5.1992
dört mayıs bin dokuz yüz doksan iki
```
