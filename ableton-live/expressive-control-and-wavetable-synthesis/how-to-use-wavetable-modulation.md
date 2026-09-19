# How to Use Wavetable Modulation

Wavetable modulation changes a selected parameter over time or in response to how a note is played. Its internal sources include envelopes and LFOs, while the MIDI tab accepts performance sources such as velocity and aftertouch. Wavetable is included with Live 12 Suite; Ableton's current [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable) documents the available sources and targets. The source video uses Live 11. This guide uses the current Live 12 Matrix, Mod Sources, and MIDI tab names.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/IHgFpWYyaqQ?rel=0"
    title="Learn Live: Wavetable – Modulation"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Identify sources and targets

Load **Wavetable** on a MIDI track and use a simple starting sound with a clearly audible oscillator and filter. In the modulation system, a **source** generates change and a **target** is the Wavetable parameter that receives it. For example, an LFO can be the source and an oscillator's **Wave Position** can be the target.

Wavetable provides five internal sources:

- **Amp**, **Env 2**, and **Env 3** envelopes.
- **LFO 1** and **LFO 2**.

Use the expanded-view button in Wavetable's title bar when more controls are needed in one view. The device adapts its visible layout to the size of Device View, but the modulation section always contains **Mod Sources**, **Matrix**, and **MIDI** tabs.

The Live 11 source video includes a separate MPE tab. Do not rely on that older layout in Live 12: all Live instruments support MPE, while Wavetable's current manual identifies the three tabs above. Configure MPE input and per-note expression with the current Live MPE tools when it is part of the patch.

## Create an internal modulation assignment

Open the **Matrix** tab to connect envelopes and LFOs to Wavetable parameters. Click the parameter that should change; it appears temporarily as a target in the matrix. The modulation sources run horizontally and the targets run vertically.

Click and drag in the cell where the selected source and target meet to set the modulation amount. Once an amount is applied, the target remains in the matrix. Start with a small value, play or loop a note, and increase it only after confirming the direction and character of the movement.

Two useful first assignments are:

- Use **LFO 1** to modulate **Wave Position** for repeating timbral movement through the selected wavetable.
- Use **Env 2** to modulate filter **Frequency** for a per-note change that follows the envelope's shape.

The same source can affect multiple targets, and a target can receive multiple sources. Add one connection at a time. This makes it clear which source is responsible for an audible change before the patch becomes more complex.

## Shape envelopes and LFOs in Mod Sources

Open **Mod Sources** to set the behavior of the selected envelope or LFO. **Amp** controls the amplitude contour of each note. **Env 2** and **Env 3** can be assigned to other targets in the Matrix and include **Initial**, **Peak**, and **Final** values in addition to their time and slope controls.

For an envelope, set **Attack**, **Decay**, **Sustain**, and **Release** to define its time course. The slope controls change the shape of each segment: a positive slope moves quickly at the start and more slowly later, while a negative slope stays flatter for longer and moves more quickly at the end. Use **None**, **Trigger**, or **Loop** in the loop-mode menu when the envelope should hold its sustain stage, run once, or repeat while a voice is active.

For an LFO, choose a waveform and set its **Rate**. Enable **Sync** when the rate should follow Live's tempo; otherwise, set it in Hertz. **Shape** changes the selected waveform, **Offset** changes its starting phase, and **Attack** fades the LFO in after note-on. Enable **Retrigger** when each new note should restart the LFO at the same phase.

Set the source before increasing its Matrix amount. A slow LFO with a moderate amount and a fast LFO with the same amount can create very different results, so the source's timing is as important as the connection itself.

## Add performance-responsive MIDI modulation

Open **MIDI** to assign incoming MIDI sources through the MIDI Modulation Matrix. It uses the same target rows as the Matrix tab. The available sources are **Velocity**, **Note**, **Pitch Bend**, **Aftertouch**, **Modulation Wheel**, and **Random**.

Click the desired Wavetable parameter to add it to the matrix, then set an amount at the source and target intersection. For example, assign Velocity to filter frequency to make harder-played notes brighter, or assign Note to filter frequency to make the filter track keyboard pitch.

MIDI sources that depend on hardware, such as Pitch Bend, Aftertouch, and Modulation Wheel, require a controller that sends the corresponding message. When hardware is unavailable, Live can use clip envelopes to modulate Wavetable parameters. Treat external MIDI, internal modulation, and MPE as separate layers, then introduce each only when it serves a distinct musical purpose.

## Scale the entire modulation system

Wavetable's global **Amount** and **Time** controls adjust the internal modulation system as a whole. **Amount** changes the overall strength of the modulation sources in the Matrix. Use it to reduce or increase the depth of an established group of assignments without revising each matrix cell.

**Time** scales the speed of all modulators. Negative values make envelopes and LFOs faster, while positive values make them slower. Time can itself be modulated by an envelope or LFO; that modulation does not alter the timing of the source assigned to Time, but it does scale the timing of the other destinations.

Use these global controls after individual mappings work correctly. They are useful for turning a patch's motion up or down as a single gesture, but can hide the source of an unwanted change if they are adjusted before the underlying assignments are understood.

## Build and troubleshoot a moving patch

Use a short, repeatable MIDI phrase while building the sound:

1. Start with one internal source and one target, such as LFO 1 to Wave Position.
2. Set the source's rate or envelope shape before increasing the matrix amount.
3. Add a second target only if it has a different role, such as Env 2 to filter frequency.
4. Add MIDI response, such as velocity, after the automatic movement is balanced.
5. Use global Amount or Time for a final overall adjustment, then recheck the individual matrix cells.

If the sound changes too much, lower the newest matrix amount first. If no change is audible, verify that the target is still present in the matrix with a nonzero amount, then confirm that the source is active and its range or timing can reach a noticeable value. Keeping the patch to a small number of intentional connections produces modulation that remains repeatable and editable.

Wavetable modulation is most useful when each connection has an identifiable role: an envelope for a note-shaped change, an LFO for cyclical movement, or MIDI for performance response. Establish the source, target, and amount in that order, then use the global controls to refine the complete motion.

For current details, see Ableton's [Wavetable reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#30-13-wavetable), [MPE in Live FAQ](https://help.ableton.com/hc/en-us/articles/360019144999-MPE-in-Live-FAQ), and [Live edition comparison](https://www.ableton.com/en/live/compare-editions/). For the original Live 11-era demonstration, watch Ableton's [Learn Live: Wavetable – Modulation](https://www.youtube.com/watch?v=IHgFpWYyaqQ).
