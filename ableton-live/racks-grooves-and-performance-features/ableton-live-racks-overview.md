# Ableton Live Racks Overview

Racks combine devices and their settings into one configurable device in a Live track. They can simplify a device chain, create parallel processing or layers, and expose the controls that matter through Macros. Start with [Ableton Live](https://www.ableton.com/en/live/) open and a track that contains at least one device. The current Live 12 editions include Instrument, Drum, MIDI Effect, and Audio Effect Racks.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/oNEKxxjgdpc?rel=0"
    title="Learn Live: Racks Overview"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Recognize the four Rack types

Live provides four Rack variants. The type determines what can be placed inside and where the Rack can be used:

- **MIDI Effect Racks** contain MIDI effects and can be placed only on MIDI tracks.
- **Audio Effect Racks** contain audio effects. They work on audio, return, and Main tracks, and on MIDI tracks after an instrument.
- **Instrument Racks** can contain MIDI effects, an instrument, and audio effects. Keep that signal-flow order: MIDI effects first, then the instrument, then audio effects.
- **Drum Racks** organize instruments, MIDI effects, and audio effects around MIDI-note-triggered drum chains. They also support their own return chains.

An Instrument or Effect Rack can hold parallel chains. Each chain receives the Rack’s input, processes it through its own devices, and the chains’ outputs are mixed together. Drum Rack chains differ because each one receives the MIDI note assigned to it. Treat a Rack itself as one device in the surrounding track chain: devices before it feed the Rack, and devices after it receive the Rack’s output.

## Create a Rack from existing devices

To group devices that are already in a track:

1. In Device View, select the title bar of one or more compatible devices.
2. Right-click a selected title bar and choose **Group**. Live creates the Rack type appropriate for the selected devices.
3. Use the Rack’s view selectors to show its Macros, Chain List, or contained devices as needed.

You can also drag an empty generic Rack preset, such as **Audio Effect Rack**, from the Browser to a compatible track and then add devices to it. Select a Rack’s title bar and choose **Ungroup** from its context menu or the Edit menu when you need to return its contained devices to the surrounding chain.

Grouping a Rack again creates a Rack inside a Rack. Nested Racks are valid, but they can make a chain harder to inspect, so name and fold them deliberately.

## Use the Chain List to understand the signal path

Open the **Chain List** when you need to see the paths inside a Rack. Every entry in the list is a device chain, and the drop area beneath the list can accept a device, preset, or an existing chain to create another chain. Select a chain in this list to show its devices in the Devices view.

For a first experiment, create an Audio Effect Rack from two effects, then add another effect or preset to the Chain List. This makes the parallel nature of the Rack visible: the input reaches both chains, while each chain still processes its own devices in series. Set chain levels conservatively when combining parallel signals so that the Rack does not become unexpectedly louder.

## Map important controls to Macros

Macros provide a focused interface for a Rack. A Macro can control one parameter or several parameters across the Rack, so it can represent one musical decision instead of exposing every device control.

New Racks show eight Macro controls by default. Use the Rack’s plus and minus Macro view selectors to show or hide Macros, up to a maximum of 16. Hiding a Macro does not remove its mappings.

To make a mapping:

1. Show the Rack’s Macro controls and enable **Map** mode.
2. Click the device parameter you want to control.
3. Click the **Map** button beneath the chosen Macro.
4. In the Mapping Browser, set an appropriate minimum and maximum range. Reverse the range when the Macro should move the parameter in the opposite direction.
5. Exit Map mode and rename the Macro to describe the result it controls.

Map only controls that work together. For example, one Macro could increase a filter frequency while reducing a reverb’s dry/wet amount, but only if that relationship produces a useful, repeatable change in the sound.

## Store and recall Macro variations

Macro variations store snapshots of the current Macro values. They are useful for preserving a few sound-design states, mix treatments, or performance-ready transitions without changing the devices inside the Rack.

Open the Macro Variations view with its view selector. After at least one Macro has a mapping, click **New** to store the current Macro state. You can rename, duplicate, or delete a selected variation from its context menu, and use its launch control to recall the stored values. Select a variation only when you want to edit or inspect it; launch it when you want the Rack to change state.

Use the **Rand** button in the Rack’s title bar to randomize mapped Macro values while exploring possibilities. If a Macro should remain stable, exclude it from randomization in that Macro’s context menu. Store only the randomized results that are useful in the context of the Set.

## Keep a Rack usable as it grows

Racks are most useful when they simplify a real task: a compact performance control surface, a reusable effect chain, a layered instrument, or a drum kit with individual treatment. Keep the Macro names clear, use a small number of purposeful mappings, and check the Chain List before adding new parallel paths.

Once the Rack represents a useful configuration, save it as a preset so it can be reused in another Set. This overview establishes the Rack structure, chains, Macros, and variations; use the deeper Rack tools only when they serve a specific sound or performance need.

For current details, see Ableton’s [Instrument, Drum and Effect Racks reference](https://www.ableton.com/en/live-manual/12/instrument-drum-and-effect-racks/), [Macros and Variations FAQ](https://help.ableton.com/hc/en-us/articles/360019103480-Macros-and-Variations-FAQ), and [Live edition comparison](https://www.ableton.com/en/live/compare-editions/). The source walkthrough is Ableton’s [Learn Live: Racks Overview](https://www.youtube.com/watch?v=oNEKxxjgdpc).
