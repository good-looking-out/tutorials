# How to Edit MIDI Clips in Ableton Live

A MIDI clip defines when a group of MIDI notes starts, ends, and repeats. Editing the clip is different from editing its individual notes: clip controls shape the playback region and structure of the pattern, while the MIDI Note Editor changes the notes inside it. This guide uses Live 12's Clip View. Refer to Ableton's [Clip View documentation](https://www.ableton.com/en/live-manual/12/clip-view/) for the current control reference.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/_gDAcf0EUUY?rel=0"
    title="Learn Live: Editing MIDI clips"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Open Clip View and identify the playback region

Double-click a MIDI clip in Session View or Arrangement View to open it in Clip View. The Main Clip Properties panel contains the clip's start and end controls, along with its loop controls. The MIDI Note Editor shows the same material graphically on the right.

Two related regions determine what you hear:

- The **clip start** and **clip end** define the playable extent of the clip.
- The **loop position** and **loop length** define the part that repeats when **Clip Loop** is enabled.

An unlooped MIDI clip plays once from its start point to its end point, unless it is stopped. A looped clip repeatedly plays the loop region. Keep this distinction in mind before changing markers: shortening the clip end controls how long an unlooped clip can play, while shortening the loop length changes what repeats.

## Set and adjust a MIDI clip loop

Use the loop controls when a pattern should repeat at a defined length, such as a one-bar drum part or a four-bar chord progression.

1. Select the clip and open Clip View.
2. Turn on **Clip Loop**.
3. Set the **Loop Position** and **Loop Length** fields to the musical range that should repeat.
4. Alternatively, drag the loop start and end markers in the MIDI Note Editor to adjust the loop brace directly.

The loop region can be changed while the clip plays, which is useful for auditioning a smaller phrase before committing to a new loop length. Turn off **Clip Loop** when the MIDI pattern should play through only once.

You can also use the **Set** buttons beside the loop controls to establish a loop during playback. The current playback position becomes the loop start or end, rounded according to Global Quantization.

## Duplicate a loop to extend a pattern

Duplicating the loop is a quick way to turn a short idea into a longer arrangement block without copying notes by hand.

Select the loop brace in the MIDI Note Editor and press `Ctrl`+`D` on Windows or `Cmd`+`D` on macOS. Live doubles the loop length and copies the notes from the original loop into the new section. Any notes after the loop move to the right so they retain their position relative to the loop's end.

Use this method before making a variation. For example, duplicate a one-bar rhythm to make a two-bar clip, then alter only the second bar in the MIDI Note Editor. The first bar remains a reference while the new section develops the pattern.

## Restructure time inside a MIDI clip

Clip-level time commands change the structure of the material, not only the selected notes. First drag in the MIDI Note Editor to create the time range that should be affected, then use the relevant command from the Edit or context menu:

- **Duplicate Time** copies the selected timespan and its contained notes into the clip.
- **Delete Time** removes the selected duration and closes the gap by moving later notes earlier.
- **Insert Time** adds empty time before the selection and moves later notes later.

These commands do not change the clip start or end positions, or the loop brace settings. Review the resulting loop after a structural change so the repeated region still begins and ends at the intended musical points.

## Crop unused MIDI data deliberately

Recorded or imported clips can contain notes outside the active loop. Once the loop and clip region are correct, right-click the clip in Session View or Arrangement View and choose **Crop Clip** to delete MIDI data outside the loop brace.

If a time selection is active, use **Crop to Time Selection** instead to keep only that selected duration. Cropping a MIDI clip does not create or modify a separate file on disk, but it does remove the excluded notes from the clip, so audition the result first and use Undo if needed.

## Move from clip structure to note detail

Start by defining the clip's playback range and loop, then duplicate or restructure time only when the overall pattern needs to change. After the clip plays at the right length, use the MIDI Note Editor to refine individual pitches, timings, lengths, and velocities. See [How to Edit MIDI Notes in Ableton Live](how-to-edit-midi-notes-in-ableton-live.md) for that note-level workflow.

## References

- [Ableton Live 12 Reference Manual: Clip View](https://www.ableton.com/en/live-manual/12/clip-view/)
- [Ableton Live 12 Reference Manual: Editing MIDI Clips](https://www.ableton.com/en/live-manual/12/editing-midi/)
- [Learn Live: Editing MIDI clips](https://www.youtube.com/watch?v=_gDAcf0EUUY)
