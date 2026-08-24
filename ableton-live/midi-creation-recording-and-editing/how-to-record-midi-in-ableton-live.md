# How to Record MIDI in Ableton Live

Recording MIDI turns a performance from a controller or the Computer MIDI Keyboard into an editable MIDI clip. This guide uses the current Ableton Live 12 workflow. Before recording, place an instrument on a MIDI track and make sure Live is receiving MIDI input. The [Ableton Live 12 reference manual](https://www.ableton.com/en/live-manual/12/recording-new-clips/) explains the current recording controls and options in more detail.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/4auPj7yQ3uY?rel=0"
    title="Learn Live: Recording MIDI"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Prepare a MIDI track

MIDI notes do not contain audio by themselves. To hear the performance while recording, the MIDI track needs an instrument or external MIDI destination that responds to those notes.

1. Create or select a MIDI track, then load an instrument onto it.
2. Connect and configure a MIDI controller, or enable Live's Computer MIDI Keyboard if a hardware controller is not available.
3. Click the track's **Arm** button. An armed track is ready to record its selected input, and Live normally monitors that input through the track's device chain.
4. Play a few notes and confirm that the track's MIDI activity indicator responds and that the instrument produces sound.

Clicking an Arm button normally disarms another armed track. To keep several tracks armed, hold `Ctrl` on Windows or `Cmd` on macOS while arming them.

## Choose timing settings before recording

Set up the timing controls before starting a performance. This makes it easier to start on the beat and, when needed, align notes as Live records them.

- In Session View, set **Global Quantization** to a value other than **None**. A one-bar setting is a practical starting point for recording a loop because it starts and ends the clip at bar boundaries.
- Turn on the metronome when a timing reference is useful. Open the menu beside the metronome to choose a **Count-In** length and the metronome sound. When a count-in is selected, Live waits for it to finish before beginning to record.
- To align notes while recording, choose a resolution from **Edit > Record Quantization**. For example, sixteenth-note quantization places recorded note starts on sixteenth-note divisions. Leave this set to **None** when you want to preserve the played timing.

Record Quantization cannot be changed while a Session or Arrangement recording is in progress. It can also be applied later with Live's MIDI editing tools when the musical part needs different treatment.

## Record a looping MIDI pattern in Session View

Session View is useful for building a repeating drum part, bass line, chord loop, or other pattern one layer at a time.

1. Set **Global Quantization** to one bar or another appropriate launch interval.
2. Double-click an empty Session View slot on the MIDI track to create an empty MIDI clip. A newly created clip defaults to a one-bar loop; adjust its loop properties in Clip View if the pattern needs a different length.
3. Arm the MIDI track.
4. Press the Control Bar's **Session Record** button, then play the part. The clip loops while Live adds the notes you play.
5. Press **Session Record** again to stop overdubbing while the clip continues to play. Press it again whenever you are ready to add another pass.

This method is particularly useful for layered drum patterns. Start with a simple rhythm, listen to the loop, and add one group of notes per pass. Use Undo if the latest pass was not useful, or open the clip in the MIDI Editor to correct individual notes.

## Record directly into an empty Session slot

For a performance that should define the clip's length as you play it, use an empty slot's recording control instead of creating the clip first.

1. Arm the MIDI track. Empty slots on the armed track display **Clip Record** buttons.
2. Click the Clip Record button in the target slot, then play the MIDI part.
3. Click that clip's **Launch** button to end recording and begin looping the recorded clip. Use the clip's **Stop** button, or the Control Bar Stop button, when you want playback to stop.

To record new clips into the selected Session scene on every armed track, use the Control Bar's **Session Record** button instead. This is helpful when recording related parts across several MIDI tracks at the same time.

## Record MIDI into the Arrangement

Use Arrangement View when the performance should be recorded along the song timeline instead of into a Session slot.

1. Switch to Arrangement View and place the playback position where the recording should begin. Set a count-in if you need time to prepare.
2. Arm each MIDI track that should record.
3. Start playback and enable the Control Bar's **Arrangement Record** button. Live creates a MIDI clip on every armed MIDI track while recording runs.
4. Stop recording when the performance is complete.

To add notes to an existing MIDI clip in the Arrangement instead of replacing its content, enable **MIDI Arrangement Overdub** before recording. This control applies only to MIDI tracks, so confirm that it is off when a new take is required.

## Review the recorded clip

Double-click the finished clip to open it in Clip View and inspect the MIDI Editor. Check that the recorded notes start where expected, that the clip loops for the intended length, and that the instrument plays the correct sound. You can move, delete, duplicate, or quantize notes after recording without re-recording the part.

For a practical first pass, record a one-bar pattern in Session View with a metronome, add an overdub only after listening to the first loop, then move to Arrangement recording when the part is ready to be performed along the timeline.

## References

- [Ableton Live 12 Reference Manual: Recording New Clips](https://www.ableton.com/en/live-manual/12/recording-new-clips/)
- [Ableton Live 12 Reference Manual: Editing MIDI](https://www.ableton.com/en/live-manual/12/editing-midi/)
- [Learn Live: Recording MIDI](https://www.youtube.com/watch?v=4auPj7yQ3uY)
