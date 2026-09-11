# Wavetable Overview in Ableton Live

Wavetable is a synthesizer built around two wavetable oscillators, two analog-modelled filters, and an internal modulation system. It is included with Live 12 Suite; see Ableton's current [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable) before following along. The source video uses the Live 11 interface. This overview uses current Live 12 labels, including its three modulation tabs rather than the separate MPE tab shown in the video.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/9wovKSfR66A?rel=0"
    title="Learn Live: Wavetable – Overview"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Open Wavetable and reveal its working areas

Create or select a MIDI track, then load **Wavetable** from Live's Instruments. The device is organized around three areas:

- The **Osc 1** and **Osc 2** tabs, which hold the two main sound sources.
- The filter section, which contains two multimode filters and their routing controls.
- The modulation section, which is divided into **Mod Sources**, **Matrix**, and **MIDI** tabs.

Click Wavetable's expanded-view button in the device title bar when you need more controls in one view. The visible arrangement of controls changes with the available Device View size, but the device sections and parameter names remain the same.

The Live 11 video also shows an **MPE** tab and an MPE label in Wavetable's header. In Live 12, Ableton removed that header label because all Live instruments support MPE; use the current MPE tools and documentation when configuring per-note expression.

## Choose and shape the oscillators

Select **Osc 1** or **Osc 2** to work on that oscillator independently. Use the two wavetable choosers to select a category and then a table within it. The arrow controls move through the available selections, including the next category when reaching the end of the current one.

The wavetable visualization represents the oscillator's current table. Drag within it or adjust **Wave Position** to move through the table and change the timbre. Switch between the linear and polar visualization when one view makes the waveform sequence easier to read; both views represent the same wavetable data.

Use these controls to establish the oscillator's basic role:

- **Gain** sets its output level and **Pan** places it in the stereo field.
- **Semi** and **Detune** provide coarse and fine tuning relative to Wavetable's global transpose setting.
- The oscillator effect chooser selects **FM**, **Classic**, or **Modern** to transform the oscillator's waveform.
- Each oscillator can be switched on or off without changing the other oscillator's settings.

Start with one active oscillator and an uncomplicated table. Bring in the second oscillator only after the first has a clear pitch and timbre. This makes tuning, filtering, and modulation decisions easier to hear.

## Add the sub oscillator and filters

The **Sub** oscillator adds a lower layer beneath the two main oscillators. Turn it on when a sound needs more weight, then set its **Gain**, **Tone**, and octave shift. At its minimum Tone value, the sub oscillator produces a sine wave; raising Tone adds harmonic content.

Use the two filters to shape the combined oscillator output. Each filter can be enabled independently and set to a low-pass, high-pass, band-pass, notch, or Morph type. **Frequency** sets the point in the harmonic spectrum that the filter affects, while **Resonance** emphasizes frequencies around that point.

The filter routing determines how the main oscillators are treated:

- **Serial** sends both main oscillators through Filter 1 and then Filter 2.
- **Parallel** sends Osc 1 to Filter 1 and Osc 2 to Filter 2.
- **Split** routes Osc 1 to Filter 1 and Osc 2 to Filter 2 while preserving either oscillator's audibility if its corresponding filter is disabled.

Choose a routing before making detailed filter adjustments. Serial routing is useful for progressive sculpting, while Parallel and Split make it easier to give each oscillator a distinct role.

## Set the voice behavior and width

Wavetable's global controls set how notes are played. Choose **Poly** to use multiple simultaneous notes and set the maximum in the **Poly Voices** menu. Choose **Mono** for a single voice with legato envelopes; **Glide** is active in this mode and controls the time overlapping notes take to slide to the next pitch.

Use the **Unison** menu to thicken each wavetable oscillator with multiple related voices. The available modes change how those voices are detuned, panned, phased, or positioned in the wavetable. **Voices** sets how many run at once, and **Amount** sets the strength of the selected unison mode.

Set polyphony and unison after balancing the two main oscillators. Both can substantially increase the density of the sound, which can obscure whether a change is coming from the wavetable, the filters, or the extra voices.

## Create movement with modulation

Open **Mod Sources** to configure Wavetable's three envelopes—**Amp**, **Env 2**, and **Env 3**—and its two LFOs. The amplitude envelope shapes the level of each note, while the other envelopes and LFOs can be assigned to a range of Wavetable parameters.

Open **Matrix** to make an internal assignment. Click a Wavetable parameter to add it temporarily as a target, then drag in the matrix cell where that target meets the desired envelope or LFO source. The sources run horizontally and targets run vertically. Applying an amount keeps the target in the matrix for later adjustment.

Open **MIDI** to assign incoming MIDI sources, including Velocity, Note, Pitch Bend, Aftertouch, Modulation Wheel, and Random, to Wavetable targets. This is useful when the sound should react to the way a part is played rather than repeating the same change on every note.

Begin with one audible assignment, such as a slow LFO to Wave Position or Env 2 to filter frequency. Reduce the amount before adding a second source so the individual contribution of each modulation remains clear.

## Build a simple patch in a controlled order

A practical starting workflow is:

1. Select a table for Osc 1 and set Wave Position, gain, and tuning.
2. Add Osc 2 only if a second timbre, interval, or stereo layer is needed.
3. Add the sub oscillator for low-frequency support, keeping its gain modest.
4. Enable and route the filters, then adjust frequency and resonance.
5. Set Poly or Mono behavior, then apply unison only if the sound needs more width or density.
6. Add one envelope, LFO, or MIDI mapping and evaluate it with the complete patch.

Save a preset after the patch has a stable balance. Wavetable's oscillator, filter, modulation, and global controls interact closely, so preserving a useful starting point makes later experimentation reversible.

Wavetable is easiest to understand as a sequence: select and position a waveform, shape it with the sub oscillator and filters, define how voices play, then add modulation. Establishing each stage before the next makes the device's range of options manageable while still leaving room for complex sound design.

For current details, see Ableton's [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable), [MPE in Live FAQ](https://help.ableton.com/hc/en-us/articles/360019144999-MPE-in-Live-FAQ), [Live edition comparison](https://www.ableton.com/en/live/compare-editions/), and [Live 12 release notes](https://www.ableton.com/en/release-notes/live-12/). For the original Live 11-era demonstration, watch Ableton's [Learn Live: Wavetable – Overview](https://www.youtube.com/watch?v=9wovKSfR66A).
