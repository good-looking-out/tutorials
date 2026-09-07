# How to Use MPE in Ableton Live

MIDI Polyphonic Expression (MPE) carries pitch bend, slide, and pressure data separately for each note, allowing simultaneous notes to respond independently. An MPE-capable controller is required to perform and record those gestures in real time; however, Live also lets you create and edit MPE data with a mouse. MPE is available in Live 11 and later in Intro, Standard, and Suite. In Live 12, every included Live instrument supports MPE, although the instruments included with a particular edition vary. Start with Ableton’s current [MPE in Live FAQ](https://help.ableton.com/hc/en-us/articles/360019144999-MPE-in-Live-FAQ) if you need to confirm your controller or edition.

The source video was made with Live 11. It refers to Preferences and the Note Expression tab; in current Live 12, use **Settings** and the **MPE** editor view instead.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/qIl1ZY29fAM?rel=0"
    title="Learn Live: MPE"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Understand the per-note data

MPE adds independent expressive information to each MIDI note. The three performance dimensions are:

- **Per-note pitch bend**, commonly produced by horizontal finger movement.
- **Slide**, commonly produced by vertical finger movement.
- **Pressure**, produced by varying pressure after the initial note strike.

Live stores this information with the individual notes in a MIDI clip. Its MPE editor also exposes velocity and release velocity, so the performance can be refined after recording. What a gesture changes musically depends on the instrument and its MPE mappings: a sound might use pressure for filter movement, slide for timbre, or per-note pitch bend for a gliding pitch.

## Enable the MPE controller in Live

Connect the MPE-capable controller, then open Live’s **Settings** with `Ctrl` + `,` on Windows or `Cmd` + `,` on macOS. Choose **Link, Tempo & MIDI** and find the controller in the MIDI Ports input list. Enable its **MPE** button.

MPE-enabled inputs receive the controller’s per-note messages together. When that controller is selected as a MIDI track input, Live uses **All Channels** for the input routing. Arm the MIDI track and set monitoring as appropriate for the way you normally play or record into Live.

If the controller does not appear in the input list, confirm its connection and any manufacturer-required setup before changing Live’s settings. The MPE button only enables MPE messages on a port that Live can already see.

## Choose an instrument and make an expressive mapping

Add a Live instrument to the armed MIDI track. All Live 12 instruments accept MPE, but the audible result still depends on the instrument’s current MPE settings or preset. Begin with a preset that responds to per-note expression, or assign an available MPE source to a parameter whose change will be easy to hear.

Start with one clear relationship, such as pressure changing a filter-related parameter or slide changing a timbral parameter. Keep the mapping amount modest at first. This makes it easier to judge the controller’s range and prevents several gestures from obscuring one another while testing.

The video uses Wavetable as its example. Wavetable is not required for the general workflow: use any Live instrument available in the installed edition. A later Wavetable-specific workflow can then be applied after the controller and basic MPE recording are working correctly.

## Record a short MPE performance

Create or select a MIDI clip on the armed track and record a short phrase. Hold individual notes while applying pitch movement, slide, or pressure. Play overlapping notes as well, so you can hear whether the instrument is reacting separately to each note instead of applying one global change to the whole chord.

After recording, play the clip back before editing it. Check that the intended gestures are audible and that the controller’s pitch-bend range agrees with the instrument’s range. A mismatch causes bends to reach an unexpected interval or fail to reach the intended pitch.

## Edit per-note expression in the MPE editor

Double-click the MIDI clip to open Clip View, then switch the editor to **MPE**. Use the expression-lane menu to show the Slide, Pressure, Velocity, or Release Velocity lanes that you need. Per-note pitch bend appears with the notes in the MIDI Note Editor.

Select a note to reveal its expression curve and breakpoints. Drag a breakpoint to reshape an existing gesture, double-click to add a breakpoint, or use Draw Mode to write a new curve. Because the data belongs to the selected note, you can make one note in a chord brighten, bend, or fade differently from the others.

This editor also provides a practical way to work without MPE hardware. Draw per-note curves into a MIDI clip, then use an MPE-capable instrument to hear the result. It is useful for correcting a recorded performance or for writing expression into material that began as ordinary MIDI notes.

## Check plug-ins and troubleshoot unexpected results

For an external instrument plug-in, verify MPE support in the developer’s current documentation. Live can pass MPE data to MPE-enabled plug-ins, but a plug-in may also need its own MPE mode enabled or a matching pitch-bend range. Do not assume that a standard MIDI plug-in will respond to per-note information.

If a gesture has no effect, check these points in order:

- The controller’s input port has **MPE** enabled in Live’s Link, Tempo & MIDI settings.
- The MIDI track receives the controller, is armed when recording, and contains an instrument.
- The instrument or preset has an audible MPE response for the gesture being tested.
- The pitch-bend range is matched between the controller and the receiving instrument or plug-in.

MPE is most effective when the musical purpose of each gesture is clear. Record a simple phrase, shape one per-note parameter at a time, and then use the MPE editor to keep only the motion that supports the sound.

For current setup, compatibility, and troubleshooting information, see Ableton’s [MPE in Live FAQ](https://help.ableton.com/hc/en-us/articles/360019144999-MPE-in-Live-FAQ), the [Editing MPE chapter of the Live 12 manual](https://www.ableton.com/en/live-manual/12/editing-mpe/), and the [Live 12 release notes](https://www.ableton.com/en/release-notes/live-12/). For the original Live 11-era demonstration, watch Ableton’s [Learn Live: MPE](https://www.youtube.com/watch?v=qIl1ZY29fAM).
