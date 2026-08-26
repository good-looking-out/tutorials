# How to Sequence MIDI in Ableton Live: Part 2

Once a MIDI clip contains notes, efficient sequencing depends on being able to focus on the useful pitches, timing range, and expression data. This follow-up covers the Live 12 MIDI Note Editor controls for folding, navigation, and velocity. Begin with a MIDI clip that already contains notes; see [How to Sequence MIDI in Ableton Live: Part 1](how-to-sequence-midi-in-ableton-live-part-1.md) for creating and placing them. Ableton's [Editing MIDI documentation](https://www.ableton.com/en/live-manual/12/editing-midi/) is the current reference for these controls.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/Paq66RsgpIk?rel=0"
    title="Learn Live: Sequencing MIDI – part 2"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Fold the editor to the pitches in use

Open the MIDI clip in Clip View and select the **Notes** tab. A pattern with notes spread over several octaves can leave many empty rows in the MIDI Note Editor. To hide those unused key tracks, activate **Fold to Notes** with the **Fold** button in the Clip View header, or press `F` while the MIDI Note Editor has focus.

Fold to Notes retains the rows that contain MIDI notes and hides the rest. It is particularly helpful when editing a Drum Rack pattern, where the available pads can span a wide range of pitches. Press **Fold** or `F` again to restore the full set of rows.

Folding is a display choice that applies across the Live Set. The rows visible in each clip still depend on the notes that exist in that clip, so check the displayed pitches when you switch to another MIDI clip.

## Zoom to the notes or phrase you need to edit

Select a note or drag to select a time range, then press `Z` to zoom fully into that selection. Press `X` to zoom back out to the full clip. This is useful when a short fill or melodic movement needs detailed editing without losing the ability to return to the complete pattern.

Use `+` and `-` to zoom horizontally around the current selection. You can also adjust the time view by dragging vertically in the time ruler, or scroll left and right by dragging horizontally in that ruler. In the note ruler, scroll to move through octaves and drag horizontally to change the vertical zoom level.

For more editing space, drag the divider between the main Session or Arrangement area and Clip View. Use `Ctrl`+`Alt`+`E` on Windows or `Cmd`+`Option`+`E` on macOS to toggle Clip View to full height.

## Show and resize the velocity lane

The **Velocity Editor** appears below the MIDI Note Editor by default. If it is hidden or another expression editor is visible, use the triangular Lane Selector in the lane header to show the appropriate lane. Drag the divider between the note grid and the editor lanes to give velocity data more space, or to reduce it when pitch and timing need more room.

The Lane Selector can also show the Chance Editor, while the Show/Hide All Expression Editors control lets you collapse or reveal the enabled lanes together. Keep the Velocity Editor visible when you are shaping performance dynamics; hide it temporarily when its extra height makes note placement harder to read.

## Shape velocity as part of the sequence

Each MIDI note has a velocity value that influences how strongly an instrument responds. In the MIDI Note Editor, higher-velocity notes appear more saturated; the matching marker in the Velocity Editor shows its value directly.

To adjust a note's velocity, click and drag its marker up or down in the Velocity Editor. Hover over a note to highlight the matching marker when several notes occur at the same time. You can also select several markers with `Shift` and adjust them together, which is useful for setting a consistent group of hi-hats, chord tones, or repeated bass notes.

For a faster single-note adjustment, select the note and hold `Alt` on Windows or `Cmd` on macOS while dragging it vertically in the MIDI Note Editor. Use velocity deliberately: a repeated pattern can remain rhythmically exact while changes in velocity establish accents and movement.

## Return from detail to the whole pattern

Fold, zoom, and lane resizing are editing aids rather than changes to the musical material. Use them to isolate a problem area, make the needed note or velocity adjustment, then zoom back out and audition the entire clip in context.

Keeping the timing, pitch layout, and velocity shape readable makes it easier to develop a longer sequence without losing the role of each note. After refining the pattern, use quantization only where timing needs correction rather than as a substitute for these deliberate editing choices.

## References

- [Ableton Live 12 Reference Manual: Editing MIDI](https://www.ableton.com/en/live-manual/12/editing-midi/)
- [Ableton Live 12 Reference Manual: Live Keyboard Shortcuts](https://www.ableton.com/en/live-manual/12/live-keyboard-shortcuts/)
- [Ableton Live 12 Reference Manual: Clip View](https://www.ableton.com/en/live-manual/12/clip-view/)
- [Learn Live: Sequencing MIDI – part 2](https://www.youtube.com/watch?v=Paq66RsgpIk)
