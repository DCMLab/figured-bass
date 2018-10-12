import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate chord from figured bass.')
    parser.add_argument('-k', dest='key', type=int, required=True,
                        help='integer specifying the key in MIDI pitch')
    parser.add_argument('-r', dest='root', type=int, required=True,
                        help='integer specifying the root of the chord relative to the key in semitones')
    parser.add_argument('-m', dest='mode', type=str, choices=['major', 'minor'], default='major',
                        help='the mode (default: "major")')
    parser.add_argument('-n', dest='numbers', type=int, nargs='*',
                        help='a list of integers specifying the required intervals relative to the bass in semintones')

    args = parser.parse_args()
    if args.numbers is None:
        args.numbers = []

    for chord_type in ['triad', 'seventh', 'failed']:
        base_chord = [
            ('1', args.key + args.root),
            ('3', args.key + args.root + (4 if args.mode == 'major' else 3)),
            ('5', args.key + args.root + 7),
        ]
        if chord_type == 'triad':
         pass
        elif chord_type == 'seventh':
            base_chord.append(
                ('7', args.key + args.root + (11 if args.mode == 'major' else 10))
            )
        else:
            break

        # go through rotations
        rotated_chord = base_chord
        for rotation in range(3 if chord_type == 'triad' else 4):
            if rotation > 0:
                new_rotation = rotated_chord[1:] + [(rotated_chord[0][0], rotated_chord[0][1] + 12)]
                rotated_chord = new_rotation
            # check if required intervals are present
            bass_tone = rotated_chord[0][1]
            all_intervals = True
            for interval in args.numbers:
                this_interval = False
                for second_tone in list(zip(*rotated_chord))[1]:
                    if second_tone - bass_tone == interval:
                        this_interval = True
                        break
                if not this_interval:
                    all_intervals = False
                    break
            if all_intervals:
                print("SUCCESS:", rotated_chord)
                exit()
            else:
                continue
    raise UserWarning("Could not compute chord. Please check your input parameters.")
