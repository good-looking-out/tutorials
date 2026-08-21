# How to Set Up MIDI in Ableton Live

MIDI devices can play instruments, record notes, control Live parameters, exchange clock information, or perform several of those tasks. Set up each device in [Ableton Live](https://www.ableton.com/en/live/) according to its purpose rather than enabling every available port.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/CWOXblksDxE?rel=0"
    title="Learn Live: Setting up MIDI"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Connect and identify the MIDI device

Install the manufacturer’s current driver or control software if the device needs it, then connect the controller or hardware instrument before opening Live. Many USB MIDI keyboards and controllers are class compliant and appear automatically.

Open **Settings** with `Cmd`+`,` on macOS or `Ctrl`+`,` on Windows, then select **Link, Tempo & MIDI**. Look first in the **Control Surfaces** list and the **MIDI Ports** input and output lists. A supported controller may be configured automatically as a control surface; do not overwrite that configuration unless its documentation calls for it.

## Configure a control surface when needed

A control surface uses a built-in script to provide preassigned controls for Live. If a supported device does not configure automatically:

1. Choose the device model in a Control Surface row.
2. Select its MIDI input port.
3. Select its MIDI output port when the controller needs feedback for LEDs, displays, or motorized controls.
4. Check the device documentation for its required operating mode or script.

Set a control-surface row to **None** if a device must be available only as a general MIDI port. This avoids an unwanted automatic control-surface assignment.

## Enable the correct MIDI-port functions

Each MIDI input and output port has independent switches. Enable only what the device needs:

- **Track** lets Live receive or send MIDI notes and control-change messages. Enable an input’s Track switch to play or record notes from a MIDI keyboard.
- **Remote** lets an input make custom MIDI mappings to Live controls. Enable an output’s Remote switch only when the controller needs mapped-value feedback.
- **Sync** sends or receives MIDI Clock or MIDI Timecode. Use it for a sequencer, drum machine, or another application that must run in time with Live.

Do not normally enable Sync on both the input and output for the same device. That can create a MIDI feedback loop. A controller without a built-in sequencer or sound generator usually needs Track input, Remote input for custom mappings, or both—not Sync.

## Test note input and control data

Create a MIDI track, load an instrument, arm the track, and play the controller. Live’s MIDI indicators in the Control Bar should show incoming activity. If notes do not reach the instrument, confirm the correct input port has **Track** enabled and that the MIDI track is armed or monitoring the intended source.

To make a custom mapping, enter MIDI Map Mode, select a mappable Live control, then move a hardware knob or fader. This workflow requires the corresponding input port’s **Remote** switch. Exit MIDI Map Mode and test that the mapping responds as expected.

## Keep the configuration easy to troubleshoot

If a device becomes unreliable, disconnect other MIDI equipment and test one port at a time. Check the device’s cable, power, operating mode, driver, and the operating system’s device list before changing several Live settings at once.

Ableton’s current [Live MIDI Settings guide](https://help.ableton.com/hc/en-us/articles/209774205-Live-s-MIDI-Settings) and [Routing and I/O manual chapter](https://www.ableton.com/en/live-manual/12/routing-and-i-o/) explain port behavior in detail. The original walkthrough is [Learn Live: Setting up MIDI](https://www.youtube.com/watch?v=CWOXblksDxE).
