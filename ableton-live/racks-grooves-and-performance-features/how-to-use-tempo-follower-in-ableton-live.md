# How to Use Tempo Follower in Ableton Live

Tempo Follower makes an Ableton Live Set adapt its tempo to a rhythmic external audio signal in real time. Use it when Live needs to follow a drummer, turntable, or another source that provides a clear pulse rather than a fixed MIDI clock. Before starting, connect that source to an available input on your audio interface and open [Ableton Live](https://www.ableton.com/en/live/).

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/b5FCXmjm5iY?rel=0"
    title="Learn Live: Tempo Follower"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Prepare a clear rhythmic input

Tempo Follower analyzes the signal arriving at one external input channel, not the overall mix of a Live Set. Choose a source with clearly defined rhythmic information. A close or dedicated microphone on a drum kit, or a record or effects-loop output from a DJ mixer, can provide a more useful signal than a broad room microphone or a full, busy mix.

Confirm that your audio interface is selected and that the required input is available in Live’s Audio Settings before configuring Tempo Follower. The selected channel must remain connected to the audio interface while the feature is in use.

## Choose the Tempo Follower input in Settings

1. Open Live’s Settings and select **Tempo & MIDI**.
2. In the **Tempo Follower** section, set **Input Channel (Ext. In)** to the audio-interface input connected to the rhythmic source.
3. Enable **Show Tempo Follower Toggle** so the control is available in the Control Bar.

The **Follow** toggle appears with the tempo-related controls on the left side of the Control Bar. If it is grayed out, Live cannot connect to the configured input channel. Check the audio interface, its input configuration, and the selected channel before trying again.

## Turn on Follow and let the source set the tempo

Start the incoming source, then activate **Follow** in the Control Bar. Live begins interpreting the selected audio input and changes the Set’s tempo to follow it. Start Live’s transport or launch clips as needed; the Set’s tempo will respond to the incoming rhythm while Follow remains enabled.

Begin with material whose timing can tolerate natural variation. A short repeating musical section makes it easier to hear whether Live is tracking the source appropriately before using Tempo Follower in a longer performance.

## Make the control usable during a performance

The Follow toggle can be assigned in Key Map Mode or MIDI Map Mode, allowing a keyboard key or MIDI controller button to turn Tempo Follower on and off. This is useful when the incoming performer should take control of the tempo only for a particular section.

Keep the toggle off while preparing the Set, then enable it shortly before the external source begins. If the source stops, changes to an unclear rhythmic signal, or you need to return to a fixed Set tempo, disable Follow and set the tempo manually as needed.

## Account for other synchronization methods

Tempo Follower and **External Sync** cannot operate at the same time. When Tempo Follower is active, Live can still send MIDI clock to external devices, but it cannot receive MIDI clock. Plan the synchronization role of each device before a rehearsal or performance so two sources are not expected to control Live’s tempo simultaneously.

Tempo Follower can be used alongside Ableton Link. In that setup, Live uses the tempo it receives from the selected audio input for the Link session.

Use a dedicated, rhythmically clear input and test the complete setup with the actual performers or hardware before relying on it. Once the source is stable, Tempo Follower provides a direct way for a Live Set to accommodate expressive tempo changes without manually adjusting the Tempo field.

For current details, see Ableton’s [Synchronizing with Link, Tempo Follower, and MIDI reference](https://www.ableton.com/en/live-manual/12/synchronizing-with-link-tempo-follower-and-midi/), [Live Settings reference](https://www.ableton.com/en/live-manual/12/first-steps/), and [MIDI and Key Remote Control reference](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/). The source walkthrough is Ableton’s [Learn Live: Tempo Follower](https://www.youtube.com/watch?v=b5FCXmjm5iY).
