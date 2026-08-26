# How to Sequence MIDI in Ableton Live: Part 1

Sequencing MIDI is the process of placing and arranging notes directly in a MIDI clip. It is useful when you want to create a drum pattern, bass line, melody, or chord part without performing it in real time. Start with a MIDI track that contains an instrument or is routed to an external MIDI device. This guide uses Live 12's MIDI Note Editor; Ableton's [Editing MIDI documentation](https://www.ableton.com/en/live-manual/12/editing-midi/) provides the current interface reference.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/1cFTonBejIQ?rel=0"
    title="Learn Live: Sequencing MIDI – part 1"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Create an empty MIDI clip

The source video begins in Session View. Double-click an empty Session slot on a MIDI track to create a new MIDI clip and open it in Clip View. Alternatively, select an empty Session slot and use **Create > Insert Empty MIDI Clip(s)**, or press `Ctrl`+`Shift`+`M` on Windows or `Cmd`+`Shift`+`M` on macOS.

You can also sequence in Arrangement View. Double-click the track display on a MIDI track, or select a timespan and insert an empty MIDI clip. In either view, double-click the resulting clip when necessary to open Clip View, then select the **Notes** tab to show the MIDI Note Editor.

The editor displays pitch vertically and musical time horizontally. Make the Clip View taller if needed so that note placement, the keyboard ruler, and the lower expression lanes are easy to read.

## Add notes with the mouse or Draw Mode

Place a single note by double-clicking a position in the MIDI Note Editor. Its vertical position sets its pitch, and its horizontal position sets when it plays in the clip.

For faster pattern entry, press `B` to enable **Draw Mode**, then click and drag in the editor to draw notes. Press `B` again to return to normal editing. In Draw Mode, clicking an existing note deletes it, so switch out of Draw Mode before selecting or repositioning existing notes.

Turn on the **Preview** switch above the piano ruler to hear notes as you add, select, or move them. Preview requires an instrument in the MIDI track's device chain. It helps you build a pattern one sound at a time without repeatedly launching the whole clip.

## Set a useful grid before placing a rhythm

The grid controls the rhythmic increments used while placing and editing notes. Use the grid setting at the right side of the Clip View header to select a suitable division for the pattern. A smaller division is useful for fast notes; a larger division keeps a simple kick, bass, or chord rhythm easier to read.

With snapping enabled, note positions and lengths align to the grid. Toggle snapping with `Ctrl`+`4` on Windows or `Cmd`+`4` on macOS when a freely placed note is needed. You can also temporarily bypass the current snapping behavior while editing by holding `Alt` on Windows or `Cmd` on macOS.

Choose the grid based on the rhythmic role, not simply the smallest available division. Starting with a larger grid makes it easier to establish the main pulse; refine only the notes that require additional detail.

## Move notes to set pitch and timing

Turn Draw Mode off, then drag a note horizontally to change its time and vertically to transpose it. Select several notes first when a phrase, chord, or drum figure should move together. The arrow keys provide the same two directions: left and right change timing, while up and down change pitch. Hold `Shift` with the up or down arrow to transpose selected notes by octaves.

To create a variation without replacing the original, hold `Ctrl` on Windows or `Option` on macOS while dragging selected notes to copy them. This is useful for extending a short motif into a longer loop before changing the copied notes.

When moving notes, use the grid to preserve the intended rhythm. If a played part has a deliberate offset, temporary snap bypass lets you retain that timing rather than forcing it onto a grid line.

## Adjust note lengths and shape the velocity

Drag either edge of a note to make it shorter or longer. The same grid and snap behavior applies to note length, so use the current division for rhythmic durations or hold the temporary snap-bypass modifier for a freely placed edge. Adjusting lengths is especially important for sustained bass notes and chords, where overlap and release change the musical result.

Use the **Velocity Editor** below the MIDI Note Editor to shape how strongly notes play. Click and drag a note's velocity marker up or down to change its value. Live highlights the corresponding marker when you hover over a note, which helps when several notes occur at the same time.

Use a consistent velocity for an even machine-like pattern, or vary selected markers to emphasize an accent, backbeat, or melodic phrase. Velocity is part of the MIDI clip, so it can be adjusted independently of a note's pitch, start time, and duration.

## Audition and refine the sequence

Launch the clip from its Session slot, or play the relevant Arrangement section, as you work. Begin with a short loop and establish its main rhythm before adding detail. Then refine one dimension at a time: timing, pitch, length, or velocity.

If notes need a timing correction after they are placed, use the current quantization controls rather than redrawing the whole phrase. See [How to Quantize MIDI in Ableton Live](how-to-quantize-midi-in-ableton-live.md) for that workflow. A simple, playable sequence is a useful starting point for the more advanced sequencing methods covered in later MIDI workflows.

## References

- [Ableton Live 12 Reference Manual: Editing MIDI](https://www.ableton.com/en/live-manual/12/editing-midi/)
- [Ableton Live 12 Reference Manual: Clip View](https://www.ableton.com/en/live-manual/12/clip-view/)
- [Ableton Live 12 Reference Manual: Session View](https://www.ableton.com/en/live-manual/12/session-view/)
- [Learn Live: Sequencing MIDI – part 1](https://www.youtube.com/watch?v=1cFTonBejIQ)
