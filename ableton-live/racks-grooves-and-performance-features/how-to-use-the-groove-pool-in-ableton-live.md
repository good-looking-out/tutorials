# How to Use the Groove Pool in Ableton Live

The Groove Pool lets you apply the timing and velocity feel of a groove file to MIDI clips and warped audio clips. It is useful for adding swing, a looser feel, or a shared rhythmic character without permanently changing the clips. Start with [Ableton Live](https://www.ableton.com/en/live/) open and one or more clips ready to audition.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/jvT8mNCKLDg?rel=0"
    title="Learn Live: Groove Pool"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Understand what the Groove Pool changes

A groove changes the rhythmic feel of an individual clip. Live’s library grooves are `.agr` files, and the timing pattern in the selected file is applied to the clip without immediately rewriting its notes or warp markers.

Grooves work with both MIDI and audio clips. On MIDI clips, a groove affects note timing and can affect note velocity. On audio clips, it adjusts warp behavior, so the clip must have **Warp** enabled before a groove can take effect. Begin with a loop whose original timing is clear enough that you can hear the difference.

## Open the Groove Pool and load a groove

Open or close the Groove Pool from the Browser view control menu, or use `Ctrl`+`Alt`+`6` on Windows or `Cmd`+`Option`+`6` on Mac. The Groove Pool holds grooves that are already assigned to clips as well as grooves you load in advance. Grooves that no clip is currently using appear with their parameters dimmed.

Find a groove in Live’s Browser, then use either of these approaches:

- Drag the groove directly onto a clip to load and assign it in one action.
- Double-click a groove to add it to the Groove Pool first, then choose it from a clip’s Groove chooser.

Loading several candidate grooves into the Pool lets you compare them from the same list while keeping the clips in place.

## Assign a loaded groove to a clip

Select the target clip and locate its **Groove** chooser in Clip View. The chooser lists the grooves currently available in the Groove Pool. Choose one, then play the clip with the rest of the Set to hear how it changes the timing and feel.

You can assign different grooves to different clips. For example, a percussion clip can use a more pronounced swing while a bass clip uses a subtler groove or none at all. Avoid assuming that every clip should share the same groove; a shared rhythmic feel is useful only when the parts still work together.

## Audition alternative grooves efficiently

Use the clip’s **Hot-Swap Groove** button to try grooves from the Browser while the clip plays. Select a groove in the Browser and double-click it or press `Enter` to load it on the clip. This replaces the groove that was previously loaded in both the clip and the Groove Pool.

Compare alternatives at the same tempo and with related tracks playing. Listen for whether the clip reinforces the rhythmic relationship you want, rather than selecting a groove only because it makes the part more noticeably late or early.

## Keep the groove editable until the result is settled

As long as a clip has a groove selected in its Groove chooser, you can change the selection or adjust the groove from the Groove Pool. This makes it practical to test the same groove on several clips before deciding which combination works.

Use the Groove Pool’s **Global Amount** control to scale the overall influence of the loaded grooves across the Set. Start with a moderate amount if the effect feels too strong, then adjust only after the clips have been assigned and compared together. The individual timing, quantization, random, and velocity settings are available in the Groove Pool when you need more detailed control.

Press **Commit** in the Clip View only when you intend to write the current groove settings into the clip. Committing moves MIDI notes or creates Warp Markers for audio, then resets the clip’s Groove chooser to **None**. In an audio clip, committing a groove with positive velocity information also creates a volume clip envelope and can overwrite an existing volume envelope.

Use the Groove Pool first as a reversible way to compare timing feels, then commit only the clips whose result is final. This preserves the flexibility to match a groove to each musical role while keeping the Set’s rhythm intentional.

For current details, see Ableton’s [Using Grooves reference](https://www.ableton.com/en/live-manual/12/using-grooves/), [Clip Groove controls](https://www.ableton.com/en/manual/clip-view/), and [Live keyboard shortcuts](https://www.ableton.com/en/manual/live-keyboard-shortcuts/). The source walkthrough is Ableton’s [Learn Live: Groove Pool](https://www.youtube.com/watch?v=jvT8mNCKLDg).
