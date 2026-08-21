# How to Set Default Behavior in Ableton Live

Defaults let [Ableton Live](https://www.ableton.com/en/live/) load tracks, devices, and new Sets in a predictable starting state. Use them for choices that you make repeatedly, such as an EQ on new audio tracks or a preferred instrument configuration, but keep the defaults simple enough to remain useful across projects.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/-RzrcrMruFY?rel=0"
    title="Learn Live: Using defaults"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Choose the kind of default you need

Live supports different defaults for different purposes:

- A **device default preset** loads a device with a chosen parameter state.
- A **default Audio Track** or **default MIDI Track** loads a new track with its chosen routing and device chain.
- A **Default Set** opens when you create a new Live Set.
- A **Template Set** provides an alternative repeatable starting point for a specific workflow.

Decide whether the repeated behavior belongs to a device, one track type, or every new Set. Do not use a Default Set for a preference that only belongs to one device.

## Save a device default preset

Load the instrument, MIDI effect, audio effect, or supported plug-in configuration that you want to customize. Adjust its parameters, then right-click its title bar or header and choose **Save as Default Preset**.

From then on, loading that Live device starts with the saved default. For third-party plug-ins, **Save as Default Configuration** saves the configured parameter panel, not the plug-in’s sound preset; save a Rack if you need to recall a particular plug-in sound with its Live configuration.

## Save default Audio and MIDI tracks

Build the track that should appear when you create a new one. It can contain routing, monitoring choices, instruments, effects, and other settings that are appropriate for every track of that type.

Right-click the track header and choose **Save as Default Audio Track** or **Save as Default MIDI Track**. Create a new track of the same type to test it immediately. Return and Main tracks do not have equivalent default-track commands, so include recurring return-track routing in a Default Set or a template instead.

## Create a Default Set or template

Create the tracks, return tracks, routing, devices, and mappings that you want at the beginning of every project. Then choose **File > Save Live Set as Default Set**. Opening a new Set with `Cmd`+`N` on macOS or `Ctrl`+`N` on Windows now uses that configuration.

Use **File > Save Live Set as Template** instead when you need several different starting points, such as separate recording, writing, and performance setups. Open the Templates Browser label to start from one of them, or right-click a template and choose **Set Default Live Set** to make it the main default.

## Restore a useful baseline

Review defaults after a few real projects. Remove a device or routing choice that appears too often or makes new Sets slow to open. To restore the factory Default Set, open the **Templates** label, right-click `DefaultLiveSet.als`, and choose **Set Default Live Set**. To restore a device or track default, remove the corresponding saved default from the User Library’s Defaults folder.

Defaults should reduce routine setup without hiding important decisions. Ableton’s current [Using defaults](https://help.ableton.com/hc/en-us/articles/209071029-Using-defaults) and [Default Set and Template Sets](https://help.ableton.com/hc/en-us/articles/209067189-Default-Set-and-Template-Sets) guides cover the available types. The source walkthrough is [Learn Live: Using defaults](https://www.youtube.com/watch?v=-RzrcrMruFY).
