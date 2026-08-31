# How to Use Follow Actions in Ableton Live

Follow Actions let Session View clips and scenes trigger a defined next action after a chosen amount of time. They are useful for making a Session View Set progress without manually launching every clip. Start with [Ableton Live](https://www.ableton.com/en/live/) open in Session View and at least two clips in successive slots on the same track.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/yoSx763s9IY?rel=0"
    title="Learn Live: Follow Actions"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Arrange the clips that should follow one another

For clip Follow Actions, Live works with a **clip group**: a run of successive Session View clip slots on one track. An empty slot separates one group from the next, so leave a gap whenever you do not want an action such as **Next** or **Any** to reach the following clips.

Place the alternate parts of a musical idea in a single group. For example, a track might contain two verse variations followed by a fill. This gives the Follow Action choices a clear, limited set of clips to launch.

Follow Actions are a Session View feature. Arrangement View playback does not use them to move between clips.

## Open and enable the Follow Actions controls

1. Select a Session View clip and open Clip View if it is hidden.
2. In the clip’s Launch settings, show the Follow Actions controls.
3. Turn on the clip’s **Follow Action** button. The button is off by default.

With one or more clips selected, press <kbd>Shift</kbd>+<kbd>Enter</kbd> to toggle their Follow Actions. A striped clip-launch button indicates that a clip has a Follow Action assigned and enabled.

## Choose when Live should run the action

The **Follow Action Time** field sets the time before Live carries out the action. Enter a musical value in bars, beats, and sixteenths when you need a fixed duration.

Choose between the two timing modes according to the result you need:

- **Linked** is the default for clips. Live performs the action when the clip reaches its end, or after the selected loop multiplier when the clip loops.
- **Unlinked** performs the action after the Follow Action Time, independently of the clip’s length.

Follow Actions happen at their action time rather than waiting for the global quantization setting. A clip quantization setting other than **Global** or **None** still controls when the next clip is launched, so use it when the transition must land on a particular rhythmic boundary.

## Select actions and set their probability

Use the **Action A** and **Action B** choosers to determine what happens next, then set each action’s chance. With Action A at 100% and Action B at 0%, the selected action always runs. Dividing the chance between them introduces a controlled variation each time the Follow Action Time is reached.

The available actions include the following:

- **Stop** ends playback of the current clip, while **Play Again** restarts it.
- **Previous**, **Next**, **First**, and **Last** select positions within the clip group. **Next** wraps from the last clip back to the first one.
- **Any** can launch any clip in the group, including the clip that is already playing. **Other** chooses a different clip when the group contains more than one clip.
- **Jump** launches the specific clip or scene selected with its target control.

For a predictable sequence, use one of the position-based actions at 100%. For a generative variation, combine **Any** or **Other** with a second action and adjust the two percentages until the changes are frequent enough to be noticeable without being disruptive.

## Preserve playback position with Legato when needed

Follow Actions can launch a different clip while the track keeps moving through the musical phrase. Turn on the clip’s **Legato** launch option when the target clip should begin at the same relative playback position as the outgoing clip instead of restarting from its own beginning.

Legato is particularly useful for alternate loops with the same length and harmonic role. It can make a variation feel continuous, while clips with Legato disabled create a more explicit restart at the transition.

## Control Follow Actions across the Set

Use Live’s global **Enable Follow Actions** control near **Back to Arrangement** to enable or disable every clip and scene Follow Action in the Set. This is useful when you want to edit a running Set without its automatic launches changing while you work.

Scenes can also have Follow Actions. Use a scene action when the entire next scene should launch as part of a performance sequence; its action takes precedence once it occurs, although clip Follow Actions can continue up to that point.

Begin with a group of two or three clips and a single 100% action, then listen through several repetitions before adding probability or a second action. This makes it easier to identify whether a transition comes from the Follow Action, the clip quantization, or the material in the next clip.

For current details, see Ableton’s [Launching Clips reference](https://www.ableton.com/en/live-manual/12/launching-clips/), [Live keyboard shortcuts](https://www.ableton.com/en/manual/live-keyboard-shortcuts/), and [Follow Actions updates in Live 11](https://help.ableton.com/hc/en-us/articles/360019101360-Updates-to-Follow-Actions-in-Live-11). The source walkthrough is Ableton’s [Learn Live: Follow Actions](https://www.youtube.com/watch?v=yoSx763s9IY).
