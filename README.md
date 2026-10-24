# chrdprog
When creating music on Suno, I typically will play rhythm with the guitar and let the vocals drive melodies. But sometimes I let Suno do the driving and I just provide the lyrics and a description of the sound and feel I'm looking for. That has led to some happy outcomes, but the problem is that if I want to later play that song on the guitar, it can be difficult to figure out the details of the chord progression and timing Suno came up with.

The address that I wrote this program to determine chord progressions along with a count of the beats used in a piece of music.

With Suno v6 you have the option of downloading the Stems. Typically I will do this and pick out the rhythm guitar part of run this program against. Results can be mixed if you try the full mix. There are tools to break out Stems from other music sources if you want to use this on existing songs.

The start of a sample run of this might look something like this:
```
$ python chrdprog.py secret.wav
Tracking beats...
Extracting chords via Chordino...

Estimated Tempo: 133.93 BPM

--- Chord Timeline (Grouped by Beat Counts) ---
Start Time:   0.38s | Chord: E      | Duration: 12 beats
Start Time:   5.79s | Chord: C#m    | Duration: 4 beats
Start Time:   7.58s | Chord: A      | Duration: 4 beats
Start Time:   9.38s | Chord: B      | Duration: 4 beats
Start Time:  11.18s | Chord: E      | Duration: 4 beats
Start Time:  12.99s | Chord: C#m    | Duration: 4 beats
Start Time:  14.81s | Chord: A      | Duration: 4 beats
Start Time:  16.61s | Chord: B      | Duration: 4 beats
Start Time:  18.42s | Chord: E      | Duration: 4 beats
Start Time:  20.22s | Chord: C#m    | Duration: 4 beats
Start Time:  22.04s | Chord: A      | Duration: 4 beats
Start Time:  23.84s | Chord: B      | Duration: 4 beats
...
```
This shows the start of a song that is in the Key of E and in 4:4 time. There are two bars of intro then it hits the chord progression of E Cm A B (or I vi IV V). When I was working on a version to play on the guitar, I ended up transposing this to the Key of G so I could use relatively easy to play chords (G Em C D) which also better suited my voice.

Some times it is easy to play in the same key as Suno by using a capo--other times (like this), not so much...

## Shameless Plug

You can listen to music by The Daft Spaniels on most streaming platforms as well as on Facebook and YouTube. The music covers a variety of styles and genres. It is about learning and having fun while making music that allows expression.

## The Fine Print
Suno is a registered trademark of Suno, Inc., a generative artificial intelligence music company based in Cambridge, Massachusetts.

This script is intended for personal use only. The user accepts responsibility for ensuring their use of this script does not violate any terms, conditions, or policies of platforms as Suno.

To the extent applicable, any original work herein is Copyright 2026 by James McClanahan.

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. 
- **Open Source:** Anyone can use, modify, and distribute this software for free.
- **Share Alike:** If you modify this code or use it in your own project, your derivative work **must** also be open-sourced under the GPLv3.
- **No Commercial Lock-in:** You cannot use this code in proprietary (closed-source) software.
- **License Inclusion:** You must include the original copyright notice and a copy of the GPLv3 license with any distribution.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
