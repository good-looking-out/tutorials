# How to Use MPE with Wavetable

MIDI Polyphonic Expression (MPE) gives each note its own pitch-bend, slide, and pressure data, so a chord can change timbre or pitch one note at a time. [Wavetable](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable) is included with Live 12 Suite; an MPE-capable controller is needed to perform and record those gestures live. MPE data can also be drawn in a MIDI clip without that hardware. The source video was made with Live 11; this guide uses Live 12 terminology, in which all Live instruments support MPE and Wavetable no longer has an MPE label in its title bar.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/fGhI7rP74ww?rel=0"
    title="Learn Live: Wavetable – MPE"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Prepare Wavetable for expressive input

Connect the MPE controller, then open Live's **Settings** and select **Link, Tempo & MIDI**. Enable the controller input's **MPE** button. When that input is selected on a MIDI track, Live receives its per-note expression across all channels.

Load **Wavetable** on that MIDI track and set its global **Poly/Mono** toggle to **Poly**. A polyphonic sound lets the result of a gesture on one held note remain distinct from the other notes in a chord. Begin with a simple patch: a clearly audible oscillator, a filter with some room to open, and no large existing modulation assignment to the parameter you intend to test.

If the controller's pitch movement is not tracking as expected, check its configured pitch-bend range and the instrument's response before adding more mappings. A mismatch can make a correct MPE connection sound like an incorrect note or an excessively large bend.

## Add an expressive destination

Wavetable's modulation area has **Matrix**, **Mod Sources**, and **MIDI** tabs. Open **MIDI** to work in the **MIDI Modulation Matrix**. Click the Wavetable parameter that should react to the gesture; Live adds it to the matrix temporarily. Once an amount is assigned, the target remains available in the matrix.

Use one MPE dimension for one audible destination at first. These pairings provide useful starting points:

- Map **Slide** to an oscillator's **Position** to move through the wavetable while a note is held.
- Map **Pressure** to filter frequency for a timbral change that follows the force applied after the initial strike.
- Use per-note pitch bend for controlled pitch movement, after first confirming that the controller and instrument ranges agree.

Set a modest positive or negative amount in the relevant matrix cell, then hold a note and make the corresponding gesture. The correct direction is musical rather than universal: for example, a positive slide mapping can make vertical movement advance through the table, while a negative amount reverses that relationship. Increase the amount only after confirming that the connection and direction are correct.

The Live 11 video shows a dedicated MPE display for these assignments. In current Live 12, rely on the Wavetable modulation controls and their displayed source and target names rather than looking for the former MPE badge in the device header.

## Test independent notes in a chord

Hold two or more notes, then apply slide, pressure, or pitch movement to only one of them. With an effective MPE mapping, that note changes without forcing the same change on the other held notes. This is the essential difference between MPE and a conventional global controller mapping.

Test each assignment in a short musical phrase as well as a sustained chord. A large change in Wavetable position can be compelling on a pad but too abrupt on a short lead line. Similarly, a pressure-to-filter mapping may need a smaller amount when resonance or oscillator effects are already adding movement.

Record a short MIDI clip once the response feels usable. Recording captures the note expression alongside the notes, so the performance can be checked and refined without repeating it exactly on the controller.

## Edit recorded MPE data

Double-click the MIDI clip to open Clip View, then select the **Note Expression** tab. Live provides separate expression lanes for **Slide**, **Pressure**, **Velocity**, and **Release Velocity**; per-note **Pitch** is shown over the corresponding note in the MIDI Note Editor.

Select a note to reveal its expression data. You can add or move breakpoints in a Slide or Pressure lane, adjust the pitch curve over the note, or use Draw Mode to create a new curve. Edit one selected note while a chord is playing to preserve the per-note behavior established in Wavetable.

This editing view also makes the workflow available without an MPE controller. Write a short polyphonic clip, add a small pressure or slide curve to one note, and use the Wavetable mapping to hear how individual note expression changes the sound.

## Refine the sound without obscuring the gesture

Keep the initial patch and modulation amounts restrained until the connection is clear. A practical approach is to establish one mapping, record it, then add a second only if it serves a different musical role. For example, slide can supply continuous timbral motion while pressure adds a smaller brightness change.

If a controller produces abrupt values or its physical range is inconvenient, place **MPE Control** before Wavetable to reshape the incoming Press, Slide, or NotePB data. It changes the data before Wavetable receives it; the Wavetable destination and amount still determine the musical result.

MPE makes Wavetable most useful when each gesture has an identifiable consequence. Build the mapping around one performance intention, verify it with a chord, and use the Note Expression editor to retain the parts of the performance that support the sound.

For current details, see Ableton's [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable), [Editing MPE guide](https://www.ableton.com/en/live-manual/12/editing-mpe/), [MPE in Live FAQ](https://help.ableton.com/hc/en-us/articles/360019144999-MPE-in-Live-FAQ), and [Live edition comparison](https://www.ableton.com/en/live/compare-editions/). For the original Live 11-era demonstration, watch Ableton's [Learn Live: Wavetable – MPE](https://www.youtube.com/watch?v=fGhI7rP74ww).
