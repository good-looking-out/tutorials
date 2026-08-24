# How to Capture MIDI in Ableton Live

Capture MIDI retrieves MIDI notes that you have just played without first turning on Live's recording controls. It is useful when improvising, testing a sound, or recovering an idea after forgetting to record. This guide covers the current Ableton Live 12 behavior. You need a MIDI input source and an eligible MIDI track before you begin; see Ableton's [Recording New Clips](https://www.ableton.com/en/live-manual/12/recording-new-clips/) documentation for the complete reference.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/aJg1UfePwTc?rel=0"
    title="Learn Live: Capturing MIDI"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Make a MIDI track eligible for Capture

Live listens to MIDI input on armed or input-monitored tracks. The simplest setup is a MIDI track containing an instrument, with its **Arm** button enabled so you can both hear and capture the notes you play.

1. Create or select a MIDI track and load an instrument onto it.
2. Connect and configure a MIDI controller, or enable Live's Computer MIDI Keyboard.
3. Click the track's **Arm** button and play a few notes to confirm that the instrument responds.

Capture MIDI retrieves incoming MIDI notes, not audio. If a track is not armed, it must be input-monitored for Capture to retain the notes played on it.

## Play before pressing Record

Do not turn on Arrangement Record or Session Record for the phrase you intend to capture. Play naturally, experiment with a rhythm or melody, and press the Control Bar's **Capture MIDI** button when there is a performance worth keeping.

When Capture needs to infer tempo from an otherwise empty, stopped Set, finish the phrase on the first beat of the next bar when possible. This gives Live a clear downbeat from which to identify the phrase and create its loop.

## Capture MIDI in a new, stopped Set

Capture behaves differently when the Set has no other clips and the transport is stopped. In this situation, it can infer the tempo and loop from the performance.

1. Choose either Session View or Arrangement View. With a new Set, Capture creates clips in the view that currently has focus.
2. On an armed or input-monitored MIDI track, play the phrase you want to keep.
3. Press **Capture MIDI** in the Control Bar.

Live creates a new clip containing the played phrase on each monitored MIDI track. It detects and sets a tempo between 80 and 160 BPM, chooses loop boundaries, places the notes on the grid, and begins playback of the captured loop.

Capture retains the full performance, including notes that occurred before the detected phrase. Those earlier notes appear before the clip's start marker, so you can adjust the clip or loop boundaries if Live chose a different phrase than intended.

## Capture MIDI in an existing Set

When the transport is running, the Set already contains clips, or tempo automation is in use, Capture preserves the existing song tempo. It uses that tempo to identify a meaningful phrase from the material you played and creates a loop from it.

1. Keep the Set playing, or work in a Set that already contains clips.
2. Play a MIDI part on an armed or input-monitored track without engaging the usual recording controls.
3. Press **Capture MIDI** when the phrase is complete.
4. Open the resulting clip and confirm its loop length and note placement.

You can also play along with an existing, playing MIDI clip on the same track. Pressing **Capture MIDI** adds the material you just played to that clip, allowing a pattern to be built up in layers without starting a conventional recording pass.

## Refine the captured result

Double-click the captured clip to open its MIDI Editor. Review the note timing, loop brace, and start and end markers before building on the part.

- Move the clip start, end, or loop markers when a different section of the played material should repeat.
- To remove retained notes outside the desired loop, right-click the clip and choose **Crop Clip**.
- Edit individual notes in the MIDI Editor when the captured phrase needs a timing, pitch, length, or velocity adjustment.

Capture MIDI is most useful as a low-pressure starting point: improvise without committing to a record pass, recover the useful phrase, then refine its loop or continue arranging it in the Set.

## References

- [Ableton Live 12 Reference Manual: Capturing MIDI](https://www.ableton.com/en/live-manual/12/recording-new-clips/)
- [Ableton Live 12 Reference Manual: Editing MIDI](https://www.ableton.com/en/live-manual/12/editing-midi/)
- [Learn Live: Capturing MIDI](https://www.youtube.com/watch?v=aJg1UfePwTc)
