# How to Quantize MIDI in Ableton Live

Quantization moves MIDI notes toward a rhythmic grid. It can correct a performance that is slightly early or late, or make an intentionally loose part more consistent without replacing it. Begin with a MIDI clip that contains notes to adjust, then use Live 12's quantization controls to choose the timing target and the degree of correction. Ableton's [Editing MIDI documentation](https://www.ableton.com/en/live-manual/12/editing-midi/) describes the current commands and shortcuts.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/3FlbtZawNTs?rel=0"
    title="Learn Live: Quantizing MIDI"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Choose the notes and timing range

Double-click the MIDI clip to open it in Clip View, then work in the MIDI Note Editor. Select one or more notes when only part of the performance needs correction. This is useful when, for example, the main rhythm is in time but a few chord notes or percussion hits need adjustment.

The Quantize MIDI Tool can also act on a time selection. If neither notes nor time are selected, the tool uses the clip loop as its working range. Define the loop first if the intent is to correct one repeating musical phrase rather than the whole clip.

Before quantizing, listen to the part and decide whether its timing should be made exact or merely tightened. A small amount of natural timing variation can be useful, while a strongly repetitive pattern may benefit from a more exact result.

## Set quantization with the Quantize MIDI Tool

Live 12 provides the Quantize MIDI Tool in Clip View's Transform panel. It gives more control than applying the command alone.

1. Select the target notes or make a time selection in the MIDI Note Editor.
2. Open the Transform panel and choose the **Quantize** MIDI Tool.
3. Choose a quantization value that matches the intended rhythm. The tool can follow the current grid or use a specific metrical value, including triplets.
4. Choose whether the tool affects each note's start, end, or both.
5. Set **Amount** to control how far notes move toward the selected timing position.

An Amount of 100% moves the chosen note position fully to the target. A lower amount moves it only part of the way, retaining some of the original performance timing. Quantizing note ends stretches notes so their end positions land on the selected subdivision; use this when note lengths, rather than note attacks, need to become more regular.

The Transform panel normally applies changes as settings are changed. Turn off **Auto Apply** when you want to adjust the settings before applying the result, then use **Apply** when the result is ready. Use Undo to compare the change with the original performance.

## Apply the current quantization settings quickly

After choosing suitable settings, select the notes to change and use the Quantize command:

- Press `Ctrl`+`U` on Windows or `Cmd`+`U` on macOS to quantize with the current settings.
- Press `Ctrl`+`Shift`+`U` on Windows or `Cmd`+`Shift`+`U` on macOS to open **Quantize Settings** before applying the command.

The shortcut is useful for repeated corrections, such as aligning individual drum hits after a recorded pass. Reopen Quantize Settings when the rhythm changes from straight notes to a different subdivision or a triplet feel.

## Preserve a musical feel

Choose the coarsest grid that describes the rhythmic role of the notes. For instance, quantizing sustained chords to short subdivisions can make their attacks overly rigid, while a faster melodic run may require a smaller value to avoid moving notes to unintended beats.

For a controlled but less mechanical result, begin with a moderate Amount and audition the clip in context with the rest of the Set. Increase the Amount only when the remaining timing variation is a problem. Quantize related notes together when their relationship matters, such as a chord or a layered kick and bass accent.

## Quantize as you record

To apply a fixed timing grid during recording, choose **Edit > Record Quantization** and select the desired metrical division before starting to record. Live applies that setting to incoming MIDI notes as they are recorded.

Record Quantization cannot be changed while Session or Arrangement recording is active. It is most useful for parts that must immediately conform to a defined rhythmic structure; for expressive performances, recording without it and applying quantization afterward provides more control over the selection and Amount.

## Use quantization as a correction, not a substitute for editing

Quantize the smallest useful part of a performance, then listen for timing relationships and note lengths that still need attention. Individual notes can be moved or resized afterward, and a partial Amount can retain the character of the original playing while improving its rhythmic placement. See [How to Edit MIDI Notes in Ableton Live](how-to-edit-midi-notes-in-ableton-live.md) for the complementary note-editing workflow.

## References

- [Ableton Live 12 Reference Manual: Editing MIDI](https://www.ableton.com/en/live-manual/12/editing-midi/)
- [Ableton Live 12 Reference Manual: MIDI Tools](https://www.ableton.com/en/live-manual/12/midi-tools/)
- [Ableton Live 12 Reference Manual: Recording New Clips](https://www.ableton.com/en/live-manual/12/recording-new-clips/)
- [Learn Live: Quantizing MIDI](https://www.youtube.com/watch?v=3FlbtZawNTs)
