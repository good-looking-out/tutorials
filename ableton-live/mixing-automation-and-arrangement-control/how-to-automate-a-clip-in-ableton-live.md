# How to Automate a Clip in Ableton Live

Clip automation records or draws a parameter’s exact value over time inside a Session View clip. It is useful when a loop should reproduce the same filter movement, level change, send change, or device adjustment each time it launches. Open [Ableton Live](https://www.ableton.com/en/live/) in Session View with a clip playing on a track that has a Mixer or device parameter to automate.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/IdQYUk8w5jM?rel=0"
    title="Learn Live: Clip automation"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Choose the clip and parameter to automate

Clip automation is available for Session View clips. It stores an absolute value for a Mixer or device parameter at each point in the clip, so the parameter follows the same path whenever that clip plays. Automation is shown in red; use [modulation](automation-vs-modulation-in-ableton-live.md) instead when the movement should remain relative to the control’s current value.

Start with one short, already-playing clip and one clear target. A filter cutoff, track volume, Pan, return-send amount, or device on/off switch are practical choices. Avoid moving several controls during the first pass, since it is easier to hear and revise one envelope at a time.

## Record automation into a playing Session clip

Use the Control Bar to prepare Live to write the parameter movement into the clip:

1. Launch the Session clip that should contain the automation and arm its track.
2. Turn on **Automation Arm** in the Control Bar.
3. Click **Session Record**. Live is now ready to write parameter movements to the playing clip.
4. Move the target Mixer or device control with the mouse or a mapped MIDI controller while the clip loops.
5. Click **Session Record** again when the pass is complete, then turn off **Automation Arm** if you do not intend to record further changes.

When you move a control with the mouse, Live stops recording that gesture as soon as you release the mouse button. With a MIDI controller, recording continues until the end of the clip loop after you release the controller, which can make the result easier to capture as a complete pass.

## Set the recording scope before writing to several clips

Live can record Session automation only in armed tracks, or into all currently playing Session clips. The latter is useful for a coordinated performance change, but it can write automation into more clips than intended.

Before recording across a scene, open **Settings** and select **Record, Warp & Launch**. Find the Session automation recording setting and choose the scope that matches the task. Use the armed-track option when you want to protect other playing clips; use the all-tracks option only after confirming every clip that may receive the movement.

If a clip already contains automation for the selected parameter, record one intentional pass and inspect the result before making another. Writing again over the same loop replaces the values in the portion being recorded.

## Open the clip Envelope editor

Select the automated Session clip, open Clip View, and open its **Envelopes** tab. Its two choosers identify the envelope to edit:

1. Select **Mixer** or the device that contains the parameter in the **Device** chooser.
2. Select the parameter in the **Control** chooser.
3. Select **Automation** below the choosers.

Parameters that have clip automation are marked with a red indicator in the choosers. Choose **Only show adjusted envelopes** from a chooser when the track contains several devices and you want to review only the controls that already have an altered envelope.

The source video shows an earlier Live interface. In Live 12, select the full **Automation** toggle in the Envelopes tab rather than the abbreviated label shown in that video.

## Draw and refine the automation envelope

The Envelope Editor displays a red line across the clip timeline. With Draw Mode off, click a line segment to add a breakpoint, then drag the breakpoint to set its time and value. Click a breakpoint to remove it. This makes it practical to correct a recorded gesture, create an exact fade, or set a device switch at a precise point in the loop.

For faster stepped changes, turn on Draw Mode with `B` and drag in the Envelope Editor. The visible grid determines the width of the drawn steps. To make a smooth transition, hold `Alt` on Windows or `Option` on macOS while dragging a line segment to curve it. Right-click a breakpoint and choose **Edit Value** when an exact parameter value matters.

You can also right-click a time selection in the envelope to insert a predefined automation shape. Start with a simple ramp or curve, then listen through the clip’s loop before adding more complex movement.

## Clear, override, and transfer clip automation deliberately

To remove an envelope for the currently selected parameter, right-click in the Envelope Editor and choose **Clear Envelope**. You can also use `Ctrl`+`Backspace` on Windows or `Cmd`+`Delete` on macOS. This resets that clip envelope to its default value without changing the audio or MIDI content of the clip.

Changing an automated parameter while not recording overrides its active automation temporarily. Live’s **Re-Enable Automation** control lights when one or more automated controls are overridden; click it to restore the recorded values. Relaunching a Session clip that contains the automation also restores its clip automation.

When a Session clip is recorded or copied into Arrangement View, its clip automation becomes track-based automation. Review the Arrangement’s automation lane after that transfer, particularly if the clip will appear more than once in the song.

## Use clip automation for repeatable Session performances

Clip automation gives a Session loop a repeatable parameter gesture without requiring a separate performance pass each time it launches. Record or draw one clear change, check it through several loop repetitions, and make small breakpoint edits until the movement supports the rest of the Set. Keep the automation in a Session clip when it belongs to that reusable loop; use Arrangement automation when the change belongs to a fixed song timeline.

For current details, see Ableton’s [Automation and Editing Envelopes](https://www.ableton.com/en/live-manual/12/automation-and-editing-envelopes/), [Clip Envelopes](https://www.ableton.com/en/manual/clip-envelopes/), and [Working with Automation and Modulation](https://help.ableton.com/hc/en-us/articles/209070629-Working-with-Automation-and-Modulation). The source walkthrough is Ableton’s [Learn Live: Clip automation](https://www.youtube.com/watch?v=IdQYUk8w5jM).
