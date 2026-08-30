# How to Automate in Arrangement View

Arrangement automation changes a Mixer or device parameter at specific points on Live’s linear song timeline. Use it for a level fade, filter sweep, effect change, or other movement that belongs to a fixed section of an arrangement rather than to an individual Session clip. Open [Ableton Live](https://www.ableton.com/en/live/) in Arrangement View with an audio or MIDI track and a parameter you want to change over time.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/DPBN34nQ_v4?rel=0"
    title="Learn Live: Arrangement View automation"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Show Automation Mode in Arrangement View

In Arrangement View, automation belongs to a track and is displayed on the track’s main lane or in separate automation lanes below it. Turn on **Automation Mode** with its toggle above the track headers, or press `A`. The view shows the track’s automation envelopes as red lines over the audio waveform or MIDI notes.

If the `A` shortcut does not work, disable the Computer MIDI Keyboard. In Live 12, you can also hold `Shift` while using a single-letter shortcut, so `Shift`+`A` toggles Automation Mode while the Computer MIDI Keyboard remains enabled.

Automation in Arrangement View is separate from [Session clip automation](how-to-automate-a-clip-in-ableton-live.md). A Session clip can carry an automation gesture with it, while an Arrangement automation envelope is tied to the track’s position on the song timeline.

## Select the parameter to automate

With Automation Mode enabled, select a target by clicking a Mixer or device parameter. Live displays that parameter’s envelope on the track. You can also use the **Device** chooser to select the track Mixer or a device, then use the **Automation Control** chooser to select the control.

The available controls depend on the selected target. Common starting points include track volume, Pan, a return-send amount, filter cutoff, device Dry/Wet, or a device activator. Choose one parameter that has a clear musical purpose before adding more envelopes.

An envelope that has not yet been changed appears as a dotted red line. A red indicator on the associated control and in the choosers identifies a parameter that already has automation.

## Record a parameter movement

Record automation when you want to perform the gesture in real time with the mouse or a MIDI controller:

1. Select the desired track and set the Arrangement loop or time selection if you want to rehearse a particular section.
2. Enable **Automation Arm** in the Control Bar.
3. Start Arrangement playback, then enable **Arrangement Record**.
4. Move the selected Mixer or device control while the arrangement plays.
5. Stop Arrangement Record when the pass is complete, then turn off Automation Arm when you are finished recording parameter changes.

Live records every change made to an automatable control while Automation Arm and Arrangement Record are enabled. If you are recording only control changes, disarm any audio or MIDI tracks that should not receive new material. Listen through the recorded pass before recording again, especially around a loop boundary or transition.

## Draw and edit breakpoint envelopes

Draw an envelope when the change needs a precise time or value. With Draw Mode off, click a line segment to create a breakpoint, then drag that breakpoint to the required position. Click a breakpoint to remove it. Drag a line segment to change the values between its adjacent breakpoints.

Use the Arrangement grid as a timing reference. Breakpoints placed near a grid line snap to it; hold `Alt` on Windows or `Cmd` on macOS while dragging horizontally to bypass grid snapping. Hold `Shift` while dragging to restrict a breakpoint or line segment to a horizontal or vertical movement, and use `Shift` while dragging vertically for a finer value adjustment.

For fast stepped automation, press `B` to enable Draw Mode and drag across the envelope. Right-click a breakpoint and choose **Edit Value** when the control must reach an exact value. To turn a straight segment into a curve, hold `Alt` on Windows or `Option` on macOS while dragging the segment.

## Use shapes and selections to refine a pass

Select a time range in an automation lane, then right-click it to insert an automation shape. Shapes are useful for repeated waves, ramps, swells, and other gestures that would take longer to draw breakpoint by breakpoint. Adjust the time selection first so the shape starts, ends, and repeats where the arrangement requires.

Recorded controller moves can produce many breakpoints. Select the portion that needs cleaning up and choose **Simplify Envelope** from its context menu. Live removes unnecessary points where it can represent the same movement with straight or curved segments. Inspect the result after simplifying, particularly around quick musical accents.

When a time selection contains several points, hover near its edges to reveal transform handles. Drag them to stretch or skew the selected envelope in time or value. Use this after a first pass is musically correct but needs to happen sooner, later, wider, or more subtly.

## Separate lanes and preserve the intended song position

Move an envelope into its own automation lane when a track has more than one parameter to review. This keeps the clip’s content visible in the main lane while letting you compare several parameter changes below it. The lane header’s Device and Automation Control choosers let you switch the displayed envelope, and the lane controls let you show or hide additional lanes without deleting their data.

By default, moving a clip also moves its associated automation. Turn on **Lock Envelopes** when the automation should remain at a fixed song position while clips move beneath it. Leave Lock Envelopes off when the automation is part of the clip’s musical content and should travel with that clip. Check this setting before rearranging a section, because the two behaviors produce different results.

## Re-enable automation after a manual adjustment

Changing an automated parameter while not recording temporarily overrides its envelope. Live shows that the automation is inactive and lights the **Re-Enable Automation** control in the Control Bar. Click that control to restore all overridden automation, or use the parameter’s context menu to re-enable the selected control only.

This is useful for auditioning a different setting without deleting the recorded envelope. Re-enable the automation before judging the arrangement’s final playback, otherwise the manual setting can make it appear that the envelope is not working.

## Keep Arrangement automation focused on the song structure

Use Arrangement automation for changes that must happen at a particular time in the song, such as bringing in an effect at a transition or shaping a build across several bars. Start with one parameter, record or draw a simple gesture, then use separate lanes and selections only as the arrangement becomes more detailed. This keeps the timeline readable and makes later revisions safer.

For current details, see Ableton’s [Automation and Editing Envelopes](https://www.ableton.com/en/live-manual/12/automation-and-editing-envelopes/), [Arrangement View](https://www.ableton.com/en/manual/arrangement-view/), [Live Keyboard Shortcuts](https://www.ableton.com/en/manual/live-keyboard-shortcuts/), and [Unable to edit automation](https://help.ableton.com/hc/en-us/articles/360000070444-Unable-to-edit-automation). The source walkthrough is Ableton’s [Learn Live: Arrangement View automation](https://www.youtube.com/watch?v=DPBN34nQ_v4).
