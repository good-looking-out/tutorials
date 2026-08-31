# How to Use the Groove Pool in Depth

The Groove Pool provides detailed control over how a groove affects timing and velocity, and it can turn the feel of an existing audio or MIDI clip into a reusable groove. Start with [Ableton Live](https://www.ableton.com/en/live/) open, a groove loaded in the Groove Pool, and a looping MIDI clip or warped audio clip assigned to that groove.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/tVG8AOQGmNI?rel=0"
    title="Learn Live: Groove Pool – In depth"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Work from an assigned groove, not only a loaded one

The Groove Pool lists grooves that are loaded in the Set, but its active parameters affect only clips that use each groove. Assign a groove from the Clip View **Groove** chooser, then keep the clip playing while you make adjustments in the Groove Pool. This makes the result immediate and reversible until you commit it.

If a groove is not assigned to any clip, Live shows its parameters dimmed. This is useful for keeping candidates available, but it does not provide an audible reference until you select the groove on a clip.

## Set the rhythmic reference with Base and Quantize

The **Base** chooser sets the timing resolution against which Live measures the groove. For example, at a Base of 1/4, the notes in the groove are compared with the nearest quarter notes; at 1/8, they are compared with the nearest eighth notes. Notes that already fall exactly on the selected grid are not moved by the groove.

**Quantize** controls how much straight quantization Live applies before it applies the groove:

- At 0%, Live leaves the clip’s notes at their original positions before applying the groove.
- At 100%, Live first snaps them to the note values selected in Base, then applies the groove.
- Values in between combine the clip’s original placement with the selected grid reference.

Choose a Base that reflects the rhythmic detail you want to influence. A coarse Base can leave smaller events largely unchanged, while a finer Base can make the groove affect more of the clip. Use Quantize carefully on intentionally loose performances, since a high value can remove timing details before the groove is applied.

## Shape timing, randomization, and velocity independently

**Timing** sets how strongly the groove pattern affects clips that use it. Begin with a moderate setting and increase it only when the timing change supports the part’s role in the arrangement.

**Random** adds random timing fluctuation. Small amounts can make an overly rigid electronic pattern less uniform. Random applies a different offset to every voice in the clip, so notes that originally occur together can move apart. Keep it low when simultaneous notes must stay tightly aligned.

**Velocity** determines how much the velocity information stored in the groove affects clip notes. Its range is −100 to +100. At negative values, the groove’s velocity relationship is reversed: notes that the groove treats as loud become quieter and vice versa. On MIDI clips, use this deliberately to change accents rather than as a substitute for balancing the track.

## Use Global Amount to compare the complete effect

The Groove Pool’s **Global Amount** scales the combined influence of Timing, Random, and Velocity across the available grooves. At 100%, those controls apply at their assigned values; the Amount control can rise to 130% for a more exaggerated result.

Use Global Amount as a final intensity control after setting the individual parameters. This makes it easier to compare a restrained version of the same rhythmic idea with a stronger one. Because it affects the Set’s loaded grooves, check every clip using grooves before leaving it at an extreme value.

## Extract a custom groove from an audio or MIDI clip

You can capture the timing and volume information of an existing audio or MIDI clip as a new groove. Drag the clip to the Groove Pool, or select **Extract Groove** from the clip’s context menu. Live creates a groove from the material in the clip’s playing portion and adds it to the Pool.

Rename the extracted groove so its source and intended use are clear, then use the buttons next to its name in the Groove Pool to save it or hot-swap it. A custom groove can be assigned to other compatible clips in the same way as a library groove.

Extracting is especially useful when one recorded or programmed part has the rhythmic feel you want other parts to follow. Apply the extracted groove selectively and listen for whether it improves the relationship between clips rather than making every part move identically.

## Commit only after checking the resulting clip data

The Clip View **Commit** button writes the current groove settings into the selected clip. For MIDI clips, it moves the notes. For audio clips, it creates Warp Markers at the corresponding positions. After committing, Live changes the clip’s Groove chooser to **None**.

Check audio clips especially carefully before committing. If the groove uses positive velocity values, committing creates a volume clip envelope to translate that velocity information into audio volume changes. This can overwrite an existing volume clip envelope. Duplicate the clip or preserve the envelope first if that automation matters.

Treat the Groove Pool as an editable timing layer while you are choosing a feel. Once Base, Quantize, Timing, Random, Velocity, and Global Amount create the intended result in context, commit only the clips that need permanent edited data.

For current details, see Ableton’s [Using Grooves reference](https://www.ableton.com/en/live-manual/12/using-grooves/), [Clip Groove controls](https://www.ableton.com/en/manual/clip-view/), and [Working with the Browser](https://www.ableton.com/en/live-manual/12/working-with-the-browser/). The source walkthrough is Ableton’s [Learn Live: Groove Pool – In depth](https://www.youtube.com/watch?v=tVG8AOQGmNI).
