# How to Map MIDI and Computer Keys in Ableton Live

Ableton Live 12 can assign external MIDI messages and computer-key presses to many interface controls, so common performance or recording actions do not require the mouse. Before creating a MIDI assignment, connect the controller and configure it for remote control in Live’s settings. The video walkthrough predates Live 12; the instructions here use current Live 12 labels and behavior from Ableton’s [MIDI and Key Remote Control documentation](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/).

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/l0DM9JbkQBA?rel=0"
    title="Learn Live: MIDI mapping and key mapping"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Prepare a MIDI controller for remote control

Open Live’s **Settings** and select **Link, Tempo & MIDI**. If the controller is listed in the **Control Surface** chooser, select it and choose its MIDI input and output ports. Live provides instant mappings for supported control surfaces, which can follow the selected device automatically.

For a controller that is not listed, use the **MIDI Ports** table in the same settings tab. Turn on **Remote** for the controller’s input port. If the controller has motorized controls or LED feedback, also turn on Remote for its output port so Live can send updates back to the hardware. Move a control and confirm that Live’s MIDI indicators respond before trying to make an assignment.

An absolute knob or fader can jump to its physical position when it first controls a different value in Live. In the **Takeover Mode** setting, choose **Pick-Up** when the control should wait until it reaches the current software value, or **Value Scaling** when it should converge smoothly. This is particularly useful for mixer and device parameters.

## Enter MIDI Map Mode and assign a control

Press the **MIDI** switch in the Control Bar, or use `Ctrl`+`M` on Windows or `Cmd`+`M` on macOS. Live enters **MIDI Map Mode**: controls that can accept MIDI assignments are highlighted in blue and the **Mapping Browser** becomes available.

To make one assignment:

1. Click the highlighted Live control you want to operate, such as a track activator, a device parameter, a transport button, or a Session View slot.
2. Send the MIDI message from the controller: turn a knob or encoder, move a fader, press a pad, or play a controller key.
3. Check that the new entry appears in the Mapping Browser.
4. Leave MIDI Map Mode by pressing the MIDI switch again or using the same shortcut.

The mapping is active after you leave the mode. Return to MIDI Map Mode whenever you need to review its assignment or edit it.

## Choose MIDI notes and controllers deliberately

MIDI Map Mode can use both notes and controller messages. A MIDI note assigned to a switch toggles it; one assigned to a continuous control switches between that mapping’s minimum and maximum values. An absolute knob or fader maps its 0–127 value range across the target parameter’s range.

This has an important consequence for a MIDI keyboard used to play instruments: a note assigned to Live’s interface is no longer available as MIDI input to MIDI tracks. Reserve a dedicated pad, button, or unused note range for remote control when the same device is also used for playing musical parts.

For Session View, assignments belong to the slots, not to the clips currently inside them. Replacing a clip does not move the slot assignment. A Session slot can also be mapped to a MIDI note range for chromatic playing; follow the range-assignment method in Ableton’s manual when that is the intended use.

## Refine or remove a MIDI mapping

While MIDI Map Mode is open, the Mapping Browser lists each manual mapping’s control element, parameter path, parameter name, and **Min** and **Max** values. Narrow the range when a hardware knob should cover only a useful part of a parameter, or invert the range from the mapping’s context menu when the physical direction should be reversed.

To remove a manual mapping, select it in the Mapping Browser and press `Backspace` on Windows or `Delete` on macOS. Instant mappings supplied by supported control surfaces are contextual and do not appear in this browser; a manual mapping can override an instant assignment for the selected target.

If a controller uses endless encoders, Live can interpret relative increment and decrement messages. Move an unrecognized encoder slowly to the left while assigning it so Live can suggest a suitable relative mode, then use the mode chooser if the suggested behavior needs adjustment. Relative encoders and an appropriate takeover mode help avoid sudden parameter changes.

## Map computer keys to discrete actions

Use **Key Map Mode** for computer-key assignments. Press the **KEY** switch in the Control Bar, or use `Ctrl`+`K` on Windows or `Cmd`+`K` on macOS. Mappable controls are highlighted in red and the Mapping Browser opens.

Click a highlighted control, then press the computer key that should operate it. Exit Key Map Mode and test the key. Computer-key mappings are suited to Session View slots and discrete controls such as switches, buttons, and radio buttons. For example, a key can toggle a track activator, start a mapped clip slot, or cycle a radio-button setting.

Choose keys that do not interfere with shortcuts you need during work or performance. Key Map Mode is separate from the **Computer MIDI Keyboard**, which is toggled with `M` and turns computer keys into playable MIDI notes. Use Key Map Mode to control Live’s interface; use the Computer MIDI Keyboard when the goal is to play an instrument.

## Test mappings in the context of the Set

Test each assignment at the point in the Set where it will be used. Check toggle behavior for buttons, the minimum and maximum range of continuous controls, and the controller feedback if the hardware has LEDs or motorized faders. Map Clip View controls cautiously: because Clip View shows whichever clip is selected, a mapped control can affect different clips as selection changes.

Save the Live Set after organizing the mappings. This preserves the assignments with the Set and makes them available the next time it is opened. A small, clearly planned set of mappings for transport, track activation, macros, and Session View actions is generally easier to operate and troubleshoot than many overlapping assignments.

## References

- [Ableton Live 12 Reference Manual: MIDI and Key Remote Control](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/)
- [Ableton Live 12 Reference Manual: Live Keyboard Shortcuts](https://www.ableton.com/en/manual/live-keyboard-shortcuts/)
- [Ableton Help: Using MIDI CC in Live](https://help.ableton.com/hc/en-us/articles/360010389480-Using-MIDI-CC-in-Live)
- [Learn Live: MIDI mapping and key mapping](https://www.youtube.com/watch?v=l0DM9JbkQBA)
