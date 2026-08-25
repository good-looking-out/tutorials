# How to Edit MIDI Notes in Ableton Live

Ableton Live represents the pitch, timing, length, and velocity of a MIDI performance as editable notes in the MIDI Note Editor. Use it to correct a recording, program a pattern, or reshape an existing musical part without recording it again. This guide uses the current Live 12 MIDI Note Editor; Ableton's [Editing MIDI](https://www.ableton.com/en/live-manual/12/editing-midi/) reference explains its full set of controls.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/14biudaGwdM?rel=0"
    title="Learn Live 12: Editing MIDI Notes"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Open the MIDI Note Editor

Double-click a MIDI clip to open Clip View, then select the **Notes** tab in its header. The MIDI Note Editor uses a horizontal time ruler and a vertical note ruler: move right to work later in the clip and move up to work at higher pitches. A Drum Rack replaces the piano-style pitch rows with its drum-pad rows.

The grid chooser at the upper-right of the editor controls the resolution used for most note placement and editing operations. Choose a grid that matches the detail of the part—for example, a sixteenth-note grid for a typical drum pattern—before moving or drawing notes.

To make the editor easier to read:

- Drag in the time ruler to move through the clip or change the time zoom.
- Scroll the note ruler to reveal other octaves or drum-pad rows.
- Use **Fold** to show only rows that contain notes. This is especially useful for a Drum Rack.
- When the clip uses Scale Mode, use **Highlight Scale** or **Scale** to make the active scale easier to see or to fold the editor to its scale rows.

## Select notes before editing

Most MIDI editing operations apply to the current selection. Click a note to select it, drag across several notes to select a group, or hold `Shift` while clicking to add or remove individual notes from the selection. Press `Esc` or click outside the selection to deselect it.

Dragging across an empty area creates a time selection. If that time range contains notes, Live selects those notes as well. This makes it practical to edit every note in a bar or beat together rather than selecting them one by one.

Enable the **Preview** switch above the piano ruler when you want to hear pitches while adding, moving, or selecting notes. It requires an instrument on the track and is particularly useful when correcting a melody by ear.

## Add, delete, and move notes

There are two straightforward ways to add notes:

- Double-click an empty position in the grid to create a note at that pitch and time.
- Turn on **Draw Mode** with the Control Bar button or the `B` key, then click and drag in the grid to draw notes.

With Draw Mode turned off, drag a note horizontally to change its timing or vertically to transpose it. The arrow keys provide the same types of adjustment for selected notes: left and right move them in time, while up and down transpose them. The current grid determines the usual increments and snapping behavior.

To remove a note while Draw Mode is off, double-click it. In Draw Mode, clicking an existing note deletes it. Use the Edit menu's Undo command whenever an edit produces an unwanted result.

## Change note length and timing

Drag either edge of a note to change its duration. The note snaps according to the current grid as you extend or shorten it, which helps keep repeated parts aligned. You can also hold `Shift` and press the left or right arrow key to adjust the duration of selected notes by the current grid increment.

When several notes or a time range are selected, Note Stretch markers appear below the editor's scrub area. Drag a marker horizontally to stretch or compress the selection proportionally while preserving the relative spacing of the notes. Use this when a phrase should fit a longer or shorter section without manually moving each note.

If a note needs to be divided, select it and use **Chop Note(s) on Grid** from the Edit or context menu. The `Ctrl`+`E` shortcut on Windows or `Cmd`+`E` on macOS also chops selected notes according to the grid. With no note selection, the same shortcut splits notes that intersect the insert marker or a time selection.

To combine adjacent notes, select notes on the same pitch row and use **Join Notes**, or press `Ctrl`+`J` on Windows or `Cmd`+`J` on macOS. Live creates one note from the selected notes on that row.

## Adjust note velocity

Velocity determines how strongly a MIDI note is played. In the MIDI Note Editor, a note's color saturation indicates its velocity: less saturated notes are softer, while more saturated notes are louder.

Use the **Velocity Editor** lane below the notes to adjust this value precisely:

1. Select a note or its velocity marker.
2. Drag the marker up or down to raise or lower its velocity.
3. For an exact value, select the marker, type a number, and press `Enter`.

Select several velocity markers to change a group together. This is useful for making repeated drums consistent, creating a deliberate accent, or shaping a gradual dynamic change. The lane's controls can also randomize or ramp velocities across a selected group when a fixed value is not appropriate.

## Review the edited part

Play the clip after a focused group of changes and check the rhythm, pitch, note lengths, and dynamics together. Work in small selections so that an edit has a clear musical purpose, then use Undo if the result is less suitable than the previous version.

MIDI note edits remain editable in the Live Set. If the clip came from an imported MIDI file, changing it in Live does not alter the original file on disk.

## References

- [Ableton Live 12 Reference Manual: Editing MIDI](https://www.ableton.com/en/live-manual/12/editing-midi/)
- [Learn Live 12: Editing MIDI Notes](https://www.youtube.com/watch?v=14biudaGwdM)
