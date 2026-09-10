# How to Use Wavetable Oscillator Effect Modes

Wavetable's oscillator effects reshape an oscillator's waveform before its signal reaches the instrument's filters and other processing. They provide a quick way to add harmonic movement or distortion without changing the selected wavetable. [Wavetable](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable) is included with Live 12 Suite. This guide uses current Live 12 control names; the source video demonstrates the same workflow in Live 11.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/kzlwOZZ1STg?rel=0"
    title="Learn Live: Wavetable – Oscillator Effect Modes"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Select an oscillator and establish a reference sound

Load **Wavetable** onto a MIDI track, then select the **Osc 1** or **Osc 2** tab. Each oscillator has its own effect setting, so an effect selected for Osc 1 does not alter Osc 2. Begin with one enabled oscillator, a held note or short MIDI loop, and the oscillator effect set to **None**. This gives you a clear reference for the chosen wavetable before the effect changes its timbre.

Use the oscillator effect chooser to select **FM**, **Classic**, or **Modern**. The two adjacent effect parameters change names and behavior with the selected mode. The current parameter values are retained when you change modes, which makes it possible to compare how the same values affect a waveform in each process.

## Use FM for frequency-modulated overtones

Choose **FM** to apply frequency modulation to the selected oscillator. **Amt** sets the intensity of the modulation, while **Tune** sets the frequency of its modulation oscillator.

Start with **Amt** near zero and raise it slowly while holding a simple note or chord. Small values add upper harmonic movement; higher values can become much more complex. Set **Tune** to a simple relationship before exploring inharmonic results:

- At **50%** or **-50%**, the modulation oscillator is one octave above or below the audible oscillator.
- At **100%** or **-100%**, it is two octaves above or below.
- Values between those points create inharmonic ratios, which are useful for noisy or metallic overtones.

Keep the amount restrained while finding a useful tune relationship. Once the timbre is established, use the oscillator's **Gain** and the filter to place the more harmonically dense sound in the mix.

## Shape the waveform with Classic mode

Select **Classic** for its two controls: **PW** and **Sync**. **PW** adjusts pulse width. Unlike a hardware synth in which pulse-width adjustment is generally limited to square waves, Wavetable lets you apply it to any loaded wavetable. Move PW slightly in either direction to hear how it reshapes the selected table.

**Sync** uses a hidden oscillator to reset the phase of the audible oscillator. Raise Sync gradually to alter the timbre while retaining the basic pitch of the played note. A restrained Sync setting is useful when the selected wavetable already has a detailed harmonic profile; a larger setting makes the synchronization character more apparent.

Try PW and Sync one at a time before combining them. This makes it easier to identify whether a change comes from the waveform reshaping or the phase resets, especially when the instrument also has active filter or modulation assignments.

## Use Modern mode for waveform distortion

Select **Modern** to access **Warp** and **Fold**. Warp reshapes the waveform in a way similar to pulse width, while Fold applies wavefolding distortion. These controls can make a simple wavetable sound more angular or dense without replacing the source table.

Set either Warp or Fold to a small value first, then increase it while playing notes in different registers. Wavefolding can introduce a noticeably different harmonic balance at high and low pitches, so check the result with the range in which the part will be played. If both controls are used, reduce one before raising the other to keep the source of each change clear.

## Compare modes in context

Audition the modes with the same notes, wavetable position, filter settings, and oscillator level. A practical comparison is:

1. Play the reference sound with the effect set to **None**.
2. Choose one effect mode and make a small adjustment to one control.
3. Return the control to zero before testing the second control in that mode.
4. Switch to another mode while keeping the effect values in view, then judge the result in the same musical phrase.
5. Once a mode is useful on one oscillator, decide whether the second oscillator should remain clean, receive a contrasting effect, or be mixed at a lower gain.

The effect mode changes the oscillator rather than the whole instrument. Keeping another oscillator or the sub oscillator comparatively simple can preserve a stable fundamental while the processed oscillator supplies movement and texture.

## Add movement after choosing the mode

Choose the static effect mode and range before adding modulation. To animate a selected effect parameter, click it to add it to Wavetable's **Matrix** tab, then apply an envelope or LFO with a modest amount. An envelope can make an effect stronger at the start of each note, while a slow LFO can create ongoing timbral change.

Review the effect with the filter, envelope, and unison settings already used in the patch. Multiple sources of harmonic movement can accumulate quickly, so reduce an effect amount or modulation depth if the played notes lose their pitch definition.

FM, Classic, and Modern are alternative ways to reshape the oscillator, not preset categories. Start with the mode that matches the required behavior—frequency modulation, pulse-width and synchronization shaping, or waveform distortion—then set only enough depth to support the part.

For current details, see Ableton's [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable), [Live edition comparison](https://www.ableton.com/en/live/compare-editions/), and [Live 12 release notes](https://www.ableton.com/en/release-notes/live-12/). For the original Live 11-era demonstration, watch Ableton's [Learn Live: Wavetable – Oscillator Effect Modes](https://www.youtube.com/watch?v=kzlwOZZ1STg).
