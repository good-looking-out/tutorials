# How to Route Audio and MIDI in Ableton Live

Routing determines where a track receives its signal and where that signal goes next. In Ableton Live, this can mean bringing an input from an audio interface into a track, sending MIDI to a hardware instrument, combining tracks, or recording the output of another track. Open [Ableton Live](https://www.ableton.com/en/live/) with a Set that contains at least one audio track and one MIDI track before following along. Connect and enable any audio interface or MIDI hardware you intend to use first.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/wxGrjJh8SrI?rel=0"
    title="Learn Live: Routing"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Show the In/Out section

Most track routing is configured in the Mixer’s **In/Out** section. Show it from the Mixer View control menu in the lower-right corner of either Session View or Arrangement View, or choose **View > Mixer Controls > In/Out**. The shortcut is `Ctrl` + `Alt` + `I` on Windows or `Ctrl` + `Option` + `I` on macOS.

Each audio or MIDI track has three routing areas:

- The upper **Audio From** or **MIDI From** chooser pair selects the input source and, when applicable, its channel or routing point.
- **Monitor** controls when the selected input is heard through that track’s device chain and output.
- The lower **Audio To** or **MIDI To** chooser pair selects the destination and, when applicable, its channel or a device within that destination track.

The first chooser in a pair selects a source or destination category, such as an external interface or another Live track. The second chooser selects the specific interface channel, MIDI channel, or internal tap point available for that choice.

The source video uses an earlier version of Live, where the final output track is named **Master**. In Live 12, the corresponding track and usual routing destination are named **Main**.

## Distinguish audio paths from MIDI paths

Audio carries the sound itself; MIDI carries note, control, and timing messages. Audio tracks receive and play audio clips, while MIDI tracks receive and play MIDI clips. A MIDI instrument converts the MIDI reaching it into audio, which can then be processed and sent to an audio destination.

This distinction explains the labels in the In/Out section. An audio track can receive an external audio channel, the output of another track, or the Main output for resampling. A MIDI track can receive a MIDI input port, another MIDI track, or MIDI from the computer keyboard, then send MIDI either to an instrument in Live or to an enabled external MIDI port.

Before changing a route, identify both ends of the signal path: the source that should produce the signal and the destination where it should be heard, processed, recorded, or sent to hardware. This avoids routing a track successfully but leaving it unheard because its destination is not connected to Main or a physical output.

## Route an external audio input to a track

Use an audio track when recording or processing a microphone, instrument, or another source connected to an audio interface.

1. In Live’s Audio Settings, make the required interface input and output channels available to Live. The channels shown in the In/Out section depend on this configuration.
2. On the destination audio track, set **Audio From** to **Ext. In**, then use the second chooser to select the mono input or stereo pair carrying the source.
3. Choose a Monitor mode. **In** passes the input through the track continuously and suppresses the track’s clips. **Auto** monitors an armed track but normally gives playback to its clips when they are playing. **Off** stops Live from monitoring the input; use it when monitoring elsewhere, such as through an interface’s direct-monitoring path.
4. Set **Audio To** to **Main** for normal playback through the main mix, or choose **Ext. Out** and a specific physical output when the signal needs a separate hardware destination.
5. Arm the track before recording its selected input into a clip or the Arrangement.

The input signal passes through the audio track’s devices before its selected output. For example, an audio effect placed on a monitored guitar track processes the guitar before the signal reaches Main.

## Route MIDI from a controller or to external hardware

To use a MIDI keyboard or controller as a track input, enable **Track** for that device’s input in the Link, Tempo & MIDI Settings. On a MIDI track, choose the device under **MIDI From** and select its MIDI channel, or choose **All Ins** and **All Channels** when the track should accept every available MIDI input. Add an instrument to the track when the MIDI should produce sound in Live.

To send notes or control changes to external hardware, enable **Track** for the hardware device’s output in the same Settings page. Then set the source MIDI track’s **MIDI To** chooser to that output port and select the receiving MIDI channel. The hardware’s audio must return to Live through an audio input if you need to monitor or record its sound in the Set.

**Sync** is separate from **Track**. Enable Sync only when the external device or application needs MIDI Clock or MIDI Timecode synchronization; it is not required merely to play an instrument or record notes.

## Route tracks inside a Set

Internal routing is useful for submixes, instrument layering, parallel processing, and recording a processed signal. There are two complementary ways to connect tracks.

### Send multiple tracks to one destination

To combine sources, select the destination track in each source track’s **Audio To** or **MIDI To** chooser. This is useful when several audio tracks should feed one submix or when several MIDI tracks should play one instrument. The receiving track keeps its own input and output settings, so it can continue to send the combined signal to Main.

For MIDI, choose the receiving instrument or a particular MIDI channel rather than **Track In** when the intention is to play that instrument directly. **Track In** targets the receiving track’s recordable input instead.

Grouping tracks is a practical form of audio submixing. When tracks are placed in a group, Live normally routes their audio to the Group Track, which can then be processed and sent to Main.

### Tap one source from several tracks

To make several tracks receive from one source, set each receiving track’s **Audio From** or **MIDI From** chooser to the source track. An audio receiver can use its second input chooser to select one of three tap points:

- **Pre FX** takes the signal before the source track’s devices and mixer controls.
- **Post FX** takes the signal after the source track’s devices but before its mixer controls.
- **Post Mixer** takes the signal after its devices, pan, and volume controls.

Set the receiving audio track’s Monitor mode deliberately. **In** makes the selected source audible through the receiving track; **Auto** makes it audible while the receiver is armed. For example, a processing track can monitor a live input with **In**, while a separate recording track receives that processor’s **Post FX** output and records it with monitoring set according to the recording setup.

## Use return tracks and resampling purposefully

Send controls route part of a track’s audio to a matching Return Track, which is commonly used for shared effects such as reverb or delay. A Return Track normally sends its result to Main, but its **Audio To** chooser can send the processed signal elsewhere, including an audio track for recording.

An audio track can also choose **Resampling** under **Audio From**. This makes the Main output its input. Arm that track and record to capture what is currently reaching Main, including the tracks, returns, and processing that feed it. During resampling, Live suppresses the recording track’s own output from the resampled signal, preventing it from recording itself.

Use **Sends Only** as an audio output only when you intend a track to reach the mix through Return Tracks rather than through its normal direct route to Main. Confirm that a send level and a return destination are set before relying on it.

## Check a route before recording or performing

Test one signal path at a time before recording or relying on a route in a performance. Start playback or play the input source, then check the source-track meter, the destination-track meter, and finally the Main meter or the relevant physical output. If a meter stops responding, work backward through the visible In/Out choosers and confirm the selected channel, monitoring mode, device configuration, and track activation state.

Keep the In/Out section visible only while configuring or diagnosing a route. Once a signal path works, hiding it returns space to the clips and Mixer while preserving the routing choices in the Set.

For current details, see Ableton’s [Routing and I/O](https://www.ableton.com/en/manual/routing-and-i-o/), [Mixing](https://www.ableton.com/en/live-manual/12/mixing/), and [Live Manual](https://help.ableton.com/hc/en-us/articles/206769450-Live-Manual). The source walkthrough is Ableton’s [Learn Live: Routing](https://www.youtube.com/watch?v=wxGrjJh8SrI).
