# How to Use Wavetable Unison Modes

Wavetable's unison section creates multiple related voices for each wavetable oscillator, making it possible to add width, detuning, phase movement, or variation to a sound. Wavetable is included with Live 12 Suite; refer to Ableton's current [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable) for the device's complete controls. The source video uses Live 11, while this guide uses current Live 12 labels.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/GTZuartMQGE?rel=0"
    title="Learn Live: Wavetable – Unison Modes"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Enable unison from Wavetable's global controls

Load **Wavetable** on a MIDI track and open its global controls on the right side of the device. Use the **Unison** drop-down menu to select a mode or choose **None** to turn unison off. The unison setting applies multiple related voices to each wavetable oscillator rather than adding a separate instrument to the track.

Set **Voices** to choose how many simultaneous voices run per wavetable oscillator. More voices make the sound denser; fewer voices preserve a clearer individual oscillator character. Use **Amount** to set the strength of the selected unison mode. Its exact effect depends on the mode, so a value that is subtle in one mode can be prominent in another.

Begin with a single active oscillator, an uncomplicated wavetable, a stable held note or MIDI loop, and unison set to **None**. This makes the change introduced by each unison mode easier to identify.

## Choose a mode that matches the intended movement

Wavetable provides six unison modes. Select one in the Unison menu, then use Voices and Amount to establish a useful range before changing the oscillator, filters, or modulation.

### Classic

**Classic** detunes the voices with equal spacing and pans them to alternating stereo channels. Use it when the sound needs straightforward stereo width and a predictable detuned layer. Start with a low number of voices and a modest amount, then increase either control only if the original pitch and attack remain clear.

### Shimmer and Noise

**Shimmer** introduces random pitch jitter at intervals and adds a small wavetable-position offset for extra fullness. It is appropriate when a sustained sound should have gentle, changing pitch movement rather than fixed detuning.

**Noise** uses a much faster version of the pitch jitter and also adds a small wavetable-position offset. It produces a noisier, breathier texture than Shimmer. Compare both modes at the same Voices and Amount settings to hear whether the required motion should be slow and diffuse or fast and textural.

### Phase Sync

**Phase Sync** detunes voices as in Classic, but synchronizes their phases when a note begins. This creates a pronounced sweeping, phaser-like effect at the start of a note. Test it with short notes and sustained notes, because the phase relationship is renewed by each note-on event.

### Position spread and Random note

**Position spread** distributes the wavetable position of each voice evenly by an amount and adds a small amount of detuning. It is useful when the sound should contain several locations from the same wavetable at once rather than several nearly identical pitches.

**Random note** randomizes each voice's wavetable position and detune amount every time a note is played. Use it when repeated notes should not begin with the same internal timbre. Record a short phrase before committing to the setting, since each note event can produce a different result.

## Set Voices and Amount in a controlled order

Choose the unison mode first, then set **Voices** before increasing **Amount**. Voices determines how many versions of the oscillator are present, while Amount determines the scale of the selected mode's behavior. This order prevents two changes from obscuring each other.

Use this practical sequence:

1. Select a mode and keep Amount low.
2. Raise Voices only until the sound has the desired density.
3. Increase Amount until the detune, stereo placement, phase behavior, or wavetable-position variation is audible in the musical part.
4. Recheck the oscillator's gain, filter frequency, and resonance after adjusting unison.
5. Compare the result with **None** to confirm that unison improves the part rather than only making it louder or less defined.

The unison section can interact strongly with filters, oscillator effects, and modulation. Keep these other sources of movement restrained while choosing a mode, then return to them after unison has a clear role in the patch.

## Use unison with two oscillators deliberately

When both Osc 1 and Osc 2 are active, establish their wavetable choices, tuning, and gain balance before relying on unison for width. The global unison settings process both wavetable oscillators, so a dense second oscillator can make a high-voice setting harder to control.

For a stable low end, consider leaving the sub oscillator relatively simple while using unison on the main oscillators. For a layered patch, use filter routing and oscillator gain to decide how much of the unison-rich signal is heard alongside the unprocessed components.

Check the result with chords and the playing range used in the arrangement. Detuning, position spread, and randomization can be effective on sustained material but can reduce definition in fast passages. Preserve a version of the preset before raising Voices or Amount substantially, so the original balance remains available.

Unison is most effective when it has one clear job: stable width with Classic, evolving variation with Shimmer or Random note, increased texture with Noise, a note-on sweep with Phase Sync, or timbral distribution with Position spread. Set the mode first, then use Voices and Amount only as far as the part requires.

For current details, see Ableton's [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable) and [Live edition comparison](https://www.ableton.com/en/live/compare-editions/). For the original Live 11-era demonstration, watch Ableton's [Learn Live: Wavetable – Unison Modes](https://www.youtube.com/watch?v=GTZuartMQGE).
