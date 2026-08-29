# Automation vs. Modulation in Ableton Live

Automation and modulation both change a parameter over time, but they do so in different ways. Automation sets the parameter’s value at each point in time, while modulation changes that value by a relative amount. Understanding the difference makes it easier to create repeatable mix and sound-design changes without losing the ability to adjust a control manually. Open [Ableton Live](https://www.ableton.com/en/live/) with a clip and an instrument or effect before following along.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/hukVniFeCi8?rel=0"
    title="Learn Live: Automation vs. modulation"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Compare automation with modulation

Both methods use an envelope to change a mixer or device parameter across time. The key difference is whether the envelope supplies the parameter’s exact value or works around the value that is already set.

| Aspect | Automation | Modulation |
| --- | --- | --- |
| Effect on a parameter | Defines its absolute value at a given time. | Offsets or scales its current value relatively. |
| Visual identifier | Red envelope and red parameter indicator. | Blue envelope, blue parameter indicator, or blue control-ring segment. |
| Best use | A change that must play back at exact values, such as a fade, device on/off change, or tempo change. | A repeatable movement that should remain adjustable by changing the control’s base value. |

For example, automation can set a filter cutoff to a specific value at a particular bar. A modulation envelope can then sweep the cutoff around that automated or manually set base value. Moving the base control changes the result without removing the modulation pattern.

## Use automation for fixed parameter changes

Use automation when the exact parameter value is part of the arrangement or clip performance. In Arrangement View, automation is displayed as breakpoint envelopes on the track or in separate automation lanes. In Session View, a clip can contain its own automation envelope.

Practically all mixer and device controls can be automated, including the Set tempo. You can draw and edit breakpoint envelopes or record parameter movements while Live’s Automation Arm control is enabled. An automated control remains governed by its envelope until you manually override it; Live then indicates that automation is inactive until you re-enable it or launch an applicable Session clip.

Think of automation as the parameter’s scheduled position. Use it for a four-bar volume fade, an exact filter opening at a transition, or a device setting that needs to return to the same value on every playback.

## Use modulation for relative movement

Use modulation when you want an envelope to add movement while retaining direct control over the parameter’s starting position or range. A modulation envelope cannot define a device control’s absolute setting. Instead, it influences that setting relative to the value currently defined by the control or its automation.

This is useful for a filter sweep, pan movement, send variation, or another recurring gesture that needs to remain adaptable. For example, create a modulation pattern for a filter, then adjust the filter’s base cutoff while the clip plays. The modulation retains its shape, but its audible range changes with the base setting.

Modulation is constrained by the control’s usable range. If automation or the base value reaches a control’s limit, additional modulation cannot move beyond that limit. This is why a broad modulation pattern can become subtler when its base control is moved toward one end of its range.

## Find clip automation and modulation envelopes

Select a Session clip and open Clip View’s **Envelopes** tab. Choose the relevant mixer, device, clip, or MIDI control from the **Device** and **Control** choosers. The **Automation** and **Modulation** toggles below those choosers select which type of envelope you are viewing or editing for the selected parameter.

The available choices vary by clip type. Audio clips include clip controls, effects, and the Mixer; MIDI clips include MIDI controller data, devices, and the Mixer. In either case, the chooser marks parameters that already have altered envelopes: red for automation and blue for modulation. A parameter can have both.

Arrangement clips use the same Clip View editor for modulation, but their track automation is edited on the Arrangement’s automation lane rather than through a clip-level Automation toggle. Keeping this separation in mind prevents an envelope from appearing to be missing when you switch between Session and Arrangement workflows.

## Combine the two intentionally

Automation and modulation are designed to work together. Start by using automation to establish a reliable large-scale change, such as a fade or a device setting that changes across the song. Then add modulation when that change needs a smaller repeating or expressive variation.

For example, an automated filter cutoff can move gradually through a section while a modulation envelope adds a shorter rhythmic sweep. The red automation determines the cutoff’s absolute path; the blue modulation changes how the parameter moves around that path. Adjusting the filter control or the automation changes the modulation’s effective range without erasing its pattern.

When revising a Set, check the color indicators before deleting or redrawing an envelope. Clearing automation removes the fixed value changes, while clearing modulation removes only the relative movement. Treat them as separate layers of control rather than alternative names for the same edit.

## Choose the appropriate method before editing

Use automation when playback must reproduce a specific value at a specific time. Use modulation when the same envelope should respond to changes in the parameter’s base setting. For a dependable workflow, first define the broad musical motion with automation, then use modulation only where a relative variation makes the result more flexible.

For current details, see Ableton’s [Automation and Editing Envelopes](https://www.ableton.com/en/live-manual/12/automation-and-editing-envelopes/), [Clip Envelopes](https://www.ableton.com/en/manual/clip-envelopes/), and [Live Manual](https://help.ableton.com/hc/en-us/articles/206769450-Live-Manual). The source walkthrough is Ableton’s [Learn Live: Automation vs. modulation](https://www.youtube.com/watch?v=hukVniFeCi8).
