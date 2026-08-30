# How to Automate Tempo Changes in Ableton Live

Tempo changes can be assigned to Session View scenes for instant performance changes or written as Song Tempo automation in Arrangement View for changes that happen across a fixed song timeline. Before working with either method, make sure the Set’s clips are prepared to follow the project tempo as intended. Open [Ableton Live](https://www.ableton.com/en/live/) with a Session scene or an Arrangement section where the tempo should change.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/iI06kTUtNDg?rel=0"
    title="Learn Live: Automating Tempo Changes"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Choose the type of tempo change

Use a **Scene Tempo** when launching a Session scene should immediately set a particular BPM. This suits performance sections that need distinct tempos. Use **Song Tempo automation** when the change belongs to a linear arrangement, such as a gradual accelerando into a chorus or a controlled slowdown at the end of a piece.

The two methods can work together. Recording a Session performance into Arrangement View writes the launched clips, tempo changes, and other performance actions to the Arrangement. Once recorded, review and refine the resulting Song Tempo envelope on the Main track.

## Assign a tempo to a Session View scene

In Live 12, Scene Tempo is a dedicated scene property rather than part of the scene name:

1. In Session View, choose **View** > **Scene Tempo and Time Signature** to show the scene controls.
2. If necessary, drag the left edge of the Main track header to expand the Scene Tempo column.
3. Select the scene, click its **Scene Tempo** field, enter a BPM value from 20 to 999, and press `Enter`.
4. Launch the scene and confirm that the project tempo changes to the assigned value.

You can also select a scene and open Scene View to adjust its Tempo control. A scene with an assigned tempo has a colored Scene Launch button. Double-click a Scene Tempo field, press `Delete`, or use **Return to Default** from its context menu to remove the assignment.

The source video demonstrates the Live 10 method of placing a BPM value in a scene name. Do not use scene-name parsing for new Live 12 Sets; use the Scene Tempo controls instead.

## Record Session tempo changes into the Arrangement

Use Arrangement Record to capture a scene-based performance and its tempo changes:

1. Set the Arrangement insert marker to the point where the performance should begin.
2. Enable **Arrangement Record** in the Control Bar.
3. Launch the Session scenes in the desired order, allowing each scene to change the tempo when it starts.
4. Stop recording when the pass is complete, then switch to Arrangement View to inspect the result.

Live places the launched clips on their tracks and records the scene tempo changes in the Arrangement. Use this approach when the timing of a performance is the fastest way to establish a first tempo map, then make detailed edits after recording.

## Open the Song Tempo envelope in Arrangement View

Song Tempo is automated on the **Main** track in Arrangement View. To display it:

1. Switch to Arrangement View and enable **Automation Mode** using its toggle above the track headers or `A`.
2. Unfold the Main track.
3. Select **Mixer** in the Device chooser.
4. Select **Song Tempo** in the Automation Control chooser.

The envelope’s vertical axis is tempo in BPM and its horizontal axis is Arrangement time. The two value fields below the choosers set the minimum and maximum BPM shown in the editor. Narrow the visible range around the tempos you are using so small changes are easier to draw and inspect; these fields change the display range, not the tempo values already written in the Arrangement.

If the Computer MIDI Keyboard is enabled, press `Shift`+`A` in Live 12 to use the Automation Mode shortcut, or use the on-screen toggle.

## Draw gradual and immediate tempo changes

With the Song Tempo envelope visible, click its line to create breakpoints and drag them to define BPM and timing. For a gradual change, place one point at the starting tempo and another at the target tempo several beats or bars later. Live follows the line between them, creating a tempo ramp.

For a quick section change, keep the surrounding envelope flat and place the new value at the intended bar or beat. Use the Arrangement grid to align the change with the musical structure. Hold `Shift` while dragging vertically to make fine BPM adjustments, and right-click a breakpoint and choose **Edit Value** when an exact value is important.

Start with a modest range and listen to the transition across the full arrangement. A longer ramp is generally easier for performers and for tempo-synced effects to follow than a large change over a very short span.

## Review how clips respond to tempo automation

Tempo automation changes the project tempo, so it affects metronome timing, MIDI playback, tempo-synced devices, and audio clips that follow the Set tempo. Check audio clip Warp settings before committing to a tempo map. Warped clips can stretch to follow the changing tempo; the selected Warp Mode influences the result. In particular, Re-Pitch changes both speed and pitch, while other Warp Modes can preserve pitch but may introduce a different stretching character.

Listen through every tempo transition with the full Set playing. Pay particular attention to sustained audio, transients, delays, reverbs, and external instruments or devices that are synced to Live. If a change sounds unsuitable, adjust its duration, BPM values, or the relevant clip’s Warp settings rather than assuming that all sources will react identically.

## Keep the tempo map readable

Use separate Arrangement automation lanes when the Main track needs more than one parameter visible. Keep Song Tempo in its own lane while editing other controls, and use simple, named arrangement sections or locators to make each tempo transition easy to find later.

Tempo automation is most effective when it serves a deliberate structural change. Establish the main tempo first, add only the transitions the piece needs, and audition every edit from before the change through the section that follows it. This helps distinguish an intentional tempo map from incidental control movements recorded during a pass.

For current details, see Ableton’s [Automation and Editing Envelopes](https://www.ableton.com/en/live-manual/12/automation-and-editing-envelopes/), [Scene Tempo and Time Signature](https://help.ableton.com/hc/en-us/articles/5595081962524-Scene-Tempo-and-Time-Signature), [Session View](https://www.ableton.com/en/live-manual/12/session-view/), [Setting exact BPM values in the Arrangement View](https://help.ableton.com/hc/en-us/articles/209772085-Setting-exact-BPM-values-in-the-Arrangement-View), and [Audio Clips, Tempo, and Warping](https://www.ableton.com/en/live-manual/12/audio-clips-tempo-and-warping/). The source walkthrough is Ableton’s [Learn Live: Automating Tempo Changes](https://www.youtube.com/watch?v=iI06kTUtNDg).
