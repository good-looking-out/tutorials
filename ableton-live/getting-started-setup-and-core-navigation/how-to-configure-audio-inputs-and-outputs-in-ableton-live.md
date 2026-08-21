# How to Configure Audio Inputs and Outputs in Ableton Live

Configuring an audio interface’s inputs and outputs tells [Ableton Live](https://www.ableton.com/en/live/) which physical channels it may use. Do this after selecting the interface in Settings and before assigning microphones, instruments, speakers, headphones, or external hardware in a Set.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/wENbeUNS-IA?rel=0"
    title="Learn Live: Configuring your audio ins and outs"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Confirm the interface is selected

Open **Settings** with `Cmd`+`,` on macOS or `Ctrl`+`,` on Windows and choose **Audio**. Confirm that the correct audio interface is selected for input and output before opening either configuration dialog. The available channels come from the currently selected device.

If the controls are unavailable, resolve the device or driver connection first. An interface that is not recognized by the operating system cannot expose its channels to Live.

## Enable input channels

Select **Configure Inputs**. The dialog lists the mono inputs and stereo pairs supplied by the interface.

1. Enable each mono channel needed for a single microphone, guitar, or other one-channel source.
2. Enable a stereo pair for sources that must remain stereo, such as a stereo keyboard or external processor return.
3. Give commonly used channels clear names when the dialog permits it, such as `Vocal mic`, `Guitar DI`, or `Synth L/R`.
4. Close the dialog when the required channels are active.

Enable the channels that are useful, not every channel the interface offers. A focused configuration keeps the track-routing menu easier to read and reduces unnecessary audio-processing work.

## Enable output channels

Select **Configure Outputs** and use the same approach. Enable the stereo pair connected to the main monitors first. Enable other pairs only when they have a purpose, such as separate headphone cueing, a hardware effect send and return, or another monitoring destination.

Name the outputs according to their physical destination where possible. Clear labels prevent accidentally sending a track to the wrong speakers or external device.

## Assign channels from the Mixer

Show the Mixer’s **In/Out** section from the Mixer controls menu or with `Ctrl`+`Alt`+`I` on Windows or `Ctrl`+`Option`+`I` on macOS. On an audio track:

1. Choose **Ext. In** in **Audio From**.
2. Select an enabled mono input or stereo pair beneath it.
3. Set monitoring and arm the track if you intend to record.
4. Choose the desired destination in **Audio To**, normally the Main output for ordinary playback.

The routing menu shows only channels that were enabled in Audio settings. If an expected channel is missing, return to **Configure Inputs** or **Configure Outputs** instead of trying to recreate it on the track.

## Test each important route

Send a short signal through each configured input while checking its meter. Then play a clip to each required output at a low level. Use the meters to confirm signal presence and stop immediately if an output feeds back into an input or reaches an unexpected destination.

Document the intended channel names for more complex interfaces, especially before saving a template Set. Ableton’s [Routing and I/O manual chapter](https://www.ableton.com/en/live-manual/12/routing-and-i-o/) explains track routing, and the [audio-interface guide](https://help.ableton.com/hc/en-us/articles/211476789-Setting-up-an-Audio-Interface) covers the configuration dialogs. The source video is [Learn Live: Configuring your audio ins and outs](https://www.youtube.com/watch?v=wENbeUNS-IA).
