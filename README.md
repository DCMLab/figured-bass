# Figured Bass

Generate chord from figured bass.

For example, calling the script with arguments
```
python figured-bass.py -k 80 -r 2 -n 5 9
```
will produce output
```
SUCCESS: [('5', 89), ('1', 94), ('3', 98)]
```
That is for the key of C major (```-k 80```) a fourth and a sixth (```-n 5 9```) are realized by the second inversion
resulting in the order ```5-1-3``` and corresponding to MIDI pitches ```89-94-98```. Likewise, calling
```
python figured-bass.py -k 80 -r 2 -n 3 5 -m minor
```
yields
```
SUCCESS: [('5', 89), ('7', 92), ('1', 94), ('3', 97)]
```