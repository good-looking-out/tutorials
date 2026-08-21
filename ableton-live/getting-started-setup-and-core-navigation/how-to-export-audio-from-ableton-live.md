# How to Export Audio from Ableton Live

Exporting renders audio from an [Ableton Live](https://www.ableton.com/en/live/) Set into files for listening, delivery, further mixing, or use in another application. Before opening the export dialog, choose the exact time range and the signal you need to render.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/JTtSihQ8QX0?rel=0"
    title="Learn Live: Exporting"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Set the render range first

In Arrangement View, create a time selection or set the loop brace to the beginning and end of the material to export. Leave room after the final event for delay, reverb, or other effect tails when they are part of the intended result.

Listen through the full selected range before exporting. Check the Main output level for clipping, confirm that the correct scenes or arrangement content are playing, and make sure any automation is active.

## Open the Export Audio/Video dialog

Choose **File > Export Audio/Video** or press `Cmd`+`Shift`+`R` on macOS or `Ctrl`+`Shift`+`R` on Windows. Live opens its render dialog with a selection range, rendered-track chooser, rendering options, and file-format choices.

Confirm the start and length before proceeding. Do not assume that a loop brace or time selection still covers the complete song after editing the arrangement.

## Choose the rendered signal

Select the rendered track according to the delivery:

- Choose **Main** for the post-fader Main output—the result normally matches what you monitor from the Main output.
- Choose **All Individual Tracks** to create separate files for tracks and returns.
- Choose **Selected Tracks Only** when exporting a deliberate subset.

When exporting individual or selected tracks, review whether return and Main effects should be included. Including them can be useful for a reference mix, while omitting them is often appropriate for stems that will be mixed elsewhere. Always label and test exported stems before sending them.

## Select rendering and file options

Choose a sample rate and bit depth that match the destination’s requirements. WAV, AIFF, and FLAC are common PCM choices; use an additional MP3 only when a compressed listening copy is needed. Keep an uncompressed master or stem version for further work.

Use **Normalize** only when you want Live to raise the rendered file to its maximum available level. It changes the rendered level, so leave it off when preserving a mix level for mastering or comparison. Dither is relevant when reducing bit depth; select it deliberately rather than treating it as a general sound-improvement switch.

If the export is intended to loop, use the render-as-loop option only after checking the boundaries. It applies small fades to help avoid clicks, but it cannot correct a musically mismatched loop point.

## Export and check the result

Click **Export**, choose a clear filename and destination, and wait for rendering to finish. Open the rendered file in a dependable audio player or import it into a blank Live Set. Check its length, beginning and end, channel format, level, and effect tails before deleting an earlier version or delivering it.

For multiple versions, include the date or purpose in the name, such as `song-title-mix-v03` or `song-title-stems-48k`. Ableton’s [Exporting Audio and Video manual section](https://www.ableton.com/en/live-manual/12/managing-files-and-sets/) documents the dialog’s current options. The source walkthrough is [Learn Live: Exporting](https://www.youtube.com/watch?v=JTtSihQ8QX0).
