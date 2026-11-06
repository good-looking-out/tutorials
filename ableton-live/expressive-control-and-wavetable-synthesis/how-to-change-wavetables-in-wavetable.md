# How to Change Wavetables in Wavetable

Changing a wavetable replaces the waveform collection that a Wavetable oscillator reads, while changing **Wave Position** moves through the waveforms inside that collection. This distinction makes it possible to choose a new tonal source first, then create movement within it. Wavetable is included with Live 12 Suite; see Ableton's current [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#31-13-wavetable) for the device's oscillator controls. The source video uses Live 11; this guide uses current Live 12 labels.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/TmFyhsQpIx4?rel=0"
    title="Learn Live: Wavetable – Changing wavetables"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Select the oscillator to change

Load **Wavetable** on a MIDI track and select the **Osc 1** or **Osc 2** tab. Each oscillator has its own wavetable selection, gain, pan, tuning, position, and oscillator effect settings. Start with only one oscillator enabled when comparing source tables; this makes each change easier to hear.

Use the oscillator's on/off switch to isolate the table you are editing. If both oscillators are active, lower the other oscillator's **Gain** or turn it off temporarily before changing the selected table. This avoids mistaking a layer or filter setting for a change in the wavetable itself.

## Choose a category and wavetable

Each oscillator has two wavetable choosers. Use the first chooser to select a category and the second to select a specific wavetable within that category. The adjacent arrow controls step through the available selections; when you reach the end of a category, the arrows continue into the next category.

Play a repeating note or short MIDI clip while choosing tables. Keep the oscillator's **Gain**, **Semi**, **Detune**, and filter settings stable during the comparison so the selected table is the only major change. Choose a table based on its starting harmonic character rather than trying to create every variation with a filter or oscillator effect afterward.

Repeat the process on **Osc 2** only after Osc 1 has a useful source. A second table can provide an interval, a contrasting layer, or a small amount of additional harmonic content. Set the second oscillator's gain lower at first, then balance it against Osc 1.

## Scan through the selected wavetable

The selected table is displayed in the oscillator visualization. Drag within the display or use the **Wave Position** slider to move through its waveforms. A fixed position produces a consistent timbre; moving the position while a note plays changes the timbre as Wavetable reads a different part of the collection.

Use the visualization switch to choose a linear or polar view. Both show the same wavetable data: the linear view arranges waveforms from bottom to top, while the polar view arranges them as loops from inside to outside. Change the view only when it helps you see the available motion; it does not change the sound.

To hear the source table clearly, set Wave Position manually before assigning modulation. Once a useful range is identified, an LFO or envelope can move the position through that range. Keep the modulation depth modest until the movement supports the intended part.

## Distinguish table selection from other oscillator changes

Several Wavetable controls can alter the result without changing the loaded table:

- **Wave Position** scans the current wavetable rather than selecting another one.
- **FM**, **Classic**, and **Modern** oscillator effects transform the current oscillator waveform.
- **Semi** and **Detune** change the oscillator's pitch relative to Wavetable's global transpose value.
- The filters shape the oscillator's harmonic output after the selected table has produced sound.

When a new table does not sound as expected, temporarily set its oscillator effect to **None**, return Wave Position to a clear reference point, and reduce filtering or resonance. This isolates the table before other sound-design choices are restored.

## Combine tables into a usable sound

After choosing a table for each oscillator, decide how they should relate before adding more modulation:

1. Set the balance with the two oscillator **Gain** controls.
2. Use **Semi** and **Detune** to set an interval or a small pitch offset.
3. Choose a filter routing and adjust filter frequency only after the oscillator balance is clear.
4. Set a fixed Wave Position for each table, then add movement to one oscillator at a time.
5. Check the result with the notes and register used by the musical part.

For example, one oscillator can provide a stable harmonic foundation at a fixed position while the second uses a different table and a slowly changing position. This approach preserves a recognizable pitch and timbre even when the second layer provides movement.

## Compare choices without losing a useful result

Save a Wavetable preset once the selected tables and their positions form a useful starting point. Then audition nearby tables using the arrow controls or choose a different category without needing to rebuild the rest of the patch.

If browsing becomes difficult to evaluate, return to one active oscillator and a fixed Wave Position. Compare a small number of candidates with the same MIDI phrase, then restore the second oscillator, filters, and modulation only after selecting the preferred source. This separates the decision about waveform content from decisions about width, filtering, and motion.

Choosing a table establishes the raw character of an oscillator; Wave Position, modulation, filtering, and effects then refine it. Start with a clear source, scan it deliberately, and add a second oscillator only when it contributes a distinct role to the sound.

For current details, see Ableton's [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#31-13-wavetable) and [Live edition comparison](https://www.ableton.com/en/live/compare-editions/). For the original Live 11-era demonstration, watch Ableton's [Learn Live: Wavetable – Changing wavetables](https://www.youtube.com/watch?v=TmFyhsQpIx4).
