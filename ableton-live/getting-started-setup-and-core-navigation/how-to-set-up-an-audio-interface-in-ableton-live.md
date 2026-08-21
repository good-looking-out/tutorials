# How to Set Up an Audio Interface in Ableton Live

An audio interface connects microphones, instruments, headphones, and monitor speakers to a computer for use with [Ableton Live](https://www.ableton.com/en/live/). Configure it in Live before recording or monitoring. The exact controls vary by interface and operating system, but the basic sequence is the same.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/D9tjzSctp_Q?rel=0"
    title="Learn Live: Setting up an audio interface"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Prepare the interface before opening Live

Install the interface manufacturer’s current driver, control application, and firmware when they are required for the model. On macOS, many interfaces are class compliant and use CoreAudio without an additional driver. On Windows, use the interface manufacturer’s ASIO driver when available.

Connect the interface directly to the computer when possible and provide any required external power. Turn the interface’s output level down before connecting powered monitor speakers, then connect headphones or speakers to the interface rather than to the computer’s built-in audio output.

## Select the interface in Audio settings

1. Open Live’s **Settings** with `Cmd`+`,` on macOS or `Ctrl`+`,` on Windows, then select **Audio**.
2. On Windows, choose **ASIO** as the Driver Type when the interface provides an ASIO driver. On macOS, use the appropriate CoreAudio device.
3. Select the interface as the **Audio Input Device** and **Audio Output Device**. macOS can use separate input and output devices; set an unused direction to **No Device** if appropriate.
4. Confirm that the interface—not the built-in device—is shown in the device selectors.

If the interface does not appear, close Live, confirm its cable and power connection, check the operating system’s audio-device settings, and then reopen Live. Update its driver before trying third-party routing utilities.

## Choose a usable sample rate and buffer size

Set the sample rate to match the project or the material you will record. A common starting point is 44.1 kHz or 48 kHz. Higher rates can increase processing demand and do not improve an existing file recorded at a lower rate.

Set the buffer size according to the task:

- Use a smaller buffer when recording or playing a software instrument and low monitoring latency is important.
- Use a larger buffer for mixing, editing, or a demanding Set when responsiveness matters less than stable playback.

Lower buffer sizes require more CPU resources and can cause clicks or dropouts on an overloaded computer. On some Windows ASIO interfaces, the buffer control is available only through **Hardware Setup** or the manufacturer’s control panel. Test one change at a time using a simple Set.

## Enable the channels you need

Use **Configure Inputs** and **Configure Outputs** in Audio settings to make the interface channels available to Live. Enable only the mono and stereo pairs that the current workflow needs. Those choices determine what appears in the Mixer’s input and output routing menus.

For example, enable a microphone input before selecting it on an audio track. Enable additional output pairs before assigning a cue mix or external hardware destination. Channel labels can be renamed in the configuration dialogs so that routing menus describe the connected equipment clearly.

## Check monitoring and signal level

Create or select an audio track, show the Mixer’s In/Out controls, and select the relevant external input. Arm the track and set its monitoring mode deliberately. **Auto** is a practical starting point for recording through Live, while direct monitoring on the interface may be preferable when latency must be minimal.

Play or record a short test while watching the track meter. Adjust the gain on the interface so the signal is strong without reaching red overload. Then play a known clip through the Main output and raise the interface’s headphone or monitor level gradually.

Once the interface is selected, its necessary channels are enabled, and a test signal reaches the outputs cleanly, leave the configuration in place for that hardware setup. Ableton’s [audio-interface setup guide](https://help.ableton.com/hc/en-us/articles/211476789-Setting-up-an-Audio-Interface) and [Audio settings documentation](https://www.ableton.com/en/live-manual/12/first-steps/) provide current reference details. See the source [Learn Live: Setting up an audio interface](https://www.youtube.com/watch?v=D9tjzSctp_Q) video for the original walkthrough.
