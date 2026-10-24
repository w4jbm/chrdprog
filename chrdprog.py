#!/usr/bin/env python3
#####
#
# chrdprog.py - Python chord progression analysis by Jim McClanahan, W4JBM
#
# Check most streaming platforms or YouTube for music from
# !!!                The Daft Spaniels                 !!!
#
# NOTE: Google provided a significant amout of the original code.
#       I have tweaked it to be a bit friendlier to use and better
#       meet my needs, but Google provided a pretty solid starting
#       point.
#
# Revision History:
# v1.0 - Oct 2026 - Initial Release
#
#####
#
# This program accepts a single command line argument 'name.ext'. It can process either
# WAV or MP3 files. This program will print the chord progression and the number of
# beats played for each chord.
#
# Suno does seem to generally stick to the key I was playing in if I use
# an uploaded audio file as the starting point. But when Suno has more
# free rein there can be modulations between keys as well as the use of
# some chords that are in-key but would not be typically used by a beginner
# or even early intermediate player in most situations.
#
# My Python Environment:
# I use pyenv to manage the versions of Python and their associated libraries.
# for this program to work, I used:
#
# pyenv local 3.6
#
# This sets the Python version for a specific directory and its subdirectories.
# It automatically applies whenever you cd into the folder by creating a hidden
# .python-version file
#
# There are dependencies you are likely to have to install.
#
# I had to manually install the Vamp Plugins for things to work.
# This was not particularly difficult, but I encountered some
# stale web links in the process. It is probably best to ask
# Google how to handle this if you have problems. Otherwise
# I suspect any instructions I provided would quickly become
# dated.
#
# I installed mine at /usr/local/lib/vamp
#
# Installation:
# Copy the script to the directory you want to work in and use
# 'python3 chrdprog.py filename.ext' to run the program.
#
# Revision History:
# v1.0 - Oct 2026 - Initial version.
#
# Known Issues:
#   - Limited Error Checking
#
#####

import os
import sys
import librosa
import vamp

# Ensure the user passed at least one argument
if len(sys.argv) < 2:
    print("Error: The first must be the name of the audio file to be analyized.", file=sys.stderr)
    print("Usage: python chrdprog.py filename.ext")
    sys.exit(1)

# 1. Load audio safely
audio_path = sys.argv[1]
try:
    y, sr = librosa.load(audio_path, sr=None, mono=True)
except Exception as e:
    print(f"Error loading audio file: {e}")
    sys.exit(1)

# 2. Extract Beats using Librosa (Handles version variations safely)
print("Tracking beats...")
beat_result = librosa.beat.beat_track(y=y, sr=sr)

# Librosa version compatibility check for unpacking
if isinstance(beat_result, tuple):
    tempo = beat_result[0]
    beat_frames = beat_result[1]
else:
    # Fallback for older versions where it might return a tuple differently
    tempo, beat_frames = beat_result

# Safely extract the raw float array of timestamps
beat_times = [float(t) for t in librosa.frames_to_time(beat_frames, sr=sr)]

# 3. Extract Chords using Chordino safely
print("Extracting chords via Chordino...")
try:
    vamp_output = vamp.collect(y, sr, "nnls-chroma:chordino")
except Exception as e:
    print(f"Vamp library error during chord extraction: {e}")
    sys.exit(1)

# Validate that Chordino actually returned data
if not vamp_output or "list" not in vamp_output or len(vamp_output["list"]) == 0:
    print("Error: Chordino plugin executed but returned zero chords.")
    sys.exit(1)

chord_data = vamp_output["list"]

# Cast tempo safely to a standard Python float
tempo_val = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)
print(f"\nEstimated Tempo: {tempo_val:.2f} BPM")

chord_idx = 0
active_chord = None
chord_start_time = None
beat_count = 0

print("\n--- Chord Timeline (Grouped by Beat Counts) ---")

for beat_t in beat_times:
    # 1. Determine which chord is active at this beat timestamp
    while chord_idx < len(chord_data) - 1 and float(chord_data[chord_idx + 1]["timestamp"]) <= beat_t:
        chord_idx += 1

    detected_chord = str(chord_data[chord_idx].get("label", "Unknown"))

    # 2. Check if the chord has changed
    if detected_chord != active_chord:
        # If this isn't the very first beat, print the summary for the previous chord
        if active_chord is not None:
            time_string = "{:6.2f}".format(chord_start_time)
            print("Start Time: " + time_string + "s | Chord: " + active_chord.ljust(6) + " | Duration: " + str(beat_count) + " beats")

        # Reset trackers for the newly detected chord
        active_chord = detected_chord
        chord_start_time = beat_t
        beat_count = 1
    else:
        # The chord stayed the same, increment the beat counter
        beat_count += 1

# 3. Print the final chord of the song after the loop finishes
if active_chord is not None:
    time_string = "{:6.2f}".format(chord_start_time)
    print("Start Time: " + time_string + "s | Chord: " + active_chord.ljust(6) + " | Duration: " + str(beat_count) + " beats")

print("\n--- Processing Complete ---")
