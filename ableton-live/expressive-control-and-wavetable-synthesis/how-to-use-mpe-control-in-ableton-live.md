# How to Use MPE Control in Ableton Live

MPE Control is a MIDI effect that reshapes the Press, Slide, and per-note pitch-bend data arriving from an MPE controller before it reaches an instrument. Use it to make a small physical gesture produce a more deliberate response, limit a gesture’s range, or convert MPE sources into conventional global MIDI controls for an instrument that does not accept MPE. Ableton describes MPE Control as a Max for Live MIDI effect, and its current [Live edition comparison](https://www.ableton.com/en/live/compare-editions/) lists the device in Live 12 Intro, Standard, and Suite. An MPE-capable controller and an MPE-enabled input are required to process live expressive gestures.

The source video uses the Live 11 interface. This guide uses current Live 12 control names: **Press**, **Slide**, and **NotePB**.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/TW5zHEIAGPo?rel=0"
    title="Learn Live: MPE Control"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Place MPE Control before the instrument

Connect the MPE controller and enable its **MPE** button in Live’s **Settings** under **Link, Tempo & MIDI**. On the receiving MIDI track, add **MPE Control** before the instrument it should affect. The device must come earlier in the MIDI device chain so that the instrument receives MPE Control’s processed data.

MPE Control is available from Live’s MIDI Effects and can also be found through the **Max for Live** browser label. Start with an instrument or preset that has an audible MPE response. MPE Control changes the incoming expression values; it does not decide by itself which instrument parameter those values control.

Before adjusting a curve, play and record a few notes with the device at its default settings. This confirms that the controller, input port, and receiving instrument are already communicating correctly.

## Select the expression source to shape

The source chooser selects one of three independently processed signals:

- **Press** processes MPE pressure, which is created by changing pressure after striking a key or pad.
- **Slide** processes vertical-position data from an MPE controller.
- **NotePB** processes the controller’s per-note pitch bend.

Select one source, then make a single target response easy to hear. For example, use a preset in which pressure already influences a timbral parameter, then select **Press** in MPE Control. Testing one source at a time makes it clear whether a change comes from the controller, MPE Control, or the receiving instrument’s mapping.

Each source can be disabled independently. Turn off sources that are not part of the sound design so accidental pressure, slide, or pitch movements do not reach the instrument.

## Set the response curve and range

Choose a **linear** curve for a two-breakpoint response or an **S-shaped** curve for a three-breakpoint response. A linear curve is a good starting point when the goal is simply to compress the lower range of a gesture or reach higher values with less movement.

Use the **Curve** control or drag directly in the display to reshape the selected source. Set **Min** and **Max** to limit the output range. This is useful when a filter opens too far, a timbral shift begins too early, or a controller’s physical travel should use only part of an instrument’s modulation range.

Switch to the S-shaped curve when the response needs a threshold or different behavior at the beginning and end of a gesture. The additional midpoint can be moved in the display or with the X-Y controls. By default, the two curve segments are linked; disable **Curve Link** to adjust their shapes independently.

## Smooth expressive movement when needed

Open MPE Control’s advanced settings with the triangular button in the lower-right corner of the display. The selected source has its own **Smooth** control and **Rise** and **Fall** times.

Use smoothing sparingly. A short rise or fall time can prevent abrupt jumps from a sensitive controller, while a longer value makes the instrument respond more gradually. Excessive smoothing can make a gesture feel late and can weaken the connection between playing pressure or movement and the sound.

Set the curve and range first, then add only enough smoothing to remove unwanted steps. Check the result with both single notes and chords, since a setting that feels natural for a sustained note can be too slow for a short phrase.

## Adapt sources for the receiving instrument

MPE Control includes source-specific options for situations where the controller and instrument do not use the same kind of message or range.

- In **Press**, use **Press to AT** to convert per-note pressure into conventional monophonic aftertouch for a non-MPE instrument. **Swap to Slide** can send pressure through the Slide source when a controller provides polyphonic aftertouch but the desired modulation is assigned to slide.
- In **Slide**, **Slide to Mod** converts MPE slide data to Mod Wheel messages. The **Centered** option is useful for pad-based MPE controllers when the middle of a pad should produce a zero modulation value.
- In **NotePB**, adjust **Pitch Range** when the controller’s bend range does not match the instrument’s range. **NotePB to PB** translates per-note pitch bend into conventional pitch-bend messages for a non-MPE instrument.

These conversions trade per-note behavior for the global MIDI message expected by the receiving instrument. Configure the target instrument according to its documentation after enabling a conversion, and test the result with more than one note held at a time.

## Troubleshoot the signal path

If MPE Control’s changes are not audible, check the chain in this order:

1. Confirm that the controller’s input port has **MPE** enabled in Link, Tempo & MIDI settings.
2. Confirm that MPE Control is on the correct MIDI track and precedes the target instrument.
3. Select the relevant source and verify that it is active, then begin with its default curve and full range.
4. Verify that the instrument or preset responds to the MPE source, or enable the appropriate conversion for a non-MPE instrument.
5. For pitch problems, match the controller and instrument ranges or adjust MPE Control’s **Pitch Range**.

MPE Control is most useful as a small correction between the controller and an existing instrument mapping. Start by refining one source, record a short performance, and retain settings that improve control without making the gesture feel disconnected from the sound.

For current control behavior, see Ableton’s [MPE Control reference](https://www.ableton.com/en/manual/max-for-live-devices/#mpe-control), [Max for Live overview](https://www.ableton.com/en/live-manual/12/max-for-live/), and [MPE in Live FAQ](https://help.ableton.com/hc/en-us/articles/360019144999-MPE-in-Live-FAQ). For the original Live 11-era demonstration, watch Ableton’s [Learn Live: MPE Control](https://www.youtube.com/watch?v=TW5zHEIAGPo).
